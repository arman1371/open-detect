"""Edge-case tests for corpus/store.py, corpus/ingestion.py and detectors/base.py.

Unlike ``test_corpus_and_detectors.py`` (which builds a large synthetic
corpus to validate true-positive/false-positive ranking), these tests target
specific branches that a full end-to-end run doesn't naturally exercise:
missing corpus tables, empty/too-small inputs, and tables that fail to read.

These tests require a local Delta-enabled Spark session (see
``conftest.py::spark``) and are skipped automatically if one cannot be
started.
"""

from __future__ import annotations

import pytest

from unidetect.config import UniDetectConfig
from unidetect.core.enums import ErrorType
from unidetect.corpus.ingestion import CorpusIngestor
from unidetect.corpus.store import CorpusStatsStore
from unidetect.exceptions import CorpusNotFoundError
from unidetect.pipeline import UniDetect


def _write_table(spark, fqn: str, rows: list[dict], columns: list[str]) -> None:
    if rows:
        df = spark.createDataFrame([tuple(row[c] for c in columns) for row in rows], schema=columns)
    else:
        # createDataFrame cannot infer a schema from an empty list of rows,
        # so an all-string StructType is supplied explicitly instead.
        from pyspark.sql.types import StringType, StructField, StructType

        schema = StructType([StructField(c, StringType()) for c in columns])
        df = spark.createDataFrame([], schema=schema)
    df.write.format("delta").mode("overwrite").saveAsTable(fqn)


@pytest.fixture
def config(uc_location):
    return UniDetectConfig(
        location=uc_location,
        epsilon=0.05,
        alpha=0.2,
        max_mpd_block_size=200,
        max_fd_column_pairs_per_table=10,
    )


class TestCorpusStatsStoreBeforeBuild:
    """These tests need a corpus-stats/token-stats table that has genuinely
    never been written -- unlike ``config`` above, which shares its table
    names with every other Delta-backed test file against the same
    ``spark`` session, this uses table names unique to this class so an
    unrelated test's ``build_corpus_statistics()`` call elsewhere in the
    suite can never make ``table_exists()`` true before this class's own
    "before build" assertions run.
    """

    @pytest.fixture
    def config(self, uc_location):
        return UniDetectConfig(
            location=uc_location,
            corpus_stats_table="unidetect_corpus_stats_before_build_test",
            token_stats_table="unidetect_token_stats_before_build_test",
        )

    def test_table_exists_is_false(self, spark, config):
        store = CorpusStatsStore(spark, config)
        assert store.table_exists() is False

    def test_load_raises_corpus_not_found(self, spark, config):
        store = CorpusStatsStore(spark, config)
        with pytest.raises(CorpusNotFoundError):
            store.load(ErrorType.UNIQUENESS)

    def test_load_token_stats_map_is_empty_when_missing(self, spark, config):
        store = CorpusStatsStore(spark, config)
        assert store.load_token_stats_map() == {}


class TestLoadTokenStatsMapCap:
    def test_respects_max_tokens(self, spark, config):
        df = spark.createDataFrame(
            [("common", 100), ("mid", 10), ("rare", 1)],
            schema=["token", "doc_frequency"],
        )
        df.write.format("delta").mode("overwrite").saveAsTable(config.token_stats_fqn)

        store = CorpusStatsStore(spark, config)
        top_two = store.load_token_stats_map(max_tokens=2)

        assert len(top_two) == 2
        assert set(top_two) == {"common", "mid"}

        everything = store.load_token_stats_map(max_tokens=None)
        assert everything == {"common": 100, "mid": 10, "rare": 1}


class TestCorpusIngestorSkipsBadInputs:
    def test_skips_nonexistent_table(self, spark, uc_location):
        ingestor = CorpusIngestor(spark)
        fqn = f"{uc_location.catalog}.{uc_location.schema}.does_not_exist_at_all"

        result = ingestor.ingest_columns([fqn])

        assert result.count() == 0

    def test_skips_empty_table(self, spark, uc_location):
        fqn = f"{uc_location.catalog}.{uc_location.schema}.empty_table_columns"
        _write_table(spark, fqn, [], ["a"])

        ingestor = CorpusIngestor(spark)
        result = ingestor.ingest_columns([fqn])

        assert result.count() == 0

    def test_ingest_column_pairs_skips_single_column_table(self, spark, uc_location):
        fqn = f"{uc_location.catalog}.{uc_location.schema}.single_column_table"
        _write_table(spark, fqn, [{"a": "1"}, {"a": "2"}], ["a"])

        ingestor = CorpusIngestor(spark)
        result = ingestor.ingest_column_pairs([fqn])

        assert result.count() == 0

    def test_ingest_column_pairs_skips_empty_table(self, spark, uc_location):
        fqn = f"{uc_location.catalog}.{uc_location.schema}.empty_table_pairs"
        _write_table(spark, fqn, [], ["a", "b"])

        ingestor = CorpusIngestor(spark)
        result = ingestor.ingest_column_pairs([fqn])

        assert result.count() == 0


class TestDetectReturnsEmptyResultWhenNoCandidates:
    def test_uniqueness_detect_on_too_few_rows(self, spark, uc_location, config):
        fqn = f"{uc_location.catalog}.{uc_location.schema}.tiny_uniqueness_target"
        # UniquenessDetector requires >= 5 rows; this table has only 2.
        _write_table(spark, fqn, [{"code": "a"}, {"code": "b"}], ["code"])

        ud = UniDetect(config, spark=spark)
        result = ud.detect([fqn], error_types=[ErrorType.UNIQUENESS])

        assert result.count() == 0
        assert set(result.columns) == {
            "candidate_id",
            "error_type",
            "table_id",
            "column_names",
            "row_ids",
            "lr_ratio",
            "surprisal",
            "is_significant",
            "support",
            "evidence_json",
        }

    def test_uniqueness_detect_with_no_duplicates_yields_no_candidates(
        self, spark, uc_location, config
    ):
        fqn = f"{uc_location.catalog}.{uc_location.schema}.all_unique_target"
        # Enough rows, but no duplicates -> perturb_uniqueness drops nothing.
        rows = [{"code": f"id{i}"} for i in range(10)]
        _write_table(spark, fqn, rows, ["code"])

        ud = UniDetect(config, spark=spark)
        result = ud.detect([fqn], error_types=[ErrorType.UNIQUENESS])

        assert result.count() == 0
