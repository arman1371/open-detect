"""Core enumerations shared across the unidetect package."""

from __future__ import annotations

from enum import Enum


class ErrorType(str, Enum):
    """The four error classes Uni-Detect is instantiated for (paper Section 3).

    Each value doubles as the partition key used for the corpus-statistics
    Delta table, so renaming members is a breaking schema change.
    """

    UNIQUENESS = "uniqueness"
    FUNCTIONAL_DEPENDENCY = "functional_dependency"
    NUMERIC_OUTLIER = "numeric_outlier"
    SPELLING = "spelling"


class ColumnDataType(str, Enum):
    """Coarse data-type classification used for featurization (paper Fig. 5).

    This is deliberately coarser than a Spark SQL type: it groups columns the
    way a human would when reasoning about "what kind of values live here",
    which is what the corpus subsetting in the paper relies on.
    """

    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    MIXED_ALPHANUMERIC = "mixed_alphanumeric"
    UNKNOWN = "unknown"


class ComparisonDirection(str, Enum):
    """Direction in which a metric moves once the anomalous subset is removed.

    Uni-Detect's four metric functions fall into exactly two families
    (Sections 3.1-3.4):

    * ``INCREASING`` -- the metric *grows* once the anomalous rows/values are
      dropped (min-pairwise-edit-distance for spelling, uniqueness-ratio,
      FD-compliance-ratio). The "before" value is a lower bound reached from
      below (``m(D) <= theta1``) and the "after" value is a lower bound the
      perturbed data must clear (``m(D_perturbed) >= theta2``).
    * ``DECREASING`` -- the metric *shrinks* once the outlier is dropped
      (max-MAD for numeric outliers). ``m(D) >= theta1`` before, and
      ``m(D_perturbed) <= theta2`` after.

    This mirrors the monotonicity argument in Theorem 1 of the paper, which
    is proved for the DECREASING case and holds symmetrically for the
    INCREASING case.
    """

    INCREASING = "increasing"
    DECREASING = "decreasing"
