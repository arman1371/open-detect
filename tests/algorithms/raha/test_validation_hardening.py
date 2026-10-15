"""Tests for OPE-77 validation hardening on RahaDetector."""

from __future__ import annotations

import pandas as pd
import pytest

from open_detect.algorithms.raha import RahaDetector, RahaConfig
from open_detect.exceptions import ValidationError


class TestRahaValidation:
    def test_accepts_valid_literal_conflict_resolution(self):
        detector = RahaDetector(RahaConfig())
        df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
        # Should not raise
        detector.detect(df, table_id="t", conflict_resolution="homogeneity")

    def test_rejects_invalid_literal_conflict_resolution(self):
        detector = RahaDetector(RahaConfig())
        df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
        with pytest.raises(ValidationError, match="conflict_resolution"):
            detector.detect(df, table_id="t", conflict_resolution="invalid")

    def test_accepts_valid_literal_variant(self):
        detector = RahaDetector(RahaConfig())
        df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
        # Should not raise
        detector.detect(df, table_id="t", variant="A")

    def test_rejects_invalid_literal_variant(self):
        detector = RahaDetector(RahaConfig())
        df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
        with pytest.raises(ValidationError, match="variant"):
            detector.detect(df, table_id="t", variant="C")

    def test_rejects_unknown_kwargs(self):
        detector = RahaDetector(RahaConfig())
        df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
        with pytest.raises(ValidationError, match="unknown"):
            detector.detect(df, table_id="t", bad_param=1)

    def test_null_literal_params_accepted(self):
        detector = RahaDetector(RahaConfig())
        df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
        # None should pass through without validation
        detector.detect(df, table_id="t", conflict_resolution=None, variant=None)
