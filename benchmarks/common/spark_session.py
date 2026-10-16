"""Local, Delta-enabled Spark session bootstrap shared by every benchmark.

Extracted from what used to be ``benchmarks/wiki_subset/run_benchmark.py``'s own
private ``_spark_session`` so a second (or third) benchmark doesn't need to
re-implement the same warehouse-dir/heap/Delta-catalog plumbing.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import Any


class SparkUnavailable(Exception):
    """Raised only when a local Delta-enabled Spark session cannot be started at all.

    Kept narrow and distinct from any other exception so that a real failure
    *during* a benchmark run (a bad detector result, an OOM, a bug) fails the
    script loudly instead of being swallowed as if the environment simply
    lacked Spark/Delta.
    """


def _host_memory_bytes() -> int | None:
    """Best-effort read of the RAM the JVM will actually be allowed to use.

    Prefers the cgroup limit (containers) over the host total, since the JVM
    sizes its heap from the host total and gets OOM-killed when the container
    limit is smaller.
    """
    for path in ("/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"):
        try:
            raw = Path(path).read_text().strip()
        except OSError:
            continue
        if raw in ("max", ""):
            continue
        try:
            value = int(raw)
        except ValueError:
            continue
        if value > 0:
            return value
    try:
        return int(Path("/proc/meminfo").read_text().splitlines()[0].split()[1]) * 1024
    except (OSError, IndexError, ValueError):
        return None


def _cap_driver_memory(driver_memory: str) -> str:
    """Clamp ``driver_memory`` so the JVM fits inside the host/cgroup RAM.

    Spark derives its heap from the host total, but in a container the JVM is
    still constrained by the cgroup -- a heap bigger than the cgroup gets the
    process killed mid-run. Cap at 60% of the available memory (leaving room
    for the Python driver, the OS, and the executor thread pools), and never
    below 1g.
    """
    try:
        requested = int(driver_memory.rstrip("gGmM")) * (
            1024 * 1024 * 1024 if driver_memory[-1] in "gG" else 1024 * 1024
        )
    except (ValueError, IndexError):
        return driver_memory
    host = _host_memory_bytes()
    if host is None:
        return driver_memory
    cap = max(1024 * 1024 * 1024, int(host * 0.6))
    if requested <= cap:
        return driver_memory
    unit = "g" if cap % (1024 * 1024 * 1024) == 0 else "m"
    value = cap // (1024 * 1024 * 1024) if unit == "g" else cap // (1024 * 1024)
    return f"{value}{unit}"


def git_commit(repo_root: Path) -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], cwd=repo_root, text=True
        ).strip()
    except Exception:  # noqa: BLE001
        return "unknown"


@contextmanager
def spark_session(
    catalog: str,
    schema: str,
    app_name: str = "open_detect-benchmark",
    driver_memory: str = "3g",
    count_jobs: bool = False,
) -> Iterator[Any]:
    """Start a local, single-process, Delta-enabled Spark session for a benchmark run.

    Mirrors ``tests/conftest.py``'s setup: a two-core local master, a
    disposable warehouse directory, and a bumped driver heap (see the
    comment below on why the default is too small). Raises
    :class:`SparkUnavailable` -- never a raw Spark/py4j exception -- if the
    session cannot be started at all, so callers can distinguish "no local
    Spark/JDK available" from "the benchmark itself failed".

    ``count_jobs=True`` raises the retained-jobs/stages limits so
    :class:`common.spark_jobs.SparkJobCounter` can read every job back.
    """
    os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
    os.environ.setdefault("PYSPARK_DRIVER_PYTHON", sys.executable)

    from delta import configure_spark_with_delta_pip
    from pyspark.sql import SparkSession

    warehouse_dir = tempfile.mkdtemp(prefix="open_detect-benchmark-warehouse-")
    # The driver JVM runs in the same cgroup as this process, so an
    # over-allocated heap gets OOM-killed mid-run (the executor thread pool is
    # torn out from under Spark, surfacing as RejectedExecutionException, not
    # as a clean OutOfMemoryError). Cap the heap at a safe fraction of the
    # available RAM and let the caller raise it on a bigger machine.
    driver_memory = _cap_driver_memory(driver_memory)
    builder = (
        SparkSession.builder.master("local[2]")
        .appName(app_name)
        .config("spark.sql.warehouse.dir", warehouse_dir)
        .config("spark.sql.shuffle.partitions", "2")
        .config("spark.ui.enabled", "false")
        # Default driver heap is too small: corpus/store.py's
        # load_token_stats_map() calls `.orderBy(...).limit(max_tokens)` with
        # a default max_tokens of 5,000,000, and Spark's
        # TakeOrderedAndProjectExec pre-sizes an ordering buffer proportional
        # to that limit regardless of the token table's actual (tiny) size --
        # an OutOfMemoryError on the default heap, not a sign of anything
        # wrong with a benchmark's own data or config.
        .config("spark.driver.memory", driver_memory)
        .config("spark.driver.maxResultSize", "1g")
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
    )
    if count_jobs:
        from common.spark_jobs import RETAINED_LIMIT

        builder = builder.config("spark.ui.retainedJobs", str(RETAINED_LIMIT)).config(
            "spark.ui.retainedStages", str(RETAINED_LIMIT)
        )
    try:
        session = configure_spark_with_delta_pip(builder).getOrCreate()
        session.sparkContext.setLogLevel("ERROR")
        session.sql(f"CREATE NAMESPACE IF NOT EXISTS {catalog}.{schema}")
    except Exception as exc:  # noqa: BLE001
        shutil.rmtree(warehouse_dir, ignore_errors=True)
        raise SparkUnavailable(str(exc)) from exc

    try:
        yield session
    finally:
        session.stop()
        shutil.rmtree(warehouse_dir, ignore_errors=True)
