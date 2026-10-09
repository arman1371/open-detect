"""Impurity and per-column FPR (paper Equations 1-3).

``Imp_D(h)`` is the fraction of a data column's values that the hypothesis
pattern ``h`` does not cover. Because the corpus columns are assumed to come
from the same domain as the query column, the paper equates this with the
expected false-positive rate (Eqn 3), so the two functions here compute the
same number under two names.
"""

from __future__ import annotations

from collections.abc import Sequence

from open_detect.algorithms.auto_validate.hierarchy import matches


def impurity(pattern: str, values: Sequence[str]) -> float:
    """``Imp_D(h)`` (Eqn 1): the fraction of ``values`` that ``pattern`` does not match.

    Computed over every value in ``values``, counting duplicates with their
    multiplicity -- the definition's denominator is the column's value count,
    not its distinct-value count. Returns ``0.0`` for an empty column, which
    has no values to violate the pattern.
    """
    if not values:
        return 0.0
    non_matching = sum(1 for value in values if not matches(pattern, value))
    return non_matching / len(values)


def fpr_column(pattern: str, values: Sequence[str]) -> float:
    """``FPR_D(h)`` (Eqns 2-3), which the paper shows equals ``Imp_D(h)``.

    The paper derives this by noting that ``TN_D(h) + FP_D(h) = |D|`` for a
    column drawn from the same domain, so the two definitions coincide; this
    is a named alias rather than a second implementation, so the equality
    cannot drift.
    """
    return impurity(pattern, values)
