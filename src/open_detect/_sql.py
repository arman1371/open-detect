"""SQL identifier quoting helpers (OPE-76, B-M5).

Spark SQL identifiers are interpolated into DDL/catalog SQL strings. To keep
those interpolations safe, every *server-side* identifier (catalog, schema,
table) is validated against a strict ASCII pattern and wrapped in backticks
with embedded backticks doubled. Column names come from arbitrary user DataFrames
and may legitimately contain spaces, dots or backticks, so they use a separate
``quote_column`` that escapes by doubling backticks without the strict regex.

Three entry points:

- :func:`quote_ident` -- strict; catalog/schema/table parts.
- :func:`quote_qualified` -- a dotted ``catalog.schema.table`` name; each part
  is validated with :func:`quote_ident`.
- :func:`quote_column` -- lenient; wraps any string in backticks with embedded
  backticks doubled.
"""

from __future__ import annotations

import re

from open_detect.exceptions import ValidationError

#: Strict identifier pattern: ASCII letters, digits, underscore, no leading digit.
_IDENTIFIER_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")

#: Qualified-name parts separated by dots.
_QUALIFIED_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)+")


def quote_ident(name: str, *, strict: bool = True) -> str:
    """Quote a single identifier for safe interpolation into Spark SQL.

    Parameters
    ----------
    name:
        The identifier to quote.
    strict:
        When ``True`` (default), the name must match ``[A-Za-z_][A-Za-z0-9_]*``.
        When ``False``, only embedded backticks are escaped -- used internally
        by :func:`quote_column` for the parts of a column reference.

    Returns
    -------
    str
        The identifier wrapped in backticks, with any embedded backtick doubled.

    Raises
    ------
    ValidationError
        If ``strict`` is ``True`` and ``name`` is not a valid identifier.
    """
    if not isinstance(name, str):
        raise ValidationError(f"identifier must be a string, got {type(name).__name__}")
    if strict and not _IDENTIFIER_RE.fullmatch(name):
        raise ValidationError(f"invalid identifier {name!r}: must match [A-Za-z_][A-Za-z0-9_]*")
    return "`" + name.replace("`", "``") + "`"


def quote_qualified(name: str) -> str:
    """Quote a dotted ``catalog.schema.table`` (2- or 3-part) qualified name.

    Each dot-separated part is validated with :func:`quote_ident` and wrapped
    individually, so the result is ``"`c`.`s`.`t"``.

    Raises
    ------
    ValidationError
        If ``name`` is not a 2- or 3-part qualified name with valid parts.
    """
    if not isinstance(name, str):
        raise ValidationError(f"qualified name must be a string, got {type(name).__name__}")
    parts = name.split(".")
    if len(parts) not in (2, 3):
        raise ValidationError(
            f"qualified name must be 2- or 3-part, got {len(parts)} parts: {name!r}"
        )
    return ".".join(quote_ident(part) for part in parts)


def quote_column(name: str) -> str:
    """Quote a column name for safe interpolation into Spark SQL.

    Unlike :func:`quote_ident`, arbitrary characters are allowed (column names
    from user DataFrames may contain spaces, dots or backticks). Embedded
    backticks are doubled; the result is wrapped in backticks.

    Raises
    ------
    ValidationError
        If ``name`` is not a string.
    """
    if not isinstance(name, str):
        raise ValidationError(f"column name must be a string, got {type(name).__name__}")
    return "`" + name.replace("`", "``") + "`"


__all__ = ["quote_ident", "quote_qualified", "quote_column"]
