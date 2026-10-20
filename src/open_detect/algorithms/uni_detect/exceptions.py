"""Uni-Detect-specific exceptions (all subclass :class:`~open_detect.exceptions.OpenDetectError`)."""

from __future__ import annotations

from open_detect.exceptions import OpenDetectError

__all__ = [
    "CorpusNotFoundError",
    "UnityCatalogError",
    "InsufficientDataError",
    "DataQualityError",
]


class CorpusNotFoundError(OpenDetectError):
    """Raised when the corpus statistics table has not been built yet."""


class UnityCatalogError(OpenDetectError):
    """Raised for failures interacting with Unity Catalog (naming, permissions)."""


class InsufficientDataError(OpenDetectError):
    """Raised when a target column/table does not have enough data to score.

    Not a :exc:`ValueError`: the executor-side failure accounting treats it as
    "not applicable" rather than as a data-quality failure.
    """


class DataQualityError(OpenDetectError):
    """Raised when too many corpus/target items fail to score on the executors.

    The failure ratio exceeded ``UniDetectConfig.max_failure_ratio``, so the
    resulting statistics or detections would be built on a silently biased
    sample.
    """
