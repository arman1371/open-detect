"""Online scoring: batch likelihood-ratio lookups against materialized corpus statistics.

This is the "at online prediction time... perform a lookup to find relevant
predictions without computing LR from scratch" step described in the
paper's System Architecture (Sec. 2.2.3), generalized across both
:class:`~open_detect.algorithms.uni_detect.core.enums.ComparisonDirection` families via the smoothed
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

from open_detect.algorithms.uni_detect.config import UniDetectConfig
from open_detect.algorithms.uni_detect.core.enums import ComparisonDirection, ErrorType
from open_detect.algorithms.uni_detect.corpus.build_metadata import verify_build_config
from open_detect.algorithms.uni_detect.exceptions import CorpusNotFoundError
from open_detect.logging_utils import get_logger, log_duration

if TYPE_CHECKING:
    from pyspark.sql import DataFrame, SparkSession

logger = get_logger(__name__)


class CorpusStatsStore:
    """Read-side access to the materialized ``open_detect_corpus_stats`` table.

    Parameters
    ----------
    spark:
        Active Spark session.
    config:
        Must match the :class:`~open_detect.algorithms.uni_detect.config.UniDetectConfig` used to
        build the statistics (same table location). ``epsilon``/bucket edges
        are baked into the materialized table, so :meth:`load` compares them
        against the build configuration persisted on the table and raises
        :class:`~open_detect.exceptions.ConfigurationError` on mismatch
        (unless ``config.allow_corpus_config_mismatch`` is set).
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
        """Return the (partition-pruned) corpus statistics for one error type.

        If the corpus table was built before the OPE-92 optimization and lacks the
        `weight` column, it is added with a default value of 1.0 (each row represents
        one original corpus row). This maintains backward compatibility; a rebuild
        is recommended to benefit from pre-aggregation.
        """
        if not self.table_exists():
            raise CorpusNotFoundError(
                f"Corpus statistics table {self.config.corpus_stats_fqn!r} does not exist. "
                "Run open_detect.algorithms.uni_detect.corpus.CorpusStatsBuilder first."
            )
        from pyspark.sql import functions as F

        verify_build_config(self.spark, self.config.corpus_stats_fqn, error_type, self.config)
        table = self.spark.table(self.config.corpus_stats_fqn).where(
            F.col("error_type") == error_type.value
        )

        # Backward compatibility: if weight column doesn't exist (corpus built before OPE-92),
        # add it with default value 1 (each row = one original corpus row).
        if "weight" not in table.columns:
            from open_detect.logging_utils import get_logger

            logger = get_logger(__name__)
            logger.warning(
                "Corpus statistics table %s is missing 'weight' column (built before OPE-92). "
                "Adding weight=1 for backward compatibility; rebuild recommended for pre-aggregation benefits.",
                self.config.corpus_stats_fqn,
            )
            table = table.withColumn("weight", F.lit(1))
        return table

    def load_token_stats_map(self, max_tokens: int | None = 500_000) -> dict[str, int]:
        """Collect the token-document-frequency table to the driver as a dict.

        Used to build the broadcast variable consumed by featurization's
        ``Prev(C)`` computation. ``max_tokens`` guards against accidentally
        collecting an unbounded vocabulary to driver memory; raise it (or set
        to ``None``) deliberately for very large deployments with enough
        driver memory.

        The default (500k) is chosen to fit in typical executor heaps (e.g. 4g
        in CI) where Spark's ``takeOrdered`` (used by ``orderBy().limit()``)
        allocates a bounded priority queue of size ``max_tokens``.
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
            :meth:`~open_detect.algorithms.uni_detect.core.models.FeatureBucket.as_key`),
            ``theta_before`` (double) and ``theta_after`` (double).
        error_type, direction:
            Which materialized partition to read and which inequality
            family (Equation 12) to apply; see
            :func:`open_detect.algorithms.uni_detect.strategies.get_spec`.

        Returns
        -------
        DataFrame
            One row per input candidate with ``numerator_count``,
            ``denominator_count``, ``bucket_support`` and ``lr_ratio``
            (Laplace-smoothed). Candidates whose feature bucket has no
            corpus support at all get ``lr_ratio == 1.0`` (maximally
            un-surprising), consistent with "assume clean absent evidence".

        OPE-92: This method now uses the pre-aggregated ``weight`` column
        from the corpus stats table to compute weighted counts instead of
        materializing cross-products. The corpus is pre-aggregated by
        ``(feature_bucket, theta_before, theta_after)`` with weight = count
        (the number of original corpus rows in that group), so the weighted
        sum equals the original row count.

        OPE-92: Candidates are deduplicated by ``(feature_bucket, theta1, theta2)``
        before scoring to avoid redundant computation. The distinct triples are
        scored once, then joined back to the original candidates.
        """
        from pyspark.sql import functions as F

        with log_duration(logger, f"batch_score[{error_type.value}]"):
            # Load corpus with weight column
            # Keep original column names for use in join conditions
            corpus = self.load(error_type).select(
                "feature_bucket",
                "theta_before",
                "theta_after",
                "weight",
            )

            # OPE-92: Pre-aggregate corpus by (feature_bucket, theta_before, theta_after)
            # summing weights. The builder aggregates by (feature_bucket, theta_before,
            # theta_after, table_id), so we need to collapse across table_id here.
            # This drastically reduces corpus row count before the join, avoiding the
            # cross-product explosion that caused StackOverflowError in CI.
            corpus = corpus.groupBy("feature_bucket", "theta_before", "theta_after").agg(
                F.sum("weight").alias("weight")
            )

            cand = candidates.select(
                "candidate_id",
                "feature_bucket",
                F.col("theta_before").alias("theta1"),
                F.col("theta_after").alias("theta2"),
            )

            # OPE-92: Deduplicate candidates by (feature_bucket, theta1, theta2)
            dedup_cols = ["feature_bucket", "theta1", "theta2"]
            distinct_cand = cand.select(*dedup_cols).distinct()

            # OPE-92: Use left_semi join to restrict corpus to buckets present in candidates
            # instead of broadcasting all candidates. Broadcast only the distinct bucket list.
            relevant_buckets = F.broadcast(distinct_cand.select("feature_bucket").distinct())
            corpus_relevant = corpus.join(relevant_buckets, on="feature_bucket", how="inner")

            # Join corpus with distinct candidates on feature_bucket only
            # This gives us all corpus rows for each candidate's bucket
            # We then filter by theta conditions and aggregate
            joined = corpus_relevant.join(
                F.broadcast(distinct_cand), on="feature_bucket", how="inner"
            )

            if direction is ComparisonDirection.INCREASING:
                numerator_cond = (F.col("theta_before") <= F.col("theta1")) & (
                    F.col("theta_after") >= F.col("theta2")
                )
                denominator_cond = F.col("theta_before") <= F.col("theta2")
            else:
                numerator_cond = (F.col("theta_before") >= F.col("theta1")) & (
                    F.col("theta_after") <= F.col("theta2")
                )
                denominator_cond = F.col("theta_before") >= F.col("theta2")

            # OPE-92: Use weighted sum instead of count
            # weight = count where count is the number of corpus rows with same
            # (feature_bucket, theta_before, theta_after). Summing weight gives
            # the same result as counting individual rows.
            # bucket_support should sum weights (not count groups) to match the
            # original row count semantics exposed as "support" in detectors.
            counts = joined.groupBy(*dedup_cols).agg(
                F.sum(F.when(numerator_cond, F.col("weight")).otherwise(0)).alias(
                    "numerator_count"
                ),
                F.sum(F.when(denominator_cond, F.col("weight")).otherwise(0)).alias(
                    "denominator_count"
                ),
                F.sum(F.col("weight")).cast("long").alias("bucket_support"),
            )

            # Join scores back to original candidates via dedup_cols
            scored_distinct = counts.withColumn(
                "lr_ratio",
                (F.col("numerator_count") + F.lit(float(self.config.laplace_smoothing)))
                / (F.col("denominator_count") + F.lit(float(self.config.laplace_smoothing))),
            )
            scored = (
                cand.join(scored_distinct, on=dedup_cols, how="left")
                .fillna(
                    {
                        "numerator_count": 0,
                        "denominator_count": 0,
                        "bucket_support": 0,
                        "lr_ratio": 1.0,
                    }
                )
                .select(
                    "candidate_id",
                    "numerator_count",
                    "denominator_count",
                    "bucket_support",
                    "lr_ratio",
                )
            )
        return scored
