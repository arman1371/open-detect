"""Online scoring: batch likelihood-ratio lookups against materialized corpus statistics.

This is the "at online prediction time... perform a lookup to find relevant
predictions without computing LR from scratch" step described in the
paper's System Architecture (Sec. 2.2.3), generalized across both
:class:`~unidetect.core.enums.ComparisonDirection` families via the smoothed
range-based formula in Equation (12):

    INCREASING (spelling, uniqueness, FD):
        ratio = count(corpus.before <= theta1 AND corpus.after >= theta2)
                ---------------------------------------------------------
                             count(corpus.before <= theta2)

    DECREASING (numeric outliers):
        ratio = count(corpus.before >= theta1 AND corpus.after <= theta2)
                ---------------------------------------------------------
                             count(corpus.before >= theta2)

All counting happens inside Spark via a join + conditional aggregation, so a
single call scores an entire batch of candidates without pulling corpus rows
to the driver.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from unidetect.config import UniDetectConfig
from unidetect.core.enums import ComparisonDirection, ErrorType
from unidetect.exceptions import CorpusNotFoundError
from unidetect.logging_utils import get_logger, log_duration

if TYPE_CHECKING:
    from pyspark.sql import DataFrame, SparkSession

logger = get_logger(__name__)


class CorpusStatsStore:
    """Read-side access to the materialized ``unidetect_corpus_stats`` table.

    Parameters
    ----------
    spark:
        Active Spark session.
    config:
        Must match the :class:`~unidetect.config.UniDetectConfig` used to
        build the statistics (same table location); ``epsilon``/bucket edges
        only matter transitively, through what is already baked into the
        materialized table.
    """

    def __init__(self, spark: SparkSession, config: UniDetectConfig) -> None:
        self.spark = spark
        self.config = config

    def table_exists(self) -> bool:
        # Deliberately uncached: this is a cheap catalog-metadata lookup (no
        # data scan), and callers commonly build the corpus statistics table
        # and then detect() in the same session/notebook -- caching a stale
        # "does not exist" would break that interactive pattern.
        return self.spark.catalog.tableExists(self.config.corpus_stats_fqn)

    def load(self, error_type: ErrorType) -> DataFrame:
        """Return the (partition-pruned) corpus statistics for one error type."""
        if not self.table_exists():
            raise CorpusNotFoundError(
                f"Corpus statistics table {self.config.corpus_stats_fqn!r} does not exist. "
                "Run unidetect.corpus.CorpusStatsBuilder first."
            )
        from pyspark.sql import functions as F

        table = self.spark.table(self.config.corpus_stats_fqn)
        return table.where(F.col("error_type") == error_type.value)

    def load_token_stats_map(self, max_tokens: int | None = 5_000_000) -> dict[str, int]:
        """Collect the token-document-frequency table to the driver as a dict.

        Used to build the broadcast variable consumed by featurization's
        ``Prev(C)`` computation. ``max_tokens`` guards against accidentally
        collecting an unbounded vocabulary to driver memory; raise it (or set
        to ``None``) deliberately for very large deployments with enough
        driver memory.
        """
        if not self.spark.catalog.tableExists(self.config.token_stats_fqn):
            return {}
        df = self.spark.table(self.config.token_stats_fqn)
        if max_tokens is not None:
            from pyspark.sql import functions as F

            df = df.orderBy(F.col("doc_frequency").desc()).limit(max_tokens)
        return {row["token"]: int(row["doc_frequency"]) for row in df.collect()}

    def batch_score(
        self,
        candidates: DataFrame,
        error_type: ErrorType,
        direction: ComparisonDirection,
    ) -> DataFrame:
        """Score a batch of candidates against the corpus for one error type.

        Parameters
        ----------
        candidates:
            A DataFrame with (at least) columns ``candidate_id`` (string,
            unique), ``feature_bucket`` (string, matching
            :meth:`~unidetect.core.models.FeatureBucket.as_key`),
            ``theta_before`` (double) and ``theta_after`` (double).
        error_type, direction:
            Which materialized partition to read and which inequality
            family (Equation 12) to apply; see
            :func:`unidetect.strategies.get_spec`.

        Returns
        -------
        DataFrame
            One row per input candidate with ``numerator_count``,
            ``denominator_count``, ``bucket_support`` and ``lr_ratio``
            (Laplace-smoothed). Candidates whose feature bucket has no
            corpus support at all get ``lr_ratio == 1.0`` (maximally
            un-surprising), consistent with "assume clean absent evidence".
        """
        from pyspark.sql import functions as F

        with log_duration(logger, f"batch_score[{error_type.value}]"):
            corpus = self.load(error_type).select(
                F.col("feature_bucket"),
                F.col("theta_before").alias("corpus_before"),
                F.col("theta_after").alias("corpus_after"),
            )
            cand = candidates.select(
                "candidate_id",
                "feature_bucket",
                F.col("theta_before").alias("theta1"),
                F.col("theta_after").alias("theta2"),
            )

            relevant_buckets = F.broadcast(cand.select("feature_bucket").distinct())
            corpus_relevant = corpus.join(relevant_buckets, on="feature_bucket", how="inner")
            joined = corpus_relevant.join(F.broadcast(cand), on="feature_bucket", how="inner")

            if direction is ComparisonDirection.INCREASING:
                numerator_cond = (F.col("corpus_before") <= F.col("theta1")) & (
                    F.col("corpus_after") >= F.col("theta2")
                )
                denominator_cond = F.col("corpus_before") <= F.col("theta2")
            else:
                numerator_cond = (F.col("corpus_before") >= F.col("theta1")) & (
                    F.col("corpus_after") <= F.col("theta2")
                )
                denominator_cond = F.col("corpus_before") >= F.col("theta2")

            counts = joined.groupBy("candidate_id").agg(
                F.sum(F.when(numerator_cond, 1).otherwise(0)).alias("numerator_count"),
                F.sum(F.when(denominator_cond, 1).otherwise(0)).alias("denominator_count"),
                F.count(F.lit(1)).alias("bucket_support"),
            )

            smoothing = float(self.config.laplace_smoothing)
            scored = (
                cand.select("candidate_id")
                .join(counts, on="candidate_id", how="left")
                .fillna({"numerator_count": 0, "denominator_count": 0, "bucket_support": 0})
                .withColumn(
                    "lr_ratio",
                    (F.col("numerator_count") + F.lit(smoothing))
                    / (F.col("denominator_count") + F.lit(smoothing)),
                )
            )
        return scored
