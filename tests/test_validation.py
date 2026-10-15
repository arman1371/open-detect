"""Tests for shared validation utilities in src/open_detect/validation.py."""

from __future__ import annotations

import pytest

from open_detect.exceptions import ValidationError
from open_detect.validation import (
    _check_columns_unique,
    _check_unknown_kwargs,
    _check_expected_type,
    _validate_literal_value,
)


class TestCheckUnknownKwargs:
    def test_accepts_valid_kwargs(self):
        _check_unknown_kwargs({"a": 1, "b": 2}, {"a", "b"}, "detect")

    def test_rejects_unknown_kwarg(self):
        with pytest.raises(ValidationError, match="unknown"):
            _check_unknown_kwargs({"a": 1, "bad": 2}, {"a"}, "detect")

    def test_error_names_unknown_and_accepted_keys(self):
        try:
            _check_unknown_kwargs({"x": 1, "y": 2}, {"a", "b"}, "detect")
            assert False, "should have raised"
        except ValidationError as exc:
            msg = str(exc)
            assert "x" in msg and "y" in msg
            assert "a" in msg and "b" in msg


class TestCheckExpectedType:
    def test_sequence_str_accepts_list(self):
        _check_expected_type(["a", "b"], list[str], "param")

    def test_sequence_str_rejects_bare_str(self):
        with pytest.raises(ValidationError, match="wrap in a list"):
            _check_expected_type("hello", list[str], "param")

    def test_sequence_str_accepts_tuple(self):
        _check_expected_type(("a", "b"), tuple[str, ...], "param")

    def test_rejects_wrong_type(self):
        with pytest.raises(ValidationError, match="must be of type"):
            _check_expected_type(42, str, "param")

    def test_none_skipped(self):
        _check_expected_type(None, str | None, "param")
