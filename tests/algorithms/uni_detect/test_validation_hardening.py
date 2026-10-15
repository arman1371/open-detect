"""Tests for OPE-77 validation hardening on UniDetect pipeline."""

from __future__ import annotations

import pytest

from open_detect.core.enums import ErrorType
from open_detect.exceptions import ValidationError
from open_detect.algorithms.uni_detect.pipeline import UniDetect


class TestValidateInputs:
    def _make_detector(self):
        """Create a UniDetect instance with a mocked spark session."""
        from unittest.mock import MagicMock
        config = MagicMock()
        return UniDetect(config, spark=MagicMock())

    def test_rejects_unknown_kwargs(self):
        ud = self._make_detector()
        with pytest.raises(ValidationError, match="unknown"):
            ud._validate_inputs(table_names=["t1"], bad_param=1)

    def test_accepts_known_kwargs(self):
        ud = self._make_detector()
        ud._validate_inputs(table_names=["t1"], error_types=[ErrorType.UNIQUENESS])

    def test_rejects_bare_str_for_table_names(self):
        ud = self._make_detector()
        with pytest.raises(ValidationError, match="wrap in a list"):
            ud._validate_inputs(table_names="db.table")

    def test_rejects_bare_str_for_error_types(self):
        ud = self._make_detector()
        with pytest.raises(ValidationError, match="wrap in a list"):
            ud._validate_inputs(table_names=["t1"], error_types="UNIQUENESS")

    def test_accepts_list_of_tables(self):
        ud = self._make_detector()
        ud._validate_inputs(table_names=["t1", "t2"])

    def test_accepts_none_for_optional_params(self):
        ud = self._make_detector()
        ud._validate_inputs(table_names=None, error_types=None)
