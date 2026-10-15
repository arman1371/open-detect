"""Per-error-type instantiations of epsilon-perturbation (paper Definition 2).

Each function here performs the "hypothetically remove a small subset O and
recompute the metric" step described in Section 2.2.1, for one of the four
error classes. The output (:class:`PerturbationOutcome`) carries everything
a detector needs to build a :class:`~open_detect.core.models.Candidate`:
theta_before/theta_after, which rows/values were removed, and small bits of
evidence for explainability.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field
from math import ceil
from typing import Any

from open_detect.algorithms.uni_detect.metrics.functional_dependency import (
    fd_compliance_ratio,
    minority_violation_rows,
)
from open_detect.algorithms.uni_detect.metrics.outliers import finite_floats, max_mad
from open_detect.algorithms.uni_detect.metrics.spelling import (
    differing_token_lengths,
    min_pairwise_edit_distance,
)
from open_detect.algorithms.uni_detect.metrics.uniqueness import (
    duplicate_value_indices,
    uniqueness_ratio,
)

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
    """Source row ids of the dropped cells.

    With ``row_ids=None`` these are positions in the caller's input sequence (nulls
    included), i.e. ``row_ids`` defaults to ``range(len(values))``.
    """
    evidence: dict[str, Any] = field(default_factory=dict)


def _max_drop(n: int, epsilon: float) -> int:
    return max(1, ceil(epsilon * n))


def _resolve_row_ids(n: int, row_ids: Sequence[int] | None) -> Sequence[int]:
    """Source row ids for ``n`` input values: ``row_ids`` if given, else ``0..n-1``."""
    if row_ids is None:
        return range(n)
    if len(row_ids) != n:
        raise ValueError(f"row_ids has {len(row_ids)} entries but there are {n} values")
    return row_ids


def perturb_uniqueness(
    values: Sequence[object], epsilon: float, row_ids: Sequence[int] | None = None
) -> PerturbationOutcome:
    """Drop duplicate occurrences (paper Example 2).

    ``row_ids`` (parallel to ``values``) are the source row ids reported in
    ``dropped_indices``; by default they are positions in ``values``.
    """
    ids = _resolve_row_ids(len(values), row_ids)
    theta_before = uniqueness_ratio(values)
    all_dupes = duplicate_value_indices(values)
    budget = _max_drop(len(values), epsilon)
    dropped_positions = all_dupes[:budget]
    dropped = tuple(ids[i] for i in dropped_positions)

    dropped_position_set = set(dropped_positions)
    remaining = [v for i, v in enumerate(values) if i not in dropped_position_set]
    theta_after = uniqueness_ratio(remaining) if len(remaining) >= 2 else _UNDEFINED_AFTER_HIGH
    return PerturbationOutcome(
        theta_before=theta_before,
        theta_after=theta_after,
        dropped_indices=dropped,
        evidence={"num_duplicate_values": len(all_dupes)},
    )


def perturb_numeric_outlier(
    values: Sequence[float], epsilon: float, row_ids: Sequence[int] | None = None
) -> PerturbationOutcome:
    """Drop the single most outlying value by MAD-score (paper Section 3.1).

    Non-finite values (NaN, +/-inf, including string forms) and nulls are filtered out
    once up front; ``dropped_indices`` holds the dropped value's source row id (its
    position in ``values`` unless ``row_ids`` is given). With fewer than two finite
    values there is nothing to score, so a no-perturbation outcome (no dropped indices,
    both thetas 0.0) is returned.
    """
    ids = _resolve_row_ids(len(values), row_ids)
    clean, positions = finite_floats(values)
    if len(clean) < 2:
        return PerturbationOutcome(
            theta_before=_UNDEFINED_AFTER_LOW,
            theta_after=_UNDEFINED_AFTER_LOW,
            dropped_indices=(),
        )
    result = max_mad(clean)
    remaining = [v for i, v in enumerate(clean) if i != result.index]
    theta_after = max_mad(remaining).score if len(remaining) >= 2 else _UNDEFINED_AFTER_LOW
    return PerturbationOutcome(
        theta_before=result.score,
        theta_after=theta_after,
        dropped_indices=(ids[positions[result.index]],),
        evidence={"outlier_value": result.value},
    )


def perturb_spelling(
    values: Sequence[object],
    epsilon: float,
    max_block_size: int = 500,
    row_ids: Sequence[int] | None = None,
) -> PerturbationOutcome:
    """Drop the closest (min edit-distance) pair's first value (paper Section 3.2).

    MPD is taken over distinct values, so every occurrence of the dropped value is
    removed and ``dropped_indices`` lists all of them (ascending) as source row ids --
    positions in ``values`` (nulls included) unless ``row_ids`` is given.
    """
    ids = _resolve_row_ids(len(values), row_ids)
    mpd_before = min_pairwise_edit_distance(values, max_block_size=max_block_size)
    dropped = tuple(
        ids[i] for i, v in enumerate(values) if v is not None and str(v) == mpd_before.value_u
    )
    remaining = [str(v) for v in values if v is not None and str(v) != mpd_before.value_u]
    mpd_after: float
    if len(set(remaining)) >= 2:
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
        dropped_indices=dropped,
        evidence={
            "pair": (mpd_before.value_u, mpd_before.value_v),
            "avg_differing_token_length": avg_token_length,
        },
    )


def perturb_functional_dependency(
    lhs_values: Sequence[object],
    rhs_values: Sequence[object],
    epsilon: float,
    row_ids: Sequence[int] | None = None,
) -> PerturbationOutcome:
    """Drop minority rows from the smallest violating LHS groups (paper Section 3.4).

    ``dropped_indices`` are source row ids (parallel to the value sequences; positions
    by default).
    """
    ids = _resolve_row_ids(len(lhs_values), row_ids)
    before = fd_compliance_ratio(lhs_values, rhs_values)
    budget = _max_drop(len(lhs_values), epsilon)
    dropped_positions = minority_violation_rows(lhs_values, rhs_values, max_rows=budget)
    dropped = tuple(ids[i] for i in dropped_positions)

    dropped_set = set(dropped_positions)
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
