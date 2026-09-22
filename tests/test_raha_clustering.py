"""Unit tests for algorithms/raha/clustering.py."""

from __future__ import annotations

import numpy as np

from unidetect.algorithms.raha.clustering import cluster_column, sample_tuple


class TestClusterColumn:
    def test_empty_matrix(self):
        assert cluster_column(np.zeros((0, 3)), k=2).shape == (0,)

    def test_single_row(self):
        assert list(cluster_column(np.array([[1.0, 0.0]]), k=2)) == [0]

    def test_zero_features_collapses_to_one_cluster(self):
        result = cluster_column(np.zeros((5, 0)), k=3)
        assert (result == 0).all()

    def test_separates_dissimilar_rows(self):
        matrix = np.array(
            [
                [1.0, 0.0, 0.0],
                [1.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
                [0.0, 1.0, 0.0],
            ]
        )
        labels = cluster_column(matrix, k=2)
        assert labels[0] == labels[1]
        assert labels[2] == labels[3]
        assert labels[0] != labels[2]

    def test_k_capped_at_row_count(self):
        matrix = np.eye(3)
        labels = cluster_column(matrix, k=100)
        assert len(set(labels.tolist())) <= 3

    def test_handles_all_zero_rows_without_nan(self):
        # A row with no strategy firing is the literal zero vector; cosine
        # distance to it must not blow up into NaN clusters.
        matrix = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 0.0]])
        labels = cluster_column(matrix, k=2)
        assert not np.isnan(labels).any()


class TestSampleTuple:
    def test_returns_none_when_all_excluded(self):
        rng = np.random.default_rng(0)
        ids = {"a": np.array([0, 0, 1])}
        assert sample_tuple(ids, {}, excluded_rows={0, 1, 2}, rng=rng) is None

    def test_never_returns_excluded_row(self):
        rng = np.random.default_rng(0)
        ids = {"a": np.array([0, 1, 1])}
        for _ in range(20):
            result = sample_tuple(ids, {}, excluded_rows={0}, rng=rng)
            assert result in (1, 2)

    def test_favors_under_labeled_clusters(self):
        # Cluster 0 (rows 0, 1) is already fully labeled; cluster 1 (rows 2,
        # 3) has no labels yet -- the sampler should draw from cluster 1
        # far more often than chance.
        rng = np.random.default_rng(0)
        ids = {"a": np.array([0, 0, 1, 1])}
        label_counts = {("a", 0): 10}
        draws = [sample_tuple(ids, label_counts, excluded_rows=set(), rng=rng) for _ in range(200)]
        assert sum(d in (2, 3) for d in draws) > 150
