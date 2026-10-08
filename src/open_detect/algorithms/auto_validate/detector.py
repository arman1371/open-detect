"""AutoValidateAlgorithm: the end-to-end error-detection algorithm.

The Auto-Validate algorithm (Song & He, SIGMOD 2021) operates in two phases:

1. **Offline** (:meth:`build_index`) scans a background corpus ``T`` (a collection
   of cleaned tables/columns from a data lake) and produces a
   :class:`~open_detect.algorithms.auto_validate.index.PatternIndex` mapping each
   pattern to its estimated false-positive rate ``FPR_T(p)`` and coverage
   ``Cov_T(p)``. This is the paper's Sec. 2.4 offline index.
2. **Online** (:meth:`detect`) runs against a single dirty table. For each
   query column, it infers a validation pattern via the selected FMDV variant
   (config :attr:`~open_detect.algorithms.auto_validate.config.AutoValidateConfig.variant`).
   Every non-null cell whose value does not match the inferred pattern is
   flagged as an error.

The paper has no ``score`` field; we define one so that the cell-level
schema stays uniform across algorithms: for flagged cells ``score = 1 - FPR_T``,
for unflagged cells ``score = 0.0``. The paper's drift test (Sec 5.4) is
provided as the standalone helper :func:`~open_detect.algorithms.auto_validate.drift.check_drift`
and is **not** wired into :meth:`detect` -- there is no "future" column to
compare against when scanning a single table. See the fidelity notes in
``ARCHITECTURE.md``.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from typing import Any

import pandas as pd

from open_detect.algorithms.auto_validate.config import AutoValidateConfig
from open_detect.algorithms.auto_validate.exceptions import IndexNotBuiltError
from open_detect.algorithms.auto_validate.fmdv import InferredPattern, fmdv, fmdv_h
from open_detect.algorithms.auto_validate.fmdv_v import fmdv_v, fmdv_vh
from open_detect.algorithms.auto_validate.hierarchy import matches
from open_detect.algorithms.auto_validate.index import PatternIndex, build_pattern_index
from open_detect.algorithms.base import AlgorithmResult, CellResult, ErrorDetectionAlgorithm

#: Mapping from config.variant to the pattern-inference function.
_DISPATCH: dict[str, Any] = {
    "fmdv": fmdv,
    "fmdv_h": fmdv_h,
    "fmdv_v": fmdv_v,
    "fmdv_vh": fmdv_vh,
}


class AutoValidateAlgorithm(ErrorDetectionAlgorithm):
    """Registered as ``"auto_validate"`` in :mod:`open_detect.algorithms`."""

    name = "auto_validate"

    def __init__(self, config: AutoValidateConfig | None = None) -> None:
        self.config = config or AutoValidateConfig()
        self._index: PatternIndex | None = None

    @property
    def index(self) -> PatternIndex:
        """The pattern index built from the background corpus ``T``."""
        if self._index is None:
            raise IndexNotBuiltError(
                "build_index(corpus) must be called before detect or infer_pattern. "
                "The Auto-Validate algorithm requires a background corpus T."
            )
        return self._index

    def build_index(self, corpus: Iterable[pd.Series | pd.DataFrame]) -> PatternIndex:
        """Scan the background corpus and build the offline pattern index.

        Parameters
        ----------
        corpus:
            An iterable of cleaned columns from the background corpus ``T``.
            Each element may be a ``pandas.Series`` (single column), a
            ``pandas.DataFrame`` (each column is a corpus column), or a
            plain sequence of values.
        """
        self._index = build_pattern_index(corpus, self.config)
        return self._index

    def infer_pattern(self, column: pd.Series) -> InferredPattern | None:
        """Infer the validation pattern for a single column.

        Dispatches the configured FMDV variant against the offline index and
        returns the :class:`InferredPattern`, or ``None`` when no feasible
        pattern exists (e.g. the variant is unknown or the column cannot be
        satisfied under ``r``/``m``/``theta``).
        """
        infer_fn = _DISPATCH.get(self.config.variant)
        if infer_fn is None:
            return None
        return infer_fn(column, self.index, self.config)

    def detect(
        self,
        data: pd.DataFrame,
        *,
        table_id: str = "table",
        columns: list[str] | None = None,
        **kwargs: Any,
    ) -> AlgorithmResult:
        """Run Auto-Validate against a single dirty table.

        Parameters
        ----------
        data:
            The (dirty) table to scan, as a ``pandas.DataFrame``.
        table_id:
            Identifier stamped onto every result cell.
        columns:
            If given, only these columns are scanned. ``None`` means all
            columns of ``data``.
        """
        if len(data) == 0 or data.shape[1] == 0:
            return AlgorithmResult(algorithm=self.name, cells=())

        col_names = columns if columns is not None else list(data.columns)
        cells: list[CellResult] = []
        for col in col_names:
            if col not in data.columns:
                continue
            series = data[col]
            inferred = self.infer_pattern(series)
            if inferred is None:
                # Infeasible column: no flags, explainable evidence.
                cells.extend(
                    _non_null_cells(
                        series,
                        table_id,
                        col,
                        self.name,
                        is_error=False,
                        score=0.0,
                        evidence=_infeasible_evidence(self.config, None),
                    )
                )
                continue
            pattern = inferred.pattern
            fpr_t, cov_t, theta_c = inferred.fpr_t, inferred.cov_t, inferred.theta_c
            n_total = len(series) - sum(1 for v in series if _is_null(v))
            score = 1.0 - fpr_t if n_total > 0 else 0.0
            for idx, value in series.items():
                if _is_null(value):
                    continue
                is_error = not _value_matches(pattern, value)
                cells.append(
                    CellResult(
                        table_id=table_id,
                        row_index=idx,
                        column_name=col,
                        algorithm=self.name,
                        is_error=is_error,
                        score=score if is_error else 0.0,
                        evidence=_feasible_evidence(self.config, pattern, fpr_t, cov_t, theta_c),
                    )
                )
        return AlgorithmResult(algorithm=self.name, cells=tuple(cells))


def _is_null(value: Any) -> bool:
    """Return True if ``value`` should be treated as null."""
    if value is None:
        return True
    try:
        return bool(pd.isna(value))
    except (TypeError, ValueError):
        return False


def _value_matches(pattern: str | Sequence[str], value: Any) -> bool:
    """Whether ``value`` matches ``pattern`` (nulls return False).

    ``pattern`` is the inferred validation pattern: a single string for the
    single-pattern FMDV variants, or a disjunction of one pattern per coarse
    signature group for ``fmdv_v``/``fmdv_vh``.  A value is valid if it matches
    **any** of them -- the groups are a partition of the column, so each value
    belongs to exactly one group and must satisfy that group's pattern.
    """
    if _is_null(value):
        return False
    text = value if isinstance(value, str) else str(value)
    if not text:
        return False
    if isinstance(pattern, str):
        return matches(pattern, text)
    return any(matches(p, text) for p in pattern)


def _non_null_cells(
    series: pd.Series,
    table_id: str,
    col: str,
    algorithm: str,
    *,
    is_error: bool,
    score: float,
    evidence: dict[str, Any],
) -> list[CellResult]:
    """Emit one ``CellResult`` per non-null cell of ``series``."""
    cells: list[CellResult] = []
    for idx, value in series.items():
        if _is_null(value):
            continue
        text = value if isinstance(value, str) else str(value)
        if not text:
            continue
        cells.append(
            CellResult(
                table_id=table_id,
                row_index=idx,
                column_name=col,
                algorithm=algorithm,
                is_error=is_error,
                score=score,
                evidence=evidence,
            )
        )
    return cells


def _infeasible_evidence(config: AutoValidateConfig, reason: str | None) -> dict[str, Any]:
    """Evidence dict for a column with no feasible pattern."""
    return {
        "pattern": None,
        "reason": reason or "no_feasible_pattern",
        "fpr_t": 0.0,
        "cov_t": 0,
        "theta_c": 0.0,
        "variant": config.variant,
        "r": config.r,
        "m": config.m,
        "tau": config.tau,
    }


def _feasible_evidence(
    config: AutoValidateConfig,
    pattern: str | Sequence[str],
    fpr_t: float,
    cov_t: int,
    theta_c: float,
) -> dict[str, Any]:
    """Evidence dict for a column with an inferred pattern."""
    return {
        "pattern": pattern,
        "fpr_t": fpr_t,
        "cov_t": cov_t,
        "theta_c": theta_c,
        "variant": config.variant,
        "r": config.r,
        "m": config.m,
        "tau": config.tau,
    }
