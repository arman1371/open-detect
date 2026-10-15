"""Public, high-level API: :class:`UniDetect`.

This is the single entry point most users need:

>>> from open_detect import UniDetectConfig, UnityCatalogLocation
>>> from open_detect.algorithms.uni_detect.pipeline import UniDetect
>>> config = UniDetectConfig(location=UnityCatalogLocation("main", "data_quality"))
>>> ud = UniDetect(config)
>>> ud.build_corpus_statistics(table_names=my_corpus_tables)          # offline, run periodically
>>> detections = ud.detect(table_names=["main.sales.orders"])          # online, run per scan
>>> detections.show()
"""

from __future__ import annotations

from functools import reduce
from typing import TYPE_CHECKING

from open_detect.algorithms.uni_detect.catalog import ensure_schema_exists
from open_detect.algorithms.uni_detect.config import UniDetectConfig
from open_detect.algorithms.uni_detect.corpus.builder import CorpusStatsBuilder
from open_detect.algorithms.uni_detect.corpus.ingestion import CorpusIngestor
from open_detect.algorithms.uni_detect.detectors import (
    FunctionalDependencyDetector,
    NumericOutlierDetector,
    SpellingDetector,
    UniquenessDetector,
)
from open_detect.algorithms.uni_detect.spark_utils import get_spark
from open_detect.core.enums import ErrorType
from open_detect.exceptions import ConfigurationError, ValidationError
from open_detect.logging_utils import get_logger, log_duration

if TYPE_CHECKING:
    from collections.abc import Sequence

    from pyspark.sql import DataFrame, SparkSession

logger = get_logger(__name__)

_SINGLE_COLUMN_TYPES = (ErrorType.UNIQUENESS, ErrorType.NUMERIC_OUTLIER, ErrorType.SPELLING)
_TOKEN_DEPENDENT_TYPES = (ErrorType.UNIQUENESS, ErrorType.FUNCTIONAL_DEPENDENCY)


def _require_columns(columns_df: DataFrame | None) -> DataFrame:
    """Narrow ``columns_df`` to a DataFrame; unlike ``assert`` this survives ``python -O``."""
    if columns_df is None:
        raise ConfigurationError(
            "The ingested columns DataFrame is missing for a column-based error type; "
            "this indicates an inconsistent error_types selection."
        )
    return columns_df


class UniDetect:
    """Facade over the offline corpus builder and the four online detectors."""

    def __init__(self, config: UniDetectConfig, spark: SparkSession | None = None) -> None:
        self.config = config
        self.spark = spark or get_spark()
        self._detectors = {
            ErrorType.UNIQUENESS: UniquenessDetector(self.spark, config),
            ErrorType.NUMERIC_OUTLIER: NumericOutlierDetector(self.spark, config),
            ErrorType.SPELLING: SpellingDetector(self.spark, config),
            ErrorType.FUNCTIONAL_DEPENDENCY: FunctionalDependencyDetector(self.spark, config),
        }

    # ------------------------------------------------------------------
    # Offline: "learning" phase (paper Sec. 2.2.3)
    # ------------------------------------------------------------------
    def build_corpus_statistics(
        self,
        table_names: Sequence[str],
        error_types: Sequence[ErrorType] | None = None,
        create_schema: bool = True,
    ) -> None:
        """Materialize corpus statistics for ``table_names`` (the background corpus ``T``).

        Idempotent per error type: each call only overwrites the
        ``error_type`` partitions it touches, so callers can incrementally
        (re)build one error type at a time, or refresh the whole corpus by
        passing every :class:`~open_detect.core.enums.ErrorType`.

        ``table_names`` is typically produced by
        :func:`open_detect.algorithms.uni_detect.catalog.list_tables_matching` -- e.g. "every table
        in this catalog" -- playing the role the paper's 100M-table web
        crawl plays for its statistics.
        """
        error_types = tuple(error_types) if error_types else tuple(ErrorType)
        if create_schema:
            ensure_schema_exists(self.spark, self.config.location)

        builder = CorpusStatsBuilder(self.spark, self.config)
        ingestor = CorpusIngestor(
            self.spark,
            max_values_per_column=self.config.max_mpd_block_size * 200,
            max_fd_column_pairs_per_table=self.config.max_fd_column_pairs_per_table,
        )

        columns_df = None
        token_map: dict[str, int] = {}
        needs_columns = any(et in _SINGLE_COLUMN_TYPES for et in error_types)
        needs_tokens = any(et in _TOKEN_DEPENDENT_TYPES for et in error_types)

        if needs_columns or needs_tokens:
            with log_duration(logger, "ingest_columns"):
                columns_df = ingestor.ingest_columns(table_names).cache()
                columns_df.count()  # materialize the cache deterministically

        if needs_tokens:
            with log_duration(logger, "build_token_stats"):
                token_stats = ingestor.build_token_stats(_require_columns(columns_df))
                token_stats.write.format("delta").mode("overwrite").saveAsTable(
                    self.config.token_stats_fqn
                )
                token_map = {
                    row["token"]: int(row["doc_frequency"])
                    for row in self.spark.table(self.config.token_stats_fqn).collect()
                }

        for error_type in error_types:
            if error_type is ErrorType.UNIQUENESS:
                stats = builder.build_uniqueness_stats(_require_columns(columns_df), token_map)
            elif error_type is ErrorType.NUMERIC_OUTLIER:
                stats = builder.build_outlier_stats(_require_columns(columns_df))
            elif error_type is ErrorType.SPELLING:
                stats = builder.build_spelling_stats(_require_columns(columns_df))
            elif error_type is ErrorType.FUNCTIONAL_DEPENDENCY:
                pairs_df = ingestor.ingest_column_pairs(table_names)
                stats = builder.build_fd_stats(pairs_df, token_map)
            else:  # pragma: no cover - exhaustive over ErrorType
                raise ValidationError(f"Unknown error type: {error_type}")
            builder.write(stats, mode="overwrite", error_types=[error_type])

        if columns_df is not None:
            columns_df.unpersist()

    # ------------------------------------------------------------------
    # Online: detection phase
    # ------------------------------------------------------------------
    def detect(
        self,
        table_names: Sequence[str],
        error_types: Sequence[ErrorType] | None = None,
    ) -> DataFrame:
        """Score ``table_names`` for the requested error types and rank all results together.

        Returns a single DataFrame unioning every requested detector's
        output, sorted ascending by ``lr_ratio`` (Definition 3: smaller is
        more surprising, i.e. more likely a real error).
        """
        from pyspark.sql import functions as F

        error_types = tuple(error_types) if error_types else tuple(ErrorType)
        frames = [self._detectors[et].detect(table_names) for et in error_types]
        result = reduce(lambda a, b: a.unionByName(b), frames)
        return result.orderBy(F.col("lr_ratio").asc())

    def write_detections(self, detections: DataFrame, mode: str = "append") -> None:
        """Append (or overwrite) a detection result set to the configured UC table."""
        detections.write.format("delta").mode(mode).saveAsTable(self.config.detections_fqn)
