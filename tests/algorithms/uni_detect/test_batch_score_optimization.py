"""Tests for OPE-92 batch_score optimization with pre-aggregated weight column
and candidate deduplication.

These tests verify:
1. Weighted sum equivalence to original per-row counting
2. bucket_support uses sum(weight) not count(groups)
3. Candidate deduplication works correctly
4. Backward compatibility with corpora missing weight column
"""

from __future__ import annotations

import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import (
    DoubleType,
    LongType,
    StringType,
    StructField,
    StructType,
)

from open_detect.algorithms.uni_detect.config import UniDetectConfig
from open_detect.algorithms.uni_detect.core.enums import ComparisonDirection, ErrorType
from open_detect.algorithms.uni_detect.corpus.builder import _aggregate_scored_rows
from open_detect.algorithms.uni_detect.corpus.schema import CORPUS_STATS_SCHEMA
from open_detect.algorithms.uni_detect.corpus.store import CorpusStatsStore


@pytest.fixture
def config(uc_location):
    return UniDetectConfig(
        location=uc_location,
        epsilon=0.05,
        alpha=0.2,
        laplace_smoothing=1.0,
    )


class TestAggregateScoredRows:
    """Unit tests for the _aggregate_scored_rows helper."""

    def test_empty_input_returns_empty_dataframe_with_correct_schema(self):
        result = _aggregate_scored_rows([])
        assert len(result) == 0
        expected_cols = ["feature_bucket", "theta_before", "theta_after", "weight", "table_id"]
        assert list(result.columns) == expected_cols
        assert result["weight"].dtype == "int64"

    def test_single_row_returns_weight_1(self):
        rows = [
            ("table1", "bucket1", 0.1, 0.2),
        ]
        result = _aggregate_scored_rows(rows)
        assert len(result) == 1
        assert result.iloc[0]["weight"] == 1
        assert result.iloc[0]["feature_bucket"] == "bucket1"
        assert result.iloc[0]["theta_before"] == 0.1
        assert result.iloc[0]["theta_after"] == 0.2
        assert result.iloc[0]["table_id"] == "table1"

    def test_duplicate_rows_aggregated_with_weight_count(self):
        """With new OPE-92 behavior, _aggregate_scored_rows aggregates duplicates.
        Same rows are grouped and weight = count (number of original rows in group).
        Global pre-aggregation in batch_score sums these weights."""
        rows = [
            ("table1", "bucket1", 0.1, 0.2),
            ("table1", "bucket1", 0.1, 0.2),
            ("table1", "bucket1", 0.1, 0.2),
        ]
        result = _aggregate_scored_rows(rows)
        # 3 duplicate rows are aggregated into 1 row with weight=3
        assert len(result) == 1
        assert result.iloc[0]["weight"] == 3
        assert result.iloc[0]["feature_bucket"] == "bucket1"
        assert result.iloc[0]["theta_before"] == 0.1
        assert result.iloc[0]["theta_after"] == 0.2
        assert result.iloc[0]["table_id"] == "table1"

    def test_different_buckets_kept_separate(self):
        rows = [
            ("table1", "bucket1", 0.1, 0.2),
            ("table1", "bucket2", 0.1, 0.2),
        ]
        result = _aggregate_scored_rows(rows)
        assert len(result) == 2
        assert set(result["feature_bucket"]) == {"bucket1", "bucket2"}
        assert all(result["weight"] == 1)

    def test_different_thetas_kept_separate(self):
        rows = [
            ("table1", "bucket1", 0.1, 0.2),
            ("table1", "bucket1", 0.3, 0.4),
        ]
        result = _aggregate_scored_rows(rows)
        assert len(result) == 2

    def test_different_table_ids_kept_separate(self):
        rows = [
            ("table1", "bucket1", 0.1, 0.2),
            ("table2", "bucket1", 0.1, 0.2),
        ]
        result = _aggregate_scored_rows(rows)
        assert len(result) == 2
        assert set(result["table_id"]) == {"table1", "table2"}


class TestCorpusStatsSchema:
    """Test that CORPUS_STATS_SCHEMA has the correct weight field type."""

    def test_weight_is_long_type(self):
        weight_field = CORPUS_STATS_SCHEMA["weight"]
        assert weight_field is not None
        assert isinstance(weight_field.dataType, LongType)
        assert not weight_field.nullable


class TestBatchScoreOptimization:
    """End-to-end tests for batch_score with pre-aggregated weight."""

    def _write_corpus_stats(self, spark: SparkSession, fqn: str, rows: list[dict]):
        """Write a corpus stats table with given rows."""
        df = spark.createDataFrame(rows, schema=CORPUS_STATS_SCHEMA)
        df.write.format("delta").mode("overwrite").partitionBy("error_type").option(
            "overwriteSchema", "true"
        ).saveAsTable(fqn)

    def _make_config_with_fqn(self, config: UniDetectConfig, fqn: str) -> UniDetectConfig:
        """Create a config with corpus_stats_fqn set to the test table.

        ``corpus_stats_fqn`` is a derived property of ``UniDetectConfig``
        (``location.catalog.schema.corpus_stats_table``), so the test table
        name is passed via ``corpus_stats_table`` against the same catalog/schema.
        """
        from open_detect.algorithms.uni_detect.config import UnityCatalogLocation

        catalog, schema, table = fqn.split(".", 2)
        return UniDetectConfig(
            location=UnityCatalogLocation(catalog=catalog, schema=schema),
            epsilon=config.epsilon,
            alpha=config.alpha,
            laplace_smoothing=config.laplace_smoothing,
            corpus_stats_table=table,
        )

    def test_weighted_sum_equivalence_increasing(self, spark: SparkSession, uc_location, config):
        """Verify weighted sum equals original per-row count for INCREASING direction."""
        catalog, schema = uc_location.catalog, uc_location.schema
        fqn = f"{catalog}.{schema}.test_corpus_stats_equivalence"

        # Create corpus stats with weight column (pre-aggregated)
        corpus_rows = [
            # bucket1: 3 rows with theta_before=0.1, theta_after=0.5
            {
                "error_type": "uniqueness",
                "feature_bucket": "bucket1",
                "theta_before": 0.1,
                "theta_after": 0.5,
                "weight": 3,
                "table_id": "t1",
            },
            # bucket1: 2 rows with theta_before=0.3, theta_after=0.7
            {
                "error_type": "uniqueness",
                "feature_bucket": "bucket1",
                "theta_before": 0.3,
                "theta_after": 0.7,
                "weight": 2,
                "table_id": "t1",
            },
            # bucket2: 4 rows with theta_before=0.2, theta_after=0.6
            {
                "error_type": "uniqueness",
                "feature_bucket": "bucket2",
                "theta_before": 0.2,
                "theta_after": 0.6,
                "weight": 4,
                "table_id": "t2",
            },
        ]
        self._write_corpus_stats(spark, fqn, corpus_rows)

        test_config = self._make_config_with_fqn(config, fqn)
        store = CorpusStatsStore(spark, test_config)

        # Candidates:
        # cand1: bucket1, theta1=0.2, theta2=0.6
        #   numerator: corpus_before <= 0.2 AND corpus_after >= 0.6
        #     (0.1, 0.5): 0.1 <= 0.2 ✓, 0.5 >= 0.6 ✗ -> NO
        #     (0.3, 0.7): 0.3 <= 0.2 ✗ -> NO
        #     -> numerator = 0
        #   denominator: corpus_before <= 0.6 (theta2)
        #     (0.1, 0.5): 0.1 <= 0.6 ✓ -> weight=3
        #     (0.3, 0.7): 0.3 <= 0.6 ✓ -> weight=2
        #     -> denominator = 5
        #   lr_ratio = (0 + 1) / (5 + 1) = 1/6 ≈ 0.1667
        # cand2: bucket1, theta1=0.0, theta2=0.8
        #   numerator: corpus_before <= 0.0 AND corpus_after >= 0.8 -> none match
        #     -> numerator = 0
        #   denominator: corpus_before <= 0.8 (theta2)
        #     (0.1, 0.5): 0.1 <= 0.8 ✓ -> weight=3
        #     (0.3, 0.7): 0.3 <= 0.8 ✓ -> weight=2
        #     -> denominator = 5
        #   lr_ratio = (0 + 1) / (5 + 1) = 1/6 ≈ 0.1667
        # cand3: bucket2, theta1=0.2, theta2=0.6
        #   numerator: (0.2 <= 0.2) & (0.6 >= 0.6) -> YES, weight=4
        #   denominator: 0.2 <= 0.6 -> YES, weight=4
        #   lr_ratio = (4+1)/(4+1) = 1.0

        candidates_df = spark.createDataFrame(
            [
                {
                    "candidate_id": "cand1",
                    "feature_bucket": "bucket1",
                    "theta_before": 0.2,
                    "theta_after": 0.6,
                },
                {
                    "candidate_id": "cand2",
                    "feature_bucket": "bucket1",
                    "theta_before": 0.0,
                    "theta_after": 0.8,
                },
                {
                    "candidate_id": "cand3",
                    "feature_bucket": "bucket2",
                    "theta_before": 0.2,
                    "theta_after": 0.6,
                },
            ]
        )

        result = store.batch_score(
            candidates_df, ErrorType.UNIQUENESS, ComparisonDirection.INCREASING
        )
        result_pd = result.toPandas().set_index("candidate_id")

        # cand1: numerator = 0, denominator = 5 (both bucket1 groups have corpus_before <= 0.6)
        # lr_ratio = (0 + 1) / (5 + 1) = 1/6 ≈ 0.1667
        assert abs(result_pd.loc["cand1", "numerator_count"] - 0) < 0.001
        assert abs(result_pd.loc["cand1", "denominator_count"] - 5) < 0.001
        assert abs(result_pd.loc["cand1", "lr_ratio"] - (1.0 / 6.0)) < 0.001

        # cand2: numerator = 0, denominator = 5 (both bucket1 groups have corpus_before <= 0.8)
        # lr_ratio = (0 + 1) / (5 + 1) = 1/6 ≈ 0.1667
        assert abs(result_pd.loc["cand2", "numerator_count"] - 0) < 0.001
        assert abs(result_pd.loc["cand2", "denominator_count"] - 5) < 0.001
        assert abs(result_pd.loc["cand2", "lr_ratio"] - (1.0 / 6.0)) < 0.001

        # cand3: bucket2, theta1=0.2, theta2=0.6
        # numerator: (0.2 <= 0.2) & (0.6 >= 0.6) -> YES, weight=4
        # denominator: 0.2 <= 0.6 -> YES, weight=4
        # lr_ratio = (4+1)/(4+1) = 1.0
        assert abs(result_pd.loc["cand3", "numerator_count"] - 4) < 0.001
        assert abs(result_pd.loc["cand3", "denominator_count"] - 4) < 0.001
        assert abs(result_pd.loc["cand3", "lr_ratio"] - 1.0) < 0.001

    def test_weighted_sum_equivalence_decreasing(self, spark: SparkSession, uc_location, config):
        """Verify weighted sum equals original per-row count for DECREASING direction."""
        catalog, schema = uc_location.catalog, uc_location.schema
        fqn = f"{catalog}.{schema}.test_corpus_stats_decreasing"

        corpus_rows = [
            # bucket1: 5 rows with theta_before=0.8, theta_after=0.2 (outlier: before >= after)
            {
                "error_type": "numeric_outlier",
                "feature_bucket": "bucket1",
                "theta_before": 0.8,
                "theta_after": 0.2,
                "weight": 5,
                "table_id": "t1",
            },
            # bucket1: 2 rows with theta_before=0.6, theta_after=0.4
            {
                "error_type": "numeric_outlier",
                "feature_bucket": "bucket1",
                "theta_before": 0.6,
                "theta_after": 0.4,
                "weight": 2,
                "table_id": "t1",
            },
            # bucket2: 3 rows with theta_before=0.9, theta_after=0.1
            {
                "error_type": "numeric_outlier",
                "feature_bucket": "bucket2",
                "theta_before": 0.9,
                "theta_after": 0.1,
                "weight": 3,
                "table_id": "t2",
            },
        ]
        self._write_corpus_stats(spark, fqn, corpus_rows)

        test_config = self._make_config_with_fqn(config, fqn)
        store = CorpusStatsStore(spark, test_config)

        candidates_df = spark.createDataFrame(
            [
                {
                    "candidate_id": "cand1",
                    "feature_bucket": "bucket1",
                    "theta_before": 0.7,
                    "theta_after": 0.3,
                },
            ]
        )

        result = store.batch_score(
            candidates_df, ErrorType.NUMERIC_OUTLIER, ComparisonDirection.DECREASING
        )
        result_pd = result.toPandas().set_index("candidate_id")

        # DECREASING: numerator = corpus_before >= theta1 AND corpus_after <= theta2
        # cand1: theta1=0.7, theta2=0.3
        #   (0.8, 0.2): 0.8 >= 0.7 ✓, 0.2 <= 0.3 ✓ -> YES, weight=5
        #   (0.6, 0.4): 0.6 >= 0.7 ✗ -> NO
        # numerator = 5
        # denominator: corpus_before >= theta2 = corpus_before >= 0.3
        #   (0.8, 0.2): 0.8 >= 0.3 ✓, weight=5
        #   (0.6, 0.4): 0.6 >= 0.3 ✓, weight=2
        # denominator = 7
        # lr_ratio = (5+1)/(7+1) = 6/8 = 0.75
        assert abs(result_pd.loc["cand1", "numerator_count"] - 5) < 0.001
        assert abs(result_pd.loc["cand1", "denominator_count"] - 7) < 0.001
        assert abs(result_pd.loc["cand1", "lr_ratio"] - 0.75) < 0.001

    def test_bucket_support_is_sum_of_weights_not_count_of_groups(
        self, spark: SparkSession, uc_location, config
    ):
        """bucket_support should be sum(weight), not count of groups."""
        catalog, schema = uc_location.catalog, uc_location.schema
        fqn = f"{catalog}.{schema}.test_bucket_support"

        # Two groups in same bucket with different thetas
        corpus_rows = [
            {
                "error_type": "uniqueness",
                "feature_bucket": "bucket1",
                "theta_before": 0.1,
                "theta_after": 0.5,
                "weight": 3,
                "table_id": "t1",
            },
            {
                "error_type": "uniqueness",
                "feature_bucket": "bucket1",
                "theta_before": 0.3,
                "theta_after": 0.7,
                "weight": 2,
                "table_id": "t1",
            },
        ]
        self._write_corpus_stats(spark, fqn, corpus_rows)

        test_config = self._make_config_with_fqn(config, fqn)
        store = CorpusStatsStore(spark, test_config)

        candidates_df = spark.createDataFrame(
            [
                {
                    "candidate_id": "cand1",
                    "feature_bucket": "bucket1",
                    "theta_before": 1.0,
                    "theta_after": 0.0,
                },
            ]
        )

        result = store.batch_score(
            candidates_df, ErrorType.UNIQUENESS, ComparisonDirection.INCREASING
        )
        result_pd = result.toPandas().set_index("candidate_id")

        # With theta1=1.0, theta2=0.0:
        # numerator: corpus_before <= 1.0 AND corpus_after >= 0.0 -> ALL rows match (3+2=5)
        # denominator: corpus_before <= 0.0 -> NONE match (0)
        # lr_ratio = (5+1)/(0+1) = 6.0
        # bucket_support should be sum of ALL weights in bucket = 3+2 = 5
        assert abs(result_pd.loc["cand1", "bucket_support"] - 5) < 0.001

    def test_candidate_deduplication(self, spark: SparkSession, uc_location, config):
        """Duplicate (bucket, theta1, theta2) candidates should each get their own scored row."""
        catalog, schema = uc_location.catalog, uc_location.schema
        fqn = f"{catalog}.{schema}.test_dedup"

        corpus_rows = [
            {
                "error_type": "uniqueness",
                "feature_bucket": "bucket1",
                "theta_before": 0.1,
                "theta_after": 0.5,
                "weight": 3,
                "table_id": "t1",
            },
        ]
        self._write_corpus_stats(spark, fqn, corpus_rows)

        test_config = self._make_config_with_fqn(config, fqn)
        store = CorpusStatsStore(spark, test_config)

        # Two candidates with identical (bucket, theta1, theta2) but different candidate_id
        candidates_df = spark.createDataFrame(
            [
                {
                    "candidate_id": "cand1",
                    "feature_bucket": "bucket1",
                    "theta_before": 0.2,
                    "theta_after": 0.6,
                },
                {
                    "candidate_id": "cand2",
                    "feature_bucket": "bucket1",
                    "theta_before": 0.2,
                    "theta_after": 0.6,
                },
            ]
        )

        result = store.batch_score(
            candidates_df, ErrorType.UNIQUENESS, ComparisonDirection.INCREASING
        )
        result_pd = result.toPandas().set_index("candidate_id")

        # Both should get same scores
        assert len(result_pd) == 2
        assert abs(result_pd.loc["cand1", "lr_ratio"] - result_pd.loc["cand2", "lr_ratio"]) < 0.001
        assert (
            abs(
                result_pd.loc["cand1", "numerator_count"]
                - result_pd.loc["cand2", "numerator_count"]
            )
            < 0.001
        )
        assert (
            abs(
                result_pd.loc["cand1", "denominator_count"]
                - result_pd.loc["cand2", "denominator_count"]
            )
            < 0.001
        )

    def test_candidates_with_no_bucket_support_get_lr_ratio_1(
        self, spark: SparkSession, uc_location, config
    ):
        """Candidates whose feature bucket has no corpus support get lr_ratio == 1.0."""
        catalog, schema = uc_location.catalog, uc_location.schema
        fqn = f"{catalog}.{schema}.test_no_support"

        corpus_rows = [
            {
                "error_type": "uniqueness",
                "feature_bucket": "bucket1",
                "theta_before": 0.1,
                "theta_after": 0.5,
                "weight": 3,
                "table_id": "t1",
            },
        ]
        self._write_corpus_stats(spark, fqn, corpus_rows)

        test_config = self._make_config_with_fqn(config, fqn)
        store = CorpusStatsStore(spark, test_config)

        # Candidate with bucket that doesn't exist in corpus
        candidates_df = spark.createDataFrame(
            [
                {
                    "candidate_id": "cand1",
                    "feature_bucket": "nonexistent_bucket",
                    "theta_before": 0.2,
                    "theta_after": 0.6,
                },
            ]
        )

        result = store.batch_score(
            candidates_df, ErrorType.UNIQUENESS, ComparisonDirection.INCREASING
        )
        result_pd = result.toPandas().set_index("candidate_id")

        assert abs(result_pd.loc["cand1", "lr_ratio"] - 1.0) < 0.001
        assert result_pd.loc["cand1", "numerator_count"] == 0
        assert result_pd.loc["cand1", "denominator_count"] == 0
        assert result_pd.loc["cand1", "bucket_support"] == 0

    def test_backward_compatibility_missing_weight_column(
        self, spark: SparkSession, uc_location, config
    ):
        """Corpus tables without weight column should get weight=1 fallback."""
        catalog, schema = uc_location.catalog, uc_location.schema
        fqn = f"{catalog}.{schema}.test_no_weight"

        # Old schema without weight column
        old_schema = StructType(
            [
                StructField("error_type", StringType(), nullable=False),
                StructField("feature_bucket", StringType(), nullable=False),
                StructField("theta_before", DoubleType(), nullable=False),
                StructField("theta_after", DoubleType(), nullable=False),
                StructField("table_id", StringType(), nullable=True),
            ]
        )

        corpus_rows = [
            {
                "error_type": "uniqueness",
                "feature_bucket": "bucket1",
                "theta_before": 0.1,
                "theta_after": 0.5,
                "table_id": "t1",
            },
            {
                "error_type": "uniqueness",
                "feature_bucket": "bucket1",
                "theta_before": 0.2,
                "theta_after": 0.6,
                "table_id": "t1",
            },
        ]
        df = spark.createDataFrame(corpus_rows, schema=old_schema)
        df.write.format("delta").mode("overwrite").partitionBy("error_type").option(
            "overwriteSchema", "true"
        ).saveAsTable(fqn)

        test_config = self._make_config_with_fqn(config, fqn)
        store = CorpusStatsStore(spark, test_config)

        # Should not raise an error; weight should be added as 1
        loaded = store.load(ErrorType.UNIQUENESS)
        assert "weight" in loaded.columns
        # Verify weight column is LongType (not IntegerType) for type compatibility
        weight_schema = loaded.schema["weight"]
        from pyspark.sql.types import LongType

        assert isinstance(weight_schema.dataType, LongType), (
            f"weight column should be LongType for compatibility, got {weight_schema.dataType}"
        )
        # All weights should be 1
        weights = loaded.select("weight").collect()
        assert all(w["weight"] == 1 for w in weights)

        # Scoring should work
        candidates_df = spark.createDataFrame(
            [
                {
                    "candidate_id": "cand1",
                    "feature_bucket": "bucket1",
                    "theta_before": 0.2,
                    "theta_after": 0.6,
                },
            ]
        )

        result = store.batch_score(
            candidates_df, ErrorType.UNIQUENESS, ComparisonDirection.INCREASING
        )
        result_pd = result.toPandas().set_index("candidate_id")

        # With weight=1 for each row, same logic as before
        # numerator: (0.1, 0.5) -> 0.1 <= 0.2 ✓, 0.5 >= 0.6 ✗
        #            (0.2, 0.6) -> 0.2 <= 0.2 ✓, 0.6 >= 0.6 ✓ -> YES (weight=1)
        # numerator = 1
        # denominator: corpus_before <= 0.2 -> both rows (0.1 and 0.2) -> 2
        # lr_ratio = (1+1)/(2+1) = 2/3
        assert abs(result_pd.loc["cand1", "lr_ratio"] - (2.0 / 3.0)) < 0.001


class TestBuilderWeightOutput:
    """Test that builder produces LongType weight."""

    def test_aggregate_scored_rows_returns_int64_weight(self):
        """Aggregated rows get int64 weight = count. Global pre-aggregation is in batch_score."""
        rows = [
            ("table1", "bucket1", 0.1, 0.2),
            ("table1", "bucket1", 0.1, 0.2),
        ]
        result = _aggregate_scored_rows(rows)
        assert result["weight"].dtype == "int64"
        # 2 duplicate rows are aggregated into 1 row with weight=2
        assert len(result) == 1
        assert result.iloc[0]["weight"] == 2


class TestCorpusStatsSchemaWeightType:
    """Test CORPUS_STATS_SCHEMA weight field."""

    def test_weight_is_long_type(self):
        from open_detect.algorithms.uni_detect.corpus.schema import CORPUS_STATS_SCHEMA

        weight_field = CORPUS_STATS_SCHEMA["weight"]
        assert weight_field is not None
        from pyspark.sql.types import LongType

        assert isinstance(weight_field.dataType, LongType)
        assert not weight_field.nullable
