"""Shared pytest fixtures.

The Spark-backed fixture configures a local, Delta-enabled session so tests
exercise the real Delta write/read paths used on Databricks. Building that
session requires resolving the ``io.delta:delta-spark`` Maven coordinate the
first time it runs on a given machine; if that resolution is impossible
(fully air-gapped CI runner, no ivy/maven cache), Spark/Delta-dependent
tests are skipped rather than failing the whole suite -- the pure-Python
algorithmic tests (``test_metrics.py``, ``test_perturbation.py``,
``test_featurization.py``) do not depend on this fixture at all and always
run.

A local, non-Unity-Catalog Spark session only has one real catalog:
``spark_catalog``, the built-in default. Delta's ``DeltaCatalog`` is a
*delegating* catalog extension meant to override ``spark_catalog`` in place
-- it cannot be registered as an additional, independently-named catalog
(doing so raises a ``NullPointerException`` deep in Spark's analyzer, since
it has nothing to delegate to). So locally we address tables as
``spark_catalog.<schema>.<table>``, which Spark resolves natively and which
is a fully qualified three-level name -- a faithful stand-in for Unity
Catalog's ``<catalog>.<schema>.<table>`` shape from the library's point of
view, since all of open_detect's own code only ever treats the catalog
component as an opaque string.
"""

from __future__ import annotations

import os
import re
import shutil
import sys
import tempfile
import urllib.request
from collections.abc import Iterator
from pathlib import Path

import pytest

TEST_CATALOG = "spark_catalog"
TEST_SCHEMA = "open_detect_test_schema"

_MAVEN_BASE = "https://repo1.maven.org/maven2"
_SCALA_VERSION = "2.13"


# Known cgroup-v1 unlimited sentinels (max signed 64-bit, page-aligned variants)
_UNLIMITED_SENTINELS = {
    9223372036854771712,  # 2^63 - 2^26
    9223372036854775807,  # 2^63 - 1
    18446744073709551615,  # 2^64 - 1
}


def _host_memory_bytes() -> int | None:
    """Best-effort read of the RAM the JVM will actually be allowed to use.

    Prefers the cgroup limit (containers) over the host total, since the JVM
    sizes its heap from the host total and gets OOM-killed when the container
    limit is smaller. On cgroup-v1 systems without an enforced limit,
    ``memory.limit_in_bytes`` commonly holds a huge unlimited sentinel, so we
    detect and ignore such sentinels. The returned value is the **minimum**
    of the physical RAM and the cgroup limit.
    """
    physical: int | None = None
    cgroup: int | None = None
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
        if value > 0 and value not in _UNLIMITED_SENTINELS:
            cgroup = value
            break
    try:
        physical = int(Path("/proc/meminfo").read_text().splitlines()[0].split()[1]) * 1024
    except (OSError, IndexError, ValueError):
        physical = None
    if physical is not None and cgroup is not None:
        return min(physical, cgroup)
    return physical if physical is not None else cgroup


def _cap_driver_memory(driver_memory: str) -> str:
    """Clamp ``driver_memory`` so the JVM fits inside the host/cgroup RAM.

    Spark derives its heap from the host total, but in a container the JVM is
    still constrained by the cgroup -- a heap bigger than the cgroup gets the
    process killed mid-run. Cap at 60% of the available memory (leaving room
    for the Python driver, the OS, and the executor thread pools).
    Raises ValueError when the available budget cannot support even a minimal
    heap (512m), so callers never start a session that is guaranteed to be
    OOM-killed.
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
    cap = int(host * 0.6)
    # Minimum usable heap is 512m, not 1g - the 1g floor can exceed
    # small container budgets (e.g. 768 MiB cgroup -> 1g heap leaves no room
    # for Python/OS and reproduces the OOM-kill this guard prevents).
    MIN_DRIVER_MEMORY_BYTES = 512 * 1024 * 1024  # 512m
    if cap < MIN_DRIVER_MEMORY_BYTES:
        # The available memory cannot support even a minimal heap.
        raise ValueError(
            f"cannot start Spark: available memory {host} bytes cannot support the "
            f"minimum {MIN_DRIVER_MEMORY_BYTES // (1024 * 1024)}m driver heap"
        )
    if requested <= cap:
        return driver_memory
    unit = "g" if cap % (1024 * 1024 * 1024) == 0 else "m"
    value = cap // (1024 * 1024 * 1024) if unit == "g" else cap // (1024 * 1024)
    return f"{value}{unit}"


def _download(url: str, dest: Path) -> None:
    if dest.exists():
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = dest.with_suffix(dest.suffix + ".part")
    urllib.request.urlretrieve(url, tmp_path)  # noqa: S310 - fixed https://repo1.maven.org URL
    tmp_path.rename(dest)


def _delta_jars(delta_version: str) -> list[str]:
    """Download Delta's runtime JARs directly from Maven Central over plain HTTPS.

    ``configure_spark_with_delta_pip`` instead sets ``spark.jars.packages``,
    which makes the JVM resolve the same coordinates itself via Ivy at
    ``SparkSession`` startup. That has been observed to silently fail to
    register ``DeltaCatalog`` on the classpath in some CI sandboxes (the JVM
    starts and plain SQL works, but the first Delta-catalog operation raises
    ``ClassNotFoundException: ...DeltaCatalog``), even though a plain HTTPS
    GET to the very same Maven Central host succeeds -- and this project's
    own dependency install (``uv sync``) already relies on that same kind of
    plain-HTTPS resolution working. Downloading the jars ourselves and
    passing local paths via ``spark.jars`` sidesteps the JVM-side Ivy
    resolution path entirely.
    """
    cache_dir = Path(tempfile.gettempdir()) / "open_detect-test-jars" / delta_version

    pom_url = (
        f"{_MAVEN_BASE}/io/delta/delta-spark_{_SCALA_VERSION}/{delta_version}/"
        f"delta-spark_{_SCALA_VERSION}-{delta_version}.pom"
    )
    with urllib.request.urlopen(pom_url) as resp:  # noqa: S310 - fixed https://repo1.maven.org URL
        pom_text = resp.read().decode()
    match = re.search(
        r"<artifactId>antlr4-runtime</artifactId>\s*<version>([^<]+)</version>", pom_text
    )
    if not match:
        raise RuntimeError("Could not find antlr4-runtime's version in delta-spark's POM")
    antlr_version = match.group(1)

    coords = [
        ("io/delta", f"delta-spark_{_SCALA_VERSION}", delta_version),
        ("io/delta", "delta-storage", delta_version),
        ("org/antlr", "antlr4-runtime", antlr_version),
    ]
    jar_paths = []
    for group_path, artifact, version in coords:
        filename = f"{artifact}-{version}.jar"
        dest = cache_dir / filename
        _download(f"{_MAVEN_BASE}/{group_path}/{artifact}/{version}/{filename}", dest)
        jar_paths.append(str(dest))
    return jar_paths


@pytest.fixture(scope="session")
def spark() -> Iterator[pyspark.sql.SparkSession]:  # noqa: F821
    pytest.importorskip("pyspark")
    pytest.importorskip("delta")

    # PySpark spawns executor/worker processes via the "python3" found on
    # PATH by default, not via sys.executable -- so without this, workers
    # can silently run a *different* Python than the driver (e.g. the
    # system interpreter instead of this venv), missing both the editable
    # `open_detect` install and pandas/numpy/rapidfuzz. This must be set
    # before the JVM/SparkContext starts.
    os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
    os.environ.setdefault("PYSPARK_DRIVER_PYTHON", sys.executable)

    import importlib_metadata
    from pyspark.sql import SparkSession

    warehouse_dir = tempfile.mkdtemp(prefix="open_detect-warehouse-")
    # Cap driver/executor memory to fit within the CI runner's memory limit.
    # The benchmark's spark_session.py uses the same dynamic approach (60% cap, 512m min).
    # In local mode, executor runs in the same JVM as driver, so we only set driver memory
    # and cap it to fit. executor.memory is ignored in local mode but we keep a safe value.
    try:
        driver_memory = _cap_driver_memory("2g")
    except ValueError as exc:
        pytest.skip(f"Could not start a local Delta-enabled Spark session: {exc}")
        return
    executor_memory = driver_memory  # local mode: same JVM
    builder = (
        SparkSession.builder.master("local[2]")
        .appName("open_detect-tests")
        .config("spark.sql.warehouse.dir", warehouse_dir)
        .config("spark.sql.shuffle.partitions", "2")
        .config("spark.default.parallelism", "2")
        # Default driver heap is too small: ``mapInPandas`` scoring carries up to
        # ``max_values_per_column`` strings per row, so a single Arrow batch can
        # balloon to ~10^9 strings and OOM the executor on the default 1g heap.
        # Mirrors benchmarks/common/spark_session.py, which bumped this for the
        # same reason (corpus/store.py's load_token_stats_map() pre-sizes an
        # ordering buffer proportional to max_tokens; default 500k fits in 4g).
        # CI runners have limited memory (7GB total), so cap heaps to fit.
        .config("spark.driver.memory", driver_memory)
        .config("spark.executor.memory", executor_memory)
        .config("spark.driver.maxResultSize", "1g")
        # Delta replays its transaction log with this many partitions on every
        # snapshot load (default 50) -- pure overhead for tiny test tables.
        .config("spark.databricks.delta.snapshotPartitions", "2")
        .config("spark.ui.enabled", "false")
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
    )

    session = None
    try:
        jars = _delta_jars(importlib_metadata.version("delta_spark"))
        builder = builder.config("spark.jars", ",".join(jars))
        session = builder.getOrCreate()
        session.sparkContext.setLogLevel("ERROR")
        session.sql("SELECT 1").collect()
        session.sql(f"CREATE NAMESPACE IF NOT EXISTS {TEST_CATALOG}.{TEST_SCHEMA}")
    except Exception as exc:  # noqa: BLE001
        if session is not None:
            session.stop()
        pytest.skip(f"Could not start a local Delta-enabled Spark session: {exc}")
        return

    yield session

    session.stop()
    shutil.rmtree(warehouse_dir, ignore_errors=True)


@pytest.fixture(scope="session")
def uc_location(spark):  # noqa: ANN001, ARG001
    """A throwaway Unity-Catalog-shaped location backed by the local test catalog."""
    from open_detect.algorithms.uni_detect.config import UnityCatalogLocation

    return UnityCatalogLocation(catalog=TEST_CATALOG, schema=TEST_SCHEMA)
