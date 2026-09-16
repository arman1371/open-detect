"""Spark session helpers.

Kept deliberately tiny: on Databricks, ``SparkSession.builder.getOrCreate()``
returns the cluster's already-configured (Unity-Catalog-enabled) session.
Outside Databricks (unit tests, local development), callers are responsible
for configuring Delta Lake support -- see ``tests/conftest.py`` for the
reference local-testing session builder.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyspark.sql import SparkSession


def get_spark() -> SparkSession:
    from pyspark.sql import SparkSession

    spark = SparkSession.getActiveSession()
    if spark is not None:
        return spark
    return SparkSession.builder.appName("unidetect").getOrCreate()
