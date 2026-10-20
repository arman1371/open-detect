"""Exception hierarchy for open_detect.

All library-raised exceptions derive from :class:`OpenDetectError` so callers
can catch broadly (``except OpenDetectError``) or narrowly.

Choosing a type:

- bad caller input (wrong shape/type/value of an argument) -> :class:`ValidationError`
- an invalid or inconsistent configuration -> :class:`ConfigurationError`
- not enough data to compute a result -> :class:`~open_detect.algorithms.uni_detect.exceptions.InsufficientDataError`
"""

from __future__ import annotations

import warnings
from typing import Any

_MOVED = {
    "CorpusNotFoundError",
    "UnityCatalogError",
    "InsufficientDataError",
    "DataQualityError",
}


def __getattr__(name: str) -> Any:
    """Deprecated: Uni-Detect-only errors moved to ``algorithms.uni_detect.exceptions``."""
    if name in _MOVED:
        # Lazy import avoids a cycle (the new module subclasses OpenDetectError).
        from open_detect.algorithms.uni_detect import exceptions as _new

        warnings.warn(
            f"open_detect.exceptions.{name} is deprecated; import it from "
            "open_detect.algorithms.uni_detect.exceptions instead. "
            "The old path will be removed in 0.5.0.",
            DeprecationWarning,
            stacklevel=2,
        )
        return getattr(_new, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


class OpenDetectError(Exception):
    """Base class for all open_detect errors."""


class ValidationError(OpenDetectError, ValueError):
    """Raised when a caller passes an invalid argument or malformed input.

    Also a :exc:`ValueError`, so existing ``except ValueError`` callers keep working.
    """


class ConfigurationError(OpenDetectError):
    """Raised for invalid or missing configuration.

    E.g. an invalid algorithm config object or missing job arguments. Use :class:`ValidationError` for bad call arguments.
    """


class UnknownAlgorithmError(OpenDetectError):
    """Raised when an algorithm name is not registered."""


class IndexNotBuiltError(OpenDetectError):
    """Raised when an Auto-Validate query runs before the offline index exists.

    The corpus ``T`` is a required input: FPR_T and Cov_T are defined only
    relative to it, so there is deliberately no corpus-free fallback.
    """
