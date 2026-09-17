"""Exception hierarchy for unidetect.

All library-raised exceptions derive from :class:`UniDetectError` so callers
can catch broadly (``except UniDetectError``) or narrowly.
"""

from __future__ import annotations


class UniDetectError(Exception):
    """Base class for all unidetect errors."""


class ConfigurationError(UniDetectError):
    """Raised when a :class:`~unidetect.config.UniDetectConfig` is invalid."""


class CorpusNotFoundError(UniDetectError):
    """Raised when the corpus statistics table has not been built yet."""


class UnityCatalogError(UniDetectError):
    """Raised for failures interacting with Unity Catalog (naming, permissions)."""


class InsufficientDataError(UniDetectError):
    """Raised when a target column/table does not have enough data to score."""
