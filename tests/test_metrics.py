"""Unit tests for metrics/*, validated against the paper's own worked numbers.

Every assertion here ties back to a specific example in Wang & He, SIGMOD'19:
Example 3/4/5 (numeric outliers), Example 1 (spelling), Example 2
(uniqueness), and the Figure 4(c) FD example.
"""

from __future__ import annotations

import pytest

from unidetect.exceptions import InsufficientDataError
from unidetect.metrics.functional_dependency import fd_compliance_ratio, minority_violation_rows
from unidetect.metrics.outliers import (
    mad_scores,
    max_mad,
    median_absolute_deviation,
    sd_scores,
)
from unidetect.metrics.spelling import differing_token_lengths, min_pairwise_edit_distance
from unidetect.metrics.uniqueness import duplicate_value_indices, uniqueness_ratio


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
