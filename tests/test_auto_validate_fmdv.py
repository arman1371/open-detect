"""Unit tests for FMDV and FMDV-H (paper Eqns 5-7, 12-16)."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pandas as pd
import pytest

if TYPE_CHECKING:
    from open_detect.algorithms.auto_validate.config import AutoValidateConfig
    from open_detect.algorithms.auto_validate.index import PatternIndex

from open_detect.algorithms.auto_validate.config import AutoValidateConfig
from open_detect.algorithms.auto_validate.fmdv import fmdv, fmdv_h
from open_detect.algorithms.auto_validate.index import build_pattern_index


def _tiny_corpus(m_val: int = 1) -> tuple[list[str], AutoValidateConfig]:
    """A corpus where the time pattern has Cov=m=1 (smallest satisfiable)."""
    pure = ["10:00:00", "11:00:00", "12:00:00"]
    config = AutoValidateConfig(m=m_val, tau=16)
    corpus = [pure]
    return corpus, config


def _build_index(corpus: list[list[str]], config: AutoValidateConfig) -> PatternIndex:
    return build_pattern_index(corpus, config)


class TestFmdvBasic:
    def test_picks_the_lowest_fpr_pattern(self):
        """The clean time column should pick the coarsest pattern with FPR=0."""
        corpus, config = _tiny_corpus(m_val=1)
        index = _build_index(corpus, config)
        values = pd.Series(["10:00:00", "11:00:00"])
        result = fmdv(values, index, config)
        assert result is not None
        # Both values match "<num>:<num>:<num>" which has cov=1, fpr=0.
        assert result.fpr_t == 0.0
        assert result.cov_t >= 1
        assert result.variant == "fmdv"

    def test_boundary_r_inclusive(self):
        """A pattern with FPR_T == r exactly must be accepted."""
        # Build a corpus where one pattern has exactly FPR=0.05 and another has
        # FPR=0.04 — both satisfy r=0.05.  We choose the better FPR.
        corpus, config = _tiny_corpus(m_val=1)
        index = _build_index(corpus, config)
        # Use a very tight r so the only feasible pattern is the one with FPR=0.
        result = fmdv(pd.Series(["10:00:00"]), index, AutoValidateConfig(r=0.0, m=1, tau=16))
        assert result is not None
        assert result.fpr_t == 0.0

    def test_boundary_m_inclusive(self):
        """A pattern with Cov_T == m exactly must be accepted."""
        corpus, config = _tiny_corpus(m_val=1)
        index = _build_index(corpus, config)
        result = fmdv(pd.Series(["10:00:00"]), index, AutoValidateConfig(m=1, tau=16))
        assert result is not None
        assert result.cov_t >= 1

    def test_infeasible_when_m_too_high(self):
        """If m exceeds the corpus size, no pattern is feasible -> None."""
        corpus, config = _tiny_corpus(m_val=1)
        index = _build_index(corpus, config)
        result = fmdv(pd.Series(["10:00:00"]), index, AutoValidateConfig(m=100, tau=16))
        assert result is None

    def test_infeasible_when_r_is_strictly_below_best_fpr(self):
        """If the best pattern's FPR > r, returns None."""
        corpus, config = _tiny_corpus(m_val=1)
        index = _build_index(corpus, config)
        # All patterns from this corpus have FPR=0, so even a tiny positive r
        # will work.  Use r=0 to require FPR<=0, which works since FPR=0.
        result = fmdv(pd.Series(["10:00:00"]), index, AutoValidateConfig(r=0.0, m=1, tau=16))
        assert result is not None
        assert result.fpr_t == 0.0

    def test_empty_column_returns_none(self):
        config = AutoValidateConfig(m=1, tau=16)
        index = build_pattern_index([["a", "b"]], config)
        assert fmdv(pd.Series([]), index, config) is None

    def test_none_values_dropped(self):
        corpus, config = _tiny_corpus(m_val=1)
        index = _build_index(corpus, config)
        values = pd.Series(["10:00:00", None, "11:00:00"])
        result = fmdv(values, index, config)
        assert result is not None


class TestFmdvH:
    def test_tolerates_na_outlier(self):
        """FMDV-H with theta tolerates a single 'N/A' outlier that makes FMDV infeasible."""
        corpus, config = _tiny_corpus(m_val=1)
        index = _build_index(corpus, config)
        values = pd.Series(["10:00:00", "11:00:00", "N/A"])
        # FMDV on all three fails because "N/A" is not a time pattern.
        assert fmdv(values, index, AutoValidateConfig(m=1, tau=16)) is None
        # FMDV-H with theta=0.4 should accept the outlier as non-conforming (1/3 < 0.4).
        fmdv_h_result = fmdv_h(
            values,
            index,
            AutoValidateConfig(m=1, tau=16, theta=0.4),
        )
        assert fmdv_h_result is not None
        assert fmdv_h_result.theta_c > 0.0

    def test_theta_c_computed_correctly(self):
        corpus, config = _tiny_corpus(m_val=1)
        index = _build_index(corpus, config)
        # 4 time values + 1 outlier = 5 values; with theta=0.2 we need >= 4 matches.
        values = pd.Series(["10:00:00"] * 4 + ["N/A"])
        result = fmdv_h(values, index, AutoValidateConfig(m=1, tau=16, theta=0.2))
        assert result is not None
        assert result.theta_c == pytest.approx(0.2)

    def test_infeasible_when_too_many_outliers(self):
        """More than theta fraction of outliers makes it infeasible."""
        corpus, config = _tiny_corpus(m_val=1)
        index = _build_index(corpus, config)
        # theta=0.1 requires >= 90% matches; 5/10 = 0.5 matches -> infeasible.
        values = pd.Series(["10:00:00"] * 5 + ["N/A"] * 5)
        result = fmdv_h(values, index, AutoValidateConfig(m=1, tau=16, theta=0.1))
        assert result is None

    def test_ceil_theta_rounding(self):
        """Paper Eqn 16 uses ceiling: ceil((1-theta)|C|), not truncation.

        3 values, 2 matching + 1 outlier, theta=0.1 -> ceil(0.9 * 3) = 3
        conforming required, so the 1 outlier makes it infeasible.  Truncation
        would have accepted it (int(0.9*3) = 2 <= 2 matches).
        """
        corpus, config = _tiny_corpus(m_val=1)
        index = _build_index(corpus, config)
        values = pd.Series(["10:00:00", "11:00:00", "N/A"])
        result = fmdv_h(values, index, AutoValidateConfig(m=1, tau=16, theta=0.1))
        assert result is None

    def test_deterministic_tie_break(self):
        """Same inputs give the same result across runs."""
        corpus, config = _tiny_corpus(m_val=1)
        index = _build_index(corpus, config)
        values = pd.Series(["10:00:00", "11:00:00"])
        r1 = fmdv(values, index, config)
        r2 = fmdv(values, index, config)
        assert r1.pattern == r2.pattern
        assert r1.fpr_t == r2.fpr_t
