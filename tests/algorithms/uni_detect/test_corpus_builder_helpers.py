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

from open_detect.algorithms.uni_detect.config import UniDetectConfig, UnityCatalogLocation
from open_detect.algorithms.uni_detect.core.enums import ColumnDataType, ErrorType
from open_detect.algorithms.uni_detect.corpus.builder import (
    MIN_NUMERIC_FRACTION,
    _coerce_numeric,
    _score_fd_pair,
    _score_single_column,
    _stats_schema_without_error_type,
)
from open_detect.algorithms.uni_detect.corpus.schema import CORPUS_STATS_SCHEMA
from open_detect.algorithms.uni_detect.exceptions import InsufficientDataError
from open_detect.algorithms.uni_detect.strategies import get_spec
from open_detect.exceptions import ValidationError


@pytest.fixture
def config():
    return UniDetectConfig(location=UnityCatalogLocation(catalog="main", schema="data_quality"))


class TestCoerceNumeric:
    def test_parses_valid_numbers(self):
        assert _coerce_numeric(["1", "2.5", "-3"]) == [1.0, 2.5, -3.0]

    def test_skips_none_and_a_tolerable_share_of_unparseable_values(self):
        assert _coerce_numeric(["1", None, "2", "3", "4", "abc"]) == [1.0, 2.0, 3.0, 4.0]

    def test_drops_non_finite_values_and_string_forms(self):
        finite = [str(i) for i in range(16)]
        values = [*finite, "nan", "inf", "-inf", "Infinity"]
        assert _coerce_numeric(values) == [float(i) for i in range(16)]

    def test_empty_input_returns_empty_list(self):
        assert _coerce_numeric([]) == []

    def test_mixed_text_and_number_column_is_not_numeric(self):
        # Two numeric-looking ids in a text column used to make it "numeric".
        assert _coerce_numeric(["12", "34", "alpha", "beta", "gamma", "delta"]) == []

    def test_fraction_threshold_is_inclusive(self):
        assert MIN_NUMERIC_FRACTION == 0.8
        at_threshold = [str(i) for i in range(8)] + ["x", "y"]
        below_threshold = [str(i) for i in range(7)] + ["x", "y", "z"]
        assert len(_coerce_numeric(at_threshold)) == 8
        assert _coerce_numeric(below_threshold) == []

    @pytest.mark.parametrize("bad", ["nan", "NaN", "inf", "-inf", "Infinity"])
    def test_non_finite_values_are_not_numeric(self, bad):
        assert _coerce_numeric(["1", "2", "3", "4", bad]) == [1.0, 2.0, 3.0, 4.0]
        assert _coerce_numeric([bad] * 5) == []


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

    @pytest.mark.parametrize(
        "error_type", [ErrorType.UNIQUENESS, ErrorType.NUMERIC_OUTLIER, ErrorType.SPELLING]
    )
    def test_columns_below_spec_min_rows_are_skipped(self, config, error_type):
        min_rows = get_spec(error_type).min_rows

        def score(n):
            return _score_single_column(
                error_type,
                [f"{1000 + i * 7}" for i in range(n)],
                num_rows=n,
                column_index=0,
                token_document_frequency={},
                cfg=config,
            )

        with pytest.raises(InsufficientDataError):
            score(min_rows - 1)
        assert score(min_rows) is not None

    def test_min_rows_differs_per_error_type(self, config):
        values = ["1000", "1007", "1014"]
        kwargs = {"num_rows": 3, "column_index": 0, "token_document_frequency": {}, "cfg": config}
        assert _score_single_column(ErrorType.SPELLING, values, **kwargs) is not None
        with pytest.raises(InsufficientDataError):
            _score_single_column(ErrorType.UNIQUENESS, values, **kwargs)
        with pytest.raises(InsufficientDataError):
            _score_single_column(ErrorType.NUMERIC_OUTLIER, values, **kwargs)

    def test_numeric_outlier_counts_only_parseable_values_against_min_rows(self, config):
        values = ["1", "2", "3", "4", "x", "y", "z"]  # 4 of 7 parse (<80%)
        with pytest.raises(InsufficientDataError):
            _score_single_column(
                ErrorType.NUMERIC_OUTLIER,
                values,
                num_rows=7,
                column_index=0,
                token_document_frequency={},
                cfg=config,
            )

    def test_unsupported_error_type_raises(self, config):
        with pytest.raises(ValidationError, match="Unsupported single-column error type"):
            _score_single_column(
                ErrorType.FUNCTIONAL_DEPENDENCY,
                ["a", "b"],
                num_rows=2,
                column_index=0,
                token_document_frequency={},
                cfg=config,
            )

    def test_unsupported_error_type_is_still_a_value_error(self, config):
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


class TestScoreFdPair:
    def _score(self, config, n):
        return _score_fd_pair(
            [str(i % 3) for i in range(n)],
            [str(i % 3) for i in range(n)],
            num_rows=n,
            rhs_column_index=1,
            token_document_frequency={},
            cfg=config,
        )

    def test_pairs_below_spec_min_rows_are_skipped(self, config):
        min_rows = get_spec(ErrorType.FUNCTIONAL_DEPENDENCY).min_rows
        with pytest.raises(InsufficientDataError):
            self._score(config, min_rows - 1)
        assert self._score(config, min_rows) is not None
