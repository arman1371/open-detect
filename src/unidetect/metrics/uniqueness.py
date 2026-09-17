"""Uniqueness-ratio metric (paper Section 3.3, ``UR``)."""

from __future__ import annotations

from collections.abc import Sequence

from unidetect.metrics.base import drop_nulls, require_min_size


def uniqueness_ratio(values: Sequence[object]) -> float:
    """``UR(C) = num-distinct-values(C) / num-total-values(C)``.

    A ``UR`` close to 1.0 means the column is *almost* unique -- the
    conventional (and, per the paper, over-eager) signal for a uniqueness
    constraint violation. Uni-Detect uses this same metric but reasons about
    its surprisingness via the corpus rather than thresholding it directly.
    """
    clean = drop_nulls(values)
    require_min_size(clean, 2, "uniqueness_ratio")
    return len(set(clean)) / len(clean)


def duplicate_value_indices(values: Sequence[object]) -> list[int]:
    """Indices of values that participate in at least one duplicate group.

    This is the natural perturbation target for uniqueness (paper Example 2:
    "since the duplicate values are suspected errors, for perturbation we can
    naturally drop duplicate values"). We return *all* but one occurrence of
    each duplicated value, smallest duplicate groups first, so a caller can
    truncate to the configured perturbation budget ``epsilon``.
    """
    clean_indexed = [(i, v) for i, v in enumerate(values) if v is not None]
    seen: dict[object, list[int]] = {}
    for i, v in clean_indexed:
        seen.setdefault(v, []).append(i)

    duplicate_groups = [idxs for idxs in seen.values() if len(idxs) > 1]
    # Smallest groups (fewest extra duplicates) are the "cheapest" perturbation
    # and most consistent with epsilon being a small budget.
    duplicate_groups.sort(key=len)

    to_drop: list[int] = []
    for idxs in duplicate_groups:
        # keep the first occurrence, drop the rest
        to_drop.extend(idxs[1:])
    return to_drop
