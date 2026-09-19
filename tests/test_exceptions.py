"""Unit tests for the exception hierarchy (no Spark required)."""

from __future__ import annotations

import pytest

from unidetect.exceptions import (
    ConfigurationError,
    CorpusNotFoundError,
    InsufficientDataError,
    UniDetectError,
    UnityCatalogError,
)


@pytest.mark.parametrize(
    "exc_class",
    [ConfigurationError, CorpusNotFoundError, UnityCatalogError, InsufficientDataError],
)
def test_all_errors_derive_from_unidetect_error(exc_class):
    assert issubclass(exc_class, UniDetectError)


def test_unidetect_error_is_catchable_broadly():
    with pytest.raises(UniDetectError):
        raise ConfigurationError("bad config")


def test_error_message_is_preserved():
    try:
        raise InsufficientDataError("need more rows")
    except UniDetectError as exc:
        assert str(exc) == "need more rows"
