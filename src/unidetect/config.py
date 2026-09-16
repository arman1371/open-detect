"""Central configuration for a Uni-Detect deployment.

A single :class:`UniDetectConfig` instance is threaded through corpus
building and detection so that both phases agree on significance levels,
perturbation budgets, and Unity Catalog table locations.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from unidetect.exceptions import ConfigurationError

#: Row-count buckets shared by every error type's featurization (paper Sec. 3.1-3.4).
DEFAULT_ROW_COUNT_EDGES: tuple[int, ...] = (20, 50, 100, 500, 1000)

#: Token-prevalence buckets used for Uniqueness/FD featurization (paper Sec. 3.3).
DEFAULT_PREVALENCE_EDGES: tuple[int, ...] = (50, 100, 1000, 10_000, 100_000)

#: Token-length buckets used for the spelling MPD featurization (paper Sec. 3.2).
DEFAULT_TOKEN_LENGTH_EDGES: tuple[int, ...] = (5, 10, 15, 20)


@dataclass(frozen=True)
class UnityCatalogLocation:
    """A fully-qualified Unity Catalog three-level namespace."""

    catalog: str
    schema: str

    def table(self, name: str) -> str:
        return f"{self.catalog}.{self.schema}.{name}"

    def __post_init__(self) -> None:
        for part, label in ((self.catalog, "catalog"), (self.schema, "schema")):
            if not part or not part.replace("_", "").isalnum():
                raise ConfigurationError(
                    f"Invalid Unity Catalog {label} name: {part!r}. "
                    "Use alphanumeric/underscore identifiers only."
                )


@dataclass(frozen=True)
class UniDetectConfig:
    """Tunable knobs for both the offline corpus builder and the online detectors.

    Parameters
    ----------
    location:
        Unity Catalog catalog/schema where corpus-statistics and (optionally)
        detection-result tables live.
    epsilon:
        Maximum perturbation size, expressed as a *fraction* of rows
        (``0 < epsilon <= 1``) for row-level error types (FD), or interpreted
        as "drop at most one offending value/row" for the column-level types
        (uniqueness, outliers, spelling), consistent with the paper's
        single-perturbation worked examples. See Definition 2.
    alpha:
        Significance level for the likelihood-ratio test (Definition 3). A
        candidate is flagged when ``lr_ratio <= alpha``.
    laplace_smoothing:
        Additive (Laplace/add-one) smoothing applied to both the numerator
        and denominator counts before dividing, so a bucket with zero corpus
        support never produces a division by zero or an artificially perfect
        ratio of exactly zero.
    max_mpd_block_size:
        Cap on the number of values compared pairwise within one spelling
        blocking bucket (see ``metrics/spelling.py``); keeps MPD computation
        near-linear on skewed columns without materially changing recall.
    corpus_stats_table:
        Name (unqualified) of the materialized corpus-statistics Delta table.
    token_stats_table:
        Name (unqualified) of the token-document-frequency Delta table used
        for the ``Prev(C)`` featurization dimension.
    detections_table:
        Name (unqualified) of the table detection results are optionally
        appended to.
    """

    location: UnityCatalogLocation
    epsilon: float = 0.01
    alpha: float = 0.05
    laplace_smoothing: float = 1.0
    max_mpd_block_size: int = 500
    max_fd_column_pairs_per_table: int = 200
    row_count_edges: tuple[int, ...] = field(default_factory=lambda: DEFAULT_ROW_COUNT_EDGES)
    prevalence_edges: tuple[int, ...] = field(default_factory=lambda: DEFAULT_PREVALENCE_EDGES)
    token_length_edges: tuple[int, ...] = field(default_factory=lambda: DEFAULT_TOKEN_LENGTH_EDGES)
    corpus_stats_table: str = "unidetect_corpus_stats"
    token_stats_table: str = "unidetect_token_stats"
    detections_table: str = "unidetect_detections"

    def __post_init__(self) -> None:
        if not 0 < self.epsilon <= 1:
            raise ConfigurationError(f"epsilon must be in (0, 1], got {self.epsilon}")
        if not 0 < self.alpha < 1:
            raise ConfigurationError(f"alpha must be in (0, 1), got {self.alpha}")
        if self.laplace_smoothing < 0:
            raise ConfigurationError("laplace_smoothing must be >= 0")
        if self.max_mpd_block_size < 2:
            raise ConfigurationError("max_mpd_block_size must be >= 2")
        if self.max_fd_column_pairs_per_table < 1:
            raise ConfigurationError("max_fd_column_pairs_per_table must be >= 1")

    @property
    def corpus_stats_fqn(self) -> str:
        return self.location.table(self.corpus_stats_table)

    @property
    def token_stats_fqn(self) -> str:
        return self.location.table(self.token_stats_table)

    @property
    def detections_fqn(self) -> str:
        return self.location.table(self.detections_table)
