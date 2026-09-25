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


class TestDefaultClassifierSeeding:
    """Regression tests for the unseeded-GradientBoostingClassifier defect.

    ``RahaConfig.random_state`` must reach the default classifier, not just
    clustering and label sampling, or repeated runs of the same config drift
    (see OPE-17).
    """

    def test_default_classifier_is_seeded_from_config(self):
        classifier = RahaConfig(random_state=7).classifier_factory()
        assert classifier.random_state == 7

    def test_default_classifier_factory_is_deterministic(self):
        first = RahaConfig(random_state=3).classifier_factory()
        second = RahaConfig(random_state=3).classifier_factory()
        assert first.random_state == second.random_state == 3

    def test_custom_classifier_factory_is_not_reseeded(self):
        def custom_factory():
            from sklearn.tree import DecisionTreeClassifier

            return DecisionTreeClassifier(random_state=99)

        config = RahaConfig(random_state=0, classifier_factory=custom_factory)
        assert config.classifier_factory is custom_factory
        assert config.classifier_factory().random_state == 99

    def test_train_and_predict_is_reproducible_across_runs(self):
        # A larger, noisier fixture than test_learns_a_separating_feature so
        # GradientBoostingClassifier's internal subsampling/feature
        # selection has room to diverge between runs when unseeded.
        rng = np.random.default_rng(42)
        matrix = rng.normal(size=(60, 5))
        matrix[30:, :] += 2.0  # second half is separable from the first
        features = _features(matrix)
        labels = {i: (i >= 30) for i in range(0, 60, 3)}

        config = RahaConfig(random_state=0)
        first = train_and_predict(features, labels, config)
        second = train_and_predict(features, dict(labels), RahaConfig(random_state=0))

        np.testing.assert_array_equal(first.is_error, second.is_error)
        np.testing.assert_allclose(first.score, second.score)
