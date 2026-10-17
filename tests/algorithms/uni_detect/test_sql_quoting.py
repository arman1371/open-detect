"""SQL identifier quoting tests (OPE-76, B-M5).

Pure-Python: no Spark, no Java. Covers the injection surface named in the
issue -- ``quote_ident`` (strict catalog/schema/table parts), ``quote_qualified``
(dotted names) and ``quote_column`` (lenient user DataFrame columns).
"""

from __future__ import annotations

import pytest

from open_detect._sql import quote_column, quote_ident, quote_qualified
from open_detect.exceptions import ValidationError

# ---------------------------------------------------------------------------
# quote_ident (strict)
# ---------------------------------------------------------------------------


class TestQuoteIdent:
    @pytest.mark.parametrize(
        "name",
        [
            "a",
            "A",
            "a_b",
            "a1b2",
            "_private",
            "catalog",
            "open_detect_corpus_stats",
        ],
    )
    def test_accepts_valid_identifiers(self, name: str) -> None:
        assert quote_ident(name) == f"`{name}`"

    @pytest.mark.parametrize(
        "name",
        [
            "DROP TABLE x; --",
            "a`b",
            "a b",
            "a.b",
            "3foo",  # leading digit
            "",  # empty
            "a..b",  # empty part
            "٣",  # unicode digit
            "ñ",
            "a; DROP TABLE students; --",
            "`",
            "``",
            "a`",
            "`b",
        ],
    )
    def test_rejects_invalid_identifiers(self, name: str) -> None:
        with pytest.raises(ValidationError):
            quote_ident(name)

    def test_doubles_embedded_backticks_when_non_strict(self) -> None:
        assert quote_ident("a`b", strict=False) == "`a``b`"
        assert quote_ident("``", strict=False) == "``````"

    def test_non_string_raises(self) -> None:
        with pytest.raises(ValidationError):
            quote_ident(None)  # type: ignore[arg-type]
        with pytest.raises(ValidationError):
            quote_ident(123)  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# quote_qualified
# ---------------------------------------------------------------------------


class TestQuoteQualified:
    @pytest.mark.parametrize(
        "name",
        ["catalog.schema", "catalog.schema.table", "main.data_quality.t"],
    )
    def test_accepts_valid_qualified_names(self, name: str) -> None:
        parts = name.split(".")
        expected = ".".join(f"`{p}`" for p in parts)
        assert quote_qualified(name) == expected

    @pytest.mark.parametrize(
        "name",
        [
            "catalog",  # too few parts
            "a.b.c.d",  # too many parts
            "catalog.bad name.table",
            "catalog..schema.table",  # empty part
            "cat.sch.`tbl",  # backtick in part
            "",
        ],
    )
    def test_rejects_invalid_qualified_names(self, name: str) -> None:
        with pytest.raises(ValidationError):
            quote_qualified(name)

    def test_non_string_raises(self) -> None:
        with pytest.raises(ValidationError):
            quote_qualified(None)  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# quote_column (lenient)
# ---------------------------------------------------------------------------


class TestQuoteColumn:
    @pytest.mark.parametrize(
        "name,expected",
        [
            ("a", "`a`"),
            ("a b", "`a b`"),
            ("a.b", "`a.b`"),
            ("a`b", "`a``b`"),
            ("``", "``````"),
            ("col with spaces and `ticks`", "`col with spaces and ``ticks```"),
            ("DROP", "`DROP`"),
        ],
    )
    def test_escapes_and_wraps(self, name: str, expected: str) -> None:
        assert quote_column(name) == expected

    def test_non_string_raises(self) -> None:
        with pytest.raises(ValidationError):
            quote_column(None)  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# Config integration
# ---------------------------------------------------------------------------


class TestConfigValidation:
    def test_rejects_invalid_table_names(self) -> None:
        from open_detect.algorithms.uni_detect.config import (
            UniDetectConfig,
            UnityCatalogLocation,
        )
        from open_detect.exceptions import ConfigurationError

        loc = UnityCatalogLocation(catalog="main", schema="data_quality")
        with pytest.raises(ConfigurationError):
            UniDetectConfig(location=loc, corpus_stats_table="bad name")
        with pytest.raises(ConfigurationError):
            UniDetectConfig(location=loc, detections_table="a`b")
