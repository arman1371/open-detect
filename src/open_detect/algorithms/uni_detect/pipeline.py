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

from contextlib import suppress
from typing import TYPE_CHECKING, Any

from pyspark import StorageLevel

from open_detect.algorithms.uni_detect.catalog import ensure_schema_exists
from open_detect.algorithms.uni_detect.config import UniDetectConfig
from open_detect.algorithms.uni_detect.core.enums import ErrorType
from open_detect.algorithms.uni_detect.corpus.builder import CorpusStatsBuilder
from open_detect.algorithms.uni_detect.corpus.ingestion import (
    INGESTION_REPARTITION_FACTOR,
    CorpusIngestor,
)
from open_detect.algorithms.uni_detect.detectors import (
    FunctionalDependencyDetector,
    NumericOutlierDetector,
    SpellingDetector,
    UniquenessDetector,
)
from open_detect.algorithms.uni_detect.spark_utils import get_spark
from open_detect.exceptions import ConfigurationError, ValidationError
from open_detect.logging_utils import get_logger, log_duration

if TYPE_CHECKING:
    from collections.abc import Sequence

    from pyspark.sql import DataFrame, SparkSession

logger = get_logger(__name__)

_SINGLE_COLUMN_TYPES = (ErrorType.UNIQUENESS, ErrorType.NUMERIC_OUTLIER, ErrorType.SPELLING)
_TOKEN_DEPENDENT_TYPES = (ErrorType.UNIQUENESS, ErrorType.FUNCTIONAL_DEPENDENCY)
# Types that need numeric columns only (outlier)
_NUMERIC_ONLY_TYPES = (ErrorType.NUMERIC_OUTLIER,)
# Types that need non-numeric columns only (spelling)
_NON_NUMERIC_ONLY_TYPES = (ErrorType.SPELLING,)


def _require_columns(columns_df: DataFrame | None) -> DataFrame:
    """Narrow ``columns_df`` to a DataFrame; unlike ``assert`` this survives ``python -O``."""
    if columns_df is None:
        raise ConfigurationError(
            "The ingested columns DataFrame is missing for a column-based error type; "
            "this indicates an inconsistent error_types selection."
        )
    return columns_df


def _filter_by_column_type(columns_df: DataFrame, error_type: ErrorType) -> DataFrame:
    """Filter columns by their inferred data type for the given error type."""
    from pyspark.sql import functions as F

    from open_detect.algorithms.uni_detect.core.enums import ColumnDataType

    numeric_types = {ColumnDataType.INTEGER, ColumnDataType.FLOAT}
    if error_type in _NUMERIC_ONLY_TYPES:
        # Numeric outlier: only integer, float columns
        return columns_df.where(F.col("column_data_type").isin([t.value for t in numeric_types]))
    elif error_type in _NON_NUMERIC_ONLY_TYPES:
        # Spelling: only string, mixed_alphanumeric columns (not numeric)
        return columns_df.where(~F.col("column_data_type").isin([t.value for t in numeric_types]))
    # Uniqueness and FD: all types
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

    def _validate_inputs(
        self,
        table_names: Sequence[str] | None = None,
        error_types: Sequence[ErrorType] | None = None,
        **kwargs: Any,
    ) -> None:
        """Run shared validation before the online detection phase."""
        from open_detect.validation import _ensure_sequence_of_str, _reject_unknown_kwargs

        _reject_unknown_kwargs(
            kwargs,
            allowed={"table_names", "error_types"},
            param_name="detect",
        )
        if table_names is not None:
            _ensure_sequence_of_str(table_names, "table_names")
        if error_types is not None:
            _ensure_sequence_of_str(error_types, "error_types")

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
        passing every :class:`~open_detect.algorithms.uni_detect.core.enums.ErrorType`.

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
        pairs_df = None
        token_map: dict[str, int] = {}
        needs_columns = any(et in _SINGLE_COLUMN_TYPES for et in error_types)
        needs_pairs = ErrorType.FUNCTIONAL_DEPENDENCY in error_types
        needs_tokens = any(et in _TOKEN_DEPENDENT_TYPES for et in error_types)

        # Use single-scan ingestion with pairs when both columns and pairs are needed
        if (needs_columns or needs_tokens) and needs_pairs:
            with log_duration(logger, "ingest_columns_with_pairs"):
                columns_df, pairs_df = ingestor.ingest_columns_with_pairs(table_names)
                if columns_df is not None:
                    columns_df = columns_df.persist(StorageLevel.DISK_ONLY)
                    columns_df.count()  # materialize the cache deterministically
                if pairs_df is not None:
                    pairs_df = pairs_df.persist(StorageLevel.DISK_ONLY)
                    pairs_df.count()  # materialize the cache deterministically
        elif needs_columns or needs_tokens:
            with log_duration(logger, "ingest_columns"):
                columns_df = ingestor.ingest_columns(table_names).persist(StorageLevel.DISK_ONLY)
                columns_df.count()  # materialize the cache deterministically
        elif needs_pairs:
            with log_duration(logger, "ingest_column_pairs"):
                pairs_df = ingestor.ingest_column_pairs(table_names).persist(StorageLevel.DISK_ONLY)
                pairs_df.count()  # materialize the cache deterministically

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
                filtered_columns = _filter_by_column_type(_require_columns(columns_df), error_type)
                stats = builder.build_uniqueness_stats(filtered_columns, token_map)
            elif error_type is ErrorType.NUMERIC_OUTLIER:
                filtered_columns = _filter_by_column_type(_require_columns(columns_df), error_type)
                stats = builder.build_outlier_stats(filtered_columns)
            elif error_type is ErrorType.SPELLING:
                filtered_columns = _filter_by_column_type(_require_columns(columns_df), error_type)
                stats = builder.build_spelling_stats(filtered_columns)
            elif error_type is ErrorType.FUNCTIONAL_DEPENDENCY:
                # pairs_df is already available from single-scan ingestion
                assert pairs_df is not None, "pairs_df must be available for FUNCTIONAL_DEPENDENCY"
                stats = builder.build_fd_stats(pairs_df, token_map)
            else:  # pragma: no cover - exhaustive over ErrorType
                raise ValidationError(f"Unknown error type: {error_type}")
            builder.write(stats, mode="overwrite", error_types=[error_type])

        if columns_df is not None:
            columns_df.unpersist()
        if pairs_df is not None:
            pairs_df.unpersist()

    # ------------------------------------------------------------------
    # Online: detection phase
    # ------------------------------------------------------------------
    def detect(
        self,
        table_names: Sequence[str],
        error_types: Sequence[ErrorType] | None = None,
        ingested_columns_df: DataFrame | None = None,
        ingested_pairs_df: DataFrame | None = None,
        **kwargs: Any,
    ) -> DataFrame:
        """Score ``table_names`` for the requested error types and rank all results together.

        Returns a single DataFrame unioning every requested detector's
        output, sorted ascending by ``lr_ratio`` (Definition 3: smaller is
        more surprising, i.e. more likely a real error).

        The returned DataFrame is persisted and materialized once.  After
        the caller finishes using the result they should call :meth:`release`
        on the ``UniDetect`` instance to free the cached detector frames.

        Parameters
        ----------
        table_names:
            Tables to scan for errors.
        error_types:
            Which error types to detect. Defaults to all four.
        ingested_columns_df:
            Pre-ingested columns DataFrame from a shared ingestion call.
            If provided, detectors will use this instead of re-ingesting.
            If not provided, ingestion happens ONCE per detect() call and is shared
            across all detectors (requirement 5).
        ingested_pairs_df:
            Pre-ingested column pairs DataFrame for FD detection.
            If provided, FD detector will use this instead of re-ingesting.
            If not provided, FD pairs are built from the shared single-scan ingestion.

        Raises
        ------
        ValidationError
            If ``kwargs`` contains unrecognised parameters, or if
            ``table_names`` / ``error_types`` are not a sequence of ``str``.
        """
        self._validate_inputs(table_names=table_names, error_types=error_types, **kwargs)

        from pyspark.sql import functions as F

        from open_detect.algorithms.uni_detect.spark_utils import (
            ARROW_MAX_RECORDS_PER_BATCH,
            ARROW_MAX_RECORDS_PER_BATCH_KEY,
            scoped_conf,
        )

        error_types = tuple(error_types) if error_types else tuple(ErrorType)
        frames = []
        result = None
        # Ingested DataFrames that we created and need to unpersist at the end
        _shared_columns_df = None
        _shared_pairs_df = None
        try:
            # Keep Arrow limit active through ALL detector operations:
            # extract_candidates (mapInPandas), candidate materialization (count),
            # scoring (batch_score join), and result materialization.
            with scoped_conf(
                self.spark,
                **{ARROW_MAX_RECORDS_PER_BATCH_KEY: str(ARROW_MAX_RECORDS_PER_BATCH)},
            ):
                # Ingest once and share across all detectors (requirement 5).
                # If caller provided pre-ingested DataFrames, use those.
                # Otherwise, perform single-scan ingestion and share across detectors.
                if ingested_columns_df is not None or ingested_pairs_df is not None:
                    # Backward compatible: caller provided pre-ingested DataFrames
                    columns_df = ingested_columns_df
                    pairs_df = ingested_pairs_df
                else:
                    # New behavior: ingest once, share across all detectors
                    ingestor = CorpusIngestor(
                        self.spark,
                        max_values_per_column=self.config.max_mpd_block_size * 200,
                        max_fd_column_pairs_per_table=self.config.max_fd_column_pairs_per_table,
                    )
                    # Check if any detector needs column data (uniqueness, outlier, spelling)
                    needs_columns = any(et in _SINGLE_COLUMN_TYPES for et in error_types)
                    # Check if FD detector is requested
                    needs_pairs = ErrorType.FUNCTIONAL_DEPENDENCY in error_types

                    if needs_columns and needs_pairs:
                        # Both columns and pairs needed - use single-scan ingestion with pairs
                        columns_df, pairs_df = ingestor.ingest_columns_with_pairs(table_names)
                    elif needs_columns:
                        # Only columns needed
                        columns_df = ingestor.ingest_columns(table_names)
                        pairs_df = None
                    elif needs_pairs:
                        # Only pairs needed - ingest pairs directly
                        columns_df = None
                        pairs_df = ingestor.ingest_column_pairs(table_names)
                    else:
                        columns_df = None
                        pairs_df = None

                    # Repartition to spread work across cores (requirement 4) and persist DISK_ONLY
                    if columns_df is not None:
                        default_parallelism = self.spark.sparkContext.defaultParallelism
                        target_partitions = default_parallelism * INGESTION_REPARTITION_FACTOR
                        columns_df = columns_df.repartition(target_partitions)
                        columns_df = columns_df.persist(StorageLevel.DISK_ONLY)
                        columns_df.count()  # materialize cache
                        _shared_columns_df = columns_df

                    if pairs_df is not None:
                        default_parallelism = self.spark.sparkContext.defaultParallelism
                        target_partitions = default_parallelism * INGESTION_REPARTITION_FACTOR
                        pairs_df = pairs_df.repartition(target_partitions)
                        pairs_df = pairs_df.persist(StorageLevel.DISK_ONLY)
                        pairs_df.count()  # materialize cache
                        _shared_pairs_df = pairs_df

                for et in error_types:
                    frame = self._detectors[et].detect(
                        table_names,
                        ingested_columns_df=columns_df,
                        ingested_pairs_df=pairs_df,
                    )
                    frames.append(frame)
                # Balanced union (not left-deep reduce) so the final merge plan is
                # ceil(log2(N)) deep regardless of how many detectors are enabled.
                # Using balanced_union from ingestion module for consistency.
                from open_detect.algorithms.uni_detect.corpus.ingestion import (
                    balanced_union,
                )

                result = balanced_union(frames)
                # Order first, then persist and materialize the *final* frame.  Sorting
                # after persist() would return an unpersisted frame, so the caller's
                # count/show/write would re-execute the scoring stage to re-materialize
                # it -- the very thing this cache lifecycle exists to prevent.
                # The per-detector caches are released only after the union is cached.
                result = result.orderBy(F.col("lr_ratio").asc())
                result = result.persist(StorageLevel.DISK_ONLY)
                result.count()
                return result
        except Exception:
            # Clean up detector results on failure - this includes any frames
            # already returned by detector.detect() calls.
            for frame in frames:
                with suppress(Exception):
                    frame.unpersist()
            # Clean up the unioned result frame if it was created but failed
            if result is not None:
                with suppress(Exception):
                    result.unpersist()
            raise
        finally:
            # Release per-detector caches (scored, joined, result frames) now that
            # the unioned result is materialized.  Must run on both success and
            # error to avoid memory leaks from accumulated persisted frames.
            for detector in (self._detectors[et] for et in error_types):
                detector.release()
            # Unpersist shared ingestion DataFrames we created
            if _shared_columns_df is not None:
                with suppress(Exception):
                    _shared_columns_df.unpersist()
            if _shared_pairs_df is not None:
                with suppress(Exception):
                    _shared_pairs_df.unpersist()

    def release(self) -> None:
        """Release all cached detector resources.

        After calling :meth:`detect` the underlying detectors keep persisted
        frames in memory (``_persisted``).  Call this method when the result is
        no longer needed to avoid memory leaks.
        """
        for detector in self._detectors.values():
            detector.release()

    def write_detections(self, detections: DataFrame, mode: str = "append") -> None:
        """Append (or overwrite) a detection result set to the configured UC table."""
        detections.write.format("delta").mode(mode).saveAsTable(self.config.detections_fqn)
