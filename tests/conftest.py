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
view, since all of unidetect's own code only ever treats the catalog
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
TEST_SCHEMA = "unidetect_test_schema"

_MAVEN_BASE = "https://repo1.maven.org/maven2"
_SCALA_VERSION = "2.12"


def _download(url: str, dest: Path) -> None:
    if dest.exists():
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    # Suffixed with our pid so that concurrent pytest-xdist workers racing to
    # populate the same (shared, machine-wide) cache dir download to distinct
    # files instead of both writing through the same handle -- the final
    # `os.replace` is atomic, so whichever worker finishes last just
    # overwrites the dest with an equally valid copy of the same jar.
    tmp_path = dest.with_suffix(f"{dest.suffix}.{os.getpid()}.part")
    urllib.request.urlretrieve(url, tmp_path)  # noqa: S310 - fixed https://repo1.maven.org URL
    os.replace(tmp_path, dest)


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
    cache_dir = Path(tempfile.gettempdir()) / "unidetect-test-jars" / delta_version

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
    # `unidetect` install and pandas/numpy/rapidfuzz. This must be set
    # before the JVM/SparkContext starts.
    os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
    os.environ.setdefault("PYSPARK_DRIVER_PYTHON", sys.executable)

    import importlib_metadata
    from pyspark.sql import SparkSession

    warehouse_dir = tempfile.mkdtemp(prefix="unidetect-warehouse-")
    builder = (
        SparkSession.builder.master("local[2]")
        .appName("unidetect-tests")
        .config("spark.sql.warehouse.dir", warehouse_dir)
        .config("spark.sql.shuffle.partitions", "2")
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


@pytest.fixture
def uc_location(spark):  # noqa: ANN001, ARG001
    """A throwaway Unity-Catalog-shaped location backed by the local test catalog."""
    from unidetect.config import UnityCatalogLocation

    return UnityCatalogLocation(catalog=TEST_CATALOG, schema=TEST_SCHEMA)
