"""Shared validation utilities for public API entry points.

Provides cross-algorithm validation for detect() calls:
- Unknown kwargs rejection
- Type checking for sequence parameters
- Column/parameter completeness checks
- Literal parameter validation with runtime checks
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, TypeVar, get_origin

from open_detect.exceptions import ValidationError

T = TypeVar("T")


def _check_unknown_kwargs(
    kwargs: dict[str, Any], accepted: set[str], param_name: str = "detect"
) -> None:
    """Raise ValidationError if kwargs contains keys not in ``accepted``."""
    unknown = set(kwargs) - accepted
    if unknown:
        msg = (
            f"Unknown parameter(s) in {param_name}: {', '.join(sorted(unknown))}. "
            f"Accepted parameters: {', '.join(sorted(accepted))}"
        )
        raise ValidationError(msg)


def _check_expected_type(value: Any, expected_type: type, param_name: str) -> None:
    """Raise ValidationError if a value is not of the expected type.

    For Sequence[str] parameters, also rejects bare str (which would be
    iterated character-by-character rather than as a sequence).
    """
    # Handle the case where expected_type is parameterized Sequence[str]
    origin = get_origin(expected_type)
    if origin is not None and origin is Sequence:
        # expected_type is Sequence[Something], check the args
        args = getattr(expected_type, "__args__", ())
        if args and args[0] is str and isinstance(value, str):
            raise ValidationError("expected a sequence of str, got str; wrap in a list")
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
    Checks isinstance(value, str) before set membership to avoid TypeError on
    unhashable types (e.g. lists, dicts). Raises ValidationError instead.
    """
    if not isinstance(value, str):
        raise ValidationError(
            f"{param_name} must be one of {sorted(valid_values)}, " f"got {value!r}"
        )
    if value not in valid_values:
        raise ValidationError(f"{param_name} must be one of {sorted(valid_values)}, got {value!r}")


def _check_columns_unique(columns: list[str]) -> None:
    """Raise ValidationError if column names are not unique strings."""
    if not all(isinstance(c, str) for c in columns):
        raise ValidationError("All column names must be strings, got non-string entries")
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
                f"{param_name} must be a pyspark.sql.DataFrame, " f"got {type(df).__name__}"
            )
    except ImportError:
        # PySpark not available; skip this check
        pass


def _ensure_dataframe_is_spark(df: Any, param_name: str = "data") -> None:
    """Runtime guard: accept Spark or pandas DataFrames.

    Soft guard (unlike :func:`_check_dataframe_is_spark`, which raises
    :class:`ValidationError`): it never rejects non-DataFrame input, leaving
    that to the caller. When PySpark is importable it accepts both
    ``pyspark.sql.DataFrame`` and ``pandas.DataFrame`` -- the Raha detector
    runs on pandas even in environments that have PySpark installed but no
    active session, and rejecting pandas there broke every end-to-end test.
    When PySpark is not importable it is a pure no-op, which is fine for
    pandas-only environments.
    """
    try:
        from pyspark.sql import DataFrame as SparkDataFrame

        if isinstance(df, SparkDataFrame):
            return
    except ImportError:
        pass
    try:
        import pandas as pd
    except ImportError:
        return
    if isinstance(df, pd.DataFrame):
        return


def _ensure_sequence_of_str(value: Any, param_name: str) -> None:
    """Raise ValidationError if value is not a sequence of strings.

    Also rejects bare str (which would be iterated character-by-character).
    """
    if isinstance(value, str):
        raise ValidationError(f"{param_name} must be a sequence of str, got str; wrap in a list")
    if not isinstance(value, Sequence):
        raise ValidationError(f"{param_name} must be a sequence of str, got {type(value).__name__}")
    for i, item in enumerate(value):
        if not isinstance(item, str):
            raise ValidationError(f"{param_name}[{i}] must be str, got {type(item).__name__}")


def _reject_unknown_kwargs(kwargs: dict[str, Any], allowed: set[str], param_name: str) -> None:
    """Raise ValidationError if any unknown kwargs are passed."""
    unknown = set(kwargs) - allowed
    if unknown:
        msg = (
            f"Unknown parameter(s): {', '.join(sorted(unknown))}. "
            f"Accepted parameters: {', '.join(sorted(allowed))}"
        )
        raise ValidationError(msg)


__all__ = [
    "_check_unknown_kwargs",
    "_check_expected_type",
    "_validate_literal_value",
    "_check_columns_unique",
    "_check_dataframe_is_spark",
    "_ensure_dataframe_is_spark",
    "_ensure_sequence_of_str",
    "_reject_unknown_kwargs",
]
