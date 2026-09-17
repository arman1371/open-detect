# Databricks notebook source
# MAGIC %md
# MAGIC # Uni-Detect: Scan Tables for Errors (online)
# MAGIC
# MAGIC This notebook runs the online detection phase of Uni-Detect: it scores one
# MAGIC or more target tables against the corpus statistics built by
# MAGIC `01_build_corpus_statistics`, and displays the ranked, explainable results.
# MAGIC
# MAGIC For unattended scanning (e.g. nightly data-quality checks across a schema),
# MAGIC use the `run_detection_job` Databricks Job in `databricks.yml` instead.

# COMMAND ----------

# MAGIC %pip install -e ..
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

dbutils.widgets.text("unidetect_catalog", "main", "Catalog holding unidetect's own tables")
dbutils.widgets.text("unidetect_schema", "data_quality", "Schema holding unidetect's own tables")
dbutils.widgets.text("target_tables", "", "Comma-separated fully-qualified tables to scan")
dbutils.widgets.text("error_types", "uniqueness,numeric_outlier,spelling,functional_dependency", "Error types")
dbutils.widgets.text("alpha", "0.05", "Significance level (lower = fewer, higher-confidence results)")

# COMMAND ----------

import json

from unidetect.config import UniDetectConfig, UnityCatalogLocation
from unidetect.core.enums import ErrorType
from unidetect.pipeline import UniDetect

location = UnityCatalogLocation(
    catalog=dbutils.widgets.get("unidetect_catalog"), schema=dbutils.widgets.get("unidetect_schema")
)
config = UniDetectConfig(location=location, alpha=float(dbutils.widgets.get("alpha")))
target_tables = [t.strip() for t in dbutils.widgets.get("target_tables").split(",") if t.strip()]
error_types = [ErrorType(e.strip()) for e in dbutils.widgets.get("error_types").split(",") if e.strip()]

assert target_tables, "Set the target_tables widget to a comma-separated list of tables to scan."

# COMMAND ----------

ud = UniDetect(config, spark=spark)
detections = ud.detect(target_tables, error_types=error_types)
detections.cache()

print(f"{detections.count()} candidate(s) scored; {detections.where('is_significant').count()} significant at alpha={config.alpha}")
display(detections.orderBy("lr_ratio"))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Explainable evidence for the top findings
# MAGIC
# MAGIC `evidence_json` carries type-specific, human-readable context (the
# MAGIC offending value pair for spelling, the duplicate values for uniqueness,
# MAGIC the outlier value for numeric outliers, or the violating (lhs, rhs)
# MAGIC examples for functional dependencies).

# COMMAND ----------

top = detections.where("is_significant").orderBy("lr_ratio").limit(20).toPandas()
top["evidence"] = top["evidence_json"].apply(json.loads)
display(top[["error_type", "table_id", "column_names", "lr_ratio", "surprisal", "evidence"]])

# COMMAND ----------

# MAGIC %md Persist results to the `unidetect_detections` Unity Catalog table for downstream consumption (dashboards, alerts):

# COMMAND ----------

ud.write_detections(detections, mode="append")
