"""AutoValidateAlgorithm: the end-to-end error-detection algorithm.

The Auto-Validate algorithm (Song & He, SIGMOD 2021) operates in two phases:

1. **Offline** (:meth:`build_index`) scans a background corpus ``T`` (a collection
   of cleaned tables/columns from a data lake) and produces a
   :class:`~unidetect.algorithms.auto_validate.index.PatternIndex` mapping each
   pattern to its estimated false-positive rate ``FPR_T(p)`` and coverage
   ``Cov_T(p)``. This is the paper's Sec. 2.4 offline index.
2. **Online** (:meth:`detect`) runs against a single dirty table. For each
   query column, it infers a validation pattern via the selected FMDV variant
   (config :attr:`~unidetect.algorithms.auto_validate.config.AutoValidateConfig.variant`).
   Every non-null cell whose value does not match the inferred pattern is
   flagged as an error.

The paper has no ``score`` field; we define one so that the cell-level
schema stays uniform across algorithms: for flagged cells ``score = 1 - FPR_T``,
for unflagged cells ``score = 0.0``. The paper's drift test (Sec 5.4) is
provided as the standalone helper :func:`~unidetect.algorithms.auto_validate.drift.check_drift`
and is **not** wired into :meth:`detect` -- there is no "future" column to
compare against when scanning a single table. See the fidelity notes in
``ARCHITECTURE.md``.
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING, Any

import pandas as pd

from unidetect.algorithms.auto_validate.config import AutoValidateConfig
from unidetect.algorithms.auto_validate.exceptions import IndexNotBuiltError
from unidetect.algorithms.auto_validate.fmdv import fmdv, fmdv_h
from unidetect.algorithms.auto_validate.fmdv_v import fmdv_v, fmdv_vh
from unidetect.algorithms.auto_validate.index import build_pattern_index
from unidetect.algorithms.base import AlgorithmResult, CellResult, ErrorDetectionAlgorithm

if TYPE_CHECKING:
    from unidetect.algorithms.auto_validate.index import PatternIndex


#: Mapping from config.variant to the pattern-inference function.
_DISPATCH: dict[str, Any] = {
    "fmdv": fmdv,
    "fmdv_h": fmdv_h,
    "fmdv_v": fmdv_v,
    "fmdv_vh": fmdv_vh,
}


class AutoValidateAlgorithm(ErrorDetectionAlgorithm):
    """Registered as ``"auto_validate"`` in :mod:`unidetect.algorithms`."""

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

    def infer_pattern(self, column: pd.Series) -> tuple[str | None, float, int, float, str | None]:
        """Infer the validation pattern for a single column.

        Returns ``(pattern, fpr_t, cov_t, theta_c, reason)`` where ``reason``
        is ``None`` on success and an explanation string when no feasible
        pattern is found.
        """
        infer_fn = _DISPATCH.get(self.config.variant)
        if infer_fn is None:
            return None, 0.0, 0, 0.0, f"unknown variant {self.config.variant!r}"
        result = infer_fn(column, self.index, self.config)
        if result is None:
            return None, 0.0, 0, 0.0, "no_feasible_pattern"
        pat = result.pattern if isinstance(result.pattern, str) else result.pattern[0]
        return pat, result.fpr_t, result.cov_t, result.theta_c, None

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
            pattern, fpr_t, cov_t, theta_c, reason = self.infer_pattern(series)
            if pattern is None:
                # Infeasible column: no flags, explainable evidence.
                for idx, value in series.items():
                    if value is None:
                        continue
                    try:
                        if pd.isna(value):
                            continue
                    except (TypeError, ValueError):
                        pass
                    text = value if isinstance(value, str) else str(value)
                    if not text:
                        continue
                    cells.append(
                        CellResult(
                            table_id=table_id,
                            row_index=idx,
                            column_name=col,
                            algorithm=self.name,
                            is_error=False,
                            score=0.0,
                            evidence={
                                "pattern": None,
                                "reason": reason or "no_feasible_pattern",
                                "fpr_t": 0.0,
                                "cov_t": 0,
                                "theta_c": 0.0,
                                "variant": self.config.variant,
                                "r": self.config.r,
                                "m": self.config.m,
                                "tau": self.config.tau,
                            },
                        )
                    )
                continue
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
                        evidence={
                            "pattern": pattern,
                            "fpr_t": fpr_t,
                            "cov_t": cov_t,
                            "theta_c": theta_c,
                            "variant": self.config.variant,
                            "r": self.config.r,
                            "m": self.config.m,
                            "tau": self.config.tau,
                        },
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


def _value_matches(pattern: str, value: Any) -> bool:
    """Whether ``value`` matches ``pattern`` (nulls return False)."""
    if _is_null(value):
        return False
    text = value if isinstance(value, str) else str(value)
    if not text:
        return False
    from unidetect.algorithms.auto_validate.hierarchy import matches

    return matches(pattern, text)
