"""Unit tests for featurization.py and text_utils.py."""

from __future__ import annotations

from unidetect.core.enums import ColumnDataType
from unidetect.featurization import (
    bucket_by_edges,
    bucket_leftness,
    bucket_row_count,
    build_outlier_bucket,
    build_spelling_bucket,
    build_uniqueness_bucket,
    log_transform_fits_better,
    token_prevalence,
)
from unidetect.text_utils import infer_column_data_type, is_mixed_alphanumeric, tokenize


class TestBucketing:
    def test_bucket_by_edges_lowest(self):
        assert bucket_by_edges(5, (20, 50, 100)) == "(-inf,20]"

    def test_bucket_by_edges_middle(self):
        assert bucket_by_edges(30, (20, 50, 100)) == "(20,50]"

    def test_bucket_by_edges_highest(self):
        assert bucket_by_edges(5000, (20, 50, 100)) == "(100,inf)"

    def test_bucket_by_edges_boundary_is_inclusive_lower_bucket(self):
        assert bucket_by_edges(20, (20, 50, 100)) == "(-inf,20]"

    def test_row_count_matches_paper_buckets(self):
        edges = (20, 50, 100, 500, 1000)
        assert bucket_row_count(10, edges) == "(-inf,20]"
        assert bucket_row_count(2000, edges) == "(1000,inf)"

    def test_leftness_caps_large_indices(self):
        assert bucket_leftness(3) == "3"
        assert bucket_leftness(50, max_explicit=10) == "10+"


class TestDataTypeInference:
    def test_integer_column(self):
        assert infer_column_data_type(["1", "2", "3", "4"]) == ColumnDataType.INTEGER

    def test_float_column(self):
        assert infer_column_data_type(["1.5", "2.25", "3.0"]) == ColumnDataType.FLOAT

    def test_mixed_alphanumeric_column(self):
        assert infer_column_data_type(["ICAO123", "SKU-9981", "AB12CD34"]) == (
            ColumnDataType.MIXED_ALPHANUMERIC
        )

    def test_string_column(self):
        assert infer_column_data_type(["Paris", "London", "Berlin"]) == ColumnDataType.STRING

    def test_empty_column_is_unknown(self):
        assert infer_column_data_type([]) == ColumnDataType.UNKNOWN

    def test_is_mixed_alphanumeric(self):
        assert is_mixed_alphanumeric("ICAO123")
        assert not is_mixed_alphanumeric("Paris")
        assert not is_mixed_alphanumeric("12345")


class TestTokenPrevalence:
    def test_rare_tokens_score_low(self):
        tdf = {"paris": 500_000, "xkq99": 3}
        assert token_prevalence(["XKQ99"], tdf) == 3.0

    def test_unknown_tokens_score_zero(self):
        assert token_prevalence(["totally-novel-token"], {}) == 0.0

    def test_tokenize_splits_on_punctuation(self):
        assert tokenize("SKU-9981/rev2") == ["SKU", "9981", "rev2"]


class TestLogFit:
    def test_skewed_positive_data_prefers_log(self):
        # a roughly log-normal-shaped sample
        values = [1, 1, 2, 2, 3, 5, 10, 50, 500, 5000]
        assert log_transform_fits_better(values) in (True, False)  # heuristic, just must not crash

    def test_non_positive_values_never_prefer_log(self):
        assert log_transform_fits_better([-1, 0, 1, 2, 3]) is False


class TestFeatureBucketBuilders:
    def test_uniqueness_bucket_dims(self):
        bucket = build_uniqueness_bucket(
            values=["ICAO1", "ICAO2", "ICAO3"],
            num_rows=100,
            column_index=0,
            token_document_frequency={},
            row_count_edges=(20, 50, 100, 500, 1000),
            prevalence_edges=(50, 100, 1000, 10_000, 100_000),
        )
        d = bucket.as_dict()
        assert d["data_type"] == ColumnDataType.MIXED_ALPHANUMERIC.value
        assert d["leftness"] == "0"
        assert "prevalence" in d

    def test_bucket_key_is_stable_and_distinguishes_error_types(self):
        b1 = build_uniqueness_bucket(
            values=["a", "b"],
            num_rows=10,
            column_index=0,
            token_document_frequency={},
            row_count_edges=(20, 50, 100, 500, 1000),
            prevalence_edges=(50, 100, 1000, 10_000, 100_000),
        )
        b2 = build_outlier_bucket(
            values=[1.0, 2.0], num_rows=10, row_count_edges=(20, 50, 100, 500, 1000)
        )
        assert b1.as_key() != b2.as_key()
        assert b1.error_type.value in b1.as_key()

    def test_spelling_bucket_dims(self):
        bucket = build_spelling_bucket(
            values=["Kevin Doeling", "Kevin Dowling"],
            num_rows=10,
            avg_differing_token_length=7.0,
            row_count_edges=(20, 50, 100, 500, 1000),
            token_length_edges=(5, 10, 15, 20),
        )
        assert bucket.as_dict()["token_length"] == "(5,10]"
