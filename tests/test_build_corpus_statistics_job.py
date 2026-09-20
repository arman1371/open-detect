"""Unit tests for jobs/build_corpus_statistics.py (argument parsing + orchestration only).

See ``test_run_detection_job.py`` for why the pipeline itself is mocked here
rather than exercised end-to-end.
"""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from unidetect.core.enums import ErrorType
from unidetect.jobs.build_corpus_statistics import main, parse_args


class TestParseArgs:
    def test_required_arguments_and_defaults(self):
        args = parse_args(
            ["--catalog", "main", "--schema", "data_quality", "--corpus-tables", "a,b"]
        )
        assert args.catalog == "main"
        assert args.schema == "data_quality"
        assert args.corpus_tables == "a,b"
        assert args.corpus_catalog is None
        assert args.epsilon == 0.01
        assert args.alpha == 0.05

    def test_error_types_default_to_all(self):
        args = parse_args(["--catalog", "main", "--schema", "s", "--corpus-tables", "a"])
        assert set(args.error_types.split(",")) == {e.value for e in ErrorType}


class TestMain:
    def test_builds_from_explicit_corpus_tables(self):
        with (
            patch("unidetect.jobs.build_corpus_statistics.get_spark") as mock_get_spark,
            patch("unidetect.jobs.build_corpus_statistics.UniDetect") as mock_unidetect_cls,
        ):
            mock_get_spark.return_value = MagicMock()
            ud = mock_unidetect_cls.return_value

            main(
                [
                    "--catalog",
                    "main",
                    "--schema",
                    "data_quality",
                    "--corpus-tables",
                    "main.sales.orders,main.sales.customers",
                    "--error-types",
                    "uniqueness",
                ]
            )

            ud.build_corpus_statistics.assert_called_once()
            called_tables, called_kwargs = ud.build_corpus_statistics.call_args
            assert called_tables[0] == ["main.sales.orders", "main.sales.customers"]
            assert called_kwargs["error_types"] == [ErrorType.UNIQUENESS]

    def test_scans_catalog_when_corpus_tables_omitted(self):
        with (
            patch("unidetect.jobs.build_corpus_statistics.get_spark") as mock_get_spark,
            patch("unidetect.jobs.build_corpus_statistics.UniDetect") as mock_unidetect_cls,
            patch(
                "unidetect.jobs.build_corpus_statistics.list_tables_matching"
            ) as mock_list_tables,
        ):
            mock_get_spark.return_value = MagicMock()
            mock_list_tables.return_value = ["main.sales.orders"]
            ud = mock_unidetect_cls.return_value

            main(
                [
                    "--catalog",
                    "main",
                    "--schema",
                    "data_quality",
                    "--corpus-catalog",
                    "main",
                    "--corpus-schemas",
                    "sales,hr",
                ]
            )

            mock_list_tables.assert_called_once_with(
                mock_get_spark.return_value, "main", ["sales", "hr"]
            )
            ud.build_corpus_statistics.assert_called_once()
            called_tables, _ = ud.build_corpus_statistics.call_args
            assert called_tables[0] == ["main.sales.orders"]

    def test_requires_corpus_tables_or_corpus_catalog(self):
        # main() calls get_spark() before validating --corpus-tables/
        # --corpus-catalog, so this must be mocked like every other main()
        # test here -- otherwise it creates a real, plain (non-Delta)
        # SparkSession as a side effect, which every later Delta-backed test
        # in the suite then silently reuses via SparkSession.getOrCreate()
        # ("Using an existing Spark session"), permanently losing the Delta
        # catalog/jars configuration for the rest of the test run.
        with patch("unidetect.jobs.build_corpus_statistics.get_spark") as mock_get_spark:
            mock_get_spark.return_value = MagicMock()
            with pytest.raises(SystemExit):
                main(["--catalog", "main", "--schema", "s"])

    def test_exits_when_no_corpus_tables_resolved(self):
        with (
            patch("unidetect.jobs.build_corpus_statistics.get_spark") as mock_get_spark,
            patch(
                "unidetect.jobs.build_corpus_statistics.list_tables_matching"
            ) as mock_list_tables,
        ):
            mock_get_spark.return_value = MagicMock()
            mock_list_tables.return_value = []

            with pytest.raises(SystemExit):
                main(["--catalog", "main", "--schema", "s", "--corpus-catalog", "main"])
