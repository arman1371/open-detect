"""Opt-in performance profile (Spark job counts + detections snapshot) for a benchmark run.

Enabled by ``run_benchmark.py --profile-dir DIR``. Writes two files into ``DIR``:

- ``detections.csv`` -- the Uni-Detect detections snapshot (see :mod:`common.snapshot`).
- ``perf.json`` -- per-phase wall time and Spark job/stage counts, plus the
  Spark/host configuration the numbers were measured on.

Without ``--profile-dir`` none of this runs and a benchmark behaves as before.
"""

from __future__ import annotations

import json
import os
import platform
from collections.abc import Iterator
from contextlib import AbstractContextManager, contextmanager, nullcontext
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd

from common.snapshot import save_snapshot
from common.spark_jobs import SparkJobCounter

PERF_FILENAME = "perf.json"


class UniDetectProfile:
    """Collects job counts and detections for one benchmark's Uni-Detect run."""

    def __init__(self, out_dir: Path, benchmark: str) -> None:
        self.out_dir = out_dir
        self.benchmark = benchmark
        self._counter: SparkJobCounter | None = None
        self._spark: Any = None
        self._detections: list[pd.DataFrame] = []

    def attach(self, spark: Any) -> None:
        self._spark = spark
        self._counter = SparkJobCounter(spark)

    def scope(self, label: str) -> AbstractContextManager[None]:
        if self._counter is None:
            return nullcontext()
        return self._counter.scope(label)

    def add_detections(self, detections: pd.DataFrame) -> None:
        self._detections.append(detections)

    def finalize(self, git_commit: str, wall_seconds: float) -> Path:
        """Write ``detections.csv`` and ``perf.json``; ``wall_seconds`` is the whole Uni-Detect run."""
        frame = (
            pd.concat(self._detections, ignore_index=True) if self._detections else pd.DataFrame()
        )
        save_snapshot(frame, self.out_dir)
        conf = self._spark.sparkContext.getConf() if self._spark is not None else None

        def _conf(key: str) -> str | None:
            return conf.get(key, None) if conf is not None else None

        perf = {
            "benchmark": self.benchmark,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "git_commit": git_commit,
            "uni_detect_wall_seconds_including_profiling": wall_seconds,
            "detections_rows": int(len(frame)),
            "scopes": self._counter.to_list() if self._counter else [],
            "spark": {
                "version": self._spark.version if self._spark is not None else None,
                "master": _conf("spark.master"),
                "driver_memory": _conf("spark.driver.memory"),
                "shuffle_partitions": _conf("spark.sql.shuffle.partitions"),
            },
            "host": {
                "platform": platform.platform(),
                "python": platform.python_version(),
                "cpu_count": os.cpu_count(),
            },
        }
        perf_path = self.out_dir / PERF_FILENAME
        perf_path.write_text(json.dumps(perf, indent=2) + "\n")
        return perf_path


@contextmanager
def maybe_scope(profile: UniDetectProfile | None, label: str) -> Iterator[None]:
    """``profile.scope(label)`` when profiling, otherwise a no-op."""
    if profile is None:
        yield
    else:
        with profile.scope(label):
            yield
