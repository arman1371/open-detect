"""Unit tests for algorithms/raha/classifier.py."""

from __future__ import annotations

import numpy as np

from unidetect.algorithms.raha.classifier import train_and_predict
from unidetect.algorithms.raha.config import RahaConfig
from unidetect.algorithms.raha.features import ColumnFeatures


def _features(matrix: np.ndarray, names: tuple[str, ...] | None = None) -> ColumnFeatures:
    names = names or tuple(f"s{i}" for i in range(matrix.shape[1]))
    return ColumnFeatures(column_name="col", feature_names=names, matrix=matrix)


class TestDegenerateCases:
    def test_no_labels_predicts_all_clean(self):
        features = _features(np.array([[1.0], [0.0]]))
        result = train_and_predict(features, {}, RahaConfig())
        assert not result.is_error.any()
        assert (result.score == 0.0).all()

    def test_single_class_labels_fall_back_to_majority(self):
        features = _features(np.array([[1.0], [0.0], [1.0], [0.0]]))
        result = train_and_predict(features, {0: False, 1: False}, RahaConfig())
        assert not result.is_error.any()

    def test_no_informative_features_falls_back_to_majority(self):
        features = _features(np.zeros((3, 0)))
        result = train_and_predict(features, {0: True, 1: False}, RahaConfig())
        # majority of the 2 known labels is a tie -> falls back to "dirty"
        # via the >= 0.5 mean rule (1 dirty, 1 clean -> mean 0.5).
        assert result.is_error[2] == (result.score[2] >= 0.5)


class TestClassifierTrainingPath:
    def test_learns_a_separating_feature(self):
        matrix = np.array(
            [
                [1.0, 0.0],
                [1.0, 0.0],
                [1.0, 0.0],
                [0.0, 1.0],
                [0.0, 1.0],
                [0.0, 1.0],
            ]
        )
        features = _features(matrix)
        labels = {0: True, 1: True, 3: False, 4: False}
        result = train_and_predict(features, labels, RahaConfig(random_state=0))
        # Rows 2 and 5 were never directly labeled but share their feature
        # pattern with a labeled row of the same class.
        assert result.is_error[2]
        assert not result.is_error[5]
        assert result.score.shape == (6,)
