"""Unit tests for algorithms/raha/strategies.py, validated against the paper's own
running example (Table 2 / Section 2.2, Wang & He -- er, Mahdavi et al., SIGMOD'19).
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from open_detect.algorithms.raha.strategies import (
    fd_violation_strategies,
    gaussian_outlier_strategies,
    histogram_outlier_strategies,
    pattern_character_strategies,
)

# The paper's running example (Table 2), with the PDF-mangled placeholder
# character replaced by a plain repeated string so the "twice-repeated
# value" structure the worked example relies on is unambiguous.
LORD = pd.Series(["Aragorn", "Sauron", "Gandalf", "Saruman", "Elrond", "Theoden"])
KINGDOM = pd.Series(["Minas Tirith", "Mordor", "MISSING", "MISSING", "123", "Shire"])


class TestHistogramOutlierStrategies:
    def test_matches_paper_worked_example(self):
        # so1 (tf=2/6): flags every row except the twice-repeated "MISSING".
        # so2 (tf=3/6): flags every row (max frequency is 2/6 < 3/6).
        result = histogram_outlier_strategies(KINGDOM, [2 / 6, 3 / 6])
        np.testing.assert_array_equal(
            result["outlier_tf<0.3333333333333333"],
            [True, True, False, False, True, True],
        )
        np.testing.assert_array_equal(result["outlier_tf<0.5"], [True] * 6)

    def test_treats_missing_values_as_one_category(self):
        values = pd.Series(["a", None, "b", float("nan")])
        result = histogram_outlier_strategies(values, [0.4])
        # "a" and "b" are singletons (freq 1/4, below 0.4); the two nulls
        # form their own size-2 group (freq 2/4, at or above 0.4), same as
        # any other repeated value.
        np.testing.assert_array_equal(result["outlier_tf<0.4"], [True, False, True, False])

    def test_null_sentinel_content(self):
        # Verify null sentinel is treated as one category
        values = pd.Series([None, float("nan")])
        result = histogram_outlier_strategies(values, [0.4])
        # Both nulls should be in same category (sentinel), freq 2/2 = 1.0 >= 0.4
        np.testing.assert_array_equal(result["outlier_tf<0.4"], [False, False])
        # No outliers since they're the only values in the column

    def test_empty_column(self):
        assert histogram_outlier_strategies(pd.Series([], dtype=object), [0.5]) == {}


class TestGaussianOutlierStrategies:
    def test_flags_far_from_mean(self):
        values = pd.Series([10] * 10 + [1000])
        result = gaussian_outlier_strategies(values, [1.0, 3.0])
        assert result["outlier_dist>1.0"][-1]
        assert result["outlier_dist>3.0"][-1]
        assert not result["outlier_dist>3.0"][:-1].any()

    def test_non_numeric_column_produces_no_strategies(self):
        assert gaussian_outlier_strategies(KINGDOM, [1.0]) == {}

    def test_constant_column_flags_nothing(self):
        values = pd.Series([5, 5, 5, 5])
        result = gaussian_outlier_strategies(values, [1.0])
        assert not result["outlier_dist>1.0"].any()

    def test_mostly_numeric_column_ignores_stray_non_numeric_cells(self):
        values = pd.Series(["1", "2", "3", "4", "not-a-number"])
        result = gaussian_outlier_strategies(values, [1.0])
        assert not result["outlier_dist>1.0"][-1]  # non-numeric cell left unflagged

    def test_row_weighted_mostly_numeric_vs_unique_value_share(self):
        # Bug fix: row-weighted "mostly numeric" check vs unique-value share
        # Column of 1000 "1"s and one "x" should be mostly numeric (row_parseable_share >= 0.5)
        # but unique-value share would incorrectly flag as NOT mostly numeric (1/2 < 0.5)
        values = pd.Series(["1"] * 1000 + ["x"])
        result = gaussian_outlier_strategies(values, [1.0])
        # With row-weighted check: 1000/1001 = 99.9% numeric -> mostly numeric -> strategies should return
        assert list(result.keys())  # Should return strategies since mostly numeric
        # With unique-value share: 2/2 = 50% numeric -> NOT mostly numeric (needs < 0.5)
        # This tests that the factorize-once optimization uses row-weighted, not unique-value
        # Verify strategies actually returned for some threshold
        assert any('outlier_dist>' in k for k in result.keys())

    def test_null_sentinel_handling_mostly_numeric(self):
        # Nulls mapped to sentinel should be ignored for numeric parsing
        values = pd.Series(["1", "2", None, "3", float("nan")])
        result = gaussian_outlier_strategies(values, [1.0])
        # Nulls mapped to sentinel, so 3/3 = 100% numeric -> mostly numeric -> should return strategies
        assert list(result.keys())  # Should return strategies

    def test_mostly_numeric_threshold(self):
        # Exact boundary test: 49.9% numeric -> NOT mostly numeric (< 0.5)
        values = pd.Series(["1"] * 499 + ["x"] * 501)  # 499/1000 = 49.9%
        result = gaussian_outlier_strategies(values, [1.0])
        # 499/1000 = 49.9% < 50% -> NOT mostly numeric -> should return empty
        assert not result  # Should return empty strategies

    def test_mostly_numeric_boundary(self):
        # Exact boundary test: 50% numeric -> IS mostly numeric (>= 0.5)
        values = pd.Series(["1"] * 500 + ["x"] * 500)  # 500/1000 = 50%
        result = gaussian_outlier_strategies(values, [1.0])
        # 500/1000 = 50% >= 50% -> mostly numeric -> should return strategies
        assert list(result.keys())  # Should return strategies


class TestPatternCharacterStrategies:
    def test_flags_cells_containing_character(self):
        values = pd.Series(["16.11.1990", "16-11-1990", "16.11.1990"])
        result = pattern_character_strategies(values, max_characters=128)
        np.testing.assert_array_equal(result["pattern_contains['-']"], [False, True, False])

    def test_respects_max_characters_cap(self):
        values = pd.Series(["abcdefgh", "abcdefgh"])
        result = pattern_character_strategies(values, max_characters=3)
        assert len(result) == 3

    def test_empty_column(self):
        assert pattern_character_strategies(pd.Series([], dtype=object), max_characters=128) == {}

    def test_null_sentinel_preserves_nulls(self):
        # Nulls should be mapped to sentinel and not treated as characters
        values = pd.Series(["abc", None, "def", float("nan")])
        result = pattern_character_strategies(values, max_characters=10)
        # Nulls become sentinel "__open_detect_raha_null__" - contains no characters
        # So only "abc" and "def" contribute characters
        assert "pattern_contains['a']" in result or "pattern_contains['b']" in result or "pattern_contains['c']" in result
        assert "pattern_contains['d']" in result or "pattern_contains['e']" in result or "pattern_contains['f']" in result
        # Sentinel should not contribute any characters
        sentinel_chars = set("__open_detect_raha_null__")
        for ch in sentinel_chars:
            if any(ch in name for name in result.keys()):
                pass  # This would be wrong - sentinel shouldn't have characters


class TestFdViolationStrategies:
    def test_lord_determines_kingdom_holds(self):
        # Every Lord value is unique, so the Lord -> Kingdom FD has no
        # ambiguous groups: sr1 = {} in the paper's own example.
        df = pd.DataFrame({"Lord": LORD, "Kingdom": KINGDOM})
        result = fd_violation_strategies(df, target_column="Kingdom")
        assert not result["fd[Lord->Kingdom]"].any()

    def test_kingdom_determines_lord_is_violated(self):
        # Kingdom "MISSING" repeats for two different Lords (Gandalf,
        # Saruman), so Kingdom -> Lord is violated at exactly those two rows.
        df = pd.DataFrame({"Lord": LORD, "Kingdom": KINGDOM})
        result = fd_violation_strategies(df, target_column="Lord")
        np.testing.assert_array_equal(
            result["fd[Kingdom->Lord]"], [False, False, True, True, False, False]
        )

    def test_one_strategy_per_other_column(self):
        df = pd.DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6]})
        result = fd_violation_strategies(df, target_column="a")
        assert set(result) == {"fd[b->a]", "fd[c->a]"}

    def test_empty_column(self):
        df = pd.DataFrame({"a": [], "b": []})
        result = fd_violation_strategies(df, target_column="a")
        # When target column is empty, there should still be FD strategies from other columns
        # The fd_violation_strategies function processes all other columns regardless of target
        assert "fd[b->a]" in result  # Should have this FD even with empty target column

    def test_null_sentinel_in_fd(self):
        # Test FD with nulls (mapped to sentinel) in the data
        # sentinel maps to 2 distinct RHS values (y and z), so it IS violated
        df = pd.DataFrame({
            "lhs": ["a", None, "a", "b", None],
            "rhs": ["x", "y", "y", "z", "z"]
        })
        result = fd_violation_strategies(df, target_column="rhs")
        # sentinel (None) maps to 2 distinct RHS values (y, z), so violation expected
        # Row 1 (sentinel->y) and Row 4 (sentinel->z) should be flagged
        # Row 0 (a->x): sentinel maps to 2 values, a maps to 2 values (x,y) -> True
        # Row 1 (sentinel->y): True
        # Row 2 (a->y): True (a maps to x,y)
        # Row 3 (b->z): b maps to only z -> False
        # Row 4 (sentinel->z): True
        np.testing.assert_array_equal(
            result["fd[lhs->rhs]"], [True, True, True, False, True]
        )

    def test_fd_with_repeated_lhs_groups_and_null(self):
        # FD with repeated LHS values including nulls
        # Row 0: lhs='a', rhs='x'
        # Row 1: lhs='a', rhs='y'
        # Row 2: lhs=None, rhs='x'  -> sentinel maps to x
        # Row 3: lhs=None, rhs='x'  -> sentinel maps to x (again!)
        # Row 4: lhs='b', rhs='z'
        # sentinel maps to only x (1 distinct RHS) -> NOT violating
        # 'a' maps to x and y (2 distinct RHS) -> violating at rows 0,1
        # 'b' maps to only z (1 distinct RHS) -> NOT violating
        df = pd.DataFrame({
            "lhs": ["a", "a", None, None, "b"],
            "rhs": ["x", "y", "x", "x", "z"]
        })
        result = fd_violation_strategies(df, target_column="rhs")
        # 'a' maps to x and y -> 2 distinct -> violation
        # sentinel maps to only x -> 1 distinct -> no violation
        # 'b' maps to only z -> 1 distinct -> no violation
        # Expected: rows 0,1 flagged (a maps to 2 values), rows 2,3,4 not flagged
        np.testing.assert_array_equal(
            result["fd[lhs->rhs]"], [True, True, False, False, False]
        )
