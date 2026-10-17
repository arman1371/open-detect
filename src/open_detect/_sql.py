"""SQL identifier quoting helpers.

Spark/Databricks SQL identifiers are interpolated into DDL and query strings
throughout this codebase. Unvalidated interpolation is an injection vector:
a catalog or schema name such as ``a"; DROP TABLE x; --`` would execute as
arbitrary SQL. This module centralises every identifier escape so there is a
single place to audit.

Two quoting profiles are provided because the set of legal characters differs:

* :func:`quote_ident` (strict) -- catalog, schema and table names. Unity
  Catalog enforces ``[A-Za-z0-9_]``; anything else is rejected with
  :class:`~open_detect.exceptions.ValidationError`. Defence in depth: the
  returned string is wrapped in backticks and any embedded backtick is
  doubled, so even a name that slips past validation cannot break out.
* :func:`quote_column` -- DataFrame column references. User-supplied column
  names may legitimately contain spaces, dots or backticks, so the strict
  regex is *not* applied here; only backtick-doubling is performed.

Both helpers are pure Python and have no Spark dependency, so the injection
tests run without a Java gateway.
"""

from __future__ import annotations

import re

from open_detect.exceptions import ValidationError

#: Strict Unity Catalog identifier: ASCII letters, digits and underscores only.
_IDENT_RE = re.compile(r"[A-Za-z0-9_]+")

#: A single part of a qualified name (catalog/schema/table), same rules.
_QUALIFIED_PART_RE = _IDENT_RE

#: A fully-qualified ``catalog.schema.table`` name with 2 or 3 parts.
_QUALIFIED_NAME_RE = re.compile(r"[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+){1,2}")


def _validate_strict(name: str, label: str) -> str:
    """Validate ``name`` against the strict identifier regex.

    Raises :class:`ValidationError` on the first offending character so the
    caller sees which input was rejected, not just that one was.
    """
    if not isinstance(name, str):
        raise ValidationError(f"{label} must be a string, got {type(name).__name__}")
    if not name:
        raise ValidationError(f"{label} must not be empty")
    if not _IDENT_RE.fullmatch(name):
        raise ValidationError(
            f"Invalid {label} {name!r}: identifier may only contain "
            "ASCII letters, digits and underscores."
        )
    return name


def quote_ident(name: str) -> str:
    """Quote a strict catalog/schema/table identifier.

    Wraps the validated name in backticks and doubles any embedded backtick
    (defence in depth). Raises :class:`ValidationError` on invalid input.
    """
    _validate_strict(name, "identifier")
    return "`" + name.replace("`", "``") + "`"


def quote_qualified(name: str) -> str:
    """Quote a dotted ``catalog.schema.table`` (or ``schema.table``) name.

    Each part is validated with the strict regex and then quoted, so a name
    such as ``a"; DROP TABLE x; --`` is rejected before any SQL is built.
    """
    if not isinstance(name, str):
        raise ValidationError(f"qualified name must be a string, got {type(name).__name__}")
    if not name:
        raise ValidationError("qualified name must not be empty")
    if not _QUALIFIED_NAME_RE.fullmatch(name):
        raise ValidationError(
            f"Invalid qualified name {name!r}: expected 2-3 dot-separated "
            "alphanumeric/underscore parts."
        )
    parts = name.split(".")
    quoted = [quote_ident(part) for part in parts]
    return ".".join(quoted)


def quote_column(name: str) -> str:
    """Quote a DataFrame column reference.

    Unlike :func:`quote_ident`, arbitrary characters are permitted in column
    names (spaces, dots, backticks are all legal in Spark schemas). Only
    backtick-doubling is performed so a name cannot break out of the column
    reference.
    """
    if not isinstance(name, str):
        raise ValidationError(f"column name must be a string, got {type(name).__name__}")
    if not name:
        raise ValidationError("column name must not be empty")
    return "`" + name.replace("`", "``") + "`"


__all__ = ["quote_ident", "quote_qualified", "quote_column"]