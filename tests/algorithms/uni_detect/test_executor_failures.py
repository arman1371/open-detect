"""Spark integration tests: executor-side skips are counted, logged once, and gated.

Requires a local Delta-enabled Spark session (see ``conftest.py::spark``);
skipped automatically when one cannot be started (e.g. no Java).
"""

from __future__ import annotations

import logging

import pytest

from open_detect.algorithms.uni_detect.config import UniDetectConfig
from open_detect.algorithms.uni_detect.core.enums import ErrorType
from open_detect.algorithms.uni_detect.corpus.builder import CorpusStatsBuilder
from open_detect.algorithms.uni_detect.corpus.schema import CORPUS_PAIRS_SCHEMA
from open_detect.algorithms.uni_detect.detectors.base import BaseDetector
from open_detect.algorithms.uni_detect.detectors.schema import CANDIDATE_SCHEMA
from open_detect.algorithms.uni_detect.exceptions import DataQualityError
from open_detect.algorithms.uni_detect.failures import FailureCounts

FAILURES_LOGGER = "open_detect.algorithms.uni_detect.failures"

_GOOD_LHS = ["a", "a", "b", "b", "c", "c", "d", "d", "e", "e"]
_GOOD_RHS = ["1", "1", "2", "2", "3", "3", "4", "4", "5", "5"]


def _config(uc_location, table: str, max_failure_ratio: float) -> UniDetectConfig:
    return UniDetectConfig(
        location=uc_location,
        corpus_stats_table=table,
        max_failure_ratio=max_failure_ratio,
    )


def _pairs(spark, good: int, bad: int):
    """``good`` scoreable FD pairs plus ``bad`` whose lhs/rhs lengths disagree (ValueError)."""
    rows = [("t", f"l{i}", f"r{i}", 1, 10, _GOOD_LHS, _GOOD_RHS) for i in range(good)]
    rows += [("t", f"bl{i}", f"br{i}", 1, 10, _GOOD_LHS, _GOOD_RHS[:-1]) for i in range(bad)]
    return spark.createDataFrame(rows, schema=CORPUS_PAIRS_SCHEMA)


class TestCorpusBuilderFailureGate:
    def test_skips_below_threshold_are_logged_once_and_written(self, spark, uc_location, caplog):
        config = _config(uc_location, "exec_fail_below_threshold", max_failure_ratio=0.5)
        builder = CorpusStatsBuilder(spark, config)
        stats = builder.build_fd_stats(_pairs(spark, good=7, bad=1), {})

        with caplog.at_level(logging.INFO, logger=FAILURES_LOGGER):
            builder.write(stats)

        warnings = [r for r in caplog.records if r.levelno == logging.WARNING]
        assert len(warnings) == 1
        assert "skipped 1 of 8" in warnings[0].getMessage()
        assert "ValidationError=1" in warnings[0].getMessage()
        assert spark.table(config.corpus_stats_fqn).count() == 7

    def test_breach_raises_and_nothing_is_written(self, spark, uc_location):
        config = _config(uc_location, "exec_fail_over_threshold", max_failure_ratio=0.05)
        builder = CorpusStatsBuilder(spark, config)
        stats = builder.build_fd_stats(_pairs(spark, good=7, bad=1), {})

        with pytest.raises(DataQualityError, match="1 of 8"):
            builder.write(stats)
        assert not spark.catalog.tableExists(config.corpus_stats_fqn)

    def test_clean_input_logs_no_warning(self, spark, uc_location, caplog):
        config = _config(uc_location, "exec_fail_clean", max_failure_ratio=0.0)
        builder = CorpusStatsBuilder(spark, config)
        stats = builder.build_fd_stats(_pairs(spark, good=4, bad=0), {})

        with caplog.at_level(logging.WARNING, logger=FAILURES_LOGGER):
            builder.write(stats)

        assert not caplog.records
        assert spark.table(config.corpus_stats_fqn).count() == 4

    def test_non_numeric_columns_are_not_failures(self, spark, uc_location, caplog):
        config = _config(uc_location, "exec_fail_not_applicable", max_failure_ratio=0.0)
        builder = CorpusStatsBuilder(spark, config)
        columns = spark.createDataFrame(
            [("t", 0, 5, ["a", "b", "c", "d", "e"]), ("t", 1, 5, ["1", "2", "3", "4", "50"])],
            "table_id string, column_index int, num_rows int, values array<string>",
        )
        stats = builder.build_outlier_stats(columns)

        with caplog.at_level(logging.WARNING, logger=FAILURES_LOGGER):
            builder.write(stats)

        assert not caplog.records
        assert spark.table(config.corpus_stats_fqn).count() == 1


class _StubDetector(BaseDetector):
    """Reports a fixed set of scoring attempts through the shared tracker."""

    error_type = ErrorType.UNIQUENESS
    values: tuple[str, ...] = ()

    def extract_candidates(self, table_names):
        import pandas as pd

        tracker = self._new_failure_tracker()

        def compute(batches):
            for batch in batches:
                counts = FailureCounts()
                for value in batch["v"]:
                    counts.attempt(int, value)
                tracker.flush(counts)
                yield pd.DataFrame([], columns=[f.name for f in CANDIDATE_SCHEMA.fields])

        df = self.spark.createDataFrame([(v,) for v in self.values], "v string")
        return df.mapInPandas(compute, schema=CANDIDATE_SCHEMA)


class TestDetectorFailureGate:
    def test_detect_raises_when_failure_ratio_exceeded(self, spark, uc_location):
        detector = _StubDetector(spark, _config(uc_location, "exec_fail_det_a", 0.1))
        detector.values = ("1", "2", "3", "oops")
        with pytest.raises(DataQualityError, match="1 of 4"):
            detector.detect(["ignored"])

    def test_detect_logs_warning_when_within_threshold(self, spark, uc_location, caplog):
        detector = _StubDetector(spark, _config(uc_location, "exec_fail_det_b", 0.5))
        detector.values = ("1", "2", "3", "oops")
        with caplog.at_level(logging.WARNING, logger=FAILURES_LOGGER):
            result = detector.detect(["ignored"])
        assert result.count() == 0
        warnings = [r for r in caplog.records if r.levelno == logging.WARNING]
        assert len(warnings) == 1
        assert "extract_candidates[uniqueness]" in warnings[0].getMessage()
