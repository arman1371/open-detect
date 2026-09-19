"""Unit tests for catalog.py using a mocked SparkSession (no real cluster required).

``catalog.py`` only type-hints its ``spark`` parameter under ``TYPE_CHECKING``
and calls plain ``spark.sql(...)``/``spark.catalog.*`` methods at runtime, so a
``MagicMock`` standing in for a real :class:`~pyspark.sql.SparkSession` is
sufficient to exercise every branch here without starting a JVM.
"""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from unidetect.catalog import (
    ensure_schema_exists,
    list_tables,
    list_tables_matching,
    table_exists,
)
from unidetect.config import UnityCatalogLocation
from unidetect.exceptions import UnityCatalogError


class TestEnsureSchemaExists:
    def test_issues_create_catalog_and_schema_statements(self):
        spark = MagicMock()
        location = UnityCatalogLocation(catalog="main", schema="data_quality")

        ensure_schema_exists(spark, location)

        calls = [c.args[0] for c in spark.sql.call_args_list]
        assert any("CREATE CATALOG IF NOT EXISTS `main`" in c for c in calls)
        assert any("CREATE SCHEMA IF NOT EXISTS `main`.`data_quality`" in c for c in calls)

    def test_wraps_failures_in_unity_catalog_error(self):
        spark = MagicMock()
        spark.sql.side_effect = RuntimeError("no privileges")
        location = UnityCatalogLocation(catalog="main", schema="data_quality")

        with pytest.raises(UnityCatalogError, match="Failed to ensure main.data_quality"):
            ensure_schema_exists(spark, location)


class TestListTables:
    def test_returns_fully_qualified_names(self):
        spark = MagicMock()
        spark.sql.return_value.collect.return_value = [
            {"tableName": "orders"},
            {"tableName": "customers"},
        ]

        result = list_tables(spark, "main", "sales")

        assert result == ["main.sales.orders", "main.sales.customers"]
        spark.sql.assert_called_once_with("SHOW TABLES IN `main`.`sales`")


class TestListTablesMatching:
    def test_scans_every_schema_when_none_given(self):
        spark = MagicMock()

        def fake_sql(query: str):
            result = MagicMock()
            if "SHOW SCHEMAS" in query:
                result.collect.return_value = [{"databaseName": "sales"}, {"databaseName": "hr"}]
            elif "sales" in query:
                result.collect.return_value = [{"tableName": "orders"}]
            elif "hr" in query:
                result.collect.return_value = [{"tableName": "employees"}]
            return result

        spark.sql.side_effect = fake_sql

        result = list_tables_matching(spark, "main")

        assert set(result) == {"main.sales.orders", "main.hr.employees"}

    def test_uses_explicit_schema_list_without_show_schemas(self):
        spark = MagicMock()
        spark.sql.return_value.collect.return_value = [{"tableName": "orders"}]

        result = list_tables_matching(spark, "main", schemas=["sales"])

        assert result == ["main.sales.orders"]
        queries = [c.args[0] for c in spark.sql.call_args_list]
        assert not any("SHOW SCHEMAS" in q for q in queries)

    def test_skips_schema_that_fails_to_list(self):
        spark = MagicMock()

        def fake_sql(query: str):
            result = MagicMock()
            if "broken" in query:
                raise RuntimeError("permission denied")
            result.collect.return_value = [{"tableName": "orders"}]
            return result

        spark.sql.side_effect = fake_sql

        result = list_tables_matching(spark, "main", schemas=["broken", "sales"])

        assert result == ["main.sales.orders"]


class TestTableExists:
    def test_delegates_to_spark_catalog(self):
        spark = MagicMock()
        spark.catalog.tableExists.return_value = True

        assert table_exists(spark, "main.sales.orders") is True
        spark.catalog.tableExists.assert_called_once_with("main.sales.orders")
