"""Shared helpers for metric-function implementations."""

from __future__ import annotations

from collections.abc import Iterable, Sized
from typing import TypeVar

_T = TypeVar("_T")


def drop_nulls(values: Iterable[_T | None]) -> list[_T]:
    """Remove ``None``/``NaN``-like values, preserving order.

    Real-world corpus columns routinely contain nulls; every metric function
    in this package treats "missing" as "not part of the domain" rather than
    a distinguished value, matching how the paper describes counting
    "num-total-values" and "num-distinct-values" (Section 3.3).
    """
    out: list[_T] = []
    for v in values:
        if v is None:
            continue
        if isinstance(v, float) and v != v:  # NaN check without importing math/numpy
            continue
        out.append(v)
    return out


def require_min_size(values: Sized, minimum: int, metric_name: str) -> None:
    from unidetect.exceptions import InsufficientDataError

    if len(values) < minimum:
        raise InsufficientDataError(
            f"{metric_name} requires at least {minimum} non-null values, got {len(values)}"
        )
