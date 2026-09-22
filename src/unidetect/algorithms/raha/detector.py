"""Raha: A Configuration-Free Error Detection System.

Implementation of:
    Mohammad Mahdavi, Ziawasch Abedjan, Raul Castro Fernandez, Samuel Madden,
    Mourad Ouzzani, Michael Stonebraker, Nan Tang. "Raha: A Configuration-Free
    Error Detection System." SIGMOD 2019.

:class:`RahaDetector` is Algorithm 1 end-to-end: configure error detection
strategies, build feature vectors, iteratively cluster and sample tuples for
labeling, propagate labels through clusters, and train a per-column
classifier to predict the rest. See ``ARCHITECTURE.md`` for how each part of
the paper maps onto this package's modules.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import numpy as np

from unidetect.algorithms.base import AlgorithmResult, CellResult, ErrorDetectionAlgorithm
from unidetect.algorithms.raha.classifier import train_and_predict
from unidetect.algorithms.raha.clustering import cluster_column, sample_tuple
from unidetect.algorithms.raha.config import RahaConfig
from unidetect.algorithms.raha.features import build_all_features
from unidetect.algorithms.raha.labeling import HeuristicLabeler, Labeler, propagate_labels
from unidetect.logging_utils import get_logger, log_duration

if TYPE_CHECKING:
    import pandas as pd

logger = get_logger(__name__)


class RahaDetector(ErrorDetectionAlgorithm):
    """Registered as ``"raha"`` in :mod:`unidetect.algorithms`."""

    name = "raha"

    def __init__(self, config: RahaConfig | None = None) -> None:
        self.config = config or RahaConfig()

    def detect(
        self,
        data: pd.DataFrame,
        *,
        table_id: str = "table",
        labeler: Labeler | None = None,
        **kwargs: Any,
    ) -> AlgorithmResult:
        """Run Algorithm 1 against a single in-memory table.

        Parameters
        ----------
        data:
            The (dirty) table to scan, as a ``pandas.DataFrame``. Unlike
            Uni-Detect, Raha needs no background corpus -- it learns entirely
            from ``data`` itself plus a handful of labels.
        table_id:
            Stamped onto every result cell; purely descriptive.
        labeler:
            Answers "is this cell dirty?" for the tuples Raha samples
            (Section 4.3). Defaults to :class:`~unidetect.algorithms.raha.labeling.HeuristicLabeler`,
            a no-human fallback documented as a deviation from the paper in
            its own docstring -- pass a :class:`~unidetect.algorithms.raha.labeling.GroundTruthLabeler`
            (evaluation) or :class:`~unidetect.algorithms.raha.labeling.CallableLabeler`
            (a real human/UI) for results matching the paper.
        """
        df = data
        n = len(df)
        if n == 0 or df.shape[1] == 0:
            return AlgorithmResult(algorithm=self.name, cells=())

        with log_duration(logger, "raha.detect"):
            rng = np.random.default_rng(self.config.random_state)
            column_features = build_all_features(df, self.config)
            active_labeler = labeler or HeuristicLabeler(column_features)

            per_column_labels: dict[str, dict[int, bool]] = {col: {} for col in df.columns}
            labeled_rows: set[int] = set()
            budget = min(self.config.labeling_budget, n)
            k = 2
            cluster_ids_by_column: dict[str, np.ndarray] = {}

            while len(labeled_rows) < budget:
                cluster_ids_by_column = {
                    col: cluster_column(column_features[col].matrix, k) for col in df.columns
                }
                label_counts: dict[tuple[str, int], int] = {}
                for col, ids in cluster_ids_by_column.items():
                    for row, _label in per_column_labels[col].items():
                        key = (col, int(ids[row]))
                        label_counts[key] = label_counts.get(key, 0) + 1

                position = sample_tuple(cluster_ids_by_column, label_counts, labeled_rows, rng)
                if position is None:
                    break

                row_labels = active_labeler.label_tuple(df, df.index[position])
                for col, is_error in row_labels.items():
                    per_column_labels[col][position] = bool(is_error)
                labeled_rows.add(position)
                k += 1

            cells: list[CellResult] = []
            for col in df.columns:
                propagated = propagate_labels(
                    cluster_ids_by_column[col],
                    per_column_labels[col],
                    self.config.conflict_resolution,
                )
                predictions = train_and_predict(column_features[col], propagated, self.config)
                feature_names = column_features[col].feature_names
                matrix = column_features[col].matrix
                for position in range(n):
                    if position in per_column_labels[col]:
                        source = "user_label"
                        is_error = per_column_labels[col][position]
                        score = 1.0 if is_error else 0.0
                    elif position in propagated:
                        source = "propagated"
                        is_error = propagated[position]
                        score = 1.0 if is_error else 0.0
                    else:
                        source = "classifier"
                        is_error = bool(predictions.is_error[position])
                        score = float(predictions.score[position])

                    fired = [
                        name
                        for name, flagged in zip(feature_names, matrix[position], strict=True)
                        if flagged
                    ]
                    cells.append(
                        CellResult(
                            table_id=table_id,
                            row_index=df.index[position],
                            column_name=col,
                            algorithm=self.name,
                            is_error=is_error,
                            score=score,
                            evidence={"source": source, "fired_strategies": fired},
                        )
                    )

            return AlgorithmResult(algorithm=self.name, cells=tuple(cells))
