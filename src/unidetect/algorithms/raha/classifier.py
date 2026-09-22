"""Per-column classification (paper Section 4.4, Algorithm 1 lines 12-16).

Raha trains one classifier per data column -- "we want to identify errors at
the cell level, not at the tuple level. Thus, we need labels for each column"
(Section 4.3) -- on that column's feature vectors and the labels obtained
from :mod:`unidetect.algorithms.raha.labeling`'s propagation step, then uses
it to predict every remaining cell in the column.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from unidetect.algorithms.raha.config import RahaConfig
from unidetect.algorithms.raha.features import ColumnFeatures


@dataclass(frozen=True, slots=True)
class ColumnPredictions:
    """Per-row predictions for one column. ``score`` is ``P(dirty)`` in ``[0, 1]``."""

    column_name: str
    is_error: np.ndarray
    score: np.ndarray


def train_and_predict(
    column_features: ColumnFeatures, labels: dict[int, bool], config: RahaConfig
) -> ColumnPredictions:
    """Fit ``m_j`` on the labeled rows and predict every row of the column.

    Falls back to the labeled rows' majority vote (skipping the classifier
    entirely) when there is nothing to learn from: no labels at all, no
    informative features for this column, or every label belongs to a single
    class (most classifiers, including the paper's default Gradient
    Boosting, require at least two classes to fit).
    """
    n = column_features.matrix.shape[0]
    if not labels:
        return ColumnPredictions(column_features.column_name, np.zeros(n, dtype=bool), np.zeros(n))

    rows = np.array(sorted(labels))
    y = np.array([int(labels[r]) for r in rows])
    x_labeled = column_features.matrix[rows]

    if column_features.matrix.shape[1] == 0 or len(np.unique(y)) < 2:
        majority = bool(y.mean() >= 0.5)
        score = float(y.mean())
        return ColumnPredictions(
            column_features.column_name, np.full(n, majority), np.full(n, score)
        )

    classifier = config.classifier_factory()
    classifier.fit(x_labeled, y)
    probabilities = classifier.predict_proba(column_features.matrix)
    dirty_index = list(classifier.classes_).index(1)
    scores = probabilities[:, dirty_index]
    return ColumnPredictions(column_features.column_name, scores >= 0.5, scores)
