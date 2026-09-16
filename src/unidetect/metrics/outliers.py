"""Numeric-outlier metrics: MAD / SD dispersion and max-MAD scoring.

See paper Section 3.1, Equations (6)-(10).
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

import numpy as np

from unidetect.metrics.base import drop_nulls, require_min_size

#: Guards against a degenerate MAD of exactly zero (e.g. a column that is
#: constant except for one value), which would make every deviation score
#: infinite. The paper does not address this edge case explicitly; we fall
#: back to a small epsilon derived from the data's own scale.
_MIN_MAD_FLOOR = 1e-9


@dataclass(frozen=True, slots=True)
class MADResult:
    median: float
    mad: float


def median_absolute_deviation(values: Sequence[float]) -> MADResult:
    """``MAD(C) = median(|v - median(C)|)`` -- Equation (7)."""
    clean = np.asarray(drop_nulls(list(values)), dtype=float)
    require_min_size(clean, 2, "median_absolute_deviation")
    med = float(np.median(clean))
    mad = float(np.median(np.abs(clean - med)))
    return MADResult(median=med, mad=mad)


def mad_scores(values: Sequence[float]) -> np.ndarray:
    """Per-value ``score_MAD(v, C) = |v - median(C)| / MAD(C)`` -- Equation (9)."""
    clean = np.asarray(drop_nulls(list(values)), dtype=float)
    require_min_size(clean, 2, "mad_scores")
    result = median_absolute_deviation(clean.tolist())
    denom = max(result.mad, _MIN_MAD_FLOOR)
    return np.abs(clean - result.median) / denom


def sd_scores(values: Sequence[float]) -> np.ndarray:
    """Per-value ``score_SD(v, C) = |v - mean(C)| / SD(C)`` -- Equation (8)."""
    clean = np.asarray(drop_nulls(list(values)), dtype=float)
    require_min_size(clean, 2, "sd_scores")
    mean = float(np.mean(clean))
    sd = float(np.std(clean, ddof=1)) if len(clean) > 1 else 0.0
    denom = max(sd, _MIN_MAD_FLOOR)
    return np.abs(clean - mean) / denom


@dataclass(frozen=True, slots=True)
class MaxMADResult:
    score: float
    index: int
    """Index into the *null-dropped* input array of the most outlying value."""
    value: float


def max_mad(values: Sequence[float]) -> MaxMADResult:
    """``max-MAD(C) = max_v score_MAD(v, C)`` -- Equation (10).

    Returns both the score and the offending value's position so callers can
    perform the natural perturbation of dropping it (paper Section 3.1:
    "we naturally drop the suspected outlier, which is the value with the
    highest Score_MAD").
    """
    clean = drop_nulls(list(values))
    require_min_size(clean, 2, "max_mad")
    scores = mad_scores(clean)
    idx = int(np.argmax(scores))
    return MaxMADResult(score=float(scores[idx]), index=idx, value=float(clean[idx]))
