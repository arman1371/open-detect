"""Core value types shared by metrics, featurization, corpus building and detectors.

These are plain, immutable ``dataclasses`` (not pydantic) to keep the
dependency footprint minimal -- this code runs inside pandas UDFs on Spark
executors, where every extra import has a real cost.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from unidetect.core.enums import ColumnDataType, ErrorType


@dataclass(frozen=True, slots=True)
class FeatureBucket:
    """A discretized point in the featurization "cube" (paper Figure 5).

    Instances of :class:`FeatureBucket` are the grouping key used both when
    materializing corpus statistics (``S^F_D(T)`` in Definition 4) and when
    looking up statistics for a new target column. Two columns are
    considered part of the same sub-cube iff their buckets compare equal.

    ``dims`` holds the ordered (name, bucket_value) pairs so buckets remain
    self-describing and stable across schema evolution (adding a new
    dimension changes the key, which is the desired "cold start" behaviour
    rather than silently mixing incompatible statistics).
    """

    error_type: ErrorType
    dims: tuple[tuple[str, str], ...]

    def as_key(self) -> str:
        """Stable string encoding, used as a Delta partition/grouping column."""
        body = "|".join(f"{name}={value}" for name, value in self.dims)
        return f"{self.error_type.value}::{body}"

    def as_dict(self) -> dict[str, str]:
        return dict(self.dims)

    def __str__(self) -> str:  # pragma: no cover - convenience only
        return self.as_key()


@dataclass(frozen=True, slots=True)
class MetricObservation:
    """The (before, after) reading of a metric function around a perturbation.

    ``theta_before`` is ``m(D)`` and ``theta_after`` is ``m(D_perturbed)`` in
    the paper's notation (e.g. Equation 11's ``theta1``/``theta2``).
    """

    theta_before: float
    theta_after: float


@dataclass(frozen=True, slots=True)
class Candidate:
    """A single perturbation hypothesis awaiting a likelihood-ratio score.

    One :class:`Candidate` is produced per (table, column[, column-pair])
    subject to a given error type -- it packages everything the corpus store
    needs to compute Equation (4)/(12) without re-touching the raw data.
    """

    candidate_id: str
    error_type: ErrorType
    table_id: str
    column_names: tuple[str, ...]
    row_ids: tuple[Any, ...]
    """Identifiers (or positional indices) of the rows/values flagged for removal."""
    observation: MetricObservation
    bucket: FeatureBucket
    evidence: dict[str, Any] = field(default_factory=dict)
    """Human-readable extras (e.g. the offending value pair) for explainability."""


@dataclass(frozen=True, slots=True)
class Detection:
    """A scored, ranked prediction ready to be surfaced to a user or written to UC."""

    candidate_id: str
    error_type: ErrorType
    table_id: str
    column_names: tuple[str, ...]
    row_ids: tuple[Any, ...]
    lr_ratio: float
    """The (Laplace-smoothed) likelihood ratio from Equation (2). Smaller = more surprising."""
    surprisal: float
    """``-log(lr_ratio)``, monotonically decreasing in ``lr_ratio`` -- convenient for ranking UIs."""
    is_significant: bool
    """``lr_ratio <= alpha`` for the configured significance level."""
    support: int
    """Number of corpus rows the ratio was estimated from (the denominator's raw count)."""
    evidence: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "candidate_id": self.candidate_id,
            "error_type": self.error_type.value,
            "table_id": self.table_id,
            "column_names": list(self.column_names),
            "row_ids": list(self.row_ids),
            "lr_ratio": self.lr_ratio,
            "surprisal": self.surprisal,
            "is_significant": self.is_significant,
            "support": self.support,
            "evidence": self.evidence,
        }


@dataclass(frozen=True, slots=True)
class CorpusColumnRecord:
    """One row of the canonical corpus-column representation (see ``corpus/schema.py``)."""

    table_id: str
    column_name: str
    column_index: int
    num_rows: int
    data_type: ColumnDataType
    values: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class CorpusPairRecord:
    """One row of the canonical corpus column-pair representation, used for FD."""

    table_id: str
    lhs_column: str
    rhs_column: str
    num_rows: int
    lhs_values: tuple[str, ...]
    rhs_values: tuple[str, ...]
