"""Offline "learning" phase: materialize corpus statistics (paper Sec. 2.2.3).

For every corpus column (or column-pair, for FD), this module applies the
*same* metric + perturbation the online detector will later apply to a
target column, records the resulting ``(feature_bucket, theta_before,
theta_after)`` triple, and writes the whole table to Delta. At detection
time (``corpus/store.py``), answering "how surprising is this observation"
becomes a filtered count over this materialized table instead of recomputing
anything from raw data -- exactly the MapReduce-once / lookup-at-runtime
architecture the paper describes.

This is intentionally implemented with ``DataFrame.mapInPandas`` (Arrow-
vectorized, one partition-batch of corpus rows at a time) rather than a
scalar ``pandas_udf``: a scalar ``pandas_udf`` must return exactly as many
output rows as its input (one-to-one), but corpus rows that fail to score
(malformed values, too few non-null rows, etc.) need to be dropped rather
than padded with nulls -- exactly the row-count-changing transformation
``mapInPandas`` supports and scalar ``pandas_udf`` does not.
"""

from __future__ import annotations

import math
import weakref
from typing import TYPE_CHECKING

from open_detect.algorithms.uni_detect.config import UniDetectConfig
from open_detect.algorithms.uni_detect.corpus.build_metadata import write_build_config
from open_detect.algorithms.uni_detect.corpus.schema import CORPUS_STATS_SCHEMA
from open_detect.algorithms.uni_detect.failures import FailureCounts, FailureTracker
from open_detect.algorithms.uni_detect.strategies import get_spec
from open_detect.core.enums import ErrorType
from open_detect.exceptions import InsufficientDataError
from open_detect.logging_utils import get_logger, log_duration

if TYPE_CHECKING:
    from collections.abc import Sequence

    from pyspark.sql import DataFrame, SparkSession

logger = get_logger(__name__)

#: A column is treated as numeric only if at least this fraction of its non-null
#: values parse as finite numbers; otherwise it is a text column that happens to
#: contain some numeric-looking values (ids, codes, ...) and is not scored for
#: numeric outliers.
MIN_NUMERIC_FRACTION = 0.8


def _stats_schema_without_error_type():
    from pyspark.sql.types import StructType

    return StructType([f for f in CORPUS_STATS_SCHEMA.fields if f.name != "error_type"])


class CorpusStatsBuilder:
    """Builds and persists the ``open_detect_corpus_stats`` Delta table.

    Parameters
    ----------
    spark:
        Active Unity-Catalog-enabled Spark session.
    config:
        Shared :class:`~open_detect.algorithms.uni_detect.config.UniDetectConfig`; the corpus builder
        and the online detectors *must* use the same ``epsilon``, bucket
        edges, and table locations, or statistics will not line up with
        what's being scored.
    """

    def __init__(self, spark: SparkSession, config: UniDetectConfig) -> None:
        self.spark = spark
        self.config = config
        self._trackers: weakref.WeakKeyDictionary[DataFrame, FailureTracker] = (
            weakref.WeakKeyDictionary()
        )

    def _new_tracker(self, label: str) -> FailureTracker:
        return FailureTracker(self.spark.sparkContext, label, self.config.max_failure_ratio)

    def build_uniqueness_stats(
        self, corpus_columns: DataFrame, token_document_frequency: dict[str, int]
    ) -> DataFrame:
        return self._build_single_column_stats(
            corpus_columns,
            error_type=ErrorType.UNIQUENESS,
            token_document_frequency=token_document_frequency,
        )

    def build_spelling_stats(self, corpus_columns: DataFrame) -> DataFrame:
        return self._build_single_column_stats(
            corpus_columns, error_type=ErrorType.SPELLING, token_document_frequency={}
        )

    def build_outlier_stats(self, corpus_columns: DataFrame) -> DataFrame:
        return self._build_single_column_stats(
            corpus_columns, error_type=ErrorType.NUMERIC_OUTLIER, token_document_frequency={}
        )

    def build_fd_stats(
        self, corpus_pairs: DataFrame, token_document_frequency: dict[str, int]
    ) -> DataFrame:
        import pandas as pd

        cfg = self.config
        broadcast_tdf = self.spark.sparkContext.broadcast(token_document_frequency)

        tracker = self._new_tracker("build_fd_stats")

        def compute(batches):
            tdf = broadcast_tdf.value
            for batch in batches:
                counts = FailureCounts()
                out_bucket, out_before, out_after, out_table = [], [], [], []
                for tid, lhs_vals, rhs_vals, n, rhs_idx in zip(
                    batch["table_id"],
                    batch["lhs_values"],
                    batch["rhs_values"],
                    batch["num_rows"],
                    batch["rhs_column_index"],
                    strict=True,
                ):
                    scored = counts.attempt(
                        _score_fd_pair,
                        list(lhs_vals),
                        list(rhs_vals),
                        int(n),
                        int(rhs_idx),
                        tdf,
                        cfg,
                    )
                    if scored is None:
                        continue
                    bucket, outcome = scored
                    out_table.append(tid)
                    out_bucket.append(bucket.as_key())
                    out_before.append(outcome.theta_before)
                    out_after.append(outcome.theta_after)

                tracker.flush(counts)
                yield pd.DataFrame(
                    {
                        "feature_bucket": out_bucket,
                        "theta_before": out_before,
                        "theta_after": out_after,
                        "table_id": out_table,
                    }
                )

        result_schema = _stats_schema_without_error_type()
        with log_duration(logger, "build_fd_stats"):
            from pyspark.sql import functions as F

            stats = corpus_pairs.select(
                "table_id", "lhs_values", "rhs_values", "num_rows", "rhs_column_index"
            ).mapInPandas(compute, schema=result_schema)
            stats = stats.withColumn("error_type", F.lit(ErrorType.FUNCTIONAL_DEPENDENCY.value))
            stats = stats.select(*[f.name for f in CORPUS_STATS_SCHEMA.fields])
        self._trackers[stats] = tracker
        return stats

    def _build_single_column_stats(
        self,
        corpus_columns: DataFrame,
        error_type: ErrorType,
        token_document_frequency: dict[str, int],
    ) -> DataFrame:
        import pandas as pd
        from pyspark.sql import functions as F

        cfg = self.config
        broadcast_tdf = self.spark.sparkContext.broadcast(token_document_frequency)

        tracker = self._new_tracker(f"build_{error_type.value}_stats")

        def compute(batches):
            tdf = broadcast_tdf.value
            for batch in batches:
                counts = FailureCounts()
                out_bucket, out_before, out_after, out_table = [], [], [], []
                for tid, vals, n, idx in zip(
                    batch["table_id"],
                    batch["values"],
                    batch["num_rows"],
                    batch["column_index"],
                    strict=True,
                ):
                    scored = counts.attempt(
                        _score_single_column, error_type, list(vals), int(n), int(idx), tdf, cfg
                    )
                    if scored is None:
                        continue
                    bucket, outcome = scored
                    out_table.append(tid)
                    out_bucket.append(bucket.as_key())
                    out_before.append(outcome.theta_before)
                    out_after.append(outcome.theta_after)

                tracker.flush(counts)
                yield pd.DataFrame(
                    {
                        "feature_bucket": out_bucket,
                        "theta_before": out_before,
                        "theta_after": out_after,
                        "table_id": out_table,
                    }
                )

        result_schema = _stats_schema_without_error_type()
        with log_duration(logger, f"build_{error_type.value}_stats"):
            stats = corpus_columns.select(
                "table_id", "column_index", "num_rows", "values"
            ).mapInPandas(compute, schema=result_schema)
            stats = stats.withColumn("error_type", F.lit(error_type.value))
            stats = stats.select(*[f.name for f in CORPUS_STATS_SCHEMA.fields])
        self._trackers[stats] = tracker
        return stats

    def write(
        self,
        stats: DataFrame,
        mode: str = "overwrite",
        error_types: Sequence[ErrorType] | None = None,
    ) -> None:
        """Persist a stats DataFrame, replacing only its own ``error_type`` partition(s).

        ``error_types`` names the partitions ``stats`` covers; when omitted
        they are discovered with an extra pass over ``stats``. The build
        configuration is recorded on the table for each of them (see
        :mod:`~open_detect.algorithms.uni_detect.corpus.build_metadata`).

        ``replaceWhere`` only makes sense against a table that already
        exists (Delta has nothing to selectively overwrite on a first
        write), so the very first call for a given corpus-stats table falls
        back to a plain create.

        For frames produced by this builder the (small) stats frame is cached
        and materialized first, so the executor-side skip totals can be
        logged and ``max_failure_ratio`` enforced *before* anything is
        written; a breach raises :class:`~open_detect.exceptions.DataQualityError`
        and leaves the existing table untouched.
        """
        tracker = self._trackers.pop(stats, None)
        if tracker is None:
            self._write(stats, mode, error_types)
            return

        already_cached = stats.is_cached
        if not already_cached:
            stats.cache()
        try:
            stats.count()
            tracker.check()
            self._write(stats, mode, error_types)
        finally:
            if not already_cached:
                stats.unpersist()

    def _write(self, stats: DataFrame, mode: str, error_types: Sequence[ErrorType] | None) -> None:
        fqn = self.config.corpus_stats_fqn
        table_already_exists = self.spark.catalog.tableExists(fqn)

        if error_types is None:
            error_types = [
                ErrorType(r["error_type"]) for r in stats.select("error_type").distinct().collect()
            ]
        writer = stats.write.format("delta").mode(mode)
        if table_already_exists:
            # Re-declaring `.partitionBy(...)` (and `overwriteSchema`) against
            # an already-partitioned table is unnecessary -- Delta keeps the
            # table's existing partitioning -- and on some catalogs (notably
            # Spark's built-in in-memory session catalog used in local
            # testing) repeating it alongside `replaceWhere` trips an
            # internal catalog-sync assertion. Unity Catalog is unaffected,
            # but omitting the redundant options is correct everywhere.
            if mode == "overwrite" and error_types:
                predicate = " OR ".join(f"error_type = '{et.value}'" for et in error_types)
                writer = writer.option("replaceWhere", predicate)
        else:
            writer = writer.partitionBy("error_type").option("overwriteSchema", "true")
        writer.saveAsTable(fqn)
        write_build_config(self.spark, fqn, error_types, self.config)
        logger.info("Wrote corpus statistics to %s", fqn)


def _require_min_rows(n: int, error_type: ErrorType) -> None:
    min_rows = get_spec(error_type).min_rows
    if n < min_rows:
        raise InsufficientDataError(
            f"{error_type.value}: {n} usable values, need at least {min_rows}"
        )


def _score_fd_pair(
    lhs_values: list[str],
    rhs_values: list[str],
    num_rows: int,
    rhs_column_index: int,
    token_document_frequency: dict[str, int],
    cfg: UniDetectConfig,
) -> tuple:
    from open_detect.algorithms.uni_detect.featurization import (
        build_functional_dependency_bucket,
    )
    from open_detect.algorithms.uni_detect.perturbation import perturb_functional_dependency

    _require_min_rows(len(lhs_values), ErrorType.FUNCTIONAL_DEPENDENCY)

    outcome = perturb_functional_dependency(lhs_values, rhs_values, epsilon=cfg.epsilon)
    bucket = build_functional_dependency_bucket(
        rhs_values=rhs_values,
        num_rows=num_rows,
        rhs_column_index=rhs_column_index,
        token_document_frequency=token_document_frequency,
        row_count_edges=cfg.row_count_edges,
        prevalence_edges=cfg.prevalence_edges,
    )
    return bucket, outcome


def _score_single_column(
    error_type: ErrorType,
    values: list[str],
    num_rows: int,
    column_index: int,
    token_document_frequency: dict[str, int],
    cfg: UniDetectConfig,
) -> tuple:
    """Score one corpus column.

    Raises :class:`InsufficientDataError` for columns with fewer usable values
    than ``ErrorTypeSpec.min_rows``, mirroring the online detectors, so tiny
    columns do not pollute the low-row-count buckets. ``FailureCounts.attempt``
    records that as "not applicable", which is excluded from the failure ratio.
    """
    from open_detect.algorithms.uni_detect.featurization import (
        build_outlier_bucket,
        build_spelling_bucket,
        build_uniqueness_bucket,
    )
    from open_detect.algorithms.uni_detect.perturbation import (
        perturb_numeric_outlier,
        perturb_spelling,
        perturb_uniqueness,
    )

    if error_type is ErrorType.UNIQUENESS:
        _require_min_rows(len(values), error_type)
        outcome = perturb_uniqueness(values, epsilon=cfg.epsilon)
        bucket = build_uniqueness_bucket(
            values=values,
            num_rows=num_rows,
            column_index=column_index,
            token_document_frequency=token_document_frequency,
            row_count_edges=cfg.row_count_edges,
            prevalence_edges=cfg.prevalence_edges,
        )
        return bucket, outcome

    if error_type is ErrorType.NUMERIC_OUTLIER:
        numeric_values = _coerce_numeric(values)
        _require_min_rows(len(numeric_values), error_type)
        outcome = perturb_numeric_outlier(numeric_values, epsilon=cfg.epsilon)
        bucket = build_outlier_bucket(
            values=numeric_values, num_rows=num_rows, row_count_edges=cfg.row_count_edges
        )
        return bucket, outcome

    if error_type is ErrorType.SPELLING:
        _require_min_rows(len(values), error_type)
        outcome = perturb_spelling(
            values, epsilon=cfg.epsilon, max_block_size=cfg.max_mpd_block_size
        )
        avg_len = outcome.evidence.get("avg_differing_token_length", 0.0)
        bucket = build_spelling_bucket(
            values=values,
            num_rows=num_rows,
            avg_differing_token_length=avg_len,
            row_count_edges=cfg.row_count_edges,
            token_length_edges=cfg.token_length_edges,
        )
        return bucket, outcome

    raise ValueError(f"Unsupported single-column error type: {error_type}")


def _coerce_numeric(values: list[str]) -> list[float]:
    """Parse a column's values as floats, or return ``[]`` if it is not numeric.

    ``nan``/``inf`` do not count as parseable. The column is numeric only if at
    least :data:`MIN_NUMERIC_FRACTION` of its non-null values parse; the
    unparseable remainder is dropped.
    """
    non_null = 0
    out: list[float] = []
    for v in values:
        if v is None:
            continue
        non_null += 1
        try:
            f = float(v)
        except (TypeError, ValueError):
            continue
        if math.isfinite(f):
            out.append(f)
    if not out or len(out) < MIN_NUMERIC_FRACTION * non_null:
        return []
    return out
