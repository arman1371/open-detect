"""Tunable knobs for the Raha algorithm.

Mirrors the paper's own default parameter setting (Section 6.1) unless noted.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from open_detect.exceptions import ConfigurationError

if TYPE_CHECKING:
    from sklearn.base import ClassifierMixin

    #: A classifier factory is any callable returning a fresh, unfitted
    #: scikit-learn classifier. Two signatures are accepted (B-M6):
    #: ``() -> ClassifierMixin`` (legacy zero-argument form) and
    #: ``(random_state: int | None) -> ClassifierMixin`` (random_state-aware
    #: form). The default factory below uses the second form and is seeded
    #: from :attr:`RahaConfig.random_state`.
    ClassifierFactory = Callable[..., ClassifierMixin]

#: Term-frequency thresholds for the histogram outlier strategy (Section 4.1).
DEFAULT_TF_THRESHOLDS: tuple[float, ...] = (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9)

#: Distance-from-mean thresholds (in std devs) for the Gaussian outlier
#: strategy, per the paper's 68-95-99.7 rule (Section 4.1).
DEFAULT_DIST_THRESHOLDS: tuple[float, ...] = (1, 1.3, 1.5, 1.7, 2, 2.3, 2.5, 2.7, 3)


def _default_classifier_factory(random_state: int | None = None) -> ClassifierMixin:
    """The paper's default classifier (Section 6.1: "We use Gradient Boosting").

    Accepts an optional ``random_state`` so the default factory can be seeded
    from :attr:`RahaConfig.random_state` (B-M6). When ``random_state`` is
    ``None`` the classifier is left unseeded, preserving the historical
    behaviour for callers that pass a zero-argument factory.
    """
    from sklearn.ensemble import GradientBoostingClassifier

    if random_state is None:
        return GradientBoostingClassifier()
    return GradientBoostingClassifier(random_state=random_state)


@dataclass(frozen=True)
class RahaConfig:
    """Configuration for :class:`~open_detect.algorithms.raha.detector.RahaDetector`.

    Parameters
    ----------
    labeling_budget:
        ``lambda_labels`` in the paper (Algorithm 1) -- the number of tuples
        the labeler is asked to annotate. Also determines the final number of
        clusters per column, ``k = labeling_budget + 1`` (Section 4.3).
    tf_thresholds, dist_thresholds:
        Parameter grids for the histogram and Gaussian outlier strategies
        (Section 4.1). Overridable mainly for faster tests.
    conflict_resolution:
        Which rule resolves clusters with contradicting user labels when
        propagating them (Section 4.4): ``"homogeneity"`` only propagates
        through clusters with no contradicting labels; ``"majority"`` also
        propagates through mixed clusters using the majority label.
    max_pattern_characters:
        Cap on the number of distinct characters the bag-of-characters
        pattern-violation strategy (Section 4.1) generates one strategy per;
        the paper's scheme is one strategy per distinct character in a
        column, which is unbounded for free-text columns. The most frequent
        characters are kept, since a rare character already tends to be
        exposed by the histogram outlier strategies on the whole value.
    classifier_factory:
        Callable returning a fresh, unfitted scikit-learn classifier, called
        once per column. Defaults to ``GradientBoostingClassifier``, the
        paper's own default. Accepts either a zero-argument factory or a
        ``random_state``-aware one (B-M6): the default factory is seeded from
        ``random_state``, user-supplied zero-argument factories keep working.
    random_state:
        Seeds clustering, the probabilistic tuple sampler (Equation 3), and
        the default classifier, so two runs with the same config/data/labels
        produce identical predictions (B-M6 determinism).
    """

    labeling_budget: int = 20
    tf_thresholds: tuple[float, ...] = field(default_factory=lambda: DEFAULT_TF_THRESHOLDS)
    dist_thresholds: tuple[float, ...] = field(default_factory=lambda: DEFAULT_DIST_THRESHOLDS)
    conflict_resolution: str = "majority"
    max_pattern_characters: int = 128
    classifier_factory: ClassifierFactory = field(
        default_factory=lambda: _default_classifier_factory
    )
    random_state: int = 0

    def __post_init__(self) -> None:
        if self.labeling_budget < 1:
            raise ConfigurationError(f"labeling_budget must be >= 1, got {self.labeling_budget}")
        if not self.tf_thresholds or any(not 0 < t < 1 for t in self.tf_thresholds):
            raise ConfigurationError("tf_thresholds must be non-empty values in (0, 1)")
        if not self.dist_thresholds or any(t <= 0 for t in self.dist_thresholds):
            raise ConfigurationError("dist_thresholds must be non-empty positive values")
        if self.conflict_resolution not in ("homogeneity", "majority"):
            raise ConfigurationError(
                "conflict_resolution must be 'homogeneity' or 'majority', "
                f"got {self.conflict_resolution!r}"
            )
        if self.max_pattern_characters < 1:
            raise ConfigurationError("max_pattern_characters must be >= 1")
