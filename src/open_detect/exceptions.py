"""Exception hierarchy for open_detect.

All library-raised exceptions derive from :class:`OpenDetectError` so callers
can catch broadly (``except OpenDetectError``) or narrowly.
"""

from __future__ import annotations


class OpenDetectError(Exception):
    """Base class for all open_detect errors."""


class ConfigurationError(OpenDetectError):
    """Raised when a :class:`~open_detect.algorithms.uni_detect.config.UniDetectConfig` is invalid."""


class CorpusNotFoundError(OpenDetectError):
    """Raised when the corpus statistics table has not been built yet."""


class UnityCatalogError(OpenDetectError):
    """Raised for failures interacting with Unity Catalog (naming, permissions)."""


class InsufficientDataError(OpenDetectError):
    """Raised when a target column/table does not have enough data to score."""


class DataQualityError(OpenDetectError):
    """Raised when too many corpus/target items fail to score on the executors.

    The failure ratio exceeded ``UniDetectConfig.max_failure_ratio``, so the
    resulting statistics or detections would be built on a silently biased
    sample.
    """
