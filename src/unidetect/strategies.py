"""Registry tying each :class:`ErrorType` to its Definition-4 configuration.

The paper instantiates Uni-Detect per error class with a triple
``(m, F, P)`` -- a metric function, a featurization, and a perturbation.
The concrete ``m``/``F``/``P`` implementations differ in arity (uniqueness
and outliers/spelling take one column, FD takes a column pair) and live in
``metrics/``, ``featurization.py`` and ``perturbation.py`` respectively, so
they are not force-fit behind one Python interface here.

What *is* uniform across all four instantiations -- and is exactly what the
generalized, smoothed likelihood-ratio in Equation (12) needs -- is the
:class:`~unidetect.core.enums.ComparisonDirection` each metric moves in once
the anomalous subset is removed. This module is the single source of truth
for that direction, so the corpus builder/store and every detector agree.
"""

from __future__ import annotations

from dataclasses import dataclass

from unidetect.core.enums import ComparisonDirection, ErrorType


@dataclass(frozen=True, slots=True)
class ErrorTypeSpec:
    error_type: ErrorType
    direction: ComparisonDirection
    min_rows: int
    description: str


_REGISTRY: dict[ErrorType, ErrorTypeSpec] = {
    ErrorType.UNIQUENESS: ErrorTypeSpec(
        error_type=ErrorType.UNIQUENESS,
        direction=ComparisonDirection.INCREASING,
        min_rows=5,
        description="Uniqueness-ratio (UR) grows toward 1.0 once duplicate values are dropped.",
    ),
    ErrorType.FUNCTIONAL_DEPENDENCY: ErrorTypeSpec(
        error_type=ErrorType.FUNCTIONAL_DEPENDENCY,
        direction=ComparisonDirection.INCREASING,
        min_rows=5,
        description="FD-compliance-ratio (FR) grows toward 1.0 once violating rows are dropped.",
    ),
    ErrorType.NUMERIC_OUTLIER: ErrorTypeSpec(
        error_type=ErrorType.NUMERIC_OUTLIER,
        direction=ComparisonDirection.DECREASING,
        min_rows=5,
        description="max-MAD shrinks once the most outlying value is dropped.",
    ),
    ErrorType.SPELLING: ErrorTypeSpec(
        error_type=ErrorType.SPELLING,
        direction=ComparisonDirection.INCREASING,
        min_rows=3,
        description="Min-pairwise edit-distance (MPD) grows once the misspelled value is dropped.",
    ),
}


def get_spec(error_type: ErrorType) -> ErrorTypeSpec:
    return _REGISTRY[error_type]


def all_specs() -> tuple[ErrorTypeSpec, ...]:
    return tuple(_REGISTRY.values())
