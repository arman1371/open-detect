"""Unit tests for the offline pattern index (paper Eqn 4, Section 2.4)."""

from __future__ import annotations

from dataclasses import FrozenInstanceError

import pandas as pd
import pytest

from open_detect.algorithms.auto_validate.config import AutoValidateConfig
from open_detect.algorithms.auto_validate.index import (
    PatternIndex,
    build_pattern_index,
    clean_column,
    indexable_values,
)
from open_detect.algorithms.auto_validate.metrics import impurity

TIME = "<num>:<num>:<num>"


class TestCleanColumn:
    def test_str_converts_non_strings(self):
        assert clean_column([1, 2.5, True]) == ("1", "2.5", "True")

    def test_drops_nulls_and_blanks(self):
        assert clean_column(["a", None, "b", float("nan"), "", "  "]) == ("a", "b", "  ")

    def test_empty_input(self):
        assert clean_column([]) == ()


class TestIndexableValues:
    def test_drops_values_at_or_above_tau_tokens(self):
        values = ("10:20:30", "1|2|3|4|5|6|7|8|9")
        assert indexable_values(values, tau=8) == ("10:20:30",)
        assert indexable_values(values, tau=32) == values


class TestFprAggregation:
    def test_matches_paper_example_3(self):
        """4800 of 5000 columns at impurity 0 and 200 at 1% gives FPR_T = 0.04%."""
        pure = ["10:00:00", "11:00:00", "12:00:00"]
        near = ["10:00:00"] * 99 + ["zz"]  # exactly 1 of 100 values is impure
        corpus = [pure, pure, pure, pure, near]
        index = build_pattern_index(corpus, AutoValidateConfig(m=1))
        fpr, cov = index.lookup(TIME)
        assert cov == 5
        assert fpr == pytest.approx(0.01 / 5)

    def test_non_matching_columns_excluded_from_denominator(self):
        pure = ["10:00:00", "11:00:00"]
        near = ["10:00:00"] * 99 + ["zz"]
        other = ["1", "2", "3"]  # never matches TIME
        index = build_pattern_index([pure, near, other, other], AutoValidateConfig(m=1))
        fpr, cov = index.lookup(TIME)
        assert cov == 2  # the two TIME columns only
        assert fpr == pytest.approx(0.01 / 2)
        assert index.n_columns == 4  # but all four were scanned

    def test_aggregation_is_unweighted_by_column_size(self):
        small = ["10:00:00", "zz"]  # impurity 0.5, 2 values
        large = ["10:00:00"] * 99 + ["zz"]  # impurity 0.01, 100 values
        index = build_pattern_index([small, large], AutoValidateConfig(m=1))
        fpr, cov = index.lookup(TIME)
        assert cov == 2
        # A size-weighted mean would be dominated by `large`; Eqn 4 averages.
        assert fpr == pytest.approx((0.5 + 0.01) / 2)

    def test_impurity_counts_duplicate_values_with_multiplicity(self):
        values = ["10:00:00", "zz", "zz", "11:00:00"]
        assert impurity(TIME, values) == pytest.approx(0.5)

    def test_pattern_absent_from_index_returns_none(self):
        index = build_pattern_index([["10:00:00"]], AutoValidateConfig(m=1))
        assert index.lookup("<letter>+") is None
        assert index.fpr("<letter>+") is None
        assert index.coverage("<letter>+") is None


class TestTauPruning:
    def test_wide_column_is_absent_and_not_counted(self):
        wide = "1|2|3|4|5|6|7|8|9|10"  # 19 tokens
        index = build_pattern_index([[wide, "10:20:30"]], AutoValidateConfig(tau=8, m=1))
        assert wide not in index
        assert index.n_columns == 1
        assert TIME in index

    def test_raising_tau_readmits_the_wide_column(self):
        wide = "1|2|3|4|5|6|7|8|9|10"
        index = build_pattern_index([[wide]], AutoValidateConfig(tau=32, m=1))
        assert wide in index
        assert index.n_columns == 1

    def test_corpus_of_only_wide_columns_yields_empty_index(self):
        index = build_pattern_index([["1|2|3|4|5|6|7|8|9|10"]], AutoValidateConfig(tau=8, m=1))
        assert len(index) == 0
        assert index.n_columns == 0

    def test_emptied_column_does_not_count_toward_n_columns(self):
        index = build_pattern_index([[None, None, ""]], AutoValidateConfig(tau=8, m=1))
        assert index.n_columns == 0


class TestPatternIndex:
    def test_lookup_reports_fpr_and_coverage(self):
        index = build_pattern_index([["10:00:00"], ["11:00:00"]], AutoValidateConfig(tau=8, m=1))
        fpr, cov = index.lookup(TIME)
        assert (fpr, cov) == (0.0, 2)

    def test_len_counts_distinct_patterns(self):
        index = build_pattern_index([["10:00:00"]], AutoValidateConfig(tau=8, m=1))
        assert len(index) == len(index.patterns())
        assert len(index) > 0

    def test_contains_protocol(self):
        index = build_pattern_index([["10:00:00"]], AutoValidateConfig(tau=8, m=1))
        assert TIME in index
        assert "<letter>+" not in index

    def test_iteration_is_deterministic(self):
        corpus = [["10:00:00"], ["11:00:00"], ["a"]]
        first = build_pattern_index(corpus, AutoValidateConfig(tau=8, m=1))
        second = build_pattern_index(corpus, AutoValidateConfig(tau=8, m=1))
        assert first.patterns() == second.patterns()
        assert list(first) == list(second)

    def test_is_immutable_after_build(self):
        index = build_pattern_index([["10:00:00"]], AutoValidateConfig(tau=8, m=1))
        with pytest.raises(TypeError, match="mappingproxy"):
            index._entries["x"] = (0.0, 0)  # type: ignore[index]

    def test_is_hashable_value_object(self):
        index = build_pattern_index([["10:00:00"]], AutoValidateConfig(tau=8, m=1))
        assert isinstance(index, PatternIndex)
        with pytest.raises(FrozenInstanceError, match="cannot assign to field"):
            index.n_columns = 99  # type: ignore[misc]


class TestCorpusInputShapes:
    def test_accepts_series(self):
        index = build_pattern_index([pd.Series(["10:00:00"])], AutoValidateConfig(tau=8, m=1))
        assert index.n_columns == 1

    def test_dataframe_contributes_each_column(self):
        frame = pd.DataFrame({"a": ["10:00:00"], "b": ["xy"], "c": ["1/2"]})
        index = build_pattern_index([frame], AutoValidateConfig(tau=8, m=1))
        assert index.n_columns == 3

    def test_accepts_plain_sequences(self):
        index = build_pattern_index([["10:00:00", "11:00:00"]], AutoValidateConfig(tau=8, m=1))
        assert index.n_columns == 1

    def test_rejects_unsupported_entry(self):
        with pytest.raises(TypeError, match="corpus entries"):
            build_pattern_index([42], AutoValidateConfig(tau=8, m=1))

    def test_empty_corpus(self):
        index = build_pattern_index([], AutoValidateConfig(tau=8, m=1))
        assert len(index) == 0
        assert index.n_columns == 0
