"""Clustering-based sampling (paper Section 4.3).

Two pieces of Algorithm 1's inner loop (lines 6-11) live here: cutting each
column's feature vectors into ``k`` clusters via hierarchical agglomerative
clustering, and drawing the next tuple to label with the softmax probability
of Equation (3).

The loop calls the cut step once per column on every iteration with a
strictly increasing ``k`` (``k = labeling_budget + 1`` at most). A column's
feature matrix never changes across those iterations, so
:class:`ColumnClusterState` splits clustering into a one-time "build" step
and a cheap, repeatable "cut to k clusters" step, instead of re-deriving the
whole clustering from scratch every iteration.

The build step also picks *how* to cluster based on row count. Exact
cosine-distance, average-linkage clustering needs a dense condensed
pairwise-distance array of ``n * (n - 1) / 2`` floats, which is
O(n^2) memory -- about 100MB at ``n=5,000`` but 149GiB at ``n=200,000``
(the size of the paper's own Tax benchmark). Past
``RahaConfig.dense_clustering_row_limit`` rows, this module switches to
spherical k-means (Euclidean k-means over L2-normalized rows) as a
sub-quadratic substitute: for unit vectors ``a``, ``b``,
``||a - b||^2 = 2 - 2*cos(a, b)``, so minimizing Euclidean distance between
normalized rows is equivalent to minimizing cosine distance between the
originals. The paper states that the choice of similarity metric and
linkage method "does not affect Raha's performance" (Section 4.3), so this
substitution preserves the algorithm's intent while dropping the memory
requirement to O(n).
"""

from __future__ import annotations

from abc import ABC, abstractmethod

import numpy as np
from scipy.cluster.hierarchy import fcluster, linkage
from scipy.spatial.distance import pdist

#: Default ceiling on rows for exact dense-pairwise-distance clustering.
#: Mirrors ``RahaConfig.dense_clustering_row_limit``; used only by the
#: backwards-compatible ``cluster_column`` helper below.
DEFAULT_DENSE_CLUSTERING_ROW_LIMIT = 5000


class ColumnClusterState(ABC):
    """Precomputed clustering state for one column's feature matrix.

    Build once per column via :func:`build_column_cluster_state` before
    Algorithm 1's labeling loop, then call :meth:`cut` for each ``k`` the
    loop visits.
    """

    @abstractmethod
    def cut(self, k: int) -> np.ndarray:
        """Return a 0-indexed cluster id per row for (up to) ``k`` clusters."""


class _ConstantClusterState(ColumnClusterState):
    """Every row is its own trivial singleton cluster (id 0)."""

    def __init__(self, n: int) -> None:
        self._n = n

    def cut(self, k: int) -> np.ndarray:  # noqa: ARG002 -- k is meaningless here
        return np.zeros(self._n, dtype=int)


class _HierarchicalClusterState(ColumnClusterState):
    """Exact cosine-distance, average-linkage clustering (paper default).

    ``linkage`` builds the full dendrogram once; cutting it at different
    ``k`` via :func:`scipy.cluster.hierarchy.fcluster` is O(n) per call, so
    repeated cuts across the labeling loop are cheap.
    """

    def __init__(self, linkage_matrix: np.ndarray) -> None:
        self._linkage_matrix = linkage_matrix

    def cut(self, k: int) -> np.ndarray:
        labels = fcluster(self._linkage_matrix, t=k, criterion="maxclust")
        return labels - 1


class _SphericalKMeansClusterState(ColumnClusterState):
    """Sub-quadratic approximation for tables past the dense-clustering limit.

    Refit per cut rather than reused/cached: ``MiniBatchKMeans`` is
    near-linear in ``n``, so refitting it at each of the (at most
    ``labeling_budget``) values of ``k`` the loop visits is still far
    cheaper than the O(n^2) memory a single dense pairwise-distance call
    would need at this scale.
    """

    def __init__(self, normalized: np.ndarray, random_state: int) -> None:
        self._normalized = normalized
        self._random_state = random_state

    def cut(self, k: int) -> np.ndarray:
        from sklearn.cluster import MiniBatchKMeans

        n = self._normalized.shape[0]
        k = max(1, min(k, n))
        if k == 1:
            return np.zeros(n, dtype=int)
        model = MiniBatchKMeans(n_clusters=k, random_state=self._random_state, n_init=3)
        return model.fit_predict(self._normalized)


def _augment(matrix: np.ndarray) -> np.ndarray:
    n = matrix.shape[0]
    # Append a constant column so no row is the all-zero vector: cosine
    # distance is undefined (0/0) between two all-zero rows -- a real
    # possibility here, since a "clean-looking" cell fires no strategy at
    # all -- and this keeps every pairwise distance finite while only
    # slightly damping separation between rows that do carry real signal.
    return np.hstack([matrix, np.ones((n, 1))])


def build_column_cluster_state(
    matrix: np.ndarray,
    *,
    dense_clustering_row_limit: int = DEFAULT_DENSE_CLUSTERING_ROW_LIMIT,
    random_state: int = 0,
) -> ColumnClusterState:
    """Precompute clustering state for one column's feature matrix.

    Call once per column before Algorithm 1's labeling loop; reuse the
    returned state's :meth:`ColumnClusterState.cut` for every ``k`` the loop
    visits instead of rebuilding it each iteration.
    """
    n = matrix.shape[0]
    if n == 0:
        return _ConstantClusterState(0)
    if n == 1 or matrix.shape[1] == 0:
        return _ConstantClusterState(n)

    augmented = _augment(matrix)
    if n <= dense_clustering_row_limit:
        distances = pdist(augmented, metric="cosine")
        linkage_matrix = linkage(distances, method="average")
        return _HierarchicalClusterState(linkage_matrix)

    norms = np.linalg.norm(augmented, axis=1, keepdims=True)
    normalized = augmented / norms
    return _SphericalKMeansClusterState(normalized, random_state)


def cluster_column(
    matrix: np.ndarray,
    k: int,
    *,
    dense_clustering_row_limit: int = DEFAULT_DENSE_CLUSTERING_ROW_LIMIT,
    random_state: int = 0,
) -> np.ndarray:
    """Cut a column's feature matrix into (up to) ``k`` clusters, one-shot.

    Uses cosine-distance, average-linkage hierarchical agglomerative
    clustering below ``dense_clustering_row_limit`` rows, and a
    sub-quadratic spherical k-means approximation above it -- see the
    module docstring. Returns a 0-indexed cluster id per row.

    Prefer :func:`build_column_cluster_state` plus repeated
    :meth:`ColumnClusterState.cut` when the same column is clustered at
    multiple values of ``k`` in a loop (as :class:`RahaDetector.detect`
    does) -- this function rebuilds the clustering state from scratch on
    every call.
    """
    state = build_column_cluster_state(
        matrix,
        dense_clustering_row_limit=dense_clustering_row_limit,
        random_state=random_state,
    )
    return state.cut(k)


def sample_tuple(
    cluster_ids_by_column: dict[str, np.ndarray],
    label_counts_by_cluster: dict[tuple[str, int], int],
    excluded_rows: set[int],
    rng: np.random.Generator,
) -> int | None:
    """Draw the next tuple to label per the softmax rule of Equation (3).

    ``P(t) = exp(sum_{c in t} exp(-N_c)) / sum_{t' in d} exp(sum_{c in t'} exp(-N_c))``,
    where ``N_c`` is the number of already-labeled cells in cell ``c``'s
    current cluster. This favors tuples whose cells mostly sit in
    under-labeled clusters, without deterministically chasing the single
    best-covering tuple (Section 4.3: probabilistic selection is "more
    resilient ... against local optima" than a greedy set-cover heuristic).

    Returns ``None`` if every row is already in ``excluded_rows``.
    """
    columns = list(cluster_ids_by_column.values())
    if not columns:
        return None
    n = len(columns[0])

    scores = np.zeros(n)
    for column_name, cluster_ids in cluster_ids_by_column.items():
        counts = np.array(
            [label_counts_by_cluster.get((column_name, cid), 0) for cid in cluster_ids]
        )
        scores += np.exp(-counts)

    candidates = np.array([i for i in range(n) if i not in excluded_rows])
    if candidates.size == 0:
        return None

    candidate_scores = scores[candidates]
    weights = np.exp(candidate_scores - candidate_scores.max())
    probabilities = weights / weights.sum()
    return int(rng.choice(candidates, p=probabilities))
