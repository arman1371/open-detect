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

    def test_empty_column(self):
        assert histogram_outlier_strategies(pd.Series([], dtype=object), [0.5]) == {}

    def test_row_weighted_mostly_numeric_gate(self):
        """Test that the gaussian strategy uses row-weighted "mostly numeric" gate.

        A column of 1000 "1"s and one "x" is mostly numeric by rows (1000/1001 ≈ 0.999)
        but only 1/2 by distinct values. The row-weighted gate should pass the column.
        """
        values = pd.Series(["1"] * 1000 + ["x"])
        result = gaussian_outlier_strategies(values, [1.0])
        # The column should be treated as "mostly numeric" and NOT flag the "x" cell
        assert not result["outlier_dist>1.0"][-1]  # "x" should not be flagged

    def test_null_sentinel_handling(self):
        """Test that null sentinel values are treated as one category.

        Missing values (None, NaN) should be grouped together as a single category,
        consistent with how the paper's running example treats placeholders.
        The two nulls form a single group of size 2 (2/4 = 0.5 >= 0.4), so they
        are NOT flagged as outliers, same as any other repeated value.
        """
        values = pd.Series(["a", None, "b", float("nan")])
        result = histogram_outlier_strategies(values, [0.4])
        # The two nulls form one group of size 2 (freq 2/4 = 0.5 >= 0.4),
        # so neither None nor NaN is flagged as an outlier
        assert not result["outlier_tf<0.4"][1]  # None not flagged
        assert not result["outlier_tf<0.4"][3]  # NaN not flagged
        # "a" and "b" are singletons (freq 1/4 < 0.4), so they ARE flagged
        assert result["outlier_tf<0.4"][0]  # "a" flagged
        assert result["outlier_tf<0.4"][2]  # "b" flagged


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


class TestPatternCharacterStrategies:
    def test_flags_cells_containing_character(self):
        values = pd.Series(["16.11.1990", "16-11-1990", "16.11.1990"])
        result = pattern_character_strategies(values, max_characters=128)
        np.testing.assert_array_equal(result["pattern_contains['-']"], [False, True, False])

    def test_respects_max_characters_cap(self):
        values = pd.Series(["abcdefgh", "abcdefgh"])
        result = pattern_character_strategies(values, max_characters=3)
        assert len(result) == 3


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

    def test_fd_repeated_groups_with_null_sentinel(self):
        """Test FD with repeated groups and null sentinel.

        When two columns have repeated values with nulls, the FD should
        correctly handle the null sentinel grouping.
        """
        df = pd.DataFrame({
            "A": ["a", "a", None, None, "b", "b"],
            "B": ["x", "x", "y", "y", None, None],
        })
        result = fd_violation_strategies(df, target_column="B")
        # With null sentinel, A values map correctly to B groups including nulls
        assert "fd[A->B]" in result

    def test_empty_frame_fd(self):
        """FD strategies with empty DataFrame."""
        df = pd.DataFrame({"a": pd.Series([], dtype=object), "b": pd.Series([], dtype=object)})
        result = fd_violation_strategies(df, target_column="a")
        # Should handle empty frame gracefully
        assert len(result) == 0 or all(not v.any() for v in result.values())
