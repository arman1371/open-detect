"""Unit tests for jobs/run_detection.py (argument parsing + orchestration only).

``main()`` is exercised with a mocked Spark session and a mocked
:class:`~unidetect.pipeline.UniDetect`, since this module's own job is just
CLI plumbing around the pipeline -- the pipeline's actual behavior is already
covered by ``test_corpus_and_detectors.py``.
"""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from unidetect.core.enums import ErrorType
from unidetect.jobs.run_detection import main, parse_args


class TestParseArgs:
    def test_required_arguments(self):
        args = parse_args(
            [
                "--catalog",
                "main",
                "--schema",
                "data_quality",
                "--target-tables",
                "main.sales.orders",
            ]
        )
        assert args.catalog == "main"
        assert args.schema == "data_quality"
        assert args.target_tables == "main.sales.orders"
        assert args.alpha == 0.05
        assert args.top_k is None
        assert args.write_results is False

    def test_error_types_default_to_all(self):
        args = parse_args(
            ["--catalog", "main", "--schema", "s", "--target-tables", "t"],
        )
        assert set(args.error_types.split(",")) == {e.value for e in ErrorType}

    def test_can_override_optional_arguments(self):
        args = parse_args(
            [
                "--catalog",
                "main",
                "--schema",
                "s",
                "--target-tables",
                "a,b",
                "--error-types",
                "uniqueness,spelling",
                "--alpha",
                "0.1",
                "--top-k",
                "5",
                "--write-results",
            ]
        )
        assert args.target_tables == "a,b"
        assert args.error_types == "uniqueness,spelling"
        assert args.alpha == 0.1
        assert args.top_k == 5
        assert args.write_results is True


class TestMain:
    def _mock_detections(self):
        detections = MagicMock()
        detections.where.return_value.count.return_value = 0
        detections.limit.return_value = detections
        return detections

    def test_detects_and_shows_results(self):
        with (
            patch("unidetect.jobs.run_detection.get_spark") as mock_get_spark,
            patch("unidetect.jobs.run_detection.UniDetect") as mock_unidetect_cls,
        ):
            mock_get_spark.return_value = MagicMock()
            ud = mock_unidetect_cls.return_value
            detections = self._mock_detections()
            ud.detect.return_value = detections

            main(
                [
                    "--catalog",
                    "main",
                    "--schema",
                    "data_quality",
                    "--target-tables",
                    "main.sales.orders,main.sales.customers",
                    "--error-types",
                    "uniqueness",
                ]
            )

            ud.detect.assert_called_once()
            called_tables, called_kwargs = ud.detect.call_args
            assert called_tables[0] == ["main.sales.orders", "main.sales.customers"]
            assert called_kwargs["error_types"] == [ErrorType.UNIQUENESS]
            detections.show.assert_called_once()
            ud.write_detections.assert_not_called()

    def test_applies_top_k_limit(self):
        with (
            patch("unidetect.jobs.run_detection.get_spark") as mock_get_spark,
            patch("unidetect.jobs.run_detection.UniDetect") as mock_unidetect_cls,
        ):
            mock_get_spark.return_value = MagicMock()
            ud = mock_unidetect_cls.return_value
            detections = self._mock_detections()
            ud.detect.return_value = detections

            main(
                [
                    "--catalog",
                    "main",
                    "--schema",
                    "s",
                    "--target-tables",
                    "t",
                    "--top-k",
                    "3",
                ]
            )

            detections.limit.assert_called_once_with(3)

    def test_writes_results_when_requested(self):
        with (
            patch("unidetect.jobs.run_detection.get_spark") as mock_get_spark,
            patch("unidetect.jobs.run_detection.UniDetect") as mock_unidetect_cls,
        ):
            mock_get_spark.return_value = MagicMock()
            ud = mock_unidetect_cls.return_value
            detections = self._mock_detections()
            ud.detect.return_value = detections

            main(
                [
                    "--catalog",
                    "main",
                    "--schema",
                    "s",
                    "--target-tables",
                    "t",
                    "--write-results",
                ]
            )

            ud.write_detections.assert_called_once_with(detections, mode="append")
