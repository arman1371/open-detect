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

from typing import TYPE_CHECKING

from unidetect.config import UniDetectConfig
from unidetect.core.enums import ErrorType
from unidetect.corpus.schema import CORPUS_STATS_SCHEMA
from unidetect.logging_utils import get_logger, log_duration

if TYPE_CHECKING:
    from pyspark.sql import DataFrame, SparkSession

logger = get_logger(__name__)


def _stats_schema_without_error_type():
    from pyspark.sql.types import StructType

    return StructType([f for f in CORPUS_STATS_SCHEMA.fields if f.name != "error_type"])


class CorpusStatsBuilder:
    """Builds and persists the ``unidetect_corpus_stats`` Delta table.

    Parameters
    ----------
    spark:
        Active Unity-Catalog-enabled Spark session.
    config:
        Shared :class:`~unidetect.config.UniDetectConfig`; the corpus builder
        and the online detectors *must* use the same ``epsilon``, bucket
        edges, and table locations, or statistics will not line up with
        what's being scored.
    """

    def __init__(self, spark: SparkSession, config: UniDetectConfig) -> None:
        self.spark = spark
        self.config = config

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

        def compute(batches):
            from unidetect.featurization import build_functional_dependency_bucket
            from unidetect.perturbation import perturb_functional_dependency

            tdf = broadcast_tdf.value
            for batch in batches:
                out_bucket, out_before, out_after, out_table = [], [], [], []
                for tid, lhs_vals, rhs_vals, n, rhs_idx in zip(
                    batch["table_id"],
                    batch["lhs_values"],
                    batch["rhs_values"],
                    batch["num_rows"],
                    batch["rhs_column_index"],
                    strict=True,
                ):
                    try:
                        outcome = perturb_functional_dependency(
                            list(lhs_vals), list(rhs_vals), epsilon=cfg.epsilon
                        )
                        bucket = build_functional_dependency_bucket(
                            rhs_values=list(rhs_vals),
                            num_rows=int(n),
                            rhs_column_index=int(rhs_idx),
                            token_document_frequency=tdf,
                            row_count_edges=cfg.row_count_edges,
                            prevalence_edges=cfg.prevalence_edges,
                        )
                    except Exception:  # noqa: BLE001 - one bad corpus row must not fail the job
                        continue
                    out_table.append(tid)
                    out_bucket.append(bucket.as_key())
                    out_before.append(outcome.theta_before)
                    out_after.append(outcome.theta_after)

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

        def compute(batches):
            tdf = broadcast_tdf.value
            for batch in batches:
                out_bucket, out_before, out_after, out_table = [], [], [], []
                for tid, vals, n, idx in zip(
                    batch["table_id"],
                    batch["values"],
                    batch["num_rows"],
                    batch["column_index"],
                    strict=True,
                ):
                    try:
                        bucket, outcome = _score_single_column(
                            error_type, list(vals), int(n), int(idx), tdf, cfg
                        )
                    except (
                        Exception
                    ):  # noqa: BLE001 - skip unusable corpus rows, don't fail the job
                        continue
                    out_table.append(tid)
                    out_bucket.append(bucket.as_key())
                    out_before.append(outcome.theta_before)
                    out_after.append(outcome.theta_after)

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
        return stats

    def write(self, stats: DataFrame, mode: str = "overwrite") -> None:
        """Persist a stats DataFrame, replacing only its own ``error_type`` partition(s).

        ``replaceWhere`` only makes sense against a table that already
        exists (Delta has nothing to selectively overwrite on a first
        write), so the very first call for a given corpus-stats table falls
        back to a plain create.
        """
        fqn = self.config.corpus_stats_fqn
        table_already_exists = self.spark.catalog.tableExists(fqn)

        writer = (
            stats.write.format("delta")
            .mode(mode)
            .partitionBy("error_type")
            .option("overwriteSchema", "true" if mode == "overwrite" else "false")
        )
        if mode == "overwrite" and table_already_exists:
            error_types = [r["error_type"] for r in stats.select("error_type").distinct().collect()]
            if error_types:
                predicate = " OR ".join(f"error_type = '{et}'" for et in error_types)
                writer = writer.option("replaceWhere", predicate)
        writer.saveAsTable(fqn)
        logger.info("Wrote corpus statistics to %s", fqn)


def _score_single_column(
    error_type: ErrorType,
    values: list[str],
    num_rows: int,
    column_index: int,
    token_document_frequency: dict[str, int],
    cfg: UniDetectConfig,
):
    from unidetect.featurization import (
        build_outlier_bucket,
        build_spelling_bucket,
        build_uniqueness_bucket,
    )
    from unidetect.perturbation import (
        perturb_numeric_outlier,
        perturb_spelling,
        perturb_uniqueness,
    )

    if error_type is ErrorType.UNIQUENESS:
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
        outcome = perturb_numeric_outlier(numeric_values, epsilon=cfg.epsilon)
        bucket = build_outlier_bucket(
            values=numeric_values, num_rows=num_rows, row_count_edges=cfg.row_count_edges
        )
        return bucket, outcome

    if error_type is ErrorType.SPELLING:
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
    out: list[float] = []
    for v in values:
        if v is None:
            continue
        try:
            out.append(float(v))
        except (TypeError, ValueError):
            continue
    return out
