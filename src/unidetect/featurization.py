"""Featurization / corpus-subsetting (paper Section 2.2.2 and Figure 5).

Each error type projects a column (or column pair) onto a handful of
discrete dimensions; two items are considered part of the same "sub-cube"
``S^F_D(T)`` iff every dimension matches. Keeping buckets coarse and
monotonic is what makes the corpus-statistics table (``corpus/builder.py``)
tractable: it is one small ``GROUP BY`` over a bounded key space rather than
an explosion of near-unique keys.
"""

from __future__ import annotations

from collections.abc import Sequence

import numpy as np

from unidetect.core.enums import ColumnDataType, ErrorType
from unidetect.core.models import FeatureBucket
from unidetect.text_utils import infer_column_data_type, tokenize


def bucket_by_edges(value: float, edges: Sequence[int]) -> str:
    """Map ``value`` into one of ``len(edges) + 1`` half-open ranges.

    ``edges=(20, 50, 100)`` produces the ranges ``(-inf,20]``, ``(20,50]``,
    ``(50,100]``, ``(100,inf)`` -- matching the bucket notation used
    throughout the paper, e.g. ``{(0-20],(20-50],...,(1000-inf)}``.
    """
    lower: int | float = float("-inf")
    for edge in edges:
        if value <= edge:
            return f"({lower},{edge}]"
        lower = edge
    return f"({edges[-1]},inf)"


def bucket_row_count(num_rows: int, edges: Sequence[int]) -> str:
    return bucket_by_edges(num_rows, edges)


def bucket_leftness(column_index: int, max_explicit: int = 10) -> str:
    """Column position from the left (paper Sec. 3.3), capped to bound cardinality."""
    if column_index < 0:
        return "unknown"
    if column_index < max_explicit:
        return str(column_index)
    return f"{max_explicit}+"


def token_prevalence(values: Sequence[str], token_document_frequency: dict[str, int]) -> float:
    """``Prev(C)`` (paper Sec. 3.3): average, over values and their tokens, of how
    many corpus tables each token occurs in.

    ``token_document_frequency`` is expected to come from the pre-built
    token-statistics table (see ``corpus/ingestion.py``); tokens absent from
    it (never seen in the corpus) contribute 0, correctly pulling rare/novel
    tokens' average prevalence down.
    """
    scores: list[int] = []
    for v in values:
        for tok in tokenize(v):
            scores.append(token_document_frequency.get(tok.lower(), 0))
    if not scores:
        return 0.0
    return float(np.mean(scores))


def bucket_token_prevalence(prevalence: float, edges: Sequence[int]) -> str:
    return bucket_by_edges(prevalence, edges)


def bucket_token_length(avg_length: float, edges: Sequence[int]) -> str:
    return bucket_by_edges(avg_length, edges)


def log_transform_fits_better(values: Sequence[float]) -> bool:
    """Heuristic for the "whether logarithm-transform better fits the data" dimension.

    We compare the absolute skewness of the raw values against their
    log1p-transform (restricted to positive values) and prefer whichever is
    closer to a symmetric (skewness ~ 0) distribution -- a standard,
    parameter-free proxy for "this column is more naturally modeled on a log
    scale" (paper Sec. 3.1, citing [68]).
    """
    arr = np.asarray([v for v in values if v is not None], dtype=float)
    if len(arr) < 3 or np.any(arr <= 0):
        return False

    def _skew(x: np.ndarray) -> float:
        std = x.std()
        if std == 0:
            return 0.0
        return float(np.mean(((x - x.mean()) / std) ** 3))

    raw_skew = abs(_skew(arr))
    log_skew = abs(_skew(np.log1p(arr)))
    return log_skew < raw_skew


def build_uniqueness_bucket(
    *,
    values: Sequence[str],
    num_rows: int,
    column_index: int,
    token_document_frequency: dict[str, int],
    row_count_edges: Sequence[int],
    prevalence_edges: Sequence[int],
    error_type: ErrorType = ErrorType.UNIQUENESS,
) -> FeatureBucket:
    dtype = infer_column_data_type(values)
    prevalence = token_prevalence(values, token_document_frequency)
    dims = (
        ("data_type", dtype.value),
        ("row_count", bucket_row_count(num_rows, row_count_edges)),
        ("leftness", bucket_leftness(column_index)),
        ("prevalence", bucket_token_prevalence(prevalence, prevalence_edges)),
    )
    return FeatureBucket(error_type=error_type, dims=dims)


def build_functional_dependency_bucket(
    *,
    rhs_values: Sequence[str],
    num_rows: int,
    rhs_column_index: int,
    token_document_frequency: dict[str, int],
    row_count_edges: Sequence[int],
    prevalence_edges: Sequence[int],
) -> FeatureBucket:
    """FD reuses the uniqueness featurization, applied to the RHS column (Sec. 3.4)."""
    bucket = build_uniqueness_bucket(
        values=rhs_values,
        num_rows=num_rows,
        column_index=rhs_column_index,
        token_document_frequency=token_document_frequency,
        row_count_edges=row_count_edges,
        prevalence_edges=prevalence_edges,
        error_type=ErrorType.FUNCTIONAL_DEPENDENCY,
    )
    return bucket


def build_outlier_bucket(
    *, values: Sequence[float], num_rows: int, row_count_edges: Sequence[int]
) -> FeatureBucket:
    dims = (
        ("data_type", ColumnDataType.FLOAT.value),
        ("row_count", bucket_row_count(num_rows, row_count_edges)),
        ("log_fit", str(log_transform_fits_better(values))),
    )
    return FeatureBucket(error_type=ErrorType.NUMERIC_OUTLIER, dims=dims)


def build_spelling_bucket(
    *,
    values: Sequence[str],
    num_rows: int,
    avg_differing_token_length: float,
    row_count_edges: Sequence[int],
    token_length_edges: Sequence[int],
) -> FeatureBucket:
    dtype = infer_column_data_type(values)
    dims = (
        ("data_type", dtype.value),
        ("row_count", bucket_row_count(num_rows, row_count_edges)),
        ("token_length", bucket_token_length(avg_differing_token_length, token_length_edges)),
    )
    return FeatureBucket(error_type=ErrorType.SPELLING, dims=dims)
