"""Unit tests for algorithms/raha/strategies.py, validated against the paper's own
running example (Table 2 / Section 2.2, Wang & He -- er, Mahdavi et al., SIGMOD'19).
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from open_detect.algorithms.raha.config import RahaConfig
from open_detect.algorithms.raha.features import build_column_features
from open_detect.algorithms.raha.strategies import (
    NULL_SENTINEL,
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


# ---------------------------------------------------------------------------
# Factorize-once regression tests (OPE-82 P-11): naive references + edge cases
# ---------------------------------------------------------------------------


def _naive_str(values: pd.Series) -> list[str]:
    return [NULL_SENTINEL if pd.isna(v) else str(v) for v in values]


def _naive_histogram(values: pd.Series, thresholds) -> dict[str, np.ndarray]:
    raw = _naive_str(values)
    n = len(raw)
    return {
        f"outlier_tf<{t}": np.array([raw.count(v) / n < t for v in raw], dtype=bool)
        for t in thresholds
    }


def _naive_gaussian(values: pd.Series, thresholds) -> dict[str, np.ndarray]:
    from open_detect.text_utils import is_float_like

    raw = _naive_str(values)
    if not raw:
        return {}
    parseable = [is_float_like(v) for v in raw]
    if sum(parseable) / len(raw) < 0.5:
        return {}
    nums = np.array([float(v) if p else np.nan for v, p in zip(raw, parseable, strict=True)])
    finite = np.isfinite(nums)
    if finite.sum() < 2:
        return {}
    mean, std = nums[finite].mean(), nums[finite].std(ddof=0)
    if not std:
        return {f"outlier_dist>{t}": np.zeros(len(raw), dtype=bool) for t in thresholds}
    z = np.where(finite, np.abs(nums - mean) / std, 0.0)
    return {f"outlier_dist>{t}": z > t for t in thresholds}


def _naive_pattern(values: pd.Series, max_characters: int) -> dict[str, np.ndarray]:
    raw = _naive_str(values)
    counts: dict[str, int] = {}
    for v in raw:
        for ch in set(v):
            counts[ch] = counts.get(ch, 0) + 1
    top = sorted(counts, key=lambda ch: (-counts[ch], ch))[:max_characters]
    return {f"pattern_contains[{ch!r}]": np.array([ch in v for v in raw]) for ch in top}


def _naive_fd(df: pd.DataFrame, target: str) -> dict[str, np.ndarray]:
    rhs = _naive_str(df[target])
    out = {}
    for other in df.columns:
        if other == target:
            continue
        lhs = _naive_str(df[other])
        groups: dict[str, set[str]] = {}
        for a, b in zip(lhs, rhs, strict=True):
            groups.setdefault(a, set()).add(b)
        out[f"fd[{other}->{target}]"] = np.array([len(groups[a]) > 1 for a in lhs], dtype=bool)
    return out


def _assert_same(actual: dict[str, np.ndarray], expected: dict[str, np.ndarray]) -> None:
    assert list(actual) == list(expected)
    for key, exp in expected.items():
        assert actual[key].dtype == bool
        np.testing.assert_array_equal(actual[key], exp, err_msg=key)


def _random_column(rng: np.random.Generator, n: int, kind: str) -> pd.Series:
    if kind == "numeric":
        out: list = list(rng.integers(0, 8, n).astype(float))
        for i in rng.integers(0, n, max(1, n // 6)):
            out[i] = [1000.0, np.nan, None, "x"][int(rng.integers(0, 4))]
        return pd.Series(out, dtype=object)
    pool = ["a", "b-c", "12", "x.y", "", "Zed", "q q"]
    out = [pool[int(j)] for j in rng.integers(0, len(pool), n)]
    for i in rng.integers(0, n, max(1, n // 6)):
        out[i] = [None, np.nan, 3, 4.5][int(rng.integers(0, 4))]
    return pd.Series(out, dtype=object)


class TestRandomizedEquivalenceWithNaiveReference:
    TRIALS = 60

    def test_all_four_families_match_naive_reference(self):
        rng = np.random.default_rng(20241020)
        for _ in range(self.TRIALS):
            n = int(rng.integers(1, 40))
            kind = "numeric" if rng.random() < 0.5 else "text"
            col = _random_column(rng, n, kind)
            _assert_same(
                histogram_outlier_strategies(col, (0.1, 0.3, 0.6)),
                _naive_histogram(col, (0.1, 0.3, 0.6)),
            )
            _assert_same(
                gaussian_outlier_strategies(col, (0.5, 1.0, 2.0)),
                _naive_gaussian(col, (0.5, 1.0, 2.0)),
            )
            _assert_same(pattern_character_strategies(col, 5), _naive_pattern(col, 5))
            df = pd.DataFrame(
                {
                    "t": col,
                    "u": _random_column(rng, n, "text"),
                    "v": _random_column(rng, n, "numeric"),
                }
            )
            _assert_same(fd_violation_strategies(df, "t"), _naive_fd(df, "t"))

    def test_reference_is_not_vacuous(self):
        # Guard against the comparison trivially passing on all-False output.
        rng = np.random.default_rng(1)
        col = _random_column(rng, 40, "text")
        assert any(f.any() for f in _naive_histogram(col, (0.3,)).values())
        assert any(f.any() for f in _naive_pattern(col, 5).values())


class TestRowWeightedNumericGate:
    def test_gate_is_row_weighted_not_unique_weighted(self):
        # 2 of 6 distinct values parse (unique share 1/3 < 0.5) but those
        # rows are 96 of 100 (row share 0.96), so the column is mostly numeric.
        values = pd.Series(["1"] * 95 + ["2"] + ["x", "y", "z", "w"])
        result = gaussian_outlier_strategies(values, [1.0])
        assert "outlier_dist>1.0" in result
        assert result["outlier_dist>1.0"][95]
        assert not result["outlier_dist>1.0"][96:].any()

    def test_mostly_non_numeric_by_rows_is_rejected(self):
        values = pd.Series(["x"] * 10 + ["1", "2"])
        assert gaussian_outlier_strategies(values, [1.0]) == {}


class TestNullSentinel:
    def test_none_and_nan_share_one_category(self):
        values = pd.Series([None, np.nan, "a", "b", "c", "d"])
        hist = histogram_outlier_strategies(values, [0.3])["outlier_tf<0.3"]
        # nulls form a group of 2 (freq 1/3 >= 0.3); singletons (1/6) are flagged
        np.testing.assert_array_equal(hist, [False, False, True, True, True, True])

    def test_null_cells_are_unflagged_by_gaussian(self):
        values = pd.Series([1.0] * 8 + [100.0, np.nan, None])
        flags = gaussian_outlier_strategies(values, [1.0])["outlier_dist>1.0"]
        assert flags[8]
        assert not flags[9:].any()

    def test_null_cells_are_flagged_by_sentinel_characters_in_pattern(self):
        values = pd.Series([None, "k"])
        result = pattern_character_strategies(values, max_characters=128)
        np.testing.assert_array_equal(result["pattern_contains['k']"], [False, True])
        np.testing.assert_array_equal(result["pattern_contains['_']"], [True, False])


class TestFdRepeatedGroupsAndNulls:
    def test_repeated_lhs_group_flags_every_row_of_violating_group(self):
        df = pd.DataFrame(
            {
                "lhs": ["g1", "g1", "g1", "g2", "g2", "g3"],
                "rhs": ["a", "a", "b", "c", "c", "d"],
            }
        )
        flags = fd_violation_strategies(df, "rhs")["fd[lhs->rhs]"]
        np.testing.assert_array_equal(flags, [True, True, True, False, False, False])

    def test_null_lhs_and_rhs_use_sentinel_groups(self):
        df = pd.DataFrame(
            {
                "lhs": ["a", "a", None, None, np.nan, "b"],
                "rhs": ["x", "x", "y", "z", "y", None],
            }
        )
        flags = fd_violation_strategies(df, "rhs")["fd[lhs->rhs]"]
        # "a" -> {x}: ok. null LHS (None and NaN together) -> {y, z}: violating.
        # "b" -> {null}: ok.
        np.testing.assert_array_equal(flags, [False, False, True, True, True, False])


class TestEmptyFrames:
    def test_pattern_empty(self):
        assert pattern_character_strategies(pd.Series([], dtype=object), 5) == {}

    def test_gaussian_empty(self):
        assert gaussian_outlier_strategies(pd.Series([], dtype=object), [1.0]) == {}

    def test_fd_empty_yields_empty_flag_arrays(self):
        df = pd.DataFrame({"a": pd.Series([], dtype=object), "b": pd.Series([], dtype=object)})
        result = fd_violation_strategies(df, "a")
        assert list(result) == ["fd[b->a]"]
        assert result["fd[b->a]"].shape == (0,)
        assert result["fd[b->a]"].dtype == bool


class TestFeatureMatrixDtype:
    CONFIG = RahaConfig(tf_thresholds=(0.3,), dist_thresholds=(1.0,), max_pattern_characters=8)

    def test_build_column_features_is_uint8_with_binary_values(self):
        df = pd.DataFrame(
            {
                "v": ["a", "a", "a", "b-b", "a", "zz"],
                "w": ["p", "p", "q", "q", "r", "r"],
            }
        )
        feats = build_column_features(df, "v", self.CONFIG)
        assert feats.matrix.dtype == np.uint8
        assert feats.matrix.shape == (6, len(feats.feature_names))
        assert feats.matrix.shape[1] > 0
        assert set(np.unique(feats.matrix)) <= {0, 1}
        col = feats.feature_names.index("pattern_contains['-']")
        np.testing.assert_array_equal(feats.matrix[:, col], [0, 0, 0, 1, 0, 0])

    def test_constant_column_has_empty_uint8_matrix(self):
        df = pd.DataFrame({"v": ["same"] * 5})
        feats = build_column_features(df, "v", self.CONFIG)
        assert feats.matrix.dtype == np.uint8
        assert feats.matrix.shape == (5, 0)

    def test_uint8_matrix_casts_to_float_for_pdist(self):
        from scipy.spatial.distance import pdist

        df = pd.DataFrame({"v": ["a", "a", "b-b", "a", "zz", "a"]})
        feats = build_column_features(df, "v", self.CONFIG)
        d = pdist(feats.matrix.astype(np.float64), metric="hamming")
        expected = [
            (feats.matrix[i] != feats.matrix[j]).mean()
            for i in range(len(df))
            for j in range(i + 1, len(df))
        ]
        np.testing.assert_allclose(d, expected)
