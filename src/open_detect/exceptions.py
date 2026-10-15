"""Exception hierarchy for open_detect.

All library-raised exceptions derive from :class:`OpenDetectError` so callers
can catch broadly (``except OpenDetectError``) or narrowly.

Choosing a type:

- bad caller input (wrong shape/type/value of an argument) -> :class:`ValidationError`
- an invalid or inconsistent configuration -> :class:`ConfigurationError`
- not enough data to compute a result -> :class:`InsufficientDataError`
"""

from __future__ import annotations


class OpenDetectError(Exception):
    """Base class for all open_detect errors."""


class ValidationError(OpenDetectError, ValueError):
    """Raised when a caller passes an invalid argument or malformed input.

    Also a :exc:`ValueError`, so existing ``except ValueError`` callers keep working.
    """


class ConfigurationError(OpenDetectError):
    """Raised for invalid or missing configuration.

    E.g. an invalid :class:`~open_detect.algorithms.uni_detect.config.UniDetectConfig`
    or missing job arguments. Use :class:`ValidationError` for bad call arguments.
    """


class CorpusNotFoundError(OpenDetectError):
    """Raised when the corpus statistics table has not been built yet."""


class UnityCatalogError(OpenDetectError):
    """Raised for failures interacting with Unity Catalog (naming, permissions)."""


class InsufficientDataError(OpenDetectError):
    """Raised when a target column/table does not have enough data to score.

    Not a :exc:`ValueError`: the executor-side failure accounting treats it as
    "not applicable" rather than as a data-quality failure.
    """


class UnknownAlgorithmError(OpenDetectError):
    """Raised when an algorithm name is not registered."""


class IndexNotBuiltError(OpenDetectError):
    """Raised when an Auto-Validate query runs before the offline index exists.

    The corpus ``T`` is a required input: FPR_T and Cov_T are defined only
    relative to it, so there is deliberately no corpus-free fallback.
    """


class DataQualityError(OpenDetectError):
    """Raised when too many corpus/target items fail to score on the executors.

    The failure ratio exceeded ``UniDetectConfig.max_failure_ratio``, so the
    resulting statistics or detections would be built on a silently biased
    sample.
    """
