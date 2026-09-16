"""Unity Catalog convenience helpers.

Thin wrappers around Spark SQL DDL/catalog APIs -- deliberately not a
dependency on ``databricks-sdk``, since everything needed here (creating
schemas, listing tables, checking existence, writing Delta tables under a
three-level name) is already exposed through a Unity-Catalog-enabled
``SparkSession``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from unidetect.config import UnityCatalogLocation
from unidetect.exceptions import UnityCatalogError
from unidetect.logging_utils import get_logger

if TYPE_CHECKING:
    from pyspark.sql import SparkSession

logger = get_logger(__name__)


def ensure_schema_exists(spark: SparkSession, location: UnityCatalogLocation) -> None:
    """Create the catalog/schema if they do not already exist.

    Requires ``CREATE CATALOG``/``CREATE SCHEMA`` privileges; callers running
    with least-privilege service principals should instead pre-create the
    schema and grant ``USE CATALOG``/``USE SCHEMA``/``CREATE TABLE``, and can
    skip calling this helper.
    """
    try:
        spark.sql(f"CREATE CATALOG IF NOT EXISTS `{location.catalog}`")
        spark.sql(f"CREATE SCHEMA IF NOT EXISTS `{location.catalog}`.`{location.schema}`")
    except Exception as exc:  # noqa: BLE001
        raise UnityCatalogError(
            f"Failed to ensure {location.catalog}.{location.schema} exists: {exc}"
        ) from exc


def list_tables(spark: SparkSession, catalog: str, schema: str) -> list[str]:
    """Return fully-qualified names of every table in ``catalog.schema``."""
    rows = spark.sql(f"SHOW TABLES IN `{catalog}`.`{schema}`").collect()
    return [f"{catalog}.{schema}.{row['tableName']}" for row in rows]


def list_tables_matching(
    spark: SparkSession, catalog: str, schemas: list[str] | None = None
) -> list[str]:
    """Return fully-qualified table names across one or more schemas in ``catalog``.

    If ``schemas`` is ``None``, every schema in the catalog is scanned. This
    is the typical way to instantiate the background corpus ``T`` as "every
    table this catalog already governs" (see ``corpus/ingestion.py``).
    """
    if schemas is None:
        rows = spark.sql(f"SHOW SCHEMAS IN `{catalog}`").collect()
        schemas = [row["databaseName"] for row in rows]

    tables: list[str] = []
    for schema in schemas:
        try:
            tables.extend(list_tables(spark, catalog, schema))
        except Exception:  # noqa: BLE001
            logger.exception("Skipping schema %s.%s: could not list tables", catalog, schema)
    return tables


def table_exists(spark: SparkSession, fqn: str) -> bool:
    return spark.catalog.tableExists(fqn)
