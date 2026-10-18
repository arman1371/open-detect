"""Unit tests for algorithms/raha/labeling.py."""

from __future__ import annotations

import numpy as np
import pandas as pd

from open_detect.algorithms.raha.features import ColumnFeatures
from open_detect.algorithms.raha.labeling import (
    CallableLabeler,
    GroundTruthLabeler,
    HeuristicLabeler,
    propagate_labels,
)


class TestGroundTruthLabeler:
    def test_labels_by_comparison_to_clean_data(self):
        dirty = pd.DataFrame({"a": ["x", "BAD"], "b": [1, 2]})
        clean = pd.DataFrame({"a": ["x", "y"], "b": [1, 2]})
        labeler = GroundTruthLabeler(clean)
        assert labeler.label_tuple(dirty, 0) == {"a": False, "b": False}
        assert labeler.label_tuple(dirty, 1) == {"a": True, "b": False}

    def test_missing_values_on_both_sides_are_not_an_error(self):
        dirty = pd.DataFrame({"a": [None]})
        clean = pd.DataFrame({"a": [None]})
        labeler = GroundTruthLabeler(clean)
        assert labeler.label_tuple(dirty, 0) == {"a": False}

    def test_numeric_string_vs_float_is_not_an_error(self):
        # BUG-10: str() comparison marked '5' vs '5.0' as dirty.
        dirty = pd.DataFrame({"a": ["5"]})
        clean = pd.DataFrame({"a": [5.0]})
        labeler = GroundTruthLabeler(clean)
        assert labeler.label_tuple(dirty, 0) == {"a": False}

    def test_int_vs_float_column_is_not_an_error(self):
        # BUG-10: str() comparison marked int vs float as dirty.
        dirty = pd.DataFrame({"a": [1, 2]})
        clean = pd.DataFrame({"a": [1.0, 2.0]})
        labeler = GroundTruthLabeler(clean)
        assert labeler.label_tuple(dirty, 0) == {"a": False}
        assert labeler.label_tuple(dirty, 1) == {"a": False}

    def test_missing_vs_value_is_an_error(self):
        dirty = pd.DataFrame({"a": [None]})
        clean = pd.DataFrame({"a": ["x"]})
        labeler = GroundTruthLabeler(clean)
        assert labeler.label_tuple(dirty, 0) == {"a": True}

    def test_duplicate_index_labels_resolve_positionally(self):
        # BUG-10: df.loc[[row_index]] on a duplicate index returns every
        # matching row instead of one, so .iloc[0] silently picked the wrong
        # one (or raised). Resolve the position once and index by position.
        dirty = pd.DataFrame({"a": ["x", "BAD", "alpha"]}, index=[0, 0, 1])
        clean = pd.DataFrame({"a": ["x", "x", "alpha"]}, index=[0, 0, 1])
        labeler = GroundTruthLabeler(clean)
        assert labeler.label_tuple(dirty, 1) == {"a": False}
        assert labeler.label_tuple(dirty, 0) == {"a": False}


class TestCallableLabeler:
    def test_delegates_to_function(self):
        calls = []

        def fn(df, row_index):
            calls.append((row_index, list(df.columns)))
            return {"a": True}

        labeler = CallableLabeler(fn)
        df = pd.DataFrame({"a": [1, 2]})
        assert labeler.label_tuple(df, 1) == {"a": True}
        assert calls == [(1, ["a"])]


class TestHeuristicLabeler:
    def test_majority_vote_over_fired_strategies(self):
        df = pd.DataFrame({"a": [1, 2]})
        features = ColumnFeatures(
            column_name="a",
            feature_names=("s1", "s2", "s3"),
            matrix=np.array([[1.0, 1.0, 0.0], [0.0, 0.0, 0.0]]),
        )
        labeler = HeuristicLabeler({"a": features}, threshold=0.5)
        assert labeler.label_tuple(df, 0) == {"a": True}
        assert labeler.label_tuple(df, 1) == {"a": False}

    def test_no_features_means_never_flagged(self):
        df = pd.DataFrame({"a": [1]})
        features = ColumnFeatures(column_name="a", feature_names=(), matrix=np.zeros((1, 0)))
        labeler = HeuristicLabeler({"a": features})
        assert labeler.label_tuple(df, 0) == {"a": False}

    def test_duplicate_index_labels_resolve_positionally(self):
        # BUG-10: ``df.index.get_loc()`` on a duplicate label returns a slice or
        # a boolean mask; indexing the feature matrix with that raw result
        # silently picks the wrong row. Resolve to a single position first.
        df = pd.DataFrame({"a": [1, 2, 3]}, index=[0, 0, 1])
        features = ColumnFeatures(
            column_name="a",
            feature_names=("s1",),
            matrix=np.array([[1.0], [0.0], [0.0]]),
        )
        labeler = HeuristicLabeler({"a": features}, threshold=0.5)
        assert labeler.label_tuple(df, 0) == {"a": True}
        assert labeler.label_tuple(df, 1) == {"a": False}


class TestPropagateLabels:
    def test_propagates_within_a_clean_cluster(self):
        cluster_ids = [0, 0, 1, 1]
        labeled = {0: False}
        result = propagate_labels(cluster_ids, labeled, "majority")
        assert result == {0: False, 1: False}

    def test_homogeneity_skips_contradicting_clusters(self):
        cluster_ids = [0, 0, 0]
        labeled = {0: True, 1: False}
        result = propagate_labels(cluster_ids, labeled, "homogeneity")
        # cluster 0 has contradicting user labels -> nothing propagates
        # beyond the two directly labeled cells.
        assert result == {0: True, 1: False}

    def test_majority_resolves_contradicting_clusters(self):
        cluster_ids = [0, 0, 0, 0]
        labeled = {0: True, 1: True, 2: False}
        result = propagate_labels(cluster_ids, labeled, "majority")
        assert result[3] is True  # 2 dirty votes vs 1 clean -> dirty wins
        assert result[0] is True and result[1] is True and result[2] is False

    def test_user_labels_always_take_precedence(self):
        cluster_ids = [0, 0]
        labeled = {0: True, 1: False}
        result = propagate_labels(cluster_ids, labeled, "majority")
        assert result == {0: True, 1: False}
