"""Unit tests for algorithms/raha/clustering.py."""

from __future__ import annotations

import numpy as np

from unidetect.algorithms.raha.clustering import (
    build_column_cluster_state,
    cluster_column,
    sample_tuple,
)


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


class TestBuildColumnClusterState:
    """Covers OPE-22: dense pairwise-distance clustering is O(n^2) memory
    and crashed on realistically-sized tables (149GiB for a 200,000-row
    column). ``dense_clustering_row_limit`` is exercised here at a tiny
    threshold so the sub-quadratic fallback path is reached deterministically
    and cheaply, without needing an actual 200,000-row fixture.
    """

    def test_matches_hierarchical_result_below_the_limit(self):
        # Below the limit, build+cut must reproduce exact cluster_column
        # output bit-for-bit -- no behavior change for any table this
        # package currently benchmarks (all far below the 5,000-row default).
        matrix = np.array(
            [
                [1.0, 0.0, 0.0],
                [1.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
                [0.0, 1.0, 0.0],
            ]
        )
        state = build_column_cluster_state(matrix, dense_clustering_row_limit=5000)
        assert list(state.cut(2)) == list(cluster_column(matrix, k=2))

    def test_falls_back_above_the_limit_without_crashing(self):
        rng = np.random.default_rng(0)
        # Two well-separated blobs, large enough to trigger the fallback
        # at a small test-only limit but tiny next to the 200,000-row
        # dataset that crashed the old dense-pdist implementation.
        block_a = rng.normal(loc=0.0, scale=0.01, size=(30, 4)) + np.array([1.0, 0.0, 0.0, 0.0])
        block_b = rng.normal(loc=0.0, scale=0.01, size=(30, 4)) + np.array([0.0, 1.0, 0.0, 0.0])
        matrix = np.vstack([block_a, block_b])

        state = build_column_cluster_state(matrix, dense_clustering_row_limit=10, random_state=0)
        labels = state.cut(2)

        assert labels.shape == (60,)
        assert not np.isnan(labels).any()
        # The two blobs should land in different clusters far more often
        # than not -- this is an approximation, not an exactness guarantee.
        assert (labels[:30] == labels[0]).mean() > 0.8
        assert (labels[30:] == labels[30]).mean() > 0.8
        assert labels[0] != labels[30]

    def test_reused_state_answers_increasing_k_without_rebuilding(self):
        # Mirrors RahaDetector.detect's loop: build once, cut at k=2,3,4,...
        matrix = np.eye(5)
        state = build_column_cluster_state(matrix, dense_clustering_row_limit=5000)
        for k in (2, 3, 4, 5):
            labels = state.cut(k)
            assert labels.shape == (5,)
            assert len(set(labels.tolist())) <= k

    def test_empty_and_singleton_columns_ignore_the_limit(self):
        assert build_column_cluster_state(np.zeros((0, 3)), dense_clustering_row_limit=1).cut(
            2
        ).shape == (0,)
        assert list(
            build_column_cluster_state(np.array([[1.0, 0.0]]), dense_clustering_row_limit=1).cut(2)
        ) == [0]


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
