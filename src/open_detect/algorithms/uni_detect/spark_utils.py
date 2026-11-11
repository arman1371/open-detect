"""Spark session helpers.

Kept deliberately tiny: on Databricks, ``SparkSession.builder.getOrCreate()``
returns the cluster's already-configured (Unity-Catalog-enabled) session.
Outside Databricks (unit tests, local development), callers are responsible
for configuring Delta Lake support -- see ``tests/conftest.py`` for the
reference local-testing session builder.
"""

from __future__ import annotations

from contextlib import contextmanager, suppress
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyspark.sql import SparkSession


def get_spark() -> SparkSession:
    from pyspark.sql import SparkSession

    spark = SparkSession.getActiveSession()
    if spark is not None:
        return spark
    return SparkSession.builder.appName("open_detect").getOrCreate()


#: ``spark.sql.execution.arrow.maxRecordsPerBatch`` controls how many rows a
#: single Arrow batch carries between the JVM and the Python worker in
#: ``DataFrame.mapInPandas``.  The default (10000) is fine for short arrays but
#: our scoring batches hold up to ``max_values_per_column`` strings per row,
#: so a batch can balloon to ~10^9 strings and OOM the executor.  64 is the
#: recommended floor for array-heavy workloads (allowed range 32-256).
ARROW_MAX_RECORDS_PER_BATCH = 64

#: Conf key whose value is restored by :func:`scoped_conf`.
ARROW_MAX_RECORDS_PER_BATCH_KEY = "spark.sql.execution.arrow.maxRecordsPerBatch"


@contextmanager
def scoped_conf(spark: SparkSession, **overrides):
    """Temporarily set Spark conf keys, restoring the previous values on exit.

    Unlike ``spark.conf.set`` this never mutates the caller's session
    permanently -- the previous values (including keys that were unset) are
    restored even if the body raises.
    """
    previous: dict[str, str | None] = {}
    try:
        for key, value in overrides.items():
            try:
                previous[key] = spark.conf.get(key)
            except Exception:
                previous[key] = None
            spark.conf.set(key, value)
        yield
    finally:
        for key, value in previous.items():
            if value is None:
                with suppress(Exception):
                    spark.conf.unset(key)
            else:
                with suppress(Exception):
                    spark.conf.set(key, value)
