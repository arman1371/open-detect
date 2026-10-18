"""Unit tests for algorithms/raha/classifier.py."""

from __future__ import annotations

import numpy as np

from open_detect.algorithms.raha.classifier import train_and_predict
from open_detect.algorithms.raha.config import RahaConfig
from open_detect.algorithms.raha.features import ColumnFeatures


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


class TestDeterminismAndSeeding:
    def test_same_config_data_labels_produce_identical_predictions(self):
        # B-M6: the default classifier is seeded from RahaConfig.random_state,
        # so two runs with the same config/data/labels are bit-for-bit equal.
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
        config = RahaConfig(random_state=0)
        first = train_and_predict(features, labels, config)
        second = train_and_predict(features, labels, config)
        assert np.array_equal(first.is_error, second.is_error)
        assert np.array_equal(first.score, second.score)

    def test_zero_argument_factory_is_called_without_random_state(self):
        # B-M6: user-supplied factories that take no arguments must keep
        # working (additive/backwards-compatible) -- they are NOT passed
        # random_state, which would break a zero-arg factory.
        from open_detect.algorithms.raha.classifier import _make_classifier

        sentinel = object()

        def factory():
            return sentinel

        assert _make_classifier(factory, random_state=0) is sentinel

    def test_random_state_aware_factory_is_seeded(self):
        from open_detect.algorithms.raha.classifier import _make_classifier

        seen = {}

        def factory(random_state):
            seen["random_state"] = random_state
            return object()

        _make_classifier(factory, random_state=7)
        assert seen == {"random_state": 7}
