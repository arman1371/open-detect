"""Unit tests for spark_utils.py using a mocked SparkSession (no real cluster required)."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from unidetect.spark_utils import get_spark


class TestGetSpark:
    def test_returns_active_session_if_present(self):
        active = MagicMock(name="active_session")
        with patch("pyspark.sql.SparkSession") as mock_session_cls:
            mock_session_cls.getActiveSession.return_value = active
            result = get_spark()

        assert result is active
        mock_session_cls.builder.appName.assert_not_called()

    def test_builds_a_new_session_when_none_active(self):
        built = MagicMock(name="new_session")
        with patch("pyspark.sql.SparkSession") as mock_session_cls:
            mock_session_cls.getActiveSession.return_value = None
            mock_session_cls.builder.appName.return_value.getOrCreate.return_value = built
            result = get_spark()

        assert result is built
        mock_session_cls.builder.appName.assert_called_once_with("unidetect")
