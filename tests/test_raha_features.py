"""Unit tests for algorithms/raha/features.py."""

from __future__ import annotations

import pandas as pd

from unidetect.algorithms.raha.config import RahaConfig
from unidetect.algorithms.raha.features import build_all_features, build_column_features


def test_drops_constant_features():
    # Every strategy either fires on every row or on none: e.g. a
    # single-value column has no rare values (histogram) and no dependent
    # columns (fd), so its feature matrix should end up empty.
    df = pd.DataFrame({"only": ["x", "x", "x"]})
    features = build_column_features(df, "only", RahaConfig())
    assert features.matrix.shape == (3, 0)
    assert features.feature_names == ()


def test_keeps_informative_features():
    df = pd.DataFrame({"a": ["x", "x", "y"]})
    features = build_column_features(df, "a", RahaConfig())
    assert features.matrix.shape[0] == 3
    assert features.matrix.shape[1] > 0
    assert len(features.feature_names) == features.matrix.shape[1]


def test_build_all_features_covers_every_column():
    df = pd.DataFrame({"a": ["x", "y", "x"], "b": [1, 2, 3]})
    all_features = build_all_features(df, RahaConfig())
    assert set(all_features) == {"a", "b"}
    assert all_features["a"].matrix.shape[0] == 3
    assert all_features["b"].matrix.shape[0] == 3


def test_feature_values_are_binary():
    df = pd.DataFrame({"a": ["x", "y", "x", "z", "z"]})
    features = build_column_features(df, "a", RahaConfig())
    assert set(features.matrix.flatten().tolist()) <= {0.0, 1.0}
