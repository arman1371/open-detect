# Databricks notebook source
# MAGIC %md
# MAGIC # Uni-Detect: Build Corpus Statistics (offline)
# MAGIC
# MAGIC This notebook runs the "learning" phase of Uni-Detect (paper Section 2.2.3):
# MAGIC it scans a background corpus of tables `T` -- here, every table already
# MAGIC registered under a Unity Catalog catalog/set of schemas -- and materializes
# MAGIC the `(feature_bucket, theta_before, theta_after)` statistics every online
# MAGIC detector will look up against.
# MAGIC
# MAGIC Run this on a schedule (e.g. weekly) via the `build_corpus_statistics_job`
# MAGIC Databricks Job defined in `databricks.yml` -- it does not need to run on
# MAGIC every detection call.

# COMMAND ----------

# MAGIC %pip install -e ..
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

dbutils.widgets.text("unidetect_catalog", "main", "Catalog for unidetect's own tables")
dbutils.widgets.text("unidetect_schema", "data_quality", "Schema for unidetect's own tables")
dbutils.widgets.text("corpus_catalog", "main", "Catalog to scan for the background corpus")
dbutils.widgets.text("corpus_schemas", "", "Comma-separated schemas to scan (blank = all schemas)")
dbutils.widgets.text("error_types", "uniqueness,numeric_outlier,spelling,functional_dependency", "Error types")

# COMMAND ----------

from unidetect.catalog import ensure_schema_exists, list_tables_matching
from unidetect.config import UniDetectConfig, UnityCatalogLocation
from unidetect.core.enums import ErrorType
from unidetect.pipeline import UniDetect

unidetect_catalog = dbutils.widgets.get("unidetect_catalog")
unidetect_schema = dbutils.widgets.get("unidetect_schema")
corpus_catalog = dbutils.widgets.get("corpus_catalog")
corpus_schemas_raw = dbutils.widgets.get("corpus_schemas").strip()
corpus_schemas = [s.strip() for s in corpus_schemas_raw.split(",")] if corpus_schemas_raw else None
error_types = [ErrorType(e.strip()) for e in dbutils.widgets.get("error_types").split(",") if e.strip()]

location = UnityCatalogLocation(catalog=unidetect_catalog, schema=unidetect_schema)
config = UniDetectConfig(location=location)
ensure_schema_exists(spark, location)

# COMMAND ----------

corpus_tables = list_tables_matching(spark, corpus_catalog, corpus_schemas)
print(f"Resolved {len(corpus_tables)} corpus tables from {corpus_catalog} ({corpus_schemas or 'all schemas'})")
displayHTML("<br>".join(corpus_tables[:50]) + ("<br>..." if len(corpus_tables) > 50 else ""))

# COMMAND ----------

ud = UniDetect(config, spark=spark)
ud.build_corpus_statistics(corpus_tables, error_types=error_types, create_schema=False)

# COMMAND ----------

display(spark.table(config.corpus_stats_fqn).groupBy("error_type").count())
