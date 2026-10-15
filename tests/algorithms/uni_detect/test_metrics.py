"""Unit tests for metrics/*, validated against the paper's own worked numbers.

Every assertion here ties back to a specific example in Wang & He, SIGMOD'19:
Example 3/4/5 (numeric outliers), Example 1 (spelling), Example 2
(uniqueness), and the Figure 4(c) FD example.
"""

from __future__ import annotations

import random
import string
from itertools import combinations

import pytest
from rapidfuzz.distance import Levenshtein

from open_detect.algorithms.uni_detect.metrics.base import drop_nulls
from open_detect.algorithms.uni_detect.metrics.functional_dependency import (
    fd_compliance_ratio,
    minority_violation_rows,
)
from open_detect.algorithms.uni_detect.metrics.outliers import (
    finite_floats,
    mad_scores,
    max_mad,
    median_absolute_deviation,
    sd_scores,
)
from open_detect.algorithms.uni_detect.metrics.spelling import (
    differing_token_lengths,
    min_pairwise_edit_distance,
    try_min_pairwise_edit_distance,
)
from open_detect.algorithms.uni_detect.metrics.uniqueness import (
    duplicate_value_indices,
    uniqueness_ratio,
)
from open_detect.exceptions import InsufficientDataError, OpenDetectError, ValidationError


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


def _brute_force_mpd(values: list[str]) -> int:
    distinct = list(dict.fromkeys(values))
    return min(Levenshtein.distance(a, b) for a, b in combinations(distinct, 2))


def _random_words(rng: random.Random, n: int, min_len: int = 3, max_len: int = 10) -> list[str]:
    words: set[str] = set()
    while len(words) < n:
        length = rng.randint(min_len, max_len)
        words.add("".join(rng.choice(string.ascii_lowercase) for _ in range(length)))
    return sorted(words)


def _single_edit(rng: random.Random, word: str) -> str:
    kind = rng.choice("sid")
    i = rng.randrange(len(word))
    if kind == "s":
        return (
            word[:i]
            + rng.choice([c for c in string.ascii_lowercase if c != word[i]])
            + word[i + 1 :]
        )
    if kind == "i":
        return word[:i] + rng.choice(string.ascii_lowercase) + word[i:]
    return word[:i] + word[i + 1 :]


class TestFiniteFloats:
    def test_drops_nulls_unparsable_and_non_finite(self):
        vals = [1, None, "2.5", "abc", float("nan"), float("inf"), "-inf", "nan", "Infinity", 3]
        out, positions = finite_floats(vals)
        assert out == [1.0, 2.5, 3.0]
        assert positions == [0, 2, 9]

    def test_empty(self):
        assert finite_floats([]) == ([], [])


class TestSpellingBlocking:
    """BUG-11: blocking must not miss the true minimum pair (distance 1)."""

    def test_substitution_in_prefix_is_found(self):
        # Old blocking keyed on the first two chars: 'ap' != 'pp' -> pair never compared.
        filler = _random_words(random.Random(0), 30, min_len=8, max_len=12)
        result = min_pairwise_edit_distance([*filler, "apple", "ppple"], max_block_size=10)
        assert result.mpd == 1
        assert {result.value_u, result.value_v} == {"apple", "ppple"}

    def test_insertion_across_length_bucket_boundary_is_found(self):
        # len 5 -> bucket 1, len 6 -> bucket 2: the old keys never co-located them.
        filler = _random_words(random.Random(0), 30, min_len=8, max_len=12)
        result = min_pairwise_edit_distance([*filler, "apple", "applez"], max_block_size=10)
        assert result.mpd == 1
        assert {result.value_u, result.value_v} == {"apple", "applez"}

    def test_matches_brute_force_for_single_planted_typo(self):
        rng = random.Random(1234)
        for _ in range(150):
            base = _random_words(rng, rng.choice([30, 60, 100]))
            typo = _single_edit(rng, rng.choice(base))
            column = [*base, typo] if typo not in base else base
            rng.shuffle(column)
            # max_block_size below n forces the blocking path.
            got = min_pairwise_edit_distance(column, max_block_size=20).mpd
            assert got == _brute_force_mpd(column)

    def test_small_columns_are_exact(self):
        rng = random.Random(7)
        for _ in range(50):
            column = _random_words(rng, 40)
            assert min_pairwise_edit_distance(column).mpd == _brute_force_mpd(column)


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

    def test_exact_duplicates_are_collapsed(self):
        result = min_pairwise_edit_distance(["red", "red", "blue"])
        assert result.mpd == Levenshtein.distance("red", "blue")
        assert {result.value_u, result.value_v} == {"red", "blue"}

    def test_indices_point_at_first_occurrence(self):
        result = min_pairwise_edit_distance(["x", "red", "red", "bed"])
        assert (result.value_u, result.value_v) == ("red", "bed")
        assert (result.index_u, result.index_v) == (1, 3)

    def test_all_identical_values_are_not_computable(self):
        with pytest.raises(InsufficientDataError):
            min_pairwise_edit_distance(["a", "a"])
        with pytest.raises(InsufficientDataError):
            min_pairwise_edit_distance(["a", "a", None, "a"])

    def test_stringified_duplicates_collapse(self):
        with pytest.raises(InsufficientDataError):
            min_pairwise_edit_distance([1, "1", 1])

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
        # Values share no prefix/suffix blocking key, so no block
        # ever reaches size >= 2, and the column is larger than
        # max_block_size -- the bounded global-scan fallback cannot apply.
        values = ["bq1x7", "cw22y8", "dt333z9", "ek4444k0", "fm55555m1", "gn666666n2"]
        with pytest.raises(ValidationError):
            min_pairwise_edit_distance(values, max_block_size=3)
        with pytest.raises(ValueError):
            min_pairwise_edit_distance(values, max_block_size=3)

    def test_try_variant_returns_none_when_no_comparable_blocks(self):
        values = ["bq1x7", "cw22y8", "dt333z9", "ek4444k0", "fm55555m1", "gn666666n2"]
        assert try_min_pairwise_edit_distance(values, max_block_size=3) is None

    def test_try_variant_matches_strict_variant_otherwise(self):
        values = ["Kevin Doeling", "Kevin Dowling", "Alan Myerson"]
        assert try_min_pairwise_edit_distance(values) == min_pairwise_edit_distance(values)

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
        with pytest.raises(ValidationError):
            fd_compliance_ratio(["a"], ["b", "c"])
        with pytest.raises(ValueError):
            fd_compliance_ratio(["a"], ["b", "c"])

    def test_ignores_null_lhs_rows(self):
        lhs = ["1", None, "1", "2"]
        rhs = ["x", "z", "x", "y"]
        result = fd_compliance_ratio(lhs, rhs)
        assert result.ratio == 1.0
        assert result.violating_row_indices == ()

    def test_raises_when_every_lhs_value_is_null(self):
        with pytest.raises(InsufficientDataError):
            fd_compliance_ratio([None, None], ["a", "b"])
        with pytest.raises(OpenDetectError):
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
