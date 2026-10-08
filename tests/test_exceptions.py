"""Unit tests for the exception hierarchy (no Spark required)."""

from __future__ import annotations

import pytest

from open_detect.exceptions import (
    ConfigurationError,
    CorpusNotFoundError,
    InsufficientDataError,
    OpenDetectError,
    UnityCatalogError,
)


@pytest.mark.parametrize(
    "exc_class",
    [ConfigurationError, CorpusNotFoundError, UnityCatalogError, InsufficientDataError],
)
def test_all_errors_derive_from_open_detect_error(exc_class):
    assert issubclass(exc_class, OpenDetectError)


def test_open_detect_error_is_catchable_broadly():
    with pytest.raises(OpenDetectError):
        raise ConfigurationError("bad config")


def test_error_message_is_preserved():
    try:
        raise InsufficientDataError("need more rows")
    except OpenDetectError as exc:
        assert str(exc) == "need more rows"
