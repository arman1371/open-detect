"""Unit tests for metrics/*, validated against the paper's own worked numbers.

Every assertion here ties back to a specific example in Wang & He, SIGMOD'19:
Example 3/4/5 (numeric outliers), Example 1 (spelling), Example 2
(uniqueness), and the Figure 4(c) FD example.
"""

from __future__ import annotations

import pytest

from unidetect.exceptions import InsufficientDataError
from unidetect.metrics.base import drop_nulls
from unidetect.metrics.functional_dependency import fd_compliance_ratio, minority_violation_rows
from unidetect.metrics.outliers import (
    mad_scores,
    max_mad,
    median_absolute_deviation,
    sd_scores,
)
from unidetect.metrics.spelling import differing_token_lengths, min_pairwise_edit_distance
from unidetect.metrics.uniqueness import duplicate_value_indices, uniqueness_ratio


class TestDropNulls:
    def test_drops_none_and_nan(self):
        assert drop_nulls(["a", None, "b", float("nan"), "c"]) == ["a", "b", "c"]

    def test_keeps_non_nan_floats(self):
        assert drop_nulls([1.0, None, 2.5]) == [1.0, 2.5]


class TestUniquenessRatio:
    def test_all_unique(self):
        assert uniqueness_ratio(["a", "b", "c"]) == 1.0

    def test_paper_example_2_near_unique_column(self):
        # 100 values, exactly one duplicate pair -> UR = 99/100
        values = [f"id{i}" for i in range(98)] + ["dup", "dup"]
        assert uniqueness_ratio(values) == pytest.approx(0.99)

    def test_ignores_nulls(self):
        assert uniqueness_ratio(["a", None, "b", None]) == 1.0

    def test_requires_min_size(self):
        with pytest.raises(InsufficientDataError):
            uniqueness_ratio(["a"])


class TestDuplicateValueIndices:
    def test_finds_all_but_first_occurrence(self):
        idx = duplicate_value_indices(["a", "b", "a", "a", "c"])
        # two extra occurrences of "a" (indices 2 and 3) should be flagged
        assert sorted(idx) == [2, 3]

    def test_smallest_groups_first(self):
        # "a" duplicated twice (3 occurrences), "b" duplicated once (2 occurrences)
        values = ["a", "a", "a", "b", "b"]
        idx = duplicate_value_indices(values)
        # the group of size 2 ("b") should be listed before the group of size 3 ("a")
        assert idx[0] == 4  # second "b"


class TestNumericOutliers:
    def test_paper_example_3_and_4_c_minus(self):
        # paper Example 3/4: C- = {43, 22, 9, 5, 0.76, 0.32, 0.30}
        c_minus = [43, 22, 9, 5, 0.76, 0.32, 0.30]
        mad = median_absolute_deviation(c_minus)
        assert mad.median == pytest.approx(5.0)
        assert mad.mad == pytest.approx(4.68, abs=1e-6)

        result = max_mad(c_minus)
        assert result.value == pytest.approx(43.0)
        assert result.score == pytest.approx(8.1, abs=0.02)

    def test_paper_example_3_and_4_c_plus(self):
        # paper Example 3/4: C+ has "8.716" as a mis-typed outlier (should be "8,716")
        c_plus = [8011, 8.716, 9954, 11895, 13329, 11352, 11709]
        mad = median_absolute_deviation(c_plus)
        assert mad.median == pytest.approx(11352.0)
        assert mad.mad == pytest.approx(1398.0)

        result = max_mad(c_plus)
        assert result.value == pytest.approx(8.716)
        assert result.score == pytest.approx(8.1, abs=0.02)

    def test_c_plus_and_c_minus_have_indistinguishable_max_mad_scores(self):
        # This is exactly the paper's point (Example 5): SD/MAD alone cannot
        # tell these apart; only the perturbation ratio can (tested in
        # test_perturbation.py).
        c_minus = [43, 22, 9, 5, 0.76, 0.32, 0.30]
        c_plus = [8011, 8.716, 9954, 11895, 13329, 11352, 11709]
        assert max_mad(c_minus).score == pytest.approx(max_mad(c_plus).score, abs=0.02)

    def test_sd_scores_shape(self):
        scores = sd_scores([1.0, 2.0, 3.0, 4.0, 100.0])
        assert len(scores) == 5
        assert scores.argmax() == 4

    def test_requires_min_size(self):
        with pytest.raises(InsufficientDataError):
            median_absolute_deviation([1.0])

    def test_mad_scores_handles_zero_mad(self):
        # constant column except one outlier: MAD would be 0 without a floor
        scores = mad_scores([5.0, 5.0, 5.0, 5.0, 100.0])
        assert scores.max() > 0
        assert all(s >= 0 for s in scores)


class TestSpelling:
    def test_paper_example_1_kevin_doeling(self):
        column = ["Kevin Doeling", "Kevin Dowling", "Alan Myerson", "Rob Morrow"]
        result = min_pairwise_edit_distance(column)
        assert result.mpd == 1
        assert {result.value_u, result.value_v} == {"Kevin Doeling", "Kevin Dowling"}

    def test_super_bowl_false_positive_case(self):
        # paper Fig. 2(h): many roman-numeral pairs share small edit distance
        column = [
            "Super Bowl XX",
            "Super Bowl XXI",
            "Super Bowl XXII",
            "Super Bowl XXIII",
            "Super Bowl XIX",
        ]
        result = min_pairwise_edit_distance(column)
        assert result.mpd == 1  # syntactically close, but not a spelling error

    def test_differing_token_lengths_long_token(self):
        lengths = differing_token_lengths("Kevin Doeling", "Kevin Dowling")
        assert lengths == [7]  # "Doeling"/"Dowling" -> len 7

    def test_differing_token_lengths_short_token(self):
        lengths = differing_token_lengths("Super Bowl XXI", "Super Bowl XXII")
        assert lengths == [4]  # "XXI"/"XXII" -> max len 4

    def test_requires_min_size(self):
        with pytest.raises(InsufficientDataError):
            min_pairwise_edit_distance(["only-one"])

    def test_identical_values_give_zero_distance(self):
        result = min_pairwise_edit_distance(["a", "a", "b"])
        assert result.mpd == 0

    def test_oversized_block_is_deterministically_subsampled(self):
        # All 20 values share the same (prefix, length-bucket) blocking key,
        # forcing the stride-based subsampling path rather than a full
        # O(n^2) comparison within the block.
        values = [f"aa{i:03d}" for i in range(20)]
        result = min_pairwise_edit_distance(values, max_block_size=5)
        assert result.mpd >= 0
        # Re-running is deterministic (no randomness in the subsampling).
        assert result == min_pairwise_edit_distance(values, max_block_size=5)

    def test_raises_when_no_blocks_and_column_exceeds_max_block_size(self):
        # Every value has a distinct (prefix, length-bucket) key, so no block
        # ever reaches size >= 2, and the column is larger than
        # max_block_size -- the bounded global-scan fallback cannot apply.
        values = ["b1", "c22", "d333", "e4444", "f55555", "g666666"]
        with pytest.raises(ValueError):
            min_pairwise_edit_distance(values, max_block_size=3)

    def test_differing_token_lengths_with_unequal_token_counts(self):
        lengths = differing_token_lengths("Kevin Doeling Extra", "Kevin Dowling")
        # "Doeling"/"Dowling" differ (len 7), plus the trailing unmatched "Extra" (len 5).
        assert lengths == [7, 5]

    def test_differing_token_lengths_falls_back_to_whole_value_when_no_diff(self):
        lengths = differing_token_lengths("Same Value", "Same Value")
        assert lengths == [len("Same Value")]


class TestFunctionalDependency:
    def test_perfect_fd_has_ratio_one(self):
        lhs = ["1", "1", "2", "2", "3"]
        rhs = ["x", "x", "y", "y", "z"]
        result = fd_compliance_ratio(lhs, rhs)
        assert result.ratio == 1.0
        assert result.violating_row_indices == ()

    def test_paper_figure_4c_style_violation(self):
        # one lhs group ("3") has two distinct rhs values out of 3 groups / 6 rows
        lhs = ["1", "1", "2", "2", "3", "3"]
        rhs = ["x", "x", "y", "y", "z", "w"]
        result = fd_compliance_ratio(lhs, rhs)
        assert result.ratio == pytest.approx(4 / 6)
        assert set(result.violating_row_indices) == {4, 5}

    def test_minority_violation_rows_keeps_majority(self):
        lhs = ["1", "1", "1", "2", "2"]
        rhs = ["x", "x", "y", "z", "z"]  # lhs=1 has 2x "x", 1x "y" -> minority is "y" (index 2)
        dropped = minority_violation_rows(lhs, rhs, max_rows=10)
        assert dropped == [2]

    def test_requires_matching_lengths(self):
        with pytest.raises(ValueError):
            fd_compliance_ratio(["a"], ["b", "c"])

    def test_ignores_null_lhs_rows(self):
        lhs = ["1", None, "1", "2"]
        rhs = ["x", "z", "x", "y"]
        result = fd_compliance_ratio(lhs, rhs)
        assert result.ratio == 1.0
        assert result.violating_row_indices == ()

    def test_raises_when_every_lhs_value_is_null(self):
        with pytest.raises(ValueError):
            fd_compliance_ratio([None, None], ["a", "b"])

    def test_minority_violation_rows_ignores_null_lhs(self):
        lhs = [None, "1", "1"]
        rhs = ["z", "x", "y"]
        dropped = minority_violation_rows(lhs, rhs, max_rows=10)
        assert dropped == [2]

    def test_minority_violation_rows_stops_at_max_rows(self):
        lhs = ["1", "1", "1"]
        rhs = ["x", "y", "z"]
        dropped = minority_violation_rows(lhs, rhs, max_rows=1)
        assert dropped == [1]
