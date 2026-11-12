"""Opt-in Spark job/stage counter for benchmark runs.

Performance work on Uni-Detect is dominated by Spark plan/job overhead, so a
benchmark needs to report *how many* jobs and stages a ``detect()`` call
launched, not just wall time. :class:`SparkJobCounter` tags every job started
inside a ``scope(label)`` block with a unique Spark job group and reads the job
and stage ids back from ``SparkContext.statusTracker()`` afterwards.

It is opt-in: a disabled counter's ``scope`` is a no-op, so normal benchmark
runs are unaffected. :func:`spark_session` raises ``spark.ui.retainedJobs`` /
``spark.ui.retainedStages`` when counting is enabled (the status tracker only
remembers the last 1000 jobs by default).
"""

from __future__ import annotations

import time
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import asdict, dataclass
from typing import Any

#: Retained-jobs/stages limit applied to the Spark session when counting is on.
RETAINED_LIMIT = 1_000_000


@dataclass(frozen=True)
class ScopeStats:
    """Jobs/stages launched, and wall time taken, inside one ``scope`` block."""

    label: str
    jobs: int
    stages: int
    wall_seconds: float
    #: Jobs the status tracker no longer knew about (counted in ``jobs`` but not ``stages``).
    evicted_jobs: int = 0

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class SparkJobCounter:
    """Counts Spark jobs and stages per labelled scope. No-op when ``enabled`` is false."""

    def __init__(self, spark: Any, enabled: bool = True) -> None:
        self._spark = spark
        self.enabled = enabled
        self.results: list[ScopeStats] = []
        self._sequence = 0

    @contextmanager
    def scope(self, label: str) -> Iterator[None]:
        if not self.enabled:
            yield
            return

        sc = self._spark.sparkContext
        self._sequence += 1
        group = f"open_detect-bench-{self._sequence}-{label}"
        sc.setJobGroup(group, label)
        start = time.perf_counter()
        try:
            yield
        finally:
            wall = time.perf_counter() - start
            tracker = sc.statusTracker()
            job_ids = list(tracker.getJobIdsForGroup(group))
            stage_ids: set[int] = set()
            evicted = 0
            for job_id in job_ids:
                info = tracker.getJobInfo(job_id)
                if info is None:
                    evicted += 1
                else:
                    stage_ids.update(info.stageIds)
            sc.setJobGroup("", "")
            self.results.append(
                ScopeStats(
                    label=label,
                    jobs=len(job_ids),
                    stages=len(stage_ids),
                    wall_seconds=wall,
                    evicted_jobs=evicted,
                )
            )

    def to_list(self) -> list[dict[str, Any]]:
        return [r.to_dict() for r in self.results]


class ScoringJobCounter:
    """Counts scoring computation executions per labelled scope.

    Unlike :class:`SparkJobCounter` which counts all Spark jobs, this counter
    instruments the specific scoring computation (``batch_score`` in
    :mod:`open_detect.algorithms.uni_detect.corpus.store`) to assert that
    downstream actions on the returned frame (``count()``, ``collect()``,
    ``write()``) do not re-execute the scoring stage.

    It uses an executor-side accumulator to count each partition evaluation
    of the scoring DataFrame, which corresponds to actual scoring executions
    (not just plan construction).

    Use as a context manager to ensure the global ``batch_score`` patch is
    restored on exit:

        with ScoringJobCounter(spark) as counter:
            with counter.scope("detect"):
                result = detector.detect(...)
            with counter.scope("count"):
                result.count()
    """

    def __init__(self, spark: Any, enabled: bool = True) -> None:
        self._spark = spark
        self.enabled = enabled
        self.results: list[ScopeStats] = []
        self._sequence = 0
        self._acc: Any = None
        self._original_batch_score: Any = None
        self._patched = False

    def __enter__(self) -> ScoringJobCounter:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self._restore_batch_score()

    def _restore_batch_score(self) -> None:
        """Restore the original ``batch_score`` method if it was patched."""
        if self._patched and self._original_batch_score is not None:
            from open_detect.algorithms.uni_detect.corpus.store import CorpusStatsStore

            CorpusStatsStore.batch_score = self._original_batch_score
            self._patched = False
            self._original_batch_score = None

    @contextmanager
    def scope(self, label: str) -> Iterator[None]:
        if not self.enabled:
            yield
            return

        from open_detect.algorithms.uni_detect.corpus.store import CorpusStatsStore

        # Reuse one accumulator across scopes. A scoring plan built inside an
        # earlier scope retains a reference to the accumulator captured when
        # batch_score was patched, so re-executing that plan later updates the
        # same accumulator. Creating a fresh accumulator per scope would report
        # zero for any recomputation that happens outside the scope that built
        # the plan.
        if self._acc is None:
            self._acc = self._spark.sparkContext.accumulator(0)

        # Install the batch_score wrapper only in the outermost scope. Nested
        # scopes share the accumulator but must not re-wrap an already-wrapped
        # method, and only the scope that installed the wrapper should restore
        # it on exit. The original method is captured in a local closure cell so
        # that nested scopes or later installations cannot change the wrapper's
        # target mid-flight.
        if not self._patched:
            original_batch_score = CorpusStatsStore.batch_score
            self._original_batch_score = original_batch_score
            acc = self._acc

            def counting_batch_score(self_arg, *args, **kwargs):
                scored_df = original_batch_score(self_arg, *args, **kwargs)

                # Wrap the scoring DataFrame with a mapInPandas that increments
                # the accumulator for each partition evaluated. This counts actual
                # scoring executions, not just plan construction.
                def increment_acc(iterator):
                    # Increment once per partition evaluation
                    acc.add(1)
                    yield from iterator

                # Use mapInPandas to inject the side effect while preserving schema
                return scored_df.mapInPandas(increment_acc, schema=scored_df.schema)

            CorpusStatsStore.batch_score = counting_batch_score
            self._patched = True

        acc = self._acc
        baseline = acc.value
        self._sequence += 1
        try:
            yield
        finally:
            executions = acc.value - baseline
            # Restore the original batch_score after the scope exits so that
            # subsequent scopes or callers are not affected by this scope's
            # patching. Only the scope that installed the wrapper restores it;
            # nested scopes leave the wrapper in place so previously constructed
            # plans keep reporting into the shared accumulator.
            if self._patched:
                CorpusStatsStore.batch_score = self._original_batch_score
                self._patched = False
                self._original_batch_score = None
            self.results.append(
                ScopeStats(
                    label=label,
                    jobs=executions,
                    stages=0,
                    wall_seconds=0.0,
                    evicted_jobs=0,
                )
            )

    def to_list(self) -> list[dict[str, Any]]:
        return [r.to_dict() for r in self.results]
