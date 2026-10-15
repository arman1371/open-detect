"""Shared validation utilities for public API entry points.

Provides cross-algorithm validation for detect() calls:
- Unknown kwargs rejection
- Type checking for sequence parameters
- Column/parameter completeness checks
- Literal parameter validation with runtime checks
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, get_origin, TypeVar

from open_detect.exceptions import ValidationError
from open_detect.core.enums import ErrorType

T = TypeVar("T")


def _check_unknown_kwargs(kwargs: dict[str, Any], accepted: set[str]) -> None:
    """Raise ValidationError if any unknown kwargs are passed.

    Parameters
    ----------
    kwargs:
        The keyword arguments that were passed to detect().
    accepted:
        The set of kwarg names that are accepted by the algorithm.
    """
    unknown = set(kwargs) - accepted
    if unknown:
        msg = (
            f"Unknown parameter(s): {', '.join(sorted(unknown))}. "
            f"Accepted parameters: {', '.join(sorted(accepted))}"
        )
        raise ValidationError(msg)


def _check_expected_type(value: Any, expected_type: type, param_name: str) -> None:
    """Raise ValidationError if a value is not of the expected type.

    For Sequence[str] parameters, also rejects bare str (which would be
    iterated character-by-character rather than as a sequence).
    """
    # Special case: if expected_type is a parameterized Sequence[str],
    # and value is a bare str, reject with a helpful message.
    origin = get_origin(expected_type)
    if origin is not None and origin is Sequence:
        # expected_type is Sequence[Something], check the args
        args = getattr(expected_type, '__args__', ())
        if len(args) == 1 and args[0] is str and isinstance(value, str):
            raise ValidationError(
                f"expected a sequence of str, got str; wrap in a list"
            )
    # Default isinstance check
    if expected_type is not None and not isinstance(value, expected_type):
        raise ValidationError(
            f"{param_name} must be of type {expected_type.__name__}, "
            f"got {type(value).__name__}: {value!r}"
        )


def _validate_literal_value(
    value: Any,
    valid_values: set[str],
    param_name: str,
) -> None:
    """Validate that value is one of the allowed Literal values.

    Uses typing.get_origin to check the actual Literal constraint at runtime.
    """
    if value not in valid_values:
        raise ValidationError(
            f"{param_name} must be one of {sorted(valid_values)}, "
            f"got {value!r}"
        )


def _check_columns_unique(columns: list[str]) -> None:
    """Raise ValidationError if column names are not unique strings."""
    if not all(isinstance(c, str) for c in columns):
        raise ValidationError(
            f"All column names must be strings, got non-string entries"
        )
    if len(columns) != len(set(columns)):
        raise ValidationError(
            f"Column names must be unique, got duplicates: "
            f"{', '.join(sorted([c for c in columns if columns.count(c) > 1]))}"
        )


def _check_dataframe_is_spark(df: Any, param_name: str = "data") -> None:
    """Validate that data is a Spark DataFrame (when PySpark is available)."""
    try:
        from pyspark.sql import DataFrame as SparkDataFrame

        if not isinstance(df, SparkDataFrame):
            raise ValidationError(
                f"{param_name} must be a pyspark.sql.DataFrame, "
                f"got {type(df).__name__}"
            )
    except ImportError:
        # PySpark not available; skip this check
        pass


__all__ = [
    "_check_unknown_kwargs",
    "_check_expected_type",
    "_validate_literal_value",
    "_check_columns_unique",
    "_check_dataframe_is_spark",
]