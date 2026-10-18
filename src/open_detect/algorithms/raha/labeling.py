"""Labeling (paper Appendix C) and label propagation through clusters (Section 4.4).

Raha is semi-supervised: it needs a human (or an oracle) to label a handful
of sampled tuples. :class:`Labeler` is the pluggable interface for that --
implement it to wire up a UI, a CLI prompt, or (for evaluation/benchmarking)
a comparison against known-clean ground truth.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections import defaultdict
from collections.abc import Callable
from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    import pandas as pd

    from open_detect.algorithms.raha.features import ColumnFeatures


def _values_equal(a: object, b: object) -> bool:
    """dtype-normalised cell equality for ground-truth labeling (BUG-10).

    ``normalize_to_str`` maps every null-like value to ``NULL_SENTINEL``, so a
    null cell compares equal to another null cell and unequal to any real
    value. Two real values compare equal iff they are numerically equal
    (``'5'`` vs ``'5.0'``, ``1`` vs ``1.0``) -- plain ``str()`` comparison
    would mark those as dirty, which is the BUG-10 false label. Values that
    are not numeric at all fall back to string equality.
    """
    from open_detect.algorithms.raha.strategies import NULL_SENTINEL

    a_null = a == NULL_SENTINEL
    b_null = b == NULL_SENTINEL
    if a_null and b_null:
        return True
    if a_null or b_null:
        return False
    try:
        return float(a) == float(b)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return str(a) == str(b)


def _resolve_position(index: pd.Index, row_index: object) -> int:
    """Map a row *label* to its positional index (BUG-10).

    ``df.loc[[row_index]]`` returns every row whose label equals ``row_index``
    and then ``.iloc[0]`` silently picks the first one, which is wrong when
    the index has duplicate labels. ``get_loc`` returns an int for unique
    labels, a slice for contiguous duplicates, and a boolean mask otherwise;
    the slice/mask cases are resolved to the first matching position, which
    is the position ``label_tuple`` is asked about.
    """
    loc = index.get_loc(row_index)
    if isinstance(loc, int):
        return loc
    if isinstance(loc, slice):
        return loc.start
    return int(np.nonzero(loc)[0][0])


class Labeler(ABC):
    """Supplies the ``dirty``/``clean`` label for every cell of a sampled tuple."""

    @abstractmethod
    def label_tuple(self, df: pd.DataFrame, row_index: int) -> dict[str, bool]:
        """Return ``{column_name: is_error}`` for every column of ``df.loc[row_index]``."""


class GroundTruthLabeler(Labeler):
    """Labels a cell by comparing it against a known-clean version of the table.

    Intended for benchmarking/evaluation (as in ``benchmarks/``, where a
    ``clean.csv`` is already available) and for programmatic pipelines that
    already know which cells are wrong -- not for genuine "we don't know the
    errors yet" use, which is what :class:`CallableLabeler` or
    :class:`HeuristicLabeler` are for.
    """

    def __init__(self, clean_df: pd.DataFrame) -> None:
        self._clean_df = clean_df

    def label_tuple(self, df: pd.DataFrame, row_index: int) -> dict[str, bool]:
        from open_detect.algorithms.raha.strategies import normalize_to_str

        # Positional access: ``row_index`` is a *label*, and ``df.loc[[row_index]]``
        # misbehaves on duplicate index labels (BUG-10) -- it returns every
        # matching row, so ``.iloc[0]`` silently picks the first one. Resolve
        # the position once with ``get_loc`` and index by position everywhere.
        position = _resolve_position(df.index, row_index)
        dirty_row = normalize_to_str(df.iloc[[position]]).iloc[0]
        clean_row = normalize_to_str(self._clean_df.iloc[[position]]).iloc[0]
        return {col: not _values_equal(dirty_row[col], clean_row.get(col)) for col in df.columns}


class CallableLabeler(Labeler):
    """Wraps a plain function as a :class:`Labeler` -- the interactive/UI escape hatch.

    ``fn`` receives ``(df, row_index)`` (the same arguments as
    :meth:`Labeler.label_tuple`) and must return ``{column_name: is_error}``;
    this is where a real deployment plugs in a human labeler (a CLI prompt, a
    web form, a Slack message) without Raha's pipeline code needing to know
    about it.
    """

    def __init__(self, fn: Callable[[pd.DataFrame, int], dict[str, bool]]) -> None:
        self._fn = fn

    def label_tuple(self, df: pd.DataFrame, row_index: int) -> dict[str, bool]:
        return self._fn(df, row_index)


class HeuristicLabeler(Labeler):
    """No-human fallback: labels a cell by majority vote of its own feature vector.

    Deviation from the paper: Raha is designed around genuine human labels: a
    handful of tuples a person actually inspects (``labels = 20`` in the
    paper's own experiments), which is what makes its clusters and classifier
    trustworthy. This heuristic lets the pipeline still run end-to-end with
    zero user interaction -- useful for a first unsupervised pass or for
    tests -- but it is strictly weaker: a cell is only "labeled" here because
    a majority of the very strategies feeding the classifier already flagged
    it, so it mostly reinforces what those strategies already say rather than
    contributing new information. Supply a real :class:`Labeler`
    (:class:`CallableLabeler` wired to a person, or :class:`GroundTruthLabeler`
    for evaluation) for results matching the paper.
    """

    def __init__(self, column_features: dict[str, ColumnFeatures], threshold: float = 0.5) -> None:
        self._column_features = column_features
        self._threshold = threshold

    def label_tuple(self, df: pd.DataFrame, row_index: int) -> dict[str, bool]:
        position = _resolve_position(df.index, row_index)
        labels: dict[str, bool] = {}
        for column_name, column_features in self._column_features.items():
            if column_features.matrix.shape[1] == 0:
                labels[column_name] = False
                continue
            vote = column_features.matrix[position].mean()
            labels[column_name] = bool(vote >= self._threshold)
        return labels


def propagate_labels(
    cluster_ids: object,
    labeled_cells: dict[int, bool],
    conflict_resolution: str,
) -> dict[int, bool]:
    """Propagate a column's user labels to the rest of their clusters (Section 4.4).

    Every unlabeled cell in the same cluster as a labeled cell inherits that
    cluster's resolved label. ``conflict_resolution`` picks how a cluster
    with contradicting user labels is resolved:

    - ``"homogeneity"``: only propagate through clusters with no
      contradicting labels; leave mixed clusters unlabeled.
    - ``"majority"``: also propagate through mixed clusters, using whichever
      label has more votes (ties resolve to dirty, the conservative choice
      for a class-imbalanced error-detection task).

    User labels always take precedence over the propagated ("noisy") label
    for their own cell, per Section 4.4: ``L' = {user labels} U {propagated}``.
    """
    import numpy as np

    cluster_ids = np.asarray(cluster_ids)
    cluster_votes: dict[int, list[bool]] = defaultdict(list)
    for row, label in labeled_cells.items():
        cluster_votes[int(cluster_ids[row])].append(label)

    cluster_label: dict[int, bool] = {}
    for cid, votes in cluster_votes.items():
        n_dirty = sum(votes)
        n_clean = len(votes) - n_dirty
        if conflict_resolution == "homogeneity":
            if n_dirty and n_clean:
                continue
            cluster_label[cid] = n_dirty > 0
        else:
            cluster_label[cid] = n_dirty >= n_clean

    propagated = {
        row: cluster_label[cid] for row, cid in enumerate(cluster_ids) if cid in cluster_label
    }
    propagated.update(labeled_cells)
    return propagated
