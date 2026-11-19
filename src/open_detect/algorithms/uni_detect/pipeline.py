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
from open_detect.algorithms.uni_detect.corpus.ingestion import CorpusIngestor, balanced_union
from open_detect.algorithms.uni_detect.detectors import (
    FunctionalDependencyDetector,
    NumericOutlierDetector,
    SpellingDetector,
    UniquenessDetector,
)
from open_detect.algorithms.uni_detect.spark_utils import get_spark
from open_detect.exceptions import ConfigurationError, ValidationError
from open_detect.logging_utils import get_logger, log_duration
from open_detect.notifications.config import get_notification_config

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


def _should_notify_severity(severity: str, threshold: str) -> bool:
    """Check if a severity level meets the notification threshold."""
    severity_order = {"low": 0, "medium": 1, "high": 2, "critical": 3}
    threshold_order = {"low": 0, "medium": 1, "high": 2, "critical": 3}
    return severity_order.get(severity, 0) >= threshold_order.get(threshold, 1)


def _build_teams_affected_summary(
    error_type: ErrorType,
    candidates_count: int,
    description: str | None = None,
) -> str:
    """Build a human-readable summary of affected areas for Teams notification.

    Args:
        error_type: The type of detection error
        candidates_count: Number of candidates found
        description: Optional additional description

    Returns:
        Human-readable summary string
    """
    type_names = {
        "uniqueness": "Uniqueness",
        "numeric_outlier": "Numeric Outlier",
        "spelling": "Spelling",
        "functional_dependency": "Functional Dependency",
    }
    type_name = type_names.get(error_type.value, error_type.value.title())

    if candidates_count == 0:
        return f"{type_name} detection - no specific anomalies found"

    if description:
        return f"{type_name} detection: {description}"

    return f"{type_name} detection - {candidates_count} anomaly(ies) detected"


def _send_teams_notification(
    webhook_url: str,
    event_type: str,
    severity: str,
    affected: str,
    timestamp: str,
    description: str | None = None,
) -> bool:
    """Send a Teams notification, returning True if successful.

    This function is designed to be non-blocking - it should be called from
    a background thread or the caller is responsible for handling it appropriately.

    Args:
        webhook_url: Microsoft Teams webhook URL
        event_type: Type of detection event
        severity: Severity level (low, medium, high, critical)
        affected: Description of affected nodes/patterns
        timestamp: When the event occurred
        description: Optional additional description

    Returns:
        True if notification was sent successfully, False otherwise
    """

    import requests

    from open_detect.logging_utils import get_logger

    logger = get_logger(__name__)

    # Build adaptive card payload
    color_map = {
        "low": "green",
        "medium": "yellow",
        "high": "orange",
        "critical": "red",
    }
    color = color_map.get(severity, "yellow")

    card = {
        "type": "message",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "type": "AdaptiveCard",
                    "version": "1.5",
                    "fallbackText": f":alert: Scan Context Detection - {event_type}",
                    "themeColor": color,
                    "title": ":alert: Scan Context Detection",
                    "sections": [
                        {
                            "activityTitle": f":alert: {event_type.replace('_', ' ').title()}",
                            "activitySubtitle": f"Severity: {severity.title()}",
                            "facts": [
                                {
                                    "title": "Event Type",
                                    "value": event_type.replace("_", " ").title(),
                                },
                                {
                                    "title": "Severity",
                                    "value": severity.title(),
                                },
                                {
                                    "title": "Affected",
                                    "value": affected,
                                },
                                {
                                    "title": "Timestamp",
                                    "value": timestamp,
                                },
                            ],
                            "markdown": True,
                        }
                    ],
                },
            }
        ],
    }

    try:
        response = requests.post(
            webhook_url,
            json=card,
            timeout=10,
        )

        if response.status_code == 200:
            logger.info(f"Teams notification sent: {event_type} ({severity})")
            return True
        else:
            logger.warning(
                f"Teams webhook returned status {response.status_code}: "
                f"{response.text[:200]}"
            )
            return False

    except Exception as e:
        logger.error(f"Failed to send Teams notification: {e}")
        return False


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

        # Use single-scan ingestion when both columns and pairs are needed
        if (needs_columns or needs_tokens) and needs_pairs:
            with log_duration(logger, "ingest_columns_with_pairs"):
                columns_df, pairs_df = ingestor.ingest_columns_with_pairs(table_names)
                columns_df.cache()
                columns_df.count()  # materialize cache
        elif needs_columns or needs_tokens:
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
                filtered_columns = _filter_by_column_type(_require_columns(columns_df), error_type)
                stats = builder.build_uniqueness_stats(filtered_columns, token_map)
            elif error_type is ErrorType.NUMERIC_OUTLIER:
                filtered_columns = _filter_by_column_type(_require_columns(columns_df), error_type)
                stats = builder.build_outlier_stats(filtered_columns)
            elif error_type is ErrorType.SPELLING:
                filtered_columns = _filter_by_column_type(_require_columns(columns_df), error_type)
                stats = builder.build_spelling_stats(filtered_columns)
            elif error_type is ErrorType.FUNCTIONAL_DEPENDENCY:
                if pairs_df is None:
                    pairs_df = ingestor.ingest_column_pairs(table_names)
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
            If not provided, ingestion happens lazily inside each detector.
        ingested_pairs_df:
            Pre-ingested column pairs DataFrame for FD detection.
            If provided, FD detector will use this instead of re-ingesting.

        Raises
        ------
        ValidationError
            If ``kwargs`` contains unrecognised parameters, or if
            ``table_names`` / ``error_types`` are not a sequence of ``str``.
        """
        self._validate_inputs(table_names=table_names, error_types=error_types, **kwargs)

        from pyspark.sql import functions as F

        from open_detect.algorithms.uni_detect.corpus.store import _AUTO_BROADCAST_DISABLED
        from open_detect.algorithms.uni_detect.spark_utils import (
            ARROW_MAX_RECORDS_PER_BATCH,
            ARROW_MAX_RECORDS_PER_BATCH_KEY,
            scoped_conf,
        )

        # Constant for repartitioning before mapInPandas to avoid single-row partitions
        INGESTION_REPARTITION_FACTOR = 4

        error_types = tuple(error_types) if error_types else tuple(ErrorType)
        frames = []
        result = None
        try:
            # Keep Arrow limit active through ALL detector operations:
            # extract_candidates (mapInPandas), candidate materialization (count),
            # scoring (batch_score join), and result materialization.
            # Also disable auto broadcast joins to prevent OOM on CI runners with small heaps.
            with scoped_conf(
                self.spark,
                **{
                    ARROW_MAX_RECORDS_PER_BATCH_KEY: str(ARROW_MAX_RECORDS_PER_BATCH),
                    **_AUTO_BROADCAST_DISABLED,
                },
            ):
                # Ingest once and share across detectors if not provided
                shared_columns_df = None
                shared_pairs_df = None

                if ingested_columns_df is not None:
                    shared_columns_df = ingested_columns_df
                if ingested_pairs_df is not None:
                    shared_pairs_df = ingested_pairs_df

                # Perform single-scan ingestion if not provided by caller
                needs_columns = any(et in _SINGLE_COLUMN_TYPES for et in error_types)
                needs_pairs = ErrorType.FUNCTIONAL_DEPENDENCY in error_types

                # Use repartition to spread work across cores and avoid single-row partitions
                parallelism = self.spark.sparkContext.defaultParallelism

                if needs_columns and shared_columns_df is None:
                    ingestor = CorpusIngestor(
                        self.spark,
                        max_values_per_column=self.config.max_mpd_block_size * 200,
                        max_fd_column_pairs_per_table=self.config.max_fd_column_pairs_per_table,
                    )
                    shared_columns_df = (
                        ingestor.ingest_columns(table_names)
                        .repartition(parallelism * INGESTION_REPARTITION_FACTOR)
                        .cache()
                    )
                    shared_columns_df.count()  # materialize cache

                if needs_pairs and shared_pairs_df is None:
                    if "ingestor" not in locals():
                        ingestor = CorpusIngestor(
                            self.spark,
                            max_values_per_column=self.config.max_mpd_block_size * 200,
                            max_fd_column_pairs_per_table=self.config.max_fd_column_pairs_per_table,
                        )
                    shared_pairs_df = (
                        ingestor.ingest_column_pairs(table_names)
                        .repartition(parallelism * INGESTION_REPARTITION_FACTOR)
                        .cache()
                    )
                    shared_pairs_df.count()  # materialize cache

                for et in error_types:
                    frame = self._detectors[et].detect(
                        table_names,
                        ingested_columns_df=shared_columns_df,
                        ingested_pairs_df=shared_pairs_df,
                    )
                    frames.append(frame)

                    # Send Teams notification after each detector runs
                    self._send_teams_notification_after_detection(
                        et,
                        frame,
                        kwargs,
                    )

                # Balanced union (not left-deep reduce) so the final merge plan is
                # ceil(log2(N)) deep regardless of how many detectors are enabled.
                result = balanced_union(frames)
                # Order first, then persist and materialize the *final* frame.  Sorting
                # after persist() would return an unpersisted frame, so the caller's
                # count/show/write would re-execute the scoring stage to re-materialize
                # it -- the very thing this cache lifecycle exists to prevent.
                # The per-detector caches are released only after the union is cached.
                result = result.orderBy(F.col("lr_ratio").asc())
                result = result.persist(StorageLevel.MEMORY_AND_DISK)
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
            # Release shared ingestion DataFrames
            if shared_columns_df is not None and ingested_columns_df is None:
                with suppress(Exception):
                    shared_columns_df.unpersist()
            if shared_pairs_df is not None and ingested_pairs_df is None:
                with suppress(Exception):
                    shared_pairs_df.unpersist()

    def _send_teams_notification_after_detection(
        self,
        error_type: ErrorType,
        detection_frame: DataFrame,
        kwargs: dict[str, Any],
    ) -> None:
        """Send a Teams notification after a detector runs.

        This is called after each detector's ``detect()`` method completes.
        It respects severity thresholds, rate limiting, and configuration.

        Args:
            error_type: The error type that was detected
            detection_frame: The detection result DataFrame
            kwargs: Keyword arguments passed to detect(), including:
                - severity: Override default severity (low, medium, high, critical)
                - description: Optional description for the notification
                - affected_summary: Optional affected summary
        """

        # Get notification configuration
        config = get_notification_config()

        if not config["enabled"]:
            logger.debug("Teams notifications disabled, skipping notification")
            return

        # Determine severity from kwargs or default
        severity = kwargs.get("severity", "medium")
        description = kwargs.get("description")

        # Check if we should notify based on severity threshold
        if not _should_notify_severity(severity, config["severity_threshold"]):
            logger.debug(
                f"Severity {severity} below threshold {config['severity_threshold']}, "
                "skipping notification"
            )
            return

        # Initialize Teams notifier if webhook is configured
        webhook_url = config["webhook_url"]
        if not webhook_url:
            logger.debug("Teams webhook URL not configured, skipping notification")
            return

        # Get affected summary from the detection results
        candidates_count = detection_frame.count() if detection_frame is not None else 0
        affected = _build_teams_affected_summary(
            error_type,
            candidates_count,
            description,
        )

        # Get timestamp
        import time as _time

        timestamp = _time.strftime("%Y-%m-%dT%H:%M:%SZ")

        # Send the notification (non-blocking - just log for now,
        # in production this would be dispatched to a background worker)
        try:
            # For now, we log what would be sent
            # In production, this would be sent via a background worker
            _send_teams_notification(
                webhook_url=webhook_url,
                event_type=f"scan_context_{error_type.name.lower()}",
                severity=severity,
                affected=affected,
                timestamp=timestamp,
                description=description,
            )
            logger.info(
                f"Teams notification dispatched: {error_type.name} ({severity}) - {affected}"
            )
        except Exception as e:
            logger.warning(f"Failed to send Teams notification: {e}")

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