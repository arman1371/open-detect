"""FD-compliance-ratio metric (paper Section 3.4, ``FR``).

Note on fidelity to the paper: the published formula for ``FR`` renders with
a dropped comparison operator in the extracted text (a known artifact of
academic PDF math -- subscripts/relational operators are frequently lost).
We implement the standard, well-established *row-based* compliance ratio
consistent with the paper's own framing ("Like the UR metric function for
Uniqueness, an FR closer to 1 indicates likely FD violations") and with the
`Conforming-row-ratio` baseline it is compared against in Section 4.2:

    FR_D(Cl, Cr) = |{u in D : for all v in D, u(Cl) = v(Cl) => u(Cr) = v(Cr)}|
                   -------------------------------------------------------
                                        |D|

i.e. the fraction of rows whose left-hand-side group is internally
consistent on the right-hand side. FR = 1 iff the FD holds exactly; FR close
to (but below) 1 is the "almost-FD" signal the paper's uniform treatment of
near-constraint-satisfaction is built on.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Sequence
from dataclasses import dataclass

from unidetect.metrics.base import require_min_size


@dataclass(frozen=True, slots=True)
class FDResult:
    ratio: float
    violating_row_indices: tuple[int, ...]
    """Rows belonging to an LHS group with more than one distinct RHS value."""


def fd_compliance_ratio(lhs_values: Sequence[object], rhs_values: Sequence[object]) -> FDResult:
    if len(lhs_values) != len(rhs_values):
        raise ValueError("lhs_values and rhs_values must be the same length")
    require_min_size(lhs_values, 2, "fd_compliance_ratio")

    groups: dict[object, dict[object, list[int]]] = defaultdict(lambda: defaultdict(list))
    for i, (lhs, rhs) in enumerate(zip(lhs_values, rhs_values, strict=True)):
        if lhs is None:
            continue
        groups[lhs][rhs].append(i)

    total = sum(len(idxs) for rhs_map in groups.values() for idxs in rhs_map.values())
    if total == 0:
        raise ValueError("fd_compliance_ratio found no non-null LHS values")

    violating: list[int] = []
    conforming = 0
    for rhs_map in groups.values():
        group_size = sum(len(idxs) for idxs in rhs_map.values())
        if len(rhs_map) == 1:
            conforming += group_size
        else:
            for idxs in rhs_map.values():
                violating.extend(idxs)

    ratio = conforming / total
    violating.sort()
    return FDResult(ratio=ratio, violating_row_indices=tuple(violating))


def minority_violation_rows(
    lhs_values: Sequence[object], rhs_values: Sequence[object], max_rows: int
) -> list[int]:
    """Rows to drop to repair the *smallest* FD-violating groups first.

    For each LHS group with more than one distinct RHS value, keeps the
    majority RHS value and marks the minority rows for removal -- the
    natural perturbation described in Section 3.4 ("drop rows in suspected
    violations"). Smallest violating groups (by total group size) are
    prioritized so a small ``epsilon`` budget targets the most localized,
    least ambiguous violations first.
    """
    groups: dict[object, dict[object, list[int]]] = defaultdict(lambda: defaultdict(list))
    for i, (lhs, rhs) in enumerate(zip(lhs_values, rhs_values, strict=True)):
        if lhs is None:
            continue
        groups[lhs][rhs].append(i)

    violating_groups = [(lhs, rhs_map) for lhs, rhs_map in groups.items() if len(rhs_map) > 1]
    violating_groups.sort(key=lambda item: sum(len(v) for v in item[1].values()))

    to_drop: list[int] = []
    for _lhs, rhs_map in violating_groups:
        ordered = sorted(rhs_map.values(), key=len, reverse=True)
        for idxs in ordered[1:]:
            to_drop.extend(idxs)
            if len(to_drop) >= max_rows:
                return to_drop[:max_rows]
    return to_drop
