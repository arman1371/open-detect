"""Unit test for algorithms/raha/clustering.py."""

from __future__ import annotations

import numpy as np

from open_detect.algorithms.raha.clustering import (
    cluster_column,
    compute_linkage,
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

    def test_precomputed_linkage_matches_recompute(self):
        # The fast path (passing a precomputed linkage matrix) must produce
        # byte-identical clusters to the slow path that recomputes
        # pdist+linkage every call, for every k the labeling loop uses.
        rng = np.random.default_rng(42)
        matrix = rng.standard_normal((500, 8))
        linkage_obj = compute_linkage(matrix)
        for k in (2, 3, 5, 10, 500):
            old = cluster_column(matrix, k)
            new = cluster_column(matrix, k, linkage_matrix=linkage_obj)
            assert np.array_equal(old, new), f"k={k}: fast/slow paths diverge"

    def test_precomputed_linkage_matches_recompute_on_edge_cases(self):
        for matrix in (
            np.zeros((0, 3)),
            np.array([[1.0, 0.0]]),
            np.zeros((5, 0)),
            np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 0.0]]),
        ):
            linkage_obj = compute_linkage(matrix)
            for k in (2, 3):
                old = cluster_column(matrix, k)
                new = cluster_column(matrix, k, linkage_matrix=linkage_obj)
                assert np.array_equal(old, new), f"edge case {matrix.shape} k={k} diverges"


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

    def test_matches_reference_distribution(self):
        # The vectorised implementation must draw from exactly the same
        # distribution as the reference row-wise loop, for fixed RNG state.
        rng = np.random.default_rng(0)
        ids = {
            "a": rng.integers(0, 5, 100),
            "b": rng.integers(0, 4, 100),
            "c": rng.integers(0, 6, 100),
        }
        label_counts = {
            (col, cid): int(rng.integers(0, 8))
            for col in ids
            for cid in range(6)
        }
        excluded = set(rng.choice(100, 10, replace=False))

        def reference(ids, counts, excluded, rng):
            columns = list(ids.values())
            if not columns:
                return None
            n = len(columns[0])
            scores = np.zeros(n)
            for column_name, cluster_ids in ids.items():
                c = np.array([counts.get((column_name, cid), 0) for cid in cluster_ids])
                scores += np.exp(-c)
            candidates = np.array([i for i in range(n) if i not in excluded])
            if candidates.size == 0:
                return None
            candidate_scores = scores[candidates]
            weights = np.exp(candidate_scores - candidate_scores.max())
            probabilities = weights / weights.sum()
            return int(rng.choice(candidates, p=probabilities))

        rng1 = np.random.default_rng(7)
        rng2 = np.random.default_rng(7)
        assert reference(ids, label_counts, excluded, rng1) == sample_tuple(
            ids, label_counts, excluded, rng2
        )