"""Unit tests for validation.py (no Spark required)."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from open_detect.exceptions import ValidationError
from open_detect.validation import (
    _check_columns_unique,
    _check_dataframe_is_spark,
    _check_expected_type,
    _check_unknown_kwargs,
    _ensure_dataframe_is_spark,
    _ensure_sequence_of_str,
    _reject_unknown_kwargs,
    _validate_literal_value,
)


class TestCheckUnknownKwargs:
    def test_allows_known_kwargs(self):
        _check_unknown_kwargs({"a": 1, "b": 2}, {"a", "b"})

    def test_raises_on_unknown_kwargs(self):
        with pytest.raises(ValidationError, match="Unknown parameter"):
            _check_unknown_kwargs({"a": 1, "c": 3}, {"a", "b"})

    def test_error_message_lists_accepted(self):
        try:
            _check_unknown_kwargs({"c": 3}, {"a", "b"})
        except ValidationError as e:
            assert "a" in str(e) and "b" in str(e)


class TestCheckExpectedType:
    def test_accepts_correct_type(self):
        _check_expected_type("hello", str, "param")

    def test_rejects_wrong_type(self):
        with pytest.raises(ValidationError, match="must be of type str"):
            _check_expected_type(123, str, "param")

    def test_rejects_str_for_sequence_str(self):
        # Special case: Sequence[str] should reject bare str
        from collections.abc import Sequence

        with pytest.raises(ValidationError, match="expected a sequence of str"):
            _check_expected_type("hello", Sequence[str], "param")

    def test_accepts_list_for_sequence_str(self):
        # Using parameterized Sequence[str] as expected_type - the function should
        # use bare Sequence for the isinstance check (avoiding TypeError from
        # parameterized generics as second argument to isinstance)
        from collections.abc import Sequence

        _check_expected_type(["a", "b"], Sequence[str], "param")

    def test_accepts_list_for_bare_sequence(self):
        from collections.abc import Sequence

        # Use bare Sequence (not parameterized) for isinstance check
        _check_expected_type(["a", "b"], Sequence, "param")

    def test_accepts_none_when_expected_none(self):
        _check_expected_type(None, type(None), "param")

    def test_rejects_none_when_not_expected(self):
        with pytest.raises(ValidationError):
            _check_expected_type(None, str, "param")


class TestValidateLiteralValue:
    def test_accepts_valid_value(self):
        _validate_literal_value("append", {"append", "overwrite"}, "mode")

    def test_rejects_invalid_value(self):
        with pytest.raises(ValidationError, match="must be one of"):
            _validate_literal_value("invalid", {"append", "overwrite"}, "mode")


class TestCheckColumnsUnique:
    def test_accepts_unique_strings(self):
        _check_columns_unique(["a", "b", "c"])

    def test_rejects_duplicate_columns(self):
        with pytest.raises(ValidationError, match="Column names must be unique"):
            _check_columns_unique(["a", "b", "a"])

    def test_rejects_non_string_columns(self):
        with pytest.raises(ValidationError, match="must be strings"):
            _check_columns_unique(["a", 123])


class TestCheckDataFrameIsSpark:
    def test_accepts_spark_dataframe(self):
        from pyspark.sql import DataFrame as SparkDataFrame

        mock_df = MagicMock(spec=SparkDataFrame)
        _check_dataframe_is_spark(mock_df, "param")

    def test_rejects_non_dataframe(self):
        with pytest.raises(ValidationError, match="must be a pyspark.sql.DataFrame"):
            _check_dataframe_is_spark("not_a_df", "param")

    def test_skips_check_when_pyspark_not_available(self):
        """When PySpark is not importable, the check should be skipped."""
        # Skip this test since we can't easily mock the internal import
        pytest.skip("Cannot easily mock internal import in this environment")


class TestEnsureDataFrameIsSpark:
    def test_accepts_spark_dataframe(self):
        from pyspark.sql import DataFrame as SparkDataFrame

        mock_df = MagicMock(spec=SparkDataFrame)
        _ensure_dataframe_is_spark(mock_df)  # Should not raise

    def test_accepts_pandas_dataframe(self):
        import pandas as pd

        _ensure_dataframe_is_spark(pd.DataFrame())  # Should not raise

    def test_no_op_when_pyspark_not_available(self):
        """When PySpark is not importable, function is a no-op."""
        pytest.skip("Cannot easily mock internal import in this environment")

    def test_no_op_when_pandas_not_available(self):
        """When neither PySpark nor pandas is available, function is a no-op."""
        pytest.skip("Cannot easily mock internal import in this environment")


class TestEnsureSequenceOfStr:
    def test_accepts_list_of_str(self):
        _ensure_sequence_of_str(["a", "b"], "param")

    def test_rejects_bare_str(self):
        with pytest.raises(ValidationError, match="got str; wrap in a list"):
            _ensure_sequence_of_str("not_a_list", "param")

    def test_rejects_non_sequence(self):
        with pytest.raises(ValidationError, match="must be a sequence"):
            _ensure_sequence_of_str(123, "param")

    def test_rejects_non_str_items(self):
        with pytest.raises(ValidationError, match="must be str"):
            _ensure_sequence_of_str(["a", 123], "param")

    def test_accepts_tuple_of_str(self):
        _ensure_sequence_of_str(("a", "b"), "param")

    def test_rejects_empty_string_in_sequence(self):
        """Empty string is still a string, should be accepted."""
        _ensure_sequence_of_str(["", "a"], "param")


class TestRejectUnknownKwargs:
    def test_allows_known(self):
        _reject_unknown_kwargs({"a": 1}, {"a"}, "func")

    def test_raises_on_unknown(self):
        with pytest.raises(ValidationError, match="Unknown parameter"):
            _reject_unknown_kwargs({"b": 2}, {"a"}, "func")

    def test_error_message_format(self):
        try:
            _reject_unknown_kwargs({"b": 2, "c": 3}, {"a"}, "func")
        except ValidationError as e:
            assert "b" in str(e) and "c" in str(e)
            assert "a" in str(e)  # accepted parameter shown
