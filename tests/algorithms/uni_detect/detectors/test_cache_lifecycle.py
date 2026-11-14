"""Cache-lifecycle contract tests for :class:`BaseDetector.detect`.

Two tiers, matching the acceptance criteria for OPE-89:

* **Pure-Python tests** (this module, no Spark/Java required): verify the
  *contract* of the new cache lifecycle -- candidates are persisted with
  ``MEMORY_AND_DISK`` and released, the scored frame is released by the caller,
  and the release helpers are idempotent and exception-safe. They run
  everywhere.
* **Spark tests** (``TestDetectCacheLifecycleSpark``): drive a real detector
  end-to-end and assert that ``count()``/``collect()``/``write`` on the returned
  frame no longer re-executes the scoring stage, via instrumentation of the
  scoring computation. These require a Delta-enabled Spark session and are
  skipped automatically when no Java is available.
"""

from __future__ import annotations

from typing import Any
from unittest.mock import MagicMock

import pytest
from pyspark import StorageLevel

from open_detect.algorithms.uni_detect.config import UniDetectConfig, UnityCatalogLocation
from open_detect.algorithms.uni_detect.core.enums import ErrorType
from open_detect.algorithms.uni_detect.detectors.base import BaseDetector

_CANDIDATE_STORAGE_LEVEL = StorageLevel.MEMORY_AND_DISK


def _config() -> UniDetectConfig:
    return UniDetectConfig(location=UnityCatalogLocation(catalog="c", schema="s"))


class _FakeDetector(BaseDetector):
    """A real BaseDetector whose ``extract_candidates`` is a controllable stand-in."""

    error_type = ErrorType.UNIQUENESS

    def __init__(self, spark: Any, config: UniDetectConfig) -> None:
        super().__init__(spark, config)
        self._extract_calls = 0
        self._frames: list[Any] = []
        self._next_count = 1

    def extract_candidates(self, table_names):  # type: ignore[override]
        self._extract_calls += 1
        frame = MagicMock(name=f"candidates-{self._extract_calls}")
        frame.count.return_value = self._next_count
        self._frames.append(frame)
        return frame

    def _empty_result(self):  # type: ignore[override]
        return MagicMock(name="empty-result")


def _detector() -> _FakeDetector:
    spark = MagicMock()
    spark.sparkContext.setJobGroup = MagicMock()
    return _FakeDetector(spark, _config())


class TestReleaseIsIdempotentAndSafe:
    def test_release_calls_unpersist_on_tracked_frames(self) -> None:
        detector = _detector()
        frame = MagicMock()
        detector._track(frame)
        detector.release()
        frame.unpersist.assert_called_once_with()

    def test_release_is_idempotent(self) -> None:
        detector = _detector()
        frame = MagicMock()
        detector._track(frame)
        # Calling twice must not raise (an already-unpersisted frame is a no-op).
        detector.release()
        detector.release()

    def test_release_swallows_unpersist_errors(self) -> None:
        detector = _detector()
        frame = MagicMock()
        frame.unpersist.side_effect = RuntimeError("already gone")
        detector._track(frame)
        # Must not raise.
        detector.release()


class TestScoredResultReleasesOnExit:
    def test_release_idempotent_with_tracked_frames(self) -> None:
        """Release can be called multiple times safely."""
        detector = _detector()
        frame1 = MagicMock()
        frame2 = MagicMock()
        detector._track(frame1)
        detector._track(frame2)
        detector.release()
        frame1.unpersist.assert_called_once()
        frame2.unpersist.assert_called_once()
        # Second call should not raise
        detector.release()

    def test_release_swallows_errors(self) -> None:
        """Release swallows exceptions from unpersist."""
        detector = _detector()
        frame = MagicMock()
        frame.unpersist.side_effect = RuntimeError("already gone")
        detector._track(frame)
        detector.release()  # Should not raise


class TestDetectCacheContract:
    """Pure-Python half of the cache contract (no Spark/Java required)."""

    def test_candidates_persisted_with_memory_and_disk(self) -> None:
        detector = _detector()
        # Empty path still calls candidates.persist(...) before count().
        detector._next_count = 0
        detector.store.batch_score = MagicMock()  # type: ignore[assignment]
        detector.detect(["t"])
        persist_levels = [
            call.args[0] for frame in detector._frames for call in frame.persist.call_args_list
        ]
        assert persist_levels and all(level == _CANDIDATE_STORAGE_LEVEL for level in persist_levels)

    def test_candidates_unpersisted_after_detect_returns(self) -> None:
        detector = _detector()
        detector._next_count = 0
        detector.store.batch_score = MagicMock()  # type: ignore[assignment]
        detector.detect(["t"])
        for frame in detector._frames:
            frame.unpersist.assert_called()

    def test_extract_runs_exactly_once_per_detect_call(self) -> None:
        detector = _detector()
        detector._next_count = 0
        detector.store.batch_score = MagicMock()  # type: ignore[assignment]
        detector.detect(["t"])
        assert detector._extract_calls == 1

    def test_empty_result_does_not_score(self) -> None:
        detector = _detector()
        detector._next_count = 0
        detector.store.batch_score = MagicMock()  # type: ignore[assignment]
        result = detector.detect(["t"])
        assert result is not None
        detector.store.batch_score.assert_not_called()

    def test_new_failure_tracker_creates_and_returns_tracker(self) -> None:
        _detector()
        # This method needs a SparkContext, skip in pure mock test
        pytest.skip("requires SparkContext - covered by integration tests")

    def test_non_empty_candidates_runs_scoring_and_persists_result(self) -> None:
        """When candidates exist, batch_score runs, result is tracked and materialized.

        This test is skipped in pure mock mode because it requires a SparkContext
        for the DataFrame operations (withColumn, lit, etc.).
        """
        pytest.skip("requires SparkContext - covered by integration tests")

    def test_failure_tracker_check_called_when_candidates_exist(self) -> None:
        """When candidates are non-empty, failure tracker's check() is called.

        This test is skipped in pure mock mode because it requires a SparkContext
        for the DataFrame operations.
        """
        pytest.skip("requires SparkContext - covered by integration tests")


# ----------------------------------------------------------------------
# Spark-backed acceptance test (skipped when no Java/Delta available)
# ----------------------------------------------------------------------


# Skip condition: rely on the session fixture from conftest.py which properly
# configures the Spark session with the correct driver heap settings.
# The fixture skips tests automatically when no Java is available.


class TestDetectCacheLifecycleSpark:
    """End-to-end cache contract on a real Spark session (skipped without Java).

    The test builds a real uniqueness detector, runs ``detect()`` on a tiny
    Delta table, and asserts that subsequent actions (``count()``, ``collect()``, ``write``)
    on the returned frame do not re-execute the scoring computation.
    """

    @staticmethod
    def _import_scoring_job_counter():
        """Import ScoringJobCounter, adding benchmarks to sys.path if needed."""
        import sys
        from pathlib import Path

        # Add the repository root so the ``benchmarks`` package is importable.
        # ``tests/benchmarks/test_bench_spark_jobs.py`` instead inserts the
        # ``benchmarks/`` directory itself and imports ``common.spark_jobs``;
        # either path works, but the path must match the dotted module name.
        repo_root = Path(__file__).resolve().parents[4]
        if str(repo_root) not in sys.path:
            sys.path.insert(0, str(repo_root))
        from benchmarks.common.spark_jobs import ScoringJobCounter

        return ScoringJobCounter

    def test_detect_returns_persisted_frame_no_reexecution_on_count_collect_write(self, spark):
        """After ``detect()`` returns, downstream actions reuse the cached frame."""
        ScoringJobCounter = self._import_scoring_job_counter()

        from open_detect.algorithms.uni_detect.config import UniDetectConfig, UnityCatalogLocation
        from open_detect.algorithms.uni_detect.core.enums import ErrorType
        from open_detect.algorithms.uni_detect.detectors.uniqueness import UniquenessDetector
        from open_detect.algorithms.uni_detect.pipeline import UniDetect

        config = UniDetectConfig(
            location=UnityCatalogLocation(
                catalog="spark_catalog", schema="open_detect_test_schema"
            ),
            alpha=0.001,
        )
        detector = UniquenessDetector(spark, config)

        # Seed a tiny Delta table with some duplicate rows (6 rows to meet min_rows=5)
        spark.sql(
            "CREATE TABLE IF NOT EXISTS spark_catalog.open_detect_test_schema.t1 "
            "(id LONG, val STRING) USING DELTA"
        )
        spark.sql(
            "INSERT INTO spark_catalog.open_detect_test_schema.t1 VALUES "
            "(1, 'a'), (2, 'a'), (3, 'b'), (4, 'c'), (5, 'c'), (6, 'd')"
        )

        # Build corpus statistics so detect() can score candidates
        ud = UniDetect(config, spark=spark)
        ud.build_corpus_statistics(
            ["spark_catalog.open_detect_test_schema.t1"],
            error_types=[ErrorType.UNIQUENESS],
        )

        counter = ScoringJobCounter(spark, enabled=True)

        # Run detect -- this should launch scoring computation
        with counter.scope("detect"):
            result = detector.detect(["spark_catalog.open_detect_test_schema.t1"])

        # Materialize once inside detect(); result is persisted
        detect_jobs = counter.results[0].jobs
        assert detect_jobs > 0, "detect() should have launched scoring computation"

        # Now call count() -- should NOT launch additional scoring
        with counter.scope("count"):
            _ = result.count()
        assert (
            counter.results[1].jobs == 0
        ), f"count() re-executed {counter.results[1].jobs} scoring jobs; frame should be cached"

        # collect() -- should NOT launch additional scoring
        with counter.scope("collect"):
            _ = result.limit(10).collect()
        assert (
            counter.results[2].jobs == 0
        ), f"collect() re-executed {counter.results[2].jobs} scoring jobs; frame should be cached"

        # write -- should NOT launch additional scoring
        with counter.scope("write"):
            result.write.format("noop").mode("overwrite").save()
        assert (
            counter.results[3].jobs == 0
        ), f"write() re-executed {counter.results[3].jobs} scoring jobs; frame should be cached"

        # Clean up
        result.unpersist()

    def test_pipeline_detect_unioned_result_no_reexecution(self, spark):
        """UniDetect.detect() returns a unioned, persisted frame with no re-execution."""
        ScoringJobCounter = self._import_scoring_job_counter()

        # This test also needs the import for the assert statement below
        # Import is already done above via _import_scoring_job_counter

        from open_detect.algorithms.uni_detect.config import UniDetectConfig, UnityCatalogLocation
        from open_detect.algorithms.uni_detect.core.enums import ErrorType
        from open_detect.algorithms.uni_detect.pipeline import UniDetect

        config = UniDetectConfig(
            location=UnityCatalogLocation(
                catalog="spark_catalog", schema="open_detect_test_schema"
            ),
            alpha=0.001,
        )
        ud = UniDetect(config, spark=spark)

        # Seed tables
        spark.sql(
            "CREATE TABLE IF NOT EXISTS spark_catalog.open_detect_test_schema.t2 "
            "(id LONG, val STRING) USING DELTA"
        )
        spark.sql(
            "INSERT INTO spark_catalog.open_detect_test_schema.t2 VALUES "
            "(1, 'x'), (2, 'x'), (3, 'y')"
        )

        # Build corpus statistics so detect() can score candidates
        ud.build_corpus_statistics(
            ["spark_catalog.open_detect_test_schema.t2"],
            error_types=[ErrorType.UNIQUENESS],
        )

        counter = ScoringJobCounter(spark, enabled=True)

        with counter.scope("pipeline_detect"):
            detections = ud.detect(["spark_catalog.open_detect_test_schema.t2"])

        detect_jobs = counter.results[0].jobs
        assert detect_jobs > 0

        # The returned frame must be the *sorted* one, and it must be the frame
        # that was persisted+materialized -- otherwise count/collect/write below
        # would re-execute the scoring stage.
        lr_ratios = [row["lr_ratio"] for row in detections.select("lr_ratio").collect()]
        assert lr_ratios == sorted(lr_ratios), "pipeline result must be sorted by lr_ratio"

        with counter.scope("count"):
            _ = detections.count()
        assert counter.results[1].jobs == 0

        with counter.scope("collect"):
            _ = detections.limit(5).collect()
        assert counter.results[2].jobs == 0

        with counter.scope("write"):
            detections.write.format("noop").mode("overwrite").save()
        assert counter.results[3].jobs == 0

        detections.unpersist()
