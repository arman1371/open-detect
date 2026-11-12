"""Extended unit tests for spark_utils.py (no real cluster required)."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from open_detect.algorithms.uni_detect.spark_utils import (
    ARROW_MAX_RECORDS_PER_BATCH,
    ARROW_MAX_RECORDS_PER_BATCH_KEY,
    get_spark,
    scoped_conf,
)


class TestGetSparkExtended:
    """Extended tests for get_spark."""

    def test_returns_active_session_if_present(self):
        active = MagicMock()
        with patch("pyspark.sql.SparkSession") as mock_session_cls:
            mock_session_cls.getActiveSession.return_value = active
            result = get_spark()

        assert result is active
        mock_session_cls.builder.appName.assert_not_called()

    def test_builds_a_new_session_when_none_active(self):
        built = MagicMock()
        with patch("pyspark.sql.SparkSession") as mock_session_cls:
            mock_session_cls.getActiveSession.return_value = None
            mock_session_cls.builder.appName.return_value.getOrCreate.return_value = built
            result = get_spark()

        assert result is built
        mock_session_cls.builder.appName.assert_called_once_with("open_detect")


class TestScopedConf:
    """Tests for scoped_conf context manager."""

    def test_sets_and_restores_existing_key(self):
        spark = MagicMock()
        spark.conf.get.return_value = "old_value"

        with scoped_conf(spark, test_key="new_value"):
            spark.conf.set.assert_called_with("test_key", "new_value")

        # Should restore the old value
        calls = spark.conf.set.call_args_list
        # Last call should be restore
        assert calls[-1] == (("test_key", "old_value"), {})

    def test_unsets_key_that_was_not_set_before(self):
        """When previous value was None (key didn't exist), should unset on exit."""
        spark = MagicMock()
        spark.conf.get.side_effect = Exception("key not found")

        with scoped_conf(spark, test_key="new_value"):
            spark.conf.set.assert_called_with("test_key", "new_value")

        # Should unset on exit
        spark.conf.unset.assert_called_with("test_key")

    def test_handles_exception_in_body(self):
        """Previous value should be restored even if body raises."""
        spark = MagicMock()
        spark.conf.get.return_value = "old_value"

        with pytest.raises(ValueError), scoped_conf(spark, test_key="new_value"):
            raise ValueError("boom")

        # Should still restore
        calls = spark.conf.set.call_args_list
        assert calls[-1] == (("test_key", "old_value"), {})

    def test_handles_exception_during_set(self):
        """Should not crash if set/unset raises during cleanup."""
        spark = MagicMock()
        spark.conf.get.return_value = "old_value"
        spark.conf.set.side_effect = [None, Exception("set failed")]
        spark.conf.unset.side_effect = Exception("unset failed")

        # Should not raise despite cleanup failures
        with scoped_conf(spark, test_key="new_value"):
            pass

    def test_multiple_keys_restored(self):
        """Multiple keys should all be restored."""
        spark = MagicMock()
        spark.conf.get.side_effect = ["old_a", "old_b"]

        with scoped_conf(spark, key_a="new_a", key_b="new_b"):
            pass

        # Both should be restored
        set_calls = {call[0][0]: call[0][1] for call in spark.conf.set.call_args_list}
        assert set_calls.get("key_a") == "old_a"
        assert set_calls.get("key_b") == "old_b"

    def test_arrow_max_records_per_batch_constant(self):
        """Verify the constant values."""
        assert ARROW_MAX_RECORDS_PER_BATCH == 64
        assert ARROW_MAX_RECORDS_PER_BATCH_KEY == "spark.sql.execution.arrow.maxRecordsPerBatch"
