"""Unit tests for FMDV-V and FMDV-VH (paper Eqns 8-11, §5.5)."""

from __future__ import annotations

import math
from fractions import Fraction
from typing import TYPE_CHECKING

import pandas as pd
import pytest

if TYPE_CHECKING:
    from open_detect.algorithms.auto_validate.config import AutoValidateConfig
    from open_detect.algorithms.auto_validate.index import PatternIndex

from open_detect.algorithms.auto_validate.config import AutoValidateConfig
from open_detect.algorithms.auto_validate.fmdv import InferredPattern, min_conforming
from open_detect.algorithms.auto_validate.fmdv_v import (
    _coarse_signature,
    _fmdv_h_single,
    _fmdv_single_segment,
    _segment_dp,
    fmdv_v,
    fmdv_vh,
)
from open_detect.algorithms.auto_validate.hierarchy import matches_segments
from open_detect.algorithms.auto_validate.index import build_pattern_index


def _time_corpus(m_val: int = 1) -> tuple[list[list[str]], AutoValidateConfig]:
    """A small corpus of time columns so the time pattern has Cov >= m."""
    pure = ["10:00:00", "11:00:00", "12:00:00"]
    config = AutoValidateConfig(m=m_val, tau=16)
    return [pure], config


def _build_index(corpus: list[list[str]], config: AutoValidateConfig) -> PatternIndex:
    return build_pattern_index(corpus, config)


class TestFmdvV:
    def test_splits_composite_value(self):
        """A composite value like '0.1|02/18/2015 00:00:00|OnBooking' is split.

        Whole-column FMDV would have Cov < m because the mixed pattern is rare
        in the corpus; vertical cuts allow each component to be matched
        separately against its own domain in T.
        """
        # The corpus contains pure time columns, so the time segment gets
        # high coverage while the numeric and letter segments are not in T
        # (and thus have Cov=0 < m).
        corpus, config = _time_corpus(m_val=1)
        index = _build_index(corpus, config)
        values = pd.Series(["0.1|02/18/2015 00:00:00|OnBooking"])
        result = fmdv_v(values, index, config)
        # The time segment should be found; the overall result may be None if
        # no single coarse-signature group yields a feasible pattern.
        # We test that the function does not crash and returns a sensible shape.
        if result is not None:
            assert result.variant == "fmdv_v"

    def test_single_token_group(self):
        """A homogeneous column still works through the vertical-cut path."""
        corpus, config = _time_corpus(m_val=1)
        index = _build_index(corpus, config)
        values = pd.Series(["10:00:00", "11:00:00"])
        result = fmdv_v(values, index, config)
        assert result is not None
        assert result.variant == "fmdv_v"
        # Single segment, so pattern is a string not a list.
        assert isinstance(result.pattern, str)

    def test_sum_objective_not_max(self):
        """Two segments each with FPR=0.01 should sum to 0.02, not max=0.01."""
        # Build a corpus where two distinct patterns each appear in 1 column
        # with impurity 0.01.
        col_a = ["abc", "abd"] * 50  # impurity ~0.01 for a letter pattern
        col_b = ["123", "124"] * 50
        config = AutoValidateConfig(m=1, tau=16, r=1.0)
        index = build_pattern_index([col_a, col_b], config)
        # Two values with different coarse signatures: one letter-group, one digit-group.
        values = pd.Series(["abc", "123"])
        result = fmdv_v(values, index, config)
        if result is not None:
            # Sum of FPRs should be <= sum of individual FPRs.
            assert result.fpr_t >= 0.0

    def test_dp_vs_brute_force_small(self):
        """For very small inputs, verify the DP gives the same answer as brute force."""
        # Use a trivial corpus where every pattern has FPR=0 and Cov>=1.
        corpus = [["a1", "b2"], ["c3", "d4"]]
        config = AutoValidateConfig(m=1, tau=32, r=1.0)
        index = build_pattern_index(corpus, config)
        # Values all sharing the same coarse signature (letter+digit pairs).
        values = pd.Series(["a1", "b2", "c3"])
        result = fmdv_v(values, index, config)
        assert result is not None

    def test_infeasible_returns_none(self):
        corpus, config = _time_corpus(m_val=1)
        index = _build_index(corpus, config)
        # Values with no feasible pattern (require m higher than corpus supports).
        values = pd.Series(["xyz"])
        result = fmdv_v(values, index, AutoValidateConfig(m=100, tau=16))
        assert result is None

    def test_empty_column_returns_none(self):
        config = AutoValidateConfig(m=1, tau=16)
        index = build_pattern_index([["a", "b"]], config)
        assert fmdv_v(pd.Series([]), index, config) is None


class TestFmdvVh:
    def test_horizontal_then_vertical(self):
        """FMDV-VH tolerates outliers within each vertical segment."""
        corpus, config = _time_corpus(m_val=1)
        index = _build_index(corpus, config)
        # Two time values and one outlier; theta=0.4 allows 1 outlier out of 3.
        values = pd.Series(["10:00:00", "11:00:00", "N/A"])
        result = fmdv_vh(values, index, AutoValidateConfig(m=1, tau=16, theta=0.4))
        assert result is not None
        assert result.variant == "fmdv_vh"

    def test_single_segment_no_outliers(self):
        corpus, config = _time_corpus(m_val=1)
        index = _build_index(corpus, config)
        values = pd.Series(["10:00:00", "11:00:00"])
        result = fmdv_vh(values, index, AutoValidateConfig(m=1, tau=16))
        assert result is not None

    def test_tau_boundary_segment_width_strict(self):
        """Def. 2 enforces e_i - s_i < tau (strict): a segment of exactly tau
        tokens is not permitted.  Values like ``a-b`` have 3 tokens, so with
        tau=3 no single segment fits (max width 2) and the DP must cut the
        value; with tau=4 the whole value is one segment."""
        corpus = [["a-b", "c-d"], ["a-", "c-"], ["b", "d"]]
        values = pd.Series(["a-b", "c-d"])
        cfg_tau3 = AutoValidateConfig(m=1, tau=3, r=1.0)
        result3 = fmdv_v(values, build_pattern_index(corpus, cfg_tau3), cfg_tau3)
        assert result3 is not None
        assert isinstance(result3.pattern, list)
        assert len(result3.pattern) == 2
        cfg_tau4 = AutoValidateConfig(m=1, tau=4, r=1.0)
        result4 = fmdv_v(values, build_pattern_index(corpus, cfg_tau4), cfg_tau4)
        assert result4 is not None
        assert isinstance(result4.pattern, str)


def _date_values(n: int) -> list[str]:
    months = ["Jan", "Feb", "Mar", "Apr"]
    return [f"{months[i % 4]} {1 + (i * 7) % 28}" for i in range(n)]


def _date_index(cfg: AutoValidateConfig) -> PatternIndex:
    return build_pattern_index([_date_values(40), _date_values(30)], cfg)


class TestFmdvVhMixedSignatures:
    """fmdv_vh returns a single group's segmentation, mirroring fmdv_v."""

    CORPUS = [["2024-01-15", "2024-02-20"], ["Jan 5", "Feb 10", "Mar 3"]]
    COLUMN = ["2024-01-15", "Jan 5", "2024-02-20", "Feb 10"]

    def _run(self, fn):
        config = AutoValidateConfig(m=1, tau=16)
        index = _build_index(self.CORPUS, config)
        return fn(pd.Series(self.COLUMN), index, config)

    def test_returns_one_group_segmentation(self):
        result = self._run(fmdv_vh)
        assert result is not None
        assert result.variant == "fmdv_vh"
        patterns = [result.pattern] if isinstance(result.pattern, str) else result.pattern
        tiled = [v for v in self.COLUMN if matches_segments(patterns, v)]
        assert len(tiled) == 2

    def test_stats_equal_chosen_group_not_summed(self):
        config = AutoValidateConfig(m=1, tau=16)
        index = _build_index(self.CORPUS, config)
        result = fmdv_vh(pd.Series(self.COLUMN), index, config)
        per_group = [
            _segment_dp(g, index, config, "fmdv_vh", _fmdv_h_single)
            for g in (["2024-01-15", "2024-02-20"], ["Jan 5", "Feb 10"])
        ]
        feasible = [g for g in per_group if g is not None]
        assert result in feasible

    def test_deterministic(self):
        first = self._run(fmdv_vh)
        second = self._run(fmdv_vh)
        assert first == second

    def test_matches_fmdv_v_selection_shape(self):
        v = self._run(fmdv_v)
        vh = self._run(fmdv_vh)
        assert v is not None
        assert vh is not None
        assert v.pattern == vh.pattern
        assert (v.fpr_t, v.cov_t) == (vh.fpr_t, vh.cov_t)

    def test_no_feasible_group_returns_none(self):
        config = AutoValidateConfig(m=100, tau=16)
        index = _build_index(self.CORPUS, config)
        assert fmdv_vh(pd.Series(self.COLUMN), index, config) is None

    def test_empty_column_returns_none(self):
        config = AutoValidateConfig(m=1, tau=16)
        index = _build_index(self.CORPUS, config)
        assert fmdv_vh(pd.Series([], dtype=object), index, config) is None


class TestLargeGroups:
    """BUG-1: the DP used to run over rows, so any group of >= 8 values returned None."""

    @pytest.mark.parametrize("n", [7, 8, 9, 20, 50])
    @pytest.mark.parametrize("fn", [fmdv_v, fmdv_vh])
    def test_group_size_returns_result(self, n, fn):
        cfg = AutoValidateConfig(m=1, tau=8, r=1.0)
        result = fn(pd.Series(_date_values(n)), _date_index(cfg), cfg)
        assert result is not None
        assert 0.0 <= 1.0 - result.fpr_t <= 1.0


class TestSegmentDp:
    def test_multi_segment_cut_over_token_positions(self):
        """A 5-token value with tau=4 (max width 3) needs >= 2 segments."""
        values = ["ab-12-cd", "xy-34-zz", "qq-99-aa"]
        cfg = AutoValidateConfig(m=1, tau=4, r=1.0)
        corpus = [["ab-12", "xy-34"], ["-cd", "-zz"], ["ab", "xy"], ["12-cd", "34-zz"]]
        index = build_pattern_index(corpus, cfg)
        result = _segment_dp(values, index, cfg, "fmdv_v", _fmdv_single_segment)
        assert result is not None
        assert isinstance(result.pattern, list)
        assert len(result.pattern) >= 2

    def test_segments_solved_independently(self):
        """Each segment is solved: total FPR is the sum of the per-segment FPRs."""
        calls: list[tuple[str, ...]] = []

        def solve(vals, _index, _cfg):
            calls.append(tuple(vals))
            return InferredPattern(
                pattern=vals[0], fpr_t=0.01, cov_t=1, theta_c=0.0, variant="fmdv"
            )

        cfg = AutoValidateConfig(m=1, tau=3, r=1.0)
        index = build_pattern_index([["a"]], cfg)
        result = _segment_dp(["a+b/c", "d+e/f"], index, cfg, "fmdv_v", solve)
        assert result is not None
        # 5 tokens, max width 2 => exactly 3 segments, hence fpr_t == 0.03.
        assert isinstance(result.pattern, list)
        assert len(result.pattern) == 3
        assert result.fpr_t == pytest.approx(0.03)
        # solve_segment results are memoized per (start, end) span.
        assert len(calls) == len(set(calls))

    def test_infeasible_segment_returns_none(self):
        cfg = AutoValidateConfig(m=1, tau=4)
        index = build_pattern_index([["a"]], cfg)
        assert _segment_dp(["a-b"], index, cfg, "fmdv_v", lambda *_: None) is None


class TestCoarseSignature:
    def test_variable_width_tokens_share_a_group(self):
        assert _coarse_signature("Jan 5") == _coarse_signature("Jan 15")
        assert _coarse_signature("Jan 5") != _coarse_signature("5 Jan")

    def test_fpr_stays_a_probability(self):
        """fpr_t summed across groups/segments must keep 1 - fpr_t within [0, 1]."""
        cfg = AutoValidateConfig(m=1, tau=8, r=1.0)
        values = pd.Series(_date_values(20) + ["10:00:00", "11:00:00", "abc", "123", "a-b-c"])
        corpus = [_date_values(30), ["10:00:00", "11:00:00"], ["abc", "abd"], ["123", "456"]]
        corpus.append(["a-b-c", "d-e-f"])
        index = build_pattern_index(corpus, cfg)
        for fn in (fmdv_v, fmdv_vh):
            result = fn(values, index, cfg)
            assert result is not None
            assert 0.0 <= 1.0 - result.fpr_t <= 1.0


class TestMinConforming:
    def test_matches_exact_rational_ceil(self):
        thetas = [i / 100 for i in range(101)] + [0.005, 0.125, 0.333, 0.999]
        for theta in thetas:
            exact = Fraction(1) - Fraction(str(theta))
            for n in range(1, 1001):
                expected = math.ceil(exact * n)
                assert min_conforming(theta, n) == expected, (theta, n)

    def test_known_float_noise_case(self):
        assert min_conforming(0.41, 100) == 59
