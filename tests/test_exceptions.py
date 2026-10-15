"""Unit tests for the exception hierarchy (no Spark required)."""

from __future__ import annotations

import pytest

from open_detect.exceptions import (
    ConfigurationError,
    CorpusNotFoundError,
    DataQualityError,
    IndexNotBuiltError,
    InsufficientDataError,
    OpenDetectError,
    UnityCatalogError,
    UnknownAlgorithmError,
    ValidationError,
)


@pytest.mark.parametrize(
    "exc_class",
    [
        ConfigurationError,
        CorpusNotFoundError,
        UnityCatalogError,
        InsufficientDataError,
        DataQualityError,
        UnknownAlgorithmError,
        IndexNotBuiltError,
        ValidationError,
    ],
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


def test_validation_error_is_also_a_value_error():
    assert issubclass(ValidationError, ValueError)
    with pytest.raises(ValueError):
        raise ValidationError("bad input")


def test_insufficient_data_error_is_not_a_value_error():
    assert not issubclass(InsufficientDataError, ValueError)


def test_relocated_exceptions_importable_from_every_path():
    import open_detect
    from open_detect.algorithms import UnknownAlgorithmError as from_algorithms
    from open_detect.algorithms import registry
    from open_detect.algorithms.auto_validate import IndexNotBuiltError as av_pkg
    from open_detect.algorithms.auto_validate import exceptions as av_exceptions

    assert open_detect.UnknownAlgorithmError is UnknownAlgorithmError
    assert open_detect.IndexNotBuiltError is IndexNotBuiltError
    assert from_algorithms is UnknownAlgorithmError
    assert registry.UnknownAlgorithmError is UnknownAlgorithmError
    assert av_pkg is IndexNotBuiltError
    assert av_exceptions.IndexNotBuiltError is IndexNotBuiltError
