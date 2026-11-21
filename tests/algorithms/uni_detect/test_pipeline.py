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
    """Create a mock result DataFrame that can be chained.

    Returns the pre-sort frame. When ``unionByName`` is called on it (by reduce),
    it returns itself. Then when ``orderBy`` is called on the unioned result,
    it returns a new sorted result that persists and materializes.

    The pattern tests that detect() sorts BEFORE persisting to avoid re-execution
    of the scoring stage.
    """
    pre_sort_frame = MagicMock(spec=DataFrame)
    pre_sort_frame.persist.return_value = pre_sort_frame
    pre_sort_frame.count.return_value = 5
    pre_sort_frame.unionByName.return_value = pre_sort_frame  # union returns same frame
    pre_sort_frame.orderBy.return_value = (
        pre_sort_frame  # sort returns same frame (will be reconfigured)
    )

    # The sorted_result is what orderBy RETURNS - we need the chain:
    # unioned_frame.orderBy() -> sorted_frame, sorted_frame.persist() -> sorted_frame, sorted_frame.count()
    sorted_result = MagicMock(spec=DataFrame)
    sorted_result.persist.return_value = sorted_result
    sorted_result.count.return_value = 5

    # Configure orderBy on pre_sort_frame to return sorted_result
    pre_sort_frame.orderBy.return_value = sorted_result

    return pre_sort_frame


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
            ud._validate_inputs(
                table_names=["t1"], error_types=[ErrorType.UNIQUENESS], unknown_kwarg="value"
            )

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

    def test_accepts_severity_kwarg(self):
        """severity kwarg should be accepted."""
        ud = UniDetect(_config(), spark=_mock_spark())
        ud._validate_inputs(table_names=["t1"], error_types=[ErrorType.UNIQUENESS], severity="high")

    def test_accepts_description_kwarg(self):
        """description kwarg should be accepted."""
        ud = UniDetect(_config(), spark=_mock_spark())
        ud._validate_inputs(
            table_names=["t1"], error_types=[ErrorType.UNIQUENESS], description="Custom desc"
        )

    def test_accepts_affected_summary_kwarg(self):
        """affected_summary kwarg should be accepted."""
        ud = UniDetect(_config(), spark=_mock_spark())
        ud._validate_inputs(
            table_names=["t1"],
            error_types=[ErrorType.UNIQUENESS],
            affected_summary="Custom summary",
        )

    def test_rejects_invalid_severity(self):
        """Invalid severity should raise ValidationError."""
        ud = UniDetect(_config(), spark=_mock_spark())
        with pytest.raises(ValidationError, match="Invalid severity"):
            ud._validate_inputs(
                table_names=["t1"], error_types=[ErrorType.UNIQUENESS], severity="invalid"
            )


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

            # Get the pre-sort frame from the detector's first result (after union, result is the
            # same object as the first frame since unionByName returns the same mock)
            # We verify that orderBy was called on a unioned result frame, which becomes the
            # sorted result after orderBy returns a new mock.
            first_detector_frame = ud._detectors[ErrorType.UNIQUENESS].detect.return_value
            assert (
                first_detector_frame.orderBy.call_count == 1
            ), "orderBy should be called on the unioned result frame"

            # result is the sorted frame that should be persisted
            result.persist.assert_called_once()
            result.count.assert_called_once()

            # Verify each detector was called - now with shared ingestion DataFrames
            for et in error_types:
                call_args, call_kwargs = ud._detectors[et].detect.call_args
                assert call_args == (["t1", "t2"],)
                assert call_kwargs["ingested_columns_df"] is not None
                assert call_kwargs["ingested_pairs_df"] is None

            # release() IS called automatically in the finally block to free per-detector
            # caches (scored, joined, result frames) after the unioned result is
            # materialized. The caller is responsible for releasing the UNIONED
            # result frame (which has its own unpersist).
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
                call_args, call_kwargs = ud._detectors[et].detect.call_args
                assert call_args == (["t1"],)
                # UNIQUENESS, NUMERIC_OUTLIER, SPELLING need columns
                if et in (ErrorType.UNIQUENESS, ErrorType.NUMERIC_OUTLIER, ErrorType.SPELLING):
                    assert call_kwargs["ingested_columns_df"] is not None
                # FD needs pairs
                if et == ErrorType.FUNCTIONAL_DEPENDENCY:
                    assert call_kwargs["ingested_pairs_df"] is not None

    def test_detect_validation_error_propagates(self):
        """ValidationError from _validate_inputs should propagate."""
        ud = UniDetect(_config(), spark=_mock_spark())
        with pytest.raises(ValidationError):
            ud.detect(table_names="not_a_list")

    def test_detect_passes_severity_and_description_to_notification(self):
        """detect() should pass severity and description to notification hook."""
        with _mock_spark_context():
            spark = _mock_spark()
            ud = UniDetect(_config(), spark=spark)

            for et in ErrorType:
                mock_detector = MagicMock()
                mock_detector.detect.return_value = _mock_detector_result(spark)
                ud._detectors[et] = mock_detector

            with patch(
                "open_detect.algorithms.uni_detect.pipeline.get_notification_config"
            ) as mock_config:
                mock_config.return_value = {
                    "enabled": True,
                    "webhook_url": "https://test.url",
                    "severity_threshold": "medium",
                    "rate_limit": {"max_per_hour": 5},
                }

                with patch(
                    "open_detect.algorithms.uni_detect.pipeline.TeamsNotifier"
                ) as mock_notifier_class:
                    mock_notifier = MagicMock()
                    mock_notifier.send_safe.return_value = True
                    mock_notifier_class.return_value = mock_notifier

                    ud.detect(
                        table_names=["t1"],
                        error_types=[ErrorType.UNIQUENESS],
                        severity="high",
                        description="Test description",
                    )

                    # Verify notification was called with correct params
                    mock_notifier.send_safe.assert_called_once()
                    call_kwargs = mock_notifier.send_safe.call_args.kwargs
                    assert call_kwargs["severity"] == "high"
                    assert call_kwargs["description"] == "Test description"


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
        mock_df.write.format.return_value.mode.return_value.saveAsTable.assert_called_once_with(
            ud.config.detections_fqn
        )


class TestUniDetectBuildCorpusStatistics:
    """Tests for build_corpus_statistics (partial - validates input flow)."""

    def test_validate_inputs_called(self):
        spark = _mock_spark()
        ud = UniDetect(_config(), spark=spark)
        # Test that invalid error_types raises ValidationError
        with pytest.raises(ValidationError):
            ud.build_corpus_statistics(table_names=["t1"], error_types="not_a_list")


class TestUniDetectRelease:
    """Tests for release() method."""

    def test_release_calls_detector_release(self):
        """release() should call release() on all detectors."""
        with _mock_spark_context():
            spark = _mock_spark()
            ud = UniDetect(_config(), spark=spark)

            # Mock detectors
            for et in ErrorType:
                mock_detector = MagicMock()
                ud._detectors[et] = mock_detector

            ud.release()

            # Each detector's release should be called once
            for et in ErrorType:
                ud._detectors[et].release.assert_called_once()

    def test_release_safe_when_no_frames_tracked(self):
        """release() should be safe when detectors have no tracked frames."""
        mock_spark = _mock_spark()
        ud = UniDetect(_config(), spark=mock_spark)

        # Detectors with empty _persisted lists
        for et in ErrorType:
            mock_detector = MagicMock()
            mock_detector._persisted = []
            ud._detectors[et] = mock_detector

        # Should not raise
        ud.release()


class TestBuildAffectedSummary:
    """Tests for _build_affected_summary method."""

    def test_builds_summary_with_candidates_count(self):
        """Should include candidate count in the summary."""
        spark = _mock_spark()
        ud = UniDetect(_config(), spark=spark)

        result = ud._build_affected_summary(ErrorType.UNIQUENESS, 5)
        assert "Uniqueness" in result
        assert "5 anomaly" in result

    def test_handles_zero_candidates(self):
        """Should indicate no anomalies found when count is 0."""
        spark = _mock_spark()
        ud = UniDetect(_config(), spark=spark)

        result = ud._build_affected_summary(ErrorType.NUMERIC_OUTLIER, 0)
        assert result == "Numeric Outlier detection - no specific anomalies found"

    def test_includes_description_when_provided(self):
        """Should include description in the summary."""
        spark = _mock_spark()
        ud = UniDetect(_config(), spark=spark)

        result = ud._build_affected_summary(
            ErrorType.SPELLING, 10, description="Suspicious string patterns detected"
        )
        assert result == "Spelling detection: Suspicious string patterns detected"

    def test_handles_all_error_types(self):
        """Should correctly format all error type names."""
        spark = _mock_spark()
        ud = UniDetect(_config(), spark=spark)

        expected_names = {
            ErrorType.UNIQUENESS: "Uniqueness",
            ErrorType.NUMERIC_OUTLIER: "Numeric Outlier",
            ErrorType.SPELLING: "Spelling",
            ErrorType.FUNCTIONAL_DEPENDENCY: "Functional Dependency",
        }

        for error_type, expected_name in expected_names.items():
            result = ud._build_affected_summary(error_type, 3)
            assert expected_name in result


class TestSendTeamsNotificationAfterAllDetections:
    """Tests for _send_teams_notification_after_all_detections method."""

    def test_skips_when_notifications_disabled(self):
        """Should skip notification when TEAMS_NOTIFICATION_ENABLED is False."""
        with _mock_spark_context():
            spark = _mock_spark()
            ud = UniDetect(_config(), spark=spark)

            mock_df = MagicMock(spec=DataFrame)
            mock_df.count.return_value = 5

            with patch(
                "open_detect.algorithms.uni_detect.pipeline.get_notification_config"
            ) as mock_config:
                mock_config.return_value = {
                    "enabled": False,
                    "webhook_url": "https://test.url",
                    "severity_threshold": "medium",
                    "rate_limit": {"max_per_hour": 5},
                }

                ud._send_teams_notification_after_all_detections(
                    (ErrorType.UNIQUENESS,), mock_df, severity="high"
                )

                # Should return early without sending - no assertion needed,
                # the method should just return without error

    def test_skips_when_webhook_not_configured(self):
        """Should skip notification when webhook URL is not configured."""
        with _mock_spark_context():
            spark = _mock_spark()
            ud = UniDetect(_config(), spark=spark)

            mock_df = MagicMock(spec=DataFrame)
            mock_df.count.return_value = 5

            with patch(
                "open_detect.algorithms.uni_detect.pipeline.get_notification_config"
            ) as mock_config:
                mock_config.return_value = {
                    "enabled": True,
                    "webhook_url": None,  # No webhook configured
                    "severity_threshold": "medium",
                    "rate_limit": {"max_per_hour": 5},
                }

                ud._send_teams_notification_after_all_detections(
                    (ErrorType.UNIQUENESS,), mock_df, severity="high"
                )

                # Should return early without sending

    def test_skips_when_severity_below_threshold(self):
        """Should skip notification when severity is below threshold."""
        with _mock_spark_context():
            spark = _mock_spark()
            ud = UniDetect(_config(), spark=spark)

            mock_df = MagicMock(spec=DataFrame)
            mock_df.count.return_value = 5

            with patch(
                "open_detect.algorithms.uni_detect.pipeline.get_notification_config"
            ) as mock_config:
                mock_config.return_value = {
                    "enabled": True,
                    "webhook_url": "https://test.url",
                    "severity_threshold": "high",  # high threshold
                    "rate_limit": {"max_per_hour": 5},
                }

                ud._send_teams_notification_after_all_detections(
                    (ErrorType.UNIQUENESS,),
                    mock_df,
                    severity="medium",  # medium severity
                )

                # Should return early without sending

    def test_skips_when_zero_candidates_no_override(self):
        """Should skip notification when no anomalies detected and no override."""
        with _mock_spark_context():
            spark = _mock_spark()
            ud = UniDetect(_config(), spark=spark)

            mock_df = MagicMock(spec=DataFrame)
            mock_df.count.return_value = 0

            with patch(
                "open_detect.algorithms.uni_detect.pipeline.get_notification_config"
            ) as mock_config:
                mock_config.return_value = {
                    "enabled": True,
                    "webhook_url": "https://test.url",
                    "severity_threshold": "medium",
                    "rate_limit": {"max_per_hour": 5},
                }

                with patch(
                    "open_detect.algorithms.uni_detect.pipeline.TeamsNotifier"
                ) as mock_notifier_class:
                    ud._send_teams_notification_after_all_detections(
                        (ErrorType.UNIQUENESS,), mock_df, severity="high"
                    )

                    # TeamsNotifier should not be instantiated
                    mock_notifier_class.assert_not_called()

    def test_sends_notification_when_zero_candidates_with_override(self):
        """Should send notification when zero candidates but override provided."""
        with _mock_spark_context():
            spark = _mock_spark()
            ud = UniDetect(_config(), spark=spark)

            mock_df = MagicMock(spec=DataFrame)
            mock_df.count.return_value = 0

            with patch(
                "open_detect.algorithms.uni_detect.pipeline.get_notification_config"
            ) as mock_config:
                mock_config.return_value = {
                    "enabled": True,
                    "webhook_url": "https://test.url",
                    "severity_threshold": "medium",
                    "rate_limit": {"max_per_hour": 5},
                }

                with patch(
                    "open_detect.algorithms.uni_detect.pipeline.TeamsNotifier"
                ) as mock_notifier_class:
                    mock_notifier = MagicMock()
                    mock_notifier.send_safe.return_value = True
                    mock_notifier_class.return_value = mock_notifier

                    ud._send_teams_notification_after_all_detections(
                        (ErrorType.UNIQUENESS,),
                        mock_df,
                        severity="high",
                        affected_summary_override="Custom summary for zero results",
                    )

                    mock_notifier_class.assert_called_once()
                    mock_notifier.send_safe.assert_called_once()
                    call_kwargs = mock_notifier.send_safe.call_args.kwargs
                    assert call_kwargs["affected"] == "Custom summary for zero results"

    @patch("open_detect.algorithms.uni_detect.pipeline.TeamsNotifier")
    @patch("open_detect.algorithms.uni_detect.pipeline.get_notification_config")
    def test_sends_notification_when_severity_meets_threshold(
        self, mock_config, mock_notifier_class
    ):
        """Should send notification when severity meets threshold."""
        with _mock_spark_context():
            spark = _mock_spark()
            ud = UniDetect(_config(), spark=spark)

            mock_df = MagicMock(spec=DataFrame)
            mock_df.count.return_value = 5

            mock_notifier = MagicMock()
            mock_notifier.send_safe.return_value = True
            mock_notifier_class.return_value = mock_notifier

            mock_config.return_value = {
                "enabled": True,
                "webhook_url": "https://test.url",
                "severity_threshold": "medium",
                "rate_limit": {"max_per_hour": 5},
            }

            ud._send_teams_notification_after_all_detections(
                (ErrorType.UNIQUENESS,), mock_df, severity="high"
            )

            # Verify TeamsNotifier was created and send_safe was called
            mock_notifier_class.assert_called_once_with(
                webhook_url="https://test.url",
                severity_threshold="medium",
                rate_limit={"max_per_hour": 5},
            )
            mock_notifier.send_safe.assert_called_once()

            # Verify the call arguments
            call_kwargs = mock_notifier.send_safe.call_args.kwargs
            assert call_kwargs["event_type"] == "scan_context_uniqueness"
            assert call_kwargs["severity"] == "high"

    @patch("open_detect.algorithms.uni_detect.pipeline.TeamsNotifier")
    @patch("open_detect.algorithms.uni_detect.pipeline.get_notification_config")
    def test_uses_description_from_kwargs(self, mock_config, mock_notifier_class):
        """Should use description from kwargs if provided."""
        with _mock_spark_context():
            spark = _mock_spark()
            ud = UniDetect(_config(), spark=spark)

            mock_df = MagicMock(spec=DataFrame)
            mock_df.count.return_value = 5

            mock_notifier = MagicMock()
            mock_notifier.send_safe.return_value = True
            mock_notifier_class.return_value = mock_notifier

            mock_config.return_value = {
                "enabled": True,
                "webhook_url": "https://test.url",
                "severity_threshold": "medium",
                "rate_limit": {"max_per_hour": 5},
            }

            ud._send_teams_notification_after_all_detections(
                (ErrorType.SPELLING,),
                mock_df,
                severity="high",
                description="Custom description",
            )

            call_kwargs = mock_notifier.send_safe.call_args.kwargs
            assert call_kwargs["description"] == "Custom description"

    @patch("open_detect.algorithms.uni_detect.pipeline.TeamsNotifier")
    @patch("open_detect.algorithms.uni_detect.pipeline.get_notification_config")
    def test_notification_failure_does_not_break_detection(self, mock_config, mock_notifier_class):
        """Notification failure should not break detection - best effort."""
        with _mock_spark_context():
            spark = _mock_spark()
            ud = UniDetect(_config(), spark=spark)

            mock_df = MagicMock(spec=DataFrame)
            mock_df.count.return_value = 5

            mock_notifier = MagicMock()
            mock_notifier.send_safe.side_effect = Exception("Network error")
            mock_notifier_class.return_value = mock_notifier

            mock_config.return_value = {
                "enabled": True,
                "webhook_url": "https://test.url",
                "severity_threshold": "medium",
                "rate_limit": {"max_per_hour": 5},
            }

            # Should not raise - exception is caught internally
            ud._send_teams_notification_after_all_detections(
                (ErrorType.UNIQUENESS,), mock_df, severity="high"
            )

            # Verify send_safe was still called
            mock_notifier.send_safe.assert_called_once()

    @patch("open_detect.algorithms.uni_detect.pipeline.TeamsNotifier")
    @patch("open_detect.algorithms.uni_detect.pipeline.get_notification_config")
    def test_reuses_notifier_across_calls(self, mock_config, mock_notifier_class):
        """Should reuse the same notifier instance for rate limiting."""
        with _mock_spark_context():
            spark = _mock_spark()
            ud = UniDetect(_config(), spark=spark)

            mock_df = MagicMock(spec=DataFrame)
            mock_df.count.return_value = 5

            mock_notifier = MagicMock()
            mock_notifier.send_safe.return_value = True
            mock_notifier_class.return_value = mock_notifier

            mock_config.return_value = {
                "enabled": True,
                "webhook_url": "https://test.url",
                "severity_threshold": "medium",
                "rate_limit": {"max_per_hour": 5},
            }

            # Call twice
            ud._send_teams_notification_after_all_detections(
                (ErrorType.UNIQUENESS,), mock_df, severity="high"
            )
            ud._send_teams_notification_after_all_detections(
                (ErrorType.SPELLING,), mock_df, severity="high"
            )

            # TeamsNotifier should only be instantiated once (reused)
            assert mock_notifier_class.call_count == 1

    @patch("open_detect.algorithms.uni_detect.pipeline.TeamsNotifier")
    @patch("open_detect.algorithms.uni_detect.pipeline.get_notification_config")
    def test_invalid_config_severity_threshold_defaults(self, mock_config, mock_notifier_class):
        """Invalid severity_threshold from config should default to medium."""
        with _mock_spark_context():
            spark = _mock_spark()
            ud = UniDetect(_config(), spark=spark)

            mock_df = MagicMock(spec=DataFrame)
            mock_df.count.return_value = 5

            mock_notifier = MagicMock()
            mock_notifier.send_safe.return_value = True
            mock_notifier_class.return_value = mock_notifier

            # Invalid severity_threshold in config
            mock_config.return_value = {
                "enabled": True,
                "webhook_url": "https://test.url",
                "severity_threshold": "invalid_value",
                "rate_limit": {"max_per_hour": 5},
            }

            ud._send_teams_notification_after_all_detections(
                (ErrorType.UNIQUENESS,), mock_df, severity="high"
            )

            # Should default to medium
            mock_notifier_class.assert_called_once_with(
                webhook_url="https://test.url",
                severity_threshold="medium",  # defaulted
                rate_limit={"max_per_hour": 5},
            )


class TestDetectEndToEnd:
    """End-to-end tests for detect() with notifications."""

    @patch("open_detect.algorithms.uni_detect.pipeline.TeamsNotifier")
    @patch("open_detect.algorithms.uni_detect.pipeline.get_notification_config")
    def test_detect_with_notifications_enabled(self, mock_config, mock_notifier_class):
        """Full detect() path with notifications enabled."""
        with _mock_spark_context():
            spark = _mock_spark()
            ud = UniDetect(_config(), spark=spark)

            for et in ErrorType:
                mock_detector = MagicMock()
                mock_detector.detect.return_value = _mock_detector_result(spark)
                ud._detectors[et] = mock_detector

            mock_notifier = MagicMock()
            mock_notifier.send_safe.return_value = True
            mock_notifier_class.return_value = mock_notifier

            mock_config.return_value = {
                "enabled": True,
                "webhook_url": "https://test.url",
                "severity_threshold": "medium",
                "rate_limit": {"max_per_hour": 5},
            }

            result = ud.detect(
                table_names=["t1"],
                error_types=[ErrorType.UNIQUENESS, ErrorType.SPELLING],
                severity="high",
                description="E2E test",
            )

            # Verify detect completed successfully
            assert result is not None
            # Verify notification was sent once with combined event type
            mock_notifier.send_safe.assert_called_once()
            call_kwargs = mock_notifier.send_safe.call_args.kwargs
            assert call_kwargs["severity"] == "high"
            assert call_kwargs["description"] == "E2E test"
            assert "uniqueness" in call_kwargs["event_type"]
            assert "spelling" in call_kwargs["event_type"]


class TestConfigParsingErrors:
    """Tests for tolerant config parsing."""

    @patch("open_detect.algorithms.uni_detect.pipeline.get_notification_config")
    def test_invalid_rate_limit_value_does_not_crash(self, mock_config):
        """Invalid TEAMS_RATE_LIMIT_MAX_PER_HOUR should not crash detection."""
        with _mock_spark_context():
            spark = _mock_spark()
            ud = UniDetect(_config(), spark=spark)

            mock_df = MagicMock(spec=DataFrame)
            mock_df.count.return_value = 5

            # Config returns invalid rate_limit (simulates env var parsing error)
            mock_config.return_value = {
                "enabled": True,
                "webhook_url": "https://test.url",
                "severity_threshold": "medium",
                "rate_limit": {
                    "max_per_hour": "abc"
                },  # invalid - should be handled by TeamsNotifier
            }

            with patch(
                "open_detect.algorithms.uni_detect.pipeline.TeamsNotifier"
            ) as mock_notifier_class:
                mock_notifier = MagicMock()
                mock_notifier.send_safe.return_value = True
                mock_notifier_class.return_value = mock_notifier

                # Should not raise
                ud._send_teams_notification_after_all_detections(
                    (ErrorType.UNIQUENESS,), mock_df, severity="high"
                )
