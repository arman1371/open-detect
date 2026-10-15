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
