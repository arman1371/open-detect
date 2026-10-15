"""Tests for OPE-77 validation hardening on AutoValidateAlgorithm."""

from __future__ import annotations

import pandas as pd
import pytest

from open_detect.algorithms.auto_validate.detector import AutoValidateAlgorithm
from open_detect.algorithms.auto_validate.config import AutoValidateConfig
from open_detect.exceptions import ValidationError


def _make_detector() -> AutoValidateAlgorithm:
    config = AutoValidateConfig(m=1, tau=16)
    detector = AutoValidateAlgorithm(config)
    corpus = [pd.Series(["2024-01-15", "2024-02-20"])]
    detector.build_index(corpus)
    return detector


class TestAutoValidateValidation:
    def test_rejects_unknown_kwargs(self):
        detector = _make_detector()
        dirty = pd.DataFrame({"date": ["2024-01-15"]})
        with pytest.raises(ValidationError, match="unknown"):
            detector.detect(dirty, table_id="t", bad_param=1)

    def test_missing_columns_raises_by_default(self):
        detector = _make_detector()
        dirty = pd.DataFrame({"date": ["2024-01-15"]})
        with pytest.raises(ValidationError, match="not found in DataFrame"):
            detector.detect(dirty, table_id="t", columns=["date", "missing_col"])

    def test_skip_missing_suppresses_error(self):
        detector = _make_detector()
        dirty = pd.DataFrame({"date": ["2024-01-15"]})
        # Should not raise when skip_missing=True
        result = detector.detect(dirty, table_id="t", columns=["date", "missing_col"], skip_missing=True)
        assert len(result.cells) > 0

    def test_all_present_columns_no_error(self):
        detector = _make_detector()
        dirty = pd.DataFrame({"date": ["2024-01-15"], "email": ["a@b.com"]})
        result = detector.detect(dirty, table_id="t", columns=["date", "email"])
        assert len(result.cells) > 0

    def test_none_columns_no_error(self):
        detector = _make_detector()
        dirty = pd.DataFrame({"date": ["2024-01-15"]})
        result = detector.detect(dirty, table_id="t", columns=None)
        assert len(result.cells) > 0
