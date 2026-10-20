"""Unit tests for the offline pattern index (paper Eqn 4, Section 2.4)."""

from __future__ import annotations

import random
from dataclasses import FrozenInstanceError

import pandas as pd
import pytest

from open_detect.algorithms.auto_validate.config import AutoValidateConfig
from open_detect.algorithms.auto_validate.hierarchy import matches
from open_detect.algorithms.auto_validate.index import (
    PatternIndex,
    build_pattern_index,
    clean_column,
    indexable_values,
)
from open_detect.algorithms.auto_validate.metrics import impurity
from open_detect.algorithms.auto_validate.patterns import patterns_of
from open_detect.exceptions import ValidationError

TIME = "<num>:<num>:<num>"


def _reference_build_pattern_index(corpus, config=None):
    """The pre-optimization index build, kept as a test-local oracle.

    It re-scans every candidate pattern against every value of a column --
    the O(|P(D)| x |D|) behaviour OPE-85 replaces -- and produces exactly the
    same entries (pattern -> (FPR_T, Cov_T), restricted to Cov_T >= m) the optimized
    builder must match.
    """
    config = config or AutoValidateConfig()
    local: dict[str, list[float]] = {}
    n_indexed = 0
    for values in _reference_iter_corpus_columns(corpus):
        indexable = indexable_values(values, config.tau)
        if not indexable:
            continue
        n_indexed += 1
        column_patterns: set[str] = set()
        for value in indexable:
            column_patterns |= patterns_of(value, config.tau)
        for pattern in column_patterns:
            if not any(matches(pattern, value) for value in indexable):
                continue
            local.setdefault(pattern, []).append(impurity(pattern, indexable))
    entries = {
        pattern: (sum(scores) / len(scores), len(scores))
        for pattern, scores in local.items()
        if len(scores) >= config.m
    }
    return PatternIndex._build(entries, n_indexed)


def _reference_iter_corpus_columns(corpus):
    for item in corpus:
        if isinstance(item, pd.DataFrame):
            for name in item.columns:
                yield clean_column(item[name].tolist())
        elif isinstance(item, pd.Series):
            yield clean_column(item.tolist())
        elif isinstance(item, (list, tuple)):
            yield clean_column(item)
        else:
            raise ValidationError(
                "corpus entries must be pandas Series, DataFrames or sequences of values, "
                f"got {type(item).__name__}"
            )


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
        with pytest.raises(ValidationError, match="corpus entries"):
            build_pattern_index([42], AutoValidateConfig(tau=8, m=1))

    def test_unsupported_entry_is_still_a_value_error(self):
        with pytest.raises(ValueError, match="corpus entries"):
            build_pattern_index([42], AutoValidateConfig(tau=8, m=1))

    def test_empty_corpus(self):
        index = build_pattern_index([], AutoValidateConfig(tau=8, m=1))
        assert len(index) == 0
        assert index.n_columns == 0


def _datetime_column(seed: int, n: int, repeat: int = 1) -> list[str]:
    rng = random.Random(seed)
    values = [
        f"{rng.randint(1990, 2040):04d}-{rng.randint(1, 12):02d}-{rng.randint(1, 28):02d} "
        f"{rng.randint(0, 23):02d}:{rng.randint(0, 59):02d}:{rng.randint(0, 59):02d}"
        for _ in range(n)
    ]
    return values * repeat


def _wide_mixed_column() -> list[str]:
    rng = random.Random(0)
    alphabet = "abcXYZ0123456789"
    return [
        "-".join("".join(rng.choice(alphabet) for _ in range(rng.randint(1, 4))) for _ in range(6))
        for _ in range(8)
    ]


class TestEquivalenceToReferenceBuild:
    """The optimized builder must produce byte-identical entries to the
    pre-optimization O(|P(D)| x |D|) build on every corpus shape."""

    @pytest.mark.parametrize(
        "corpus, config",
        [
            # ID column: distinct integer-like values.
            (
                [[str(i) for i in range(300)]],
                AutoValidateConfig(m=1, tau=8),
            ),
            # Datetime columns, tau=20: distinct values per column, with duplicates.
            (
                [_datetime_column(seed, 10) for seed in range(4)],
                AutoValidateConfig(m=1, tau=20),
            ),
            (
                [_datetime_column(seed, 8, repeat=3) for seed in range(3)],
                AutoValidateConfig(m=2, tau=20),
            ),
            # Wide mixed-token column that reaches patterns_of's 2048 cap.
            (
                [_wide_mixed_column()],
                AutoValidateConfig(m=1, tau=20),
            ),
            # Mixed-type object column with nulls, blanks and duplicates.
            (
                [[1, None, "a", float("nan"), "", "  ", "a", 1, 2.5, True, "2020-01-01"]],
                AutoValidateConfig(m=1, tau=8),
            ),
            # Empty column and single-value column.
            (
                [[None, None, ""], ["x"], []],
                AutoValidateConfig(m=1, tau=8),
            ),
            # All-NaN column.
            (
                [[float("nan"), float("nan")]],
                AutoValidateConfig(m=1, tau=8),
            ),
            # k > distinct rows: a column with more rows than distinct values.
            (
                [["a", "b", "a", "b", "a", "b", "c"]],
                AutoValidateConfig(m=1, tau=8),
            ),
            # Multi-column corpus with mixed shapes (Series + DataFrame + list).
            (
                [
                    pd.Series(["10:00:00", "11:00:00"]),
                    pd.DataFrame({"x": ["a", "b"], "y": ["1/2", "3/4"]}),
                    ["zz", "yy"],
                ],
                AutoValidateConfig(m=1, tau=8),
            ),
        ],
    )
    def test_entries_match_reference(self, corpus, config):
        reference = _reference_build_pattern_index(corpus, config)
        actual = build_pattern_index(corpus, config)
        assert actual.n_columns == reference.n_columns
        assert set(actual._entries) == set(reference._entries)
        for pattern in reference._entries:
            assert actual.lookup(pattern) == pytest.approx(reference.lookup(pattern))

    def test_prunes_entries_below_m_and_agrees_with_reference(self):
        corpus = [["10:00:00"], ["10:00:00"], ["zz"]]
        reference = _reference_build_pattern_index(corpus, AutoValidateConfig(m=2))
        actual = build_pattern_index(corpus, AutoValidateConfig(m=2))
        assert actual.n_columns == reference.n_columns == 3
        assert set(actual._entries) == set(reference._entries)
        assert all(cov >= 2 for _, cov in actual._entries.values())
        assert len(actual) < len(build_pattern_index(corpus, AutoValidateConfig(m=1)))
