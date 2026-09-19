"""Unit tests for the pure-Python helpers in corpus/builder.py.

``_coerce_numeric``, ``_score_single_column`` and
``_stats_schema_without_error_type`` do all of their work in plain Python
(or, for the schema helper, on ``pyspark.sql.types`` objects that need no
active Spark session), so they are tested directly here rather than only
indirectly through the full Delta-backed pipeline in
``test_corpus_and_detectors.py``.
"""

from __future__ import annotations

import pytest

from unidetect.config import UniDetectConfig, UnityCatalogLocation
from unidetect.core.enums import ColumnDataType, ErrorType
from unidetect.corpus.builder import (
    _coerce_numeric,
    _score_single_column,
    _stats_schema_without_error_type,
)
from unidetect.corpus.schema import CORPUS_STATS_SCHEMA


@pytest.fixture
def config():
    return UniDetectConfig(location=UnityCatalogLocation(catalog="main", schema="data_quality"))


class TestCoerceNumeric:
    def test_parses_valid_numbers(self):
        assert _coerce_numeric(["1", "2.5", "-3"]) == [1.0, 2.5, -3.0]

    def test_skips_none_and_unparseable_values(self):
        assert _coerce_numeric(["1", None, "abc", "2"]) == [1.0, 2.0]

    def test_empty_input_returns_empty_list(self):
        assert _coerce_numeric([]) == []


class TestScoreSingleColumn:
    def test_uniqueness(self, config):
        values = ["a", "b", "a", "c", "d"]
        bucket, outcome = _score_single_column(
            ErrorType.UNIQUENESS,
            values,
            num_rows=5,
            column_index=0,
            token_document_frequency={},
            cfg=config,
        )
        assert bucket.error_type is ErrorType.UNIQUENESS
        assert outcome.theta_before < 1.0

    def test_numeric_outlier_coerces_strings_to_floats(self, config):
        values = ["1.0", "2.0", "3.0", "4.0", "100.0"]
        bucket, outcome = _score_single_column(
            ErrorType.NUMERIC_OUTLIER,
            values,
            num_rows=5,
            column_index=0,
            token_document_frequency={},
            cfg=config,
        )
        assert bucket.as_dict()["data_type"] == ColumnDataType.FLOAT.value
        assert outcome.theta_before > 0

    def test_spelling(self, config):
        values = ["Kevin Doeling", "Kevin Dowling", "Alan Myerson"]
        bucket, outcome = _score_single_column(
            ErrorType.SPELLING,
            values,
            num_rows=3,
            column_index=0,
            token_document_frequency={},
            cfg=config,
        )
        assert bucket.error_type is ErrorType.SPELLING
        assert outcome.theta_before == 1.0

    def test_unsupported_error_type_raises(self, config):
        with pytest.raises(ValueError, match="Unsupported single-column error type"):
            _score_single_column(
                ErrorType.FUNCTIONAL_DEPENDENCY,
                ["a", "b"],
                num_rows=2,
                column_index=0,
                token_document_frequency={},
                cfg=config,
            )


class TestStatsSchemaWithoutErrorType:
    def test_drops_only_the_error_type_field(self):
        schema = _stats_schema_without_error_type()
        field_names = [f.name for f in schema.fields]
        assert "error_type" not in field_names
        expected = [f.name for f in CORPUS_STATS_SCHEMA.fields if f.name != "error_type"]
        assert field_names == expected
