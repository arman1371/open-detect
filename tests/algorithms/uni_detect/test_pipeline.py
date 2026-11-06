"""Unit tests for pipeline.py using mocked SparkSession (no real cluster required)."""

from __future__ import annotations

from contextlib import contextmanager
from unittest.mock import MagicMock, patch

import pytest
from pyspark.sql import DataFrame

from open_detect.algorithms.uni_detect.config import UniDetectConfig, UnityCatalogLocation
from open_detect.algorithms.uni_detect.core.enums import ErrorType
from open_detect.algorithms.uni_detect.pipeline import UniDetect
from open_detect.exceptions import ValidationError


def _config() -> UniDetectConfig:
    return UniDetectConfig(location=UnityCatalogLocation(catalog="c", schema="s"))


def _mock_spark() -> MagicMock:
    spark = MagicMock()
    spark.sparkContext.setJobGroup = MagicMock()
    # Mock the builder chain for get_spark
    # Also mock _active_spark_context for F.col to work
    spark.sparkContext._jsc = MagicMock()
    return spark


def _mock_detector_result(spark: MagicMock) -> MagicMock:
    """Create a mock result DataFrame that can be chained."""
    result = MagicMock(spec=DataFrame)
    result.persist.return_value = result
    result.count.return_value = 5
    result.orderBy.return_value = result
    result.unionByName.return_value = result
    return result


@contextmanager
def _mock_spark_context():
    """Create a mock SparkContext that can be set as active."""
    from pyspark import SparkContext
    mock_sc = MagicMock()
    mock_sc._jsc = MagicMock()
    # Patch the _active_spark_context class attribute
    original = SparkContext._active_spark_context
    SparkContext._active_spark_context = mock_sc
    try:
        yield mock_sc
    finally:
        SparkContext._active_spark_context = original


class TestUniDetectValidateInputs:
    """Tests for _validate_inputs (no Spark required)."""

    def test_rejects_unknown_kwargs(self):
        ud = UniDetect(_config(), spark=_mock_spark())
        with pytest.raises(ValidationError, match="Unknown parameter"):
            ud._validate_inputs(table_names=["t1"], error_types=[ErrorType.UNIQUENESS], unknown_kwarg="value")

    def test_accepts_valid_kwargs(self):
        ud = UniDetect(_config(), spark=_mock_spark())
        # Should not raise
        ud._validate_inputs(table_names=["t1"], error_types=[ErrorType.UNIQUENESS])

    def test_rejects_str_for_table_names(self):
        ud = UniDetect(_config(), spark=_mock_spark())
        with pytest.raises(ValidationError, match="sequence of str"):
            ud._validate_inputs(table_names="not_a_list")

    def test_rejects_str_for_error_types(self):
        ud = UniDetect(_config(), spark=_mock_spark())
        with pytest.raises(ValidationError, match="sequence of str"):
            ud._validate_inputs(table_names=["t1"], error_types="UNIQUENESS")

    def test_accepts_none_for_table_names(self):
        ud = UniDetect(_config(), spark=_mock_spark())
        # Should not raise when None (will use default)
        ud._validate_inputs(table_names=None, error_types=[ErrorType.UNIQUENESS])

    def test_accepts_none_for_error_types(self):
        ud = UniDetect(_config(), spark=_mock_spark())
        # Should not raise when None (will use default)
        ud._validate_inputs(table_names=["t1"], error_types=None)

    def test_rejects_non_str_in_table_names(self):
        ud = UniDetect(_config(), spark=_mock_spark())
        with pytest.raises(ValidationError, match="must be str"):
            ud._validate_inputs(table_names=["t1", 123])

    def test_rejects_non_str_in_error_types(self):
        ud = UniDetect(_config(), spark=_mock_spark())
        with pytest.raises(ValidationError, match="must be str"):
            ud._validate_inputs(table_names=["t1"], error_types=["UNIQUENESS", 123])


class TestUniDetectDetect:
    """Tests for detect() with mocked detectors."""

    def test_detect_calls_all_requested_detectors(self):
        """detect() should call each requested detector and union their results."""
        with _mock_spark_context():
            spark = _mock_spark()
            ud = UniDetect(_config(), spark=spark)

            # Mock detectors
            for et in ErrorType:
                mock_detector = MagicMock()
                mock_detector.detect.return_value = _mock_detector_result(spark)
                ud._detectors[et] = mock_detector

            error_types = [ErrorType.UNIQUENESS, ErrorType.SPELLING]
            result = ud.detect(table_names=["t1", "t2"], error_types=error_types)

            # Verify each detector was called
            for et in error_types:
                ud._detectors[et].detect.assert_called_once_with(["t1", "t2"])

            # Verify union and persist happened
            result.persist.assert_called()
            result.count.assert_called()
            result.orderBy.assert_called()

            # Verify release called on all detectors
            for et in error_types:
                ud._detectors[et].release.assert_called_once()

    def test_detect_uses_all_error_types_when_none_specified(self):
        """When error_types is None, all four detectors should be used."""
        with _mock_spark_context():
            spark = _mock_spark()
            ud = UniDetect(_config(), spark=spark)

            for et in ErrorType:
                mock_detector = MagicMock()
                mock_detector.detect.return_value = _mock_detector_result(spark)
                ud._detectors[et] = mock_detector

            ud.detect(table_names=["t1"])

            for et in ErrorType:
                ud._detectors[et].detect.assert_called_once_with(["t1"])

    def test_detect_validation_error_propagates(self):
        """ValidationError from _validate_inputs should propagate."""
        ud = UniDetect(_config(), spark=_mock_spark())
        with pytest.raises(ValidationError):
            ud.detect(table_names="not_a_list")


class TestUniDetectInit:
    """Tests for __init__."""

    def test_creates_four_detectors(self):
        spark = _mock_spark()
        ud = UniDetect(_config(), spark=spark)
        assert len(ud._detectors) == 4
        assert all(et in ud._detectors for et in ErrorType)

    def test_uses_get_spark_when_no_spark_provided(self):
        """Should call get_spark when no spark session is provided."""
        with patch("open_detect.algorithms.uni_detect.pipeline.get_spark") as mock_get_spark:
            mock_get_spark.return_value = _mock_spark()
            UniDetect(_config())
            mock_get_spark.assert_called_once()


class TestUniDetectWriteDetections:
    """Tests for write_detections."""

    def test_write_detections_calls_write_delta(self):
        spark = _mock_spark()
        ud = UniDetect(_config(), spark=spark)
        mock_df = MagicMock()
        mock_df.write.format.return_value.mode.return_value.saveAsTable = MagicMock()

        ud.write_detections(mock_df, mode="append")

        mock_df.write.format.assert_called_once_with("delta")
        mock_df.write.format.return_value.mode.assert_called_once_with("append")
        mock_df.write.format.return_value.mode.return_value.saveAsTable.assert_called_once_with(ud.config.detections_fqn)


class TestUniDetectBuildCorpusStatistics:
    """Tests for build_corpus_statistics (partial - validates input flow)."""

    def test_validate_inputs_called(self):
        spark = _mock_spark()
        ud = UniDetect(_config(), spark=spark)
        # Test that invalid error_types raises ValidationError
        with pytest.raises(ValidationError):
            ud.build_corpus_statistics(table_names=["t1"], error_types="not_a_list")


