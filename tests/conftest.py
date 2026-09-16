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
import shutil
import sys
import tempfile
from collections.abc import Iterator

import pytest

TEST_CATALOG = "spark_catalog"
TEST_SCHEMA = "unidetect_test_schema"


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

    from delta import configure_spark_with_delta_pip
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
        session = configure_spark_with_delta_pip(builder).getOrCreate()
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
