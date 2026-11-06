"""Cache-lifecycle contract tests for :class:`BaseDetector.detect`.

Two tiers, matching the acceptance criteria for OPE-89:

* **Pure-Python tests** (this module, no Spark/Java required): verify the
  *contract* of the new cache lifecycle -- candidates are persisted with
  ``MEMORY_AND_DISK`` and released, the scored frame is released by the caller,
  and the release helpers are idempotent and exception-safe. They run
  everywhere.
* **Spark tests** (``TestDetectCacheLifecycleSpark``): drive a real detector
  end-to-end and assert that ``count()``/``collect()``/``write`` on the returned
  frame no longer re-executes the scoring stage, via the job counter in
  :mod:`benchmarks.common.spark_jobs`. These require a Delta-enabled Spark
  session and are skipped automatically when no Java is available.
"""

from __future__ import annotations

from typing import Any
from unittest.mock import MagicMock

import pytest
from pyspark import StorageLevel

from open_detect.algorithms.uni_detect.config import UniDetectConfig, UnityCatalogLocation
from open_detect.algorithms.uni_detect.detectors.base import BaseDetector
from open_detect.core.enums import ErrorType

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


# ----------------------------------------------------------------------
# Spark-backed acceptance test (skipped when no Java/Delta available)
# ----------------------------------------------------------------------


def _spark_available() -> bool:
    """Probe whether a Delta-enabled Spark session can be started."""
    import os
    import sys

    os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
    os.environ.setdefault("PYSPARK_DRIVER_PYTHON", sys.executable)
    try:
        from delta import configure_spark_with_delta_pip
        from pyspark.sql import SparkSession

        with SparkUnavailableContext():
            builder = (
                SparkSession.builder.master("local[1]")
                .appName("cache-test-probe")
                .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
                .config(
                    "spark.sql.catalog.spark_catalog",
                    "org.apache.spark.sql.delta.catalog.DeltaCatalog",
                )
            )
            session = configure_spark_with_delta_pip(builder).getOrCreate()
            session.sparkContext.setLogLevel("ERROR")
            session.stop()
        return True
    except Exception:
        return False


class SparkUnavailableContext:
    """Context manager that catches and silences any exception for the probe."""

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True  # suppress any exception


@pytest.mark.skipif(
    not _spark_available(), reason="requires a Delta-enabled Spark session with Java"
)
class TestDetectCacheLifecycleSpark:
    """End-to-end cache contract on a real Spark session (skipped without Java).

    The test builds a real uniqueness detector, runs ``detect()`` on a tiny
    Delta table, and asserts via :class:`benchmarks.common.spark_jobs.SparkJobCounter`
    that subsequent actions (``count()``, ``collect()``, ``write``) on the returned
    frame do not trigger additional Spark jobs beyond the initial materialization.
    """

    def test_detect_returns_persisted_frame_no_reexecution_on_count_collect_write(
        self, spark
    ):
        """After ``detect()`` returns, downstream actions reuse the cached frame."""
        # Import the job counter from benchmarks
        import sys
        from pathlib import Path

        sys.path.insert(0, str(Path(__file__).parents[5] / "benchmarks"))
        from common.spark_jobs import SparkJobCounter
        from open_detect.algorithms.uni_detect.config import UniDetectConfig, UnityCatalogLocation
        from open_detect.algorithms.uni_detect.detectors.uniqueness import UniquenessDetector

        config = UniDetectConfig(
            location=UnityCatalogLocation(
                catalog="spark_catalog", schema="open_detect_test_schema"
            ),
            alpha=0.001,
        )
        detector = UniquenessDetector(spark, config)

        # Seed a tiny Delta table with some duplicate rows
        spark.sql(
            "CREATE TABLE IF NOT EXISTS spark_catalog.open_detect_test_schema.t1 "
            "(id LONG, val STRING) USING DELTA"
        )
        spark.sql(
            "INSERT INTO spark_catalog.open_detect_test_schema.t1 VALUES "
            "(1, 'a'), (2, 'a'), (3, 'b')"
        )

        counter = SparkJobCounter(spark, enabled=True)

        # Run detect -- this should launch jobs for ingestion + scoring
        with counter.scope("detect"):
            result = detector.detect(["spark_catalog.open_detect_test_schema.t1"])

        # Materialize once inside detect(); result is persisted
        detect_jobs = counter.results[0].jobs
        assert detect_jobs > 0, "detect() should have launched at least one job"

        # Now call count() -- should NOT launch additional jobs
        with counter.scope("count"):
            _ = result.count()
        assert (
            counter.results[1].jobs == 0
        ), f"count() re-executed {counter.results[1].jobs} jobs; frame should be cached"

        # collect() -- should NOT launch additional jobs
        with counter.scope("collect"):
            _ = result.limit(10).collect()
        assert (
            counter.results[2].jobs == 0
        ), f"collect() re-executed {counter.results[2].jobs} jobs; frame should be cached"

        # write -- should NOT launch additional jobs
        with counter.scope("write"):
            result.write.format("noop").mode("overwrite").save()
        assert (
            counter.results[3].jobs == 0
        ), f"write() re-executed {counter.results[3].jobs} jobs; frame should be cached"

        # Clean up
        result.unpersist()

    def test_pipeline_detect_unioned_result_no_reexecution(self, spark):
        """UniDetect.detect() returns a unioned, persisted frame with no re-execution."""
        # Import the job counter from benchmarks
        import sys
        from pathlib import Path

        sys.path.insert(0, str(Path(__file__).parents[5] / "benchmarks"))
        from common.spark_jobs import SparkJobCounter
        from open_detect.algorithms.uni_detect.config import UniDetectConfig, UnityCatalogLocation
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

        counter = SparkJobCounter(spark, enabled=True)

        with counter.scope("pipeline_detect"):
            detections = ud.detect(["spark_catalog.open_detect_test_schema.t2"])

        detect_jobs = counter.results[0].jobs
        assert detect_jobs > 0

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