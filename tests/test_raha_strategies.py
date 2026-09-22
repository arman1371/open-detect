"""Unit tests for algorithms/raha/strategies.py, validated against the paper's own
running example (Table 2 / Section 2.2, Wang & He -- er, Mahdavi et al., SIGMOD'19).
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from unidetect.algorithms.raha.strategies import (
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
