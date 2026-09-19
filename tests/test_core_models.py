"""Unit tests for core/models.py (no Spark required)."""

from __future__ import annotations

from unidetect.core.enums import ColumnDataType, ErrorType
from unidetect.core.models import (
    Candidate,
    CorpusColumnRecord,
    CorpusPairRecord,
    Detection,
    FeatureBucket,
    MetricObservation,
)


class TestFeatureBucket:
    def test_as_key_encodes_error_type_and_dims(self):
        bucket = FeatureBucket(
            error_type=ErrorType.UNIQUENESS,
            dims=(("data_type", "string"), ("row_count", "(-inf,20]")),
        )
        assert bucket.as_key() == "uniqueness::data_type=string|row_count=(-inf,20]"

    def test_as_dict_round_trips_dims(self):
        bucket = FeatureBucket(
            error_type=ErrorType.SPELLING,
            dims=(("data_type", "string"), ("token_length", "(5,10]")),
        )
        assert bucket.as_dict() == {"data_type": "string", "token_length": "(5,10]"}

    def test_str_matches_as_key(self):
        bucket = FeatureBucket(error_type=ErrorType.NUMERIC_OUTLIER, dims=(("log_fit", "True"),))
        assert str(bucket) == bucket.as_key()

    def test_equal_dims_produce_equal_buckets(self):
        b1 = FeatureBucket(error_type=ErrorType.UNIQUENESS, dims=(("a", "1"),))
        b2 = FeatureBucket(error_type=ErrorType.UNIQUENESS, dims=(("a", "1"),))
        assert b1 == b2
        assert b1.as_key() == b2.as_key()


class TestMetricObservation:
    def test_stores_before_and_after(self):
        obs = MetricObservation(theta_before=0.5, theta_after=0.9)
        assert obs.theta_before == 0.5
        assert obs.theta_after == 0.9


class TestCandidate:
    def _bucket(self):
        return FeatureBucket(error_type=ErrorType.UNIQUENESS, dims=(("a", "1"),))

    def test_default_evidence_is_empty_dict(self):
        candidate = Candidate(
            candidate_id="c1",
            error_type=ErrorType.UNIQUENESS,
            table_id="main.schema.table",
            column_names=("col",),
            row_ids=(1, 2),
            observation=MetricObservation(theta_before=0.9, theta_after=1.0),
            bucket=self._bucket(),
        )
        assert candidate.evidence == {}

    def test_evidence_can_be_overridden(self):
        candidate = Candidate(
            candidate_id="c1",
            error_type=ErrorType.UNIQUENESS,
            table_id="main.schema.table",
            column_names=("col",),
            row_ids=(1,),
            observation=MetricObservation(theta_before=0.9, theta_after=1.0),
            bucket=self._bucket(),
            evidence={"foo": "bar"},
        )
        assert candidate.evidence == {"foo": "bar"}


class TestDetection:
    def test_to_dict_serializes_error_type_and_lists(self):
        detection = Detection(
            candidate_id="c1",
            error_type=ErrorType.SPELLING,
            table_id="main.schema.table",
            column_names=("name",),
            row_ids=(3, 4),
            lr_ratio=0.02,
            surprisal=3.9,
            is_significant=True,
            support=42,
            evidence={"pair": ("a", "b")},
        )
        d = detection.to_dict()
        assert d["error_type"] == "spelling"
        assert d["column_names"] == ["name"]
        assert d["row_ids"] == [3, 4]
        assert d["lr_ratio"] == 0.02
        assert d["is_significant"] is True
        assert d["support"] == 42
        assert d["evidence"] == {"pair": ("a", "b")}

    def test_default_evidence_is_empty_dict(self):
        detection = Detection(
            candidate_id="c1",
            error_type=ErrorType.SPELLING,
            table_id="t",
            column_names=("name",),
            row_ids=(),
            lr_ratio=1.0,
            surprisal=0.0,
            is_significant=False,
            support=0,
        )
        assert detection.evidence == {}
        assert detection.to_dict()["evidence"] == {}


class TestCorpusRecords:
    def test_corpus_column_record_fields(self):
        record = CorpusColumnRecord(
            table_id="main.schema.table",
            column_name="col",
            column_index=0,
            num_rows=10,
            data_type=ColumnDataType.STRING,
            values=("a", "b"),
        )
        assert record.column_name == "col"
        assert record.data_type is ColumnDataType.STRING
        assert record.values == ("a", "b")

    def test_corpus_pair_record_fields(self):
        record = CorpusPairRecord(
            table_id="main.schema.table",
            lhs_column="a",
            rhs_column="b",
            num_rows=10,
            lhs_values=("1", "2"),
            rhs_values=("x", "y"),
        )
        assert record.lhs_column == "a"
        assert record.rhs_column == "b"
        assert record.lhs_values == ("1", "2")
        assert record.rhs_values == ("x", "y")
