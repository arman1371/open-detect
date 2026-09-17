"""Per-error-type instantiations of epsilon-perturbation (paper Definition 2).

Each function here performs the "hypothetically remove a small subset O and
recompute the metric" step described in Section 2.2.1, for one of the four
error classes. The output (:class:`PerturbationOutcome`) carries everything
a detector needs to build a :class:`~unidetect.core.models.Candidate`:
theta_before/theta_after, which rows/values were removed, and small bits of
evidence for explainability.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field
from math import ceil
from typing import Any

from unidetect.metrics.functional_dependency import fd_compliance_ratio, minority_violation_rows
from unidetect.metrics.outliers import max_mad
from unidetect.metrics.spelling import differing_token_lengths, min_pairwise_edit_distance
from unidetect.metrics.uniqueness import duplicate_value_indices, uniqueness_ratio

#: Sentinel used when a perturbation removes all but <2 values, making the
#: metric undefined "after". Chosen so INCREASING-direction thresholds
#: (spelling, FD, uniqueness) treat it as "maximally not-suspicious" and
#: DECREASING-direction thresholds (outliers) treat it as "maximally clean".
_UNDEFINED_AFTER_HIGH = 1.0e9
_UNDEFINED_AFTER_LOW = 0.0


@dataclass(frozen=True, slots=True)
class PerturbationOutcome:
    theta_before: float
    theta_after: float
    dropped_indices: tuple[int, ...]
    evidence: dict[str, Any] = field(default_factory=dict)


def _max_drop(n: int, epsilon: float) -> int:
    return max(1, ceil(epsilon * n))


def perturb_uniqueness(values: Sequence[object], epsilon: float) -> PerturbationOutcome:
    """Drop duplicate occurrences (paper Example 2)."""
    theta_before = uniqueness_ratio(values)
    all_dupes = duplicate_value_indices(values)
    budget = _max_drop(len(values), epsilon)
    dropped = tuple(all_dupes[:budget])

    remaining = [v for i, v in enumerate(values) if i not in set(dropped)]
    theta_after = uniqueness_ratio(remaining) if len(remaining) >= 2 else _UNDEFINED_AFTER_HIGH
    return PerturbationOutcome(
        theta_before=theta_before,
        theta_after=theta_after,
        dropped_indices=dropped,
        evidence={"num_duplicate_values": len(all_dupes)},
    )


def perturb_numeric_outlier(values: Sequence[float], epsilon: float) -> PerturbationOutcome:
    """Drop the single most outlying value by MAD-score (paper Section 3.1)."""
    result = max_mad(values)
    clean = [v for v in values if v is not None]
    remaining = [v for i, v in enumerate(clean) if i != result.index]
    theta_after = max_mad(remaining).score if len(remaining) >= 2 else _UNDEFINED_AFTER_LOW
    return PerturbationOutcome(
        theta_before=result.score,
        theta_after=theta_after,
        dropped_indices=(result.index,),
        evidence={"outlier_value": result.value},
    )


def perturb_spelling(
    values: Sequence[object], epsilon: float, max_block_size: int = 500
) -> PerturbationOutcome:
    """Drop one value from the closest (min edit-distance) pair (paper Section 3.2)."""
    mpd_before = min_pairwise_edit_distance(values, max_block_size=max_block_size)
    clean = [str(v) for v in values if v is not None]
    remaining = [v for i, v in enumerate(clean) if i != mpd_before.index_u]
    mpd_after: float
    if len(remaining) >= 2:
        try:
            mpd_after = float(
                min_pairwise_edit_distance(remaining, max_block_size=max_block_size).mpd
            )
        except ValueError:
            mpd_after = _UNDEFINED_AFTER_HIGH
    else:
        mpd_after = _UNDEFINED_AFTER_HIGH

    token_lengths = differing_token_lengths(mpd_before.value_u, mpd_before.value_v)
    avg_token_length = sum(token_lengths) / len(token_lengths)
    return PerturbationOutcome(
        theta_before=float(mpd_before.mpd),
        theta_after=float(mpd_after),
        dropped_indices=(mpd_before.index_u,),
        evidence={
            "pair": (mpd_before.value_u, mpd_before.value_v),
            "avg_differing_token_length": avg_token_length,
        },
    )


def perturb_functional_dependency(
    lhs_values: Sequence[object], rhs_values: Sequence[object], epsilon: float
) -> PerturbationOutcome:
    """Drop minority rows from the smallest violating LHS groups (paper Section 3.4)."""
    before = fd_compliance_ratio(lhs_values, rhs_values)
    budget = _max_drop(len(lhs_values), epsilon)
    dropped = tuple(minority_violation_rows(lhs_values, rhs_values, max_rows=budget))

    dropped_set = set(dropped)
    remaining_lhs = [v for i, v in enumerate(lhs_values) if i not in dropped_set]
    remaining_rhs = [v for i, v in enumerate(rhs_values) if i not in dropped_set]
    theta_after = (
        fd_compliance_ratio(remaining_lhs, remaining_rhs).ratio
        if len(remaining_lhs) >= 2
        else _UNDEFINED_AFTER_HIGH
    )
    return PerturbationOutcome(
        theta_before=before.ratio,
        theta_after=theta_after,
        dropped_indices=dropped,
        evidence={"num_violating_rows": len(before.violating_row_indices)},
    )
