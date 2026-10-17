"""The offline pattern index over the background corpus ``T`` (paper Section 2.4).

One full scan of ``T`` produces, for every pattern ``p`` any corpus value can
generalize into, its estimated corpus-level false-positive rate ``FPR_T(p)``
(Eqn 4) and its coverage ``Cov_T(p)``. Online query-time pattern inference
then reads only this index instead of rescanning ``T``.

``FPR_T(p)`` is the **unweighted** mean of ``Imp_D(p)`` over exactly the
columns in ``T`` that have at least one value matching ``p`` (paper Ex. 3:
4800 of 5000 matching columns at impurity 0 and 200 at 1% gives
``200 x 1% / 5000 = 0.04%``). Columns that do not match ``p`` at all are
excluded from both the numerator and the denominator.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from types import MappingProxyType
from typing import Any

import pandas as pd

from open_detect.algorithms.auto_validate.config import AutoValidateConfig
from open_detect.algorithms.auto_validate.hierarchy import token_count
from open_detect.algorithms.auto_validate.patterns import patterns_of
from open_detect.exceptions import ValidationError

__all__ = ["PatternIndex", "build_pattern_index", "clean_column", "indexable_values"]


def clean_column(values: Iterable[object]) -> tuple[str, ...]:
    """``str()``-convert a column's values, dropping nulls and blanks.

    The paper does not discuss null handling; dropping nulls before indexing
    follows from the detection contract that null cells are never flagged,
    and from ``Imp_D`` being undefined on an empty denominator.
    """
    out: list[str] = []
    for value in values:
        if value is None:
            continue
        if not isinstance(value, str) and _is_null(value):
            continue
        text = value if isinstance(value, str) else str(value)
        if text:
            out.append(text)
    return tuple(out)


def _is_null(value: Any) -> bool:
    """``pd.isna`` that tolerates array-likes and other exotic objects."""
    try:
        return bool(pd.isna(value))
    except (TypeError, ValueError):
        return False


def indexable_values(values: tuple[str, ...], tau: int) -> tuple[str, ...]:
    """The values of ``D`` that enter ``P(D)`` under the paper's tau pruning.

    Paper Section 2.4: ``P(D) = union over {v in D : t(v) < tau} of P(v)``,
    where ``t(v)`` is the value's token count. Values wider than ``tau`` are
    skipped entirely -- this changes which patterns the index can answer for,
    not merely how long the build takes (paper-spec Section 8.4).
    """
    return tuple(value for value in values if token_count(value) < tau)


@dataclass(frozen=True, slots=True)
class PatternIndex:
    """Immutable ``pattern -> (fpr_t, cov_t)`` map built from a corpus.

    ``n_columns`` is the number of corpus columns that actually contributed
    (after tau pruning), i.e. the effective ``|T|`` behind every FPR and
    coverage figure in the index.
    """

    _entries: MappingProxyType[str, tuple[float, int]]
    n_columns: int

    @classmethod
    def _build(cls, entries: dict[str, tuple[float, int]], n_columns: int) -> PatternIndex:
        return cls(MappingProxyType(dict(entries)), n_columns)

    def lookup(self, pattern: str) -> tuple[float, int] | None:
        """``(FPR_T, Cov_T)`` for ``pattern``, or ``None`` if the index has no entry."""
        return self._entries.get(pattern)

    def fpr(self, pattern: str) -> float | None:
        """``FPR_T(pattern)``, or ``None`` when the pattern was never indexed."""
        entry = self.lookup(pattern)
        return None if entry is None else entry[0]

    def coverage(self, pattern: str) -> int | None:
        """``Cov_T(pattern)``, or ``None`` when the pattern was never indexed."""
        entry = self.lookup(pattern)
        return None if entry is None else entry[1]

    def __len__(self) -> int:
        return len(self._entries)

    def __iter__(self) -> Iterator[str]:
        return iter(self._entries)

    def __contains__(self, pattern: object) -> bool:
        return pattern in self._entries

    def patterns(self) -> tuple[str, ...]:
        """Every indexed pattern, in deterministic (coarsest-first) order."""
        from open_detect.algorithms.auto_validate.patterns import sorted_patterns

        return sorted_patterns(frozenset(self._entries))


def _iter_corpus_columns(corpus: Iterable[object]) -> Iterator[tuple[str, ...]]:
    """Normalize the corpus into per-column sequences of clean string values.

    Each ``Series`` is one column of ``T``; each ``DataFrame`` contributes each
    of its columns.
    """
    for item in corpus:
        if isinstance(item, pd.DataFrame):
            for name in item.columns:
                yield clean_column(item[name].tolist())
        elif isinstance(item, pd.Series):
            yield clean_column(item.tolist())
        elif isinstance(item, (list, tuple)):
            yield clean_column(item)
        else:
            raise ValidationError(
                "corpus entries must be pandas Series, DataFrames or sequences of values, "
                f"got {type(item).__name__}"
            )


def build_pattern_index(
    corpus: Iterable[object],
    config: AutoValidateConfig | None = None,
) -> PatternIndex:
    """One offline scan of ``T``, producing the pattern index (paper Section 2.4).

    For each corpus column ``D``, the local impurity of every pattern in
    ``P(D)`` is recorded; per-pattern, those local impurities are then averaged
    over the matching columns only to give ``FPR_T`` (Eqn 4), and the number of
    such columns gives ``Cov_T``.
    """
    config = config or AutoValidateConfig()

    # pattern -> [sum of Imp_D(p), number of columns where p matched]
    local: dict[str, list[float]] = {}
    n_indexed = 0
    for values in _iter_corpus_columns(corpus):
        indexable = indexable_values(values, config.tau)
        if not indexable:
            continue
        n_indexed += 1
        counts = Counter(indexable)
        n_total = sum(counts.values())

        # A pattern matches a value iff it belongs to P(value), so the number of
        # column values a pattern matches is the sum of multiplicities over the
        # values whose P(v) contains it. Accumulating per value (each value's
        # pattern set is enumerated once) is O(sum |P(v)|) instead of the
        # O(|P(D)| x |D|) the per-pattern re-scan of the column requires.
        match_counts: dict[str, int] = {}
        for value, count in counts.items():
            for pattern in patterns_of(value, config.tau):
                match_counts[pattern] = match_counts.get(pattern, 0) + count
        for pattern, n_match in match_counts.items():
            if n_match == 0:
                continue
            local.setdefault(pattern, [0.0, 0])[0] += (n_total - n_match) / n_total
            local[pattern][1] += 1

    entries = {
        pattern: (scores[0] / scores[1], int(scores[1]))
        for pattern, scores in local.items()
        if scores[1]
    }
    return PatternIndex._build(entries, n_indexed)
