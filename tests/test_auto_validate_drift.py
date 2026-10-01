"""Unit tests for the column-level drift test (paper Section 5.4)."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pandas as pd
import pytest

if TYPE_CHECKING:
    pass

from unidetect.algorithms.auto_validate.config import AutoValidateConfig
from unidetect.algorithms.auto_validate.drift import check_drift
from unidetect.algorithms.auto_validate.fmdv import InferredPattern


def _make_pattern(pattern_str: str = "<num>:<num>:<num>") -> InferredPattern:
    return InferredPattern(
        pattern=pattern_str,
        fpr_t=0.0,
        cov_t=1,
        theta_c=0.0,
        variant="fmdv",
    )


class TestCheckDrift:
    def test_same_distribution_non_drifted(self):
        """Two identical columns should not trigger drift (p > significance)."""
        train = pd.Series(["10:00:00"] * 50 + ["11:00:00"] * 50)
        test = pd.Series(["10:00:00"] * 50 + ["11:00:00"] * 50)
        pattern = _make_pattern()
        result = check_drift(train, test, pattern, significance=0.01)
        assert result.drifted is False
        assert result.theta_train == pytest.approx(0.0)
        assert result.theta_test == pytest.approx(0.0)
        assert result.p_value > 0.01

    def test_different_non_conforming_rate_drifted(self):
        """Train has 0% outliers, test has 50% — should be detected."""
        train = pd.Series(["10:00:00"] * 100)
        test = pd.Series(["10:00:00"] * 50 + ["N/A"] * 50)
        pattern = _make_pattern()
        result = check_drift(train, test, pattern, significance=0.01)
        assert result.drifted is True
        assert result.theta_train == pytest.approx(0.0)
        assert result.theta_test == pytest.approx(0.5)
        assert result.p_value < 0.01

    def test_hand_computed_fisher(self):
        """Verify p-value against a known 2x2 table using scipy directly."""
        from scipy.stats import fisher_exact

        # 2x2 table: [[a, b], [c, d]]
        # a=conforming_train=90, b=nonconform_train=10
        # c=conforming_test=50, d=nonconform_test=50
        table = [[90, 10], [50, 50]]
        expected_p = fisher_exact(table, alternative="two-sided")[1]

        train = pd.Series(["v"] * 90 + ["x"] * 10)
        test = pd.Series(["v"] * 50 + ["x"] * 50)
        pattern = _make_pattern(pattern_str="v")
        result = check_drift(train, test, pattern, significance=0.01)
        assert result.p_value == pytest.approx(expected_p)
        assert result.drifted is True  # p should be very small for this table

    def test_nulls_dropped(self):
        """Null values in train/test should be ignored, not counted as non-conforming."""
        train = pd.Series(["a", None, "a"])
        test = pd.Series(["a", "b", None])
        pattern = _make_pattern(pattern_str="a")
        result = check_drift(train, test, pattern, significance=0.01)
        assert result is not None
        assert result.theta_train == pytest.approx(0.0)  # both non-null are "a"
        assert result.theta_test == pytest.approx(0.5)  # 1 of 2 non-null is "b"

    def test_empty_test_column(self):
        """An empty test column should not crash and returns p=1.0."""
        train = pd.Series(["a", "b"])
        test = pd.Series([], dtype=object)
        pattern = _make_pattern(pattern_str="a")
        result = check_drift(train, test, pattern, significance=0.01)
        assert result.p_value == 1.0
        assert result.drifted is False

    def test_empty_train_column(self):
        train = pd.Series([], dtype=object)
        test = pd.Series(["a", "b"])
        pattern = _make_pattern(pattern_str="a")
        result = check_drift(train, test, pattern, significance=0.01)
        assert result.p_value == 1.0
        assert result.drifted is False

    def test_default_significance(self):
        """When no significance is passed, config.drift_significance (0.01) is used."""
        train = pd.Series(["10:00:00"] * 100)
        test = pd.Series(["10:00:00"] * 50 + ["N/A"] * 50)
        pattern = _make_pattern()
        config = AutoValidateConfig(drift_significance=0.01)
        result = check_drift(train, test, pattern, config=config)
        # Same data as before; should still be detected.
        assert result.drifted is True

    def test_determinism(self):
        train = pd.Series(["a"] * 80 + ["b"] * 20)
        test = pd.Series(["a"] * 30 + ["b"] * 70)
        pattern = _make_pattern(pattern_str="a")
        r1 = check_drift(train, test, pattern, significance=0.05)
        r2 = check_drift(train, test, pattern, significance=0.05)
        assert r1.p_value == r2.p_value
        assert r1.drifted == r2.drifted
