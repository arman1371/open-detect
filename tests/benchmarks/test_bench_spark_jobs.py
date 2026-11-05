"""Java-free tests for ``benchmarks/common/spark_jobs.py`` using a fake SparkContext."""

from __future__ import annotations

import sys
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "benchmarks"))
from common.spark_jobs import SparkJobCounter  # noqa: E402


class _FakeTracker:
    def __init__(self, jobs_by_group: dict[str, list[int]], stages: dict[int, list[int]]) -> None:
        self._jobs_by_group = jobs_by_group
        self._stages = stages

    def getJobIdsForGroup(self, group: str) -> list[int]:  # noqa: N802
        return self._jobs_by_group.get(group, [])

    def getJobInfo(self, job_id: int):  # noqa: N802
        if job_id not in self._stages:
            return None
        return SimpleNamespace(stageIds=self._stages[job_id])


class _FakeContext:
    def __init__(self) -> None:
        self.groups: list[str] = []
        self.tracker = _FakeTracker({}, {})

    def setJobGroup(self, group: str, description: str) -> None:  # noqa: N802
        self.groups.append(group)

    def statusTracker(self) -> _FakeTracker:  # noqa: N802
        return self.tracker


def _spark(ctx: _FakeContext) -> SimpleNamespace:
    return SimpleNamespace(sparkContext=ctx)


def test_counts_jobs_and_distinct_stages_per_scope() -> None:
    ctx = _FakeContext()
    counter = SparkJobCounter(_spark(ctx))
    with counter.scope("detect[x]"):
        group = ctx.groups[-1]
        # Stage 2 is shared (skipped/reused) between two jobs and counts once.
        ctx.tracker = _FakeTracker({group: [10, 11, 12]}, {10: [1, 2], 11: [2, 3], 12: []})
    (stats,) = counter.results
    assert (stats.label, stats.jobs, stats.stages, stats.evicted_jobs) == ("detect[x]", 3, 3, 0)
    assert stats.wall_seconds >= 0
    assert ctx.groups[-1] == ""  # job group reset afterwards


def test_evicted_jobs_are_reported() -> None:
    ctx = _FakeContext()
    counter = SparkJobCounter(_spark(ctx))
    with counter.scope("s"):
        group = ctx.groups[-1]
        ctx.tracker = _FakeTracker({group: [1, 2]}, {1: [5]})
    assert (counter.results[0].jobs, counter.results[0].evicted_jobs) == (2, 1)


def test_disabled_counter_is_a_noop() -> None:
    ctx = _FakeContext()
    counter = SparkJobCounter(_spark(ctx), enabled=False)
    with counter.scope("s"):
        pass
    assert counter.results == []
    assert ctx.groups == []


def test_scopes_use_distinct_job_groups() -> None:
    ctx = _FakeContext()
    counter = SparkJobCounter(_spark(ctx))
    with counter.scope("a"):
        pass
    with counter.scope("a"):
        pass
    groups = [g for g in ctx.groups if g]
    assert len(set(groups)) == 2
    assert [r["label"] for r in counter.to_list()] == ["a", "a"]
