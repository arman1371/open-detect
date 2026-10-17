"""Pure-Python tests for the SQL identifier quoting helpers.

No Spark/Java gateway is needed: the helpers are intentionally dependency-free
so that injection behaviour can be asserted without a live cluster. The
Spark-dependent sites that *consume* the helpers are covered by the existing
catalog/ingestion tests, which skip without Java.
"""

from __future__ import annotations

import pytest

from open_detect._sql import quote_column, quote_ident, quote_qualified
from open_detect.exceptions import ValidationError


class TestQuoteIdent:
    @pytest.mark.parametrize(
        "name",
        ["a", "A", "Z", "z", "0", "9", "_", "under_score", "CamelCase", "a1_b2_c3"],
    )
    def test_accepts_valid_identifiers(self, name):
        assert quote_ident(name) == f"`{name}`"

    @pytest.mark.parametrize(
        "name",
        [
            "",  # empty
            "bad name",  # space
            "bad-name",  # dash
            "bad.name",  # dot
            "a; DROP TABLE x; --",  # SQL injection
            "a`b",  # embedded backtick
            "a`b`c",  # multiple embedded backticks
            "٣",  # Unicode digit
            "café",  # Unicode letter
            "a\x00b",  # control char
        ],
    )
    def test_rejects_invalid_identifiers(self, name):
        with pytest.raises(ValidationError):
            quote_ident(name)

    def test_rejects_non_string(self):
        with pytest.raises(ValidationError):
            quote_ident(123)  # type: ignore[arg-type]

    def test_rejects_embedded_backtick(self):
        # Strict identifiers cannot contain backticks; the column path
        # (quote_column) is the one that doubles them.
        with pytest.raises(ValidationError):
            quote_ident("a`b")


class TestQuoteQualified:
    @pytest.mark.parametrize(
        "name",
        ["catalog.schema.table", "main.data_quality.open_detect_corpus_stats", "s.t"],
    )
    def test_accepts_valid_qualified_names(self, name):
        assert quote_qualified(name) == ".".join(f"`{part}`" for part in name.split("."))

    @pytest.mark.parametrize(
        "name",
        [
            "",  # empty
            "single",  # only one part
            "a.b.c.d",  # four parts
            "a.b.c; DROP TABLE x",  # injection in last part
            "a.`b`.c",  # embedded backtick
            "a..b",  # empty middle part
            "main.bad name.table",  # space
        ],
    )
    def test_rejects_invalid_qualified_names(self, name):
        with pytest.raises(ValidationError):
            quote_qualified(name)

    def test_rejects_non_string(self):
        with pytest.raises(ValidationError):
            quote_qualified(None)  # type: ignore[arg-type]


class TestQuoteColumn:
    @pytest.mark.parametrize(
        "name",
        ["a", "col 1", "a.b", "a`b", "weird`col`name", "a;b", "ünïcode"],
    )
    def test_accepts_arbitrary_column_names(self, name):
        assert quote_column(name) == "`" + name.replace("`", "``") + "`"

    def test_doubles_embedded_backtick(self):
        assert quote_column("a`b`c") == "`a``b``c`"

    def test_rejects_empty_and_non_string(self):
        with pytest.raises(ValidationError):
            quote_column("")
        with pytest.raises(ValidationError):
            quote_column(5)  # type: ignore[arg-type]


class TestNoRawInterpolation:
    """Regression: the helpers must not silently accept SQL metacharacters."""

    def test_injection_string_rejected_by_strict(self):
        with pytest.raises(ValidationError):
            quote_ident('a"; DROP TABLE x; --')

    def test_injection_string_rejected_by_qualified(self):
        with pytest.raises(ValidationError):
            quote_qualified('a"; DROP TABLE x; --.b.c')