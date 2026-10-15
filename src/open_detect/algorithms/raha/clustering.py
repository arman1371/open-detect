"""Clustering-based sampling (paper Section 4.3).

Two pieces of Algorithm 1's inner loop (lines 6-11) live here: cutting each
column's feature vectors into ``k`` clusters via hierarchical agglomerative
clustering, and drawing the next tuple to label with the softmax probability
of Equation (3).
"""

from __future__ import annotations

import numpy as np
from scipy.cluster.hierarchy import fcluster, linkage as _linkage
from scipy.spatial.distance import pdist


def compute_linkage(matrix: np.ndarray) -> np.ndarray:
    """Compute the linkage matrix for a column feature matrix.

    Returns the minimal linkage needed so ``fcluster`` still behaves
    correctly downstream.  Edge cases (empty, single-row, all-zero features)
    return a degenerate linkage matrix.
    """
    n = matrix.shape[0]
    if n == 0:
        return np.array([]).reshape(0, 3)
    if n == 1 or matrix.shape[1] == 0:
        return np.array([[0.0, 1.0, 0.0, 1.0]])

    augmented = np.hstack([matrix, np.ones((n, 1))])
    distances = pdist(augmented, metric="cosine")
    linkage_matrix = _linkage(distances, method="average")
    return linkage_matrix


def cluster_column(
    matrix: np.ndarray,
    k: int,
    *,
    linkage_matrix: np.ndarray | None = None,
) -> np.ndarray:
    """Cut a column's feature matrix into (up to) ``k`` clusters.

    Uses cosine-distance, average-linkage hierarchical agglomerative
    clustering, "as the choice of the similarity metric and the linkage
    method does not affect Raha's performance" (Section 4.3). Returns a
    0-indexed cluster id per row.

    Parameters
    ----------
    matrix : np.ndarray
        The feature matrix for one column (rows=tuples).
    k : int
        Desired number of clusters.
    linkage_matrix : np.ndarray, optional
        Precomputed linkage matrix (from :func:`compute_linkage`).
        When supplied, ``pdist`` and ``linkage`` are skipped and only
        ``fcluster`` is invoked -- this is the fast path used inside the
        labeling loop where ``k`` grows but the matrix does not.
    """
    n = matrix.shape[0]
    if n == 0:
        return np.zeros(0, dtype=int)
    if n == 1 or matrix.shape[1] == 0:
        return np.zeros(n, dtype=int)

    k = max(1, min(k, n))
    if linkage_matrix is None:
        # Append a constant column so no row is the all-zero vector: cosine
        # distance is undefined (0/0) between two all-zero rows -- a real
        # possibility here, since a "clean-looking" cell fires no strategy at
        # all -- and this keeps every pairwise distance finite while only
        # slightly damping separation between rows that do carry real signal.
        augmented = np.hstack([matrix, np.ones((n, 1))])
        distances = pdist(augmented, metric="cosine")
        linkage_matrix = _linkage(distances, method="average")

    labels = fcluster(linkage_matrix, t=k, criterion="maxclust")
    return labels - 1


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
    if not cluster_ids_by_column:
        return None
    n = len(next(iter(cluster_ids_by_column.values())))

    # Vectorised: for each column, build a fast lookup array from the
    # sparse label_counts dict (most entries are 0), then index into it
    # with that column's cluster_ids. Summing exp(-count) across columns
    # gives the unnormalised log-probability per tuple.
    scores = np.zeros(n, dtype=float)
    for col_name, cluster_ids in cluster_ids_by_column.items():
        if cluster_ids.size == 0:
            continue
        max_cid = int(cluster_ids.max())
        lookup = np.zeros(max_cid + 1, dtype=float)
        for cid in range(max_cid + 1):
            lookup[cid] = label_counts_by_cluster.get((col_name, cid), 0)
        col_counts = lookup[cluster_ids]
        scores += np.exp(-col_counts)

    candidates = np.array([i for i in range(n) if i not in excluded_rows])
    if candidates.size == 0:
        return None

    candidate_scores = scores[candidates]
    weights = np.exp(candidate_scores - candidate_scores.max())
    probabilities = weights / weights.sum()
    return int(rng.choice(candidates, p=probabilities))