"""Unit tests for failures.py and the per-element scoring functions (no Spark required)."""

from __future__ import annotations

import logging

import pytest

from open_detect.algorithms.uni_detect.config import UniDetectConfig, UnityCatalogLocation
from open_detect.algorithms.uni_detect.corpus.builder import _score_fd_pair, _score_single_column
from open_detect.algorithms.uni_detect.detectors import functional_dependency as fd_detector
from open_detect.algorithms.uni_detect.detectors import numeric_outlier as outlier_detector
from open_detect.algorithms.uni_detect.detectors import spelling as spelling_detector
from open_detect.algorithms.uni_detect.detectors import uniqueness as uniqueness_detector
from open_detect.algorithms.uni_detect.failures import (
    MAX_REPORTED_EXCEPTION_TYPES,
    FailureCounts,
    FailureCountsAccumulatorParam,
    check_failure_threshold,
)
from open_detect.core.enums import ErrorType
from open_detect.exceptions import ConfigurationError, DataQualityError, InsufficientDataError

LOGGER_NAME = "open_detect.algorithms.uni_detect.failures"


@pytest.fixture
def config():
    return UniDetectConfig(location=UnityCatalogLocation(catalog="main", schema="data_quality"))


def _raise(exc: BaseException):
    raise exc


class TestAttempt:
    def test_success_is_counted_and_result_returned(self):
        counts = FailureCounts()
        assert counts.attempt(lambda x: x * 2, 21) == 42
        assert (counts.processed, counts.skipped) == (1, 0)

    @pytest.mark.parametrize(
        "exc",
        [
            ValueError("bad"),
            UnicodeDecodeError("utf-8", b"\xff", 0, 1, "bad"),
            KeyError("k"),
            ZeroDivisionError("zero"),
        ],
    )
    def test_expected_errors_are_counted_and_swallowed(self, exc):
        counts = FailureCounts()
        assert counts.attempt(_raise, exc) is None
        assert (counts.processed, counts.skipped) == (1, 1)
        assert counts.by_type == {type(exc).__name__: 1}

    @pytest.mark.parametrize("exc", [TypeError("bug"), AttributeError("bug"), RuntimeError("bug")])
    def test_unexpected_errors_propagate_and_are_not_counted(self, exc):
        counts = FailureCounts()
        with pytest.raises(type(exc)):
            counts.attempt(_raise, exc)
        assert (counts.processed, counts.skipped) == (0, 0)

    def test_insufficient_data_is_not_applicable_not_a_failure(self):
        counts = FailureCounts()
        assert counts.attempt(_raise, InsufficientDataError("too few")) is None
        assert (counts.processed, counts.skipped, counts.not_applicable) == (0, 0, 1)
        assert counts.failure_ratio == 0.0


class TestFailureCounts:
    def test_failure_ratio_with_no_items_is_zero(self):
        assert FailureCounts().failure_ratio == 0.0

    def test_merge_adds_all_fields(self):
        a, b = FailureCounts(), FailureCounts()
        a.record_success()
        a.record_skip(ValueError())
        b.record_skip(ValueError())
        b.record_skip(KeyError())
        b.record_not_applicable()
        a.merge(b)
        assert (a.processed, a.skipped, a.not_applicable) == (4, 3, 1)
        assert a.by_type == {"ValueError": 2, "KeyError": 1}

    def test_accumulator_param_merges_in_place(self):
        param = FailureCountsAccumulatorParam()
        zero = param.zero(FailureCounts())
        other = FailureCounts()
        other.record_skip(ValueError())
        result = param.addInPlace(zero, other)
        assert result is zero
        assert (result.processed, result.skipped) == (1, 1)


class TestCheckFailureThreshold:
    def _counts(self, ok: int, bad: int, exc: type[Exception] = ValueError) -> FailureCounts:
        counts = FailureCounts()
        for _ in range(ok):
            counts.record_success()
        for _ in range(bad):
            counts.record_skip(exc())
        return counts

    def test_no_failures_logs_nothing_and_never_raises(self, caplog):
        with caplog.at_level(logging.WARNING, logger=LOGGER_NAME):
            check_failure_threshold(self._counts(10, 0), label="t", max_failure_ratio=0.0)
        assert not caplog.records

    def test_below_threshold_logs_one_warning(self, caplog):
        with caplog.at_level(logging.WARNING, logger=LOGGER_NAME):
            check_failure_threshold(self._counts(99, 1), label="build_x", max_failure_ratio=0.01)
        warnings = [r for r in caplog.records if r.levelno == logging.WARNING]
        assert len(warnings) == 1
        message = warnings[0].getMessage()
        assert "build_x" in message and "1 of 100" in message and "ValueError=1" in message

    def test_exactly_at_threshold_does_not_raise(self):
        check_failure_threshold(self._counts(99, 1), label="t", max_failure_ratio=0.01)

    def test_above_threshold_raises_data_quality_error(self, caplog):
        with (
            caplog.at_level(logging.WARNING, logger=LOGGER_NAME),
            pytest.raises(DataQualityError, match="2 of 100"),
        ):
            check_failure_threshold(self._counts(98, 2), label="t", max_failure_ratio=0.01)
        assert len([r for r in caplog.records if r.levelno == logging.WARNING]) == 1

    def test_zero_threshold_fails_on_first_skip(self):
        with pytest.raises(DataQualityError):
            check_failure_threshold(self._counts(1000, 1), label="t", max_failure_ratio=0.0)

    def test_ratio_one_never_raises(self):
        check_failure_threshold(self._counts(0, 5), label="t", max_failure_ratio=1.0)

    def test_exception_type_sample_is_bounded(self, caplog):
        counts = FailureCounts()
        for i in range(MAX_REPORTED_EXCEPTION_TYPES + 3):
            counts.record_skip(type(f"Err{i}", (ValueError,), {})())
        with caplog.at_level(logging.WARNING, logger=LOGGER_NAME):
            check_failure_threshold(counts, label="t", max_failure_ratio=1.0)
        message = caplog.records[-1].getMessage()
        assert "(+3 more types)" in message
        assert message.count("Err") == MAX_REPORTED_EXCEPTION_TYPES


class TestConfigThreshold:
    def _location(self):
        return UnityCatalogLocation(catalog="main", schema="data_quality")

    def test_default_is_one_percent(self):
        assert UniDetectConfig(location=self._location()).max_failure_ratio == 0.01

    @pytest.mark.parametrize("ratio", [0, 0.5, 1])
    def test_accepts_closed_unit_interval(self, ratio):
        assert UniDetectConfig(location=self._location(), max_failure_ratio=ratio)

    @pytest.mark.parametrize("ratio", [-0.01, 1.01])
    def test_rejects_out_of_range(self, ratio):
        with pytest.raises(ConfigurationError, match="max_failure_ratio"):
            UniDetectConfig(location=self._location(), max_failure_ratio=ratio)


class TestPerElementFunctions:
    """Drive each per-element scorer through ``attempt`` with failing / unexpected inputs."""

    def test_fd_pair_length_mismatch_is_counted(self, config):
        counts = FailureCounts()
        lhs = ["a", "b", "c", "d", "e", "f"]
        result = counts.attempt(_score_fd_pair, lhs, ["x", "y"], 6, 0, {}, config)
        assert result is None
        assert counts.by_type == {"ValueError": 1}

    def test_fd_pair_success(self, config):
        counts = FailureCounts()
        lhs = ["a", "a", "b", "b", "c", "c"]
        rhs = ["x", "x", "y", "y", "z", "z"]
        assert counts.attempt(_score_fd_pair, lhs, rhs, 6, 1, {}, config) is not None
        assert (counts.processed, counts.skipped) == (1, 0)

    def test_fd_pair_unexpected_error_propagates(self, config):
        counts = FailureCounts()
        with pytest.raises(TypeError):
            counts.attempt(_score_fd_pair, None, ["x"], 1, 0, {}, config)

    def test_single_column_unsupported_error_type_is_counted(self, config):
        counts = FailureCounts()
        result = counts.attempt(
            _score_single_column, ErrorType.FUNCTIONAL_DEPENDENCY, ["a"], 1, 0, {}, config
        )
        assert result is None
        assert counts.by_type == {"ValueError": 1}

    def test_single_column_non_numeric_is_not_applicable(self, config):
        counts = FailureCounts()
        result = counts.attempt(
            _score_single_column, ErrorType.NUMERIC_OUTLIER, ["a", "b", "c"], 3, 0, {}, config
        )
        assert result is None
        assert (counts.skipped, counts.not_applicable) == (0, 1)

    def test_single_column_unexpected_error_propagates(self, config):
        counts = FailureCounts()
        with pytest.raises(TypeError):
            counts.attempt(_score_single_column, ErrorType.UNIQUENESS, 5, 5, 0, {}, config)

    def test_uniqueness_detector_scorer(self, config):
        counts = FailureCounts()
        vals = [f"id{i}" for i in range(20)] + ["dup", "dup"]
        row_ids = list(range(len(vals)))
        scored = counts.attempt(uniqueness_detector._score_column, vals, row_ids, 22, 0, {}, config)
        assert scored is not None
        outcome, bucket = scored
        assert outcome.dropped_indices
        assert (
            counts.attempt(uniqueness_detector._score_column, ["a", "b", "c"], [0, 1, 2], 3, 0, {}, config)
            is None
        )
        assert (counts.processed, counts.skipped) == (2, 0)

    def test_uniqueness_detector_scorer_unexpected_error_propagates(self, config):
        with pytest.raises(TypeError):
            FailureCounts().attempt(uniqueness_detector._score_column, 5, 5, 0, {}, config)

    def test_outlier_detector_scorer(self, config):
        counts = FailureCounts()
        vals = [1.0, 2.0, 3.0, 4.0, 1000.0]
        row_ids = list(range(len(vals)))
        scored = counts.attempt(
            outlier_detector._score_column, vals, row_ids, 5, config
        )
        assert scored is not None
        assert counts.attempt(outlier_detector._score_column, [1.0], [0], 1, config) is None
        assert (counts.processed, counts.skipped, counts.not_applicable) == (1, 0, 1)

    def test_spelling_detector_scorer(self, config):
        counts = FailureCounts()
        vals = ["apple", "apple", "aple", "pear", "plum"]
        row_ids = list(range(len(vals)))
        scored = counts.attempt(
            spelling_detector._score_column, vals, row_ids, 5, config
        )
        assert scored is not None
        with pytest.raises(TypeError):
            counts.attempt(spelling_detector._score_column, 5, 5, config)

    def test_fd_detector_scorer(self, config):
        counts = FailureCounts()
        lhs = ["a", "b"]
        rhs = ["x"]
        row_ids = [0, 1]
        assert counts.attempt(fd_detector._score_pair, lhs, rhs, row_ids, 2, 0, {}, config) is None
        assert counts.by_type == {"ValueError": 1}
        lhs = ["a"] * 10 + ["b"] * 10
        rhs = ["x"] * 9 + ["y"] + ["z"] * 10
        row_ids = list(range(20))
        scored = counts.attempt(fd_detector._score_pair, lhs, rhs, row_ids, 20, 1, {}, config)
        assert scored is not None and scored[0].dropped_indices
