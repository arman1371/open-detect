"""Local, Delta-enabled Spark session bootstrap shared by every benchmark.

Extracted from what used to be ``benchmarks/run_benchmark.py``'s own
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
    app_name: str = "unidetect-benchmark",
    driver_memory: str = "3g",
) -> Iterator[Any]:
    """Start a local, single-process, Delta-enabled Spark session for a benchmark run.

    Mirrors ``tests/conftest.py``'s setup: a two-core local master, a
    disposable warehouse directory, and a bumped driver heap (see the
    comment below on why the default is too small). Raises
    :class:`SparkUnavailable` -- never a raw Spark/py4j exception -- if the
    session cannot be started at all, so callers can distinguish "no local
    Spark/JDK available" from "the benchmark itself failed".
    """
    os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
    os.environ.setdefault("PYSPARK_DRIVER_PYTHON", sys.executable)

    from delta import configure_spark_with_delta_pip
    from pyspark.sql import SparkSession

    warehouse_dir = tempfile.mkdtemp(prefix="unidetect-benchmark-warehouse-")
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
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
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
