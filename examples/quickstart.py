"""Standalone quickstart: build a tiny corpus and run Uni-Detect against it.

Run with `python examples/quickstart.py` from a Python environment that has
`unidetect[dev]` installed (needs pyspark + delta-spark; see README). This
script uses a local, throwaway Spark session -- on Databricks you would use
the cluster's own `spark` and real Unity Catalog table names instead of the
synthetic tables created here.
"""

from __future__ import annotations

import json
import os
import sys

from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession

os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
os.environ.setdefault("PYSPARK_DRIVER_PYTHON", sys.executable)

from unidetect.config import UniDetectConfig, UnityCatalogLocation
from unidetect.core.enums import ErrorType
from unidetect.pipeline import UniDetect


def build_spark() -> SparkSession:
    builder = (
        SparkSession.builder.master("local[2]")
        .appName("unidetect-quickstart")
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config(
            "spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog"
        )
    )
    return configure_spark_with_delta_pip(builder).getOrCreate()


def main() -> None:
    spark = build_spark()
    spark.sparkContext.setLogLevel("ERROR")
    spark.sql("CREATE SCHEMA IF NOT EXISTS spark_catalog.unidetect_demo")

    # --- a minimal "corpus": mostly ID-like unique columns, a few common-name columns ---
    for i in range(15):
        codes = [f"ICAO{100000 + i * 1000 + j}" for j in range(80)]
        spark.createDataFrame([(c,) for c in codes], ["code"]).write.format("delta").mode(
            "overwrite"
        ).saveAsTable(f"spark_catalog.unidetect_demo.corpus_ids_{i}")

    for i in range(15):
        names = ["James Smith", "Mary Jones", "John Brown", "Patricia Davis"] * 25
        spark.createDataFrame([(n,) for n in names], ["name"]).write.format("delta").mode(
            "overwrite"
        ).saveAsTable(f"spark_catalog.unidetect_demo.corpus_names_{i}")

    corpus_tables = [
        f"spark_catalog.unidetect_demo.{t}"
        for t in [f"corpus_ids_{i}" for i in range(15)] + [f"corpus_names_{i}" for i in range(15)]
    ]

    config = UniDetectConfig(
        location=UnityCatalogLocation(catalog="spark_catalog", schema="unidetect_demo"),
        alpha=0.2,
    )
    ud = UniDetect(config, spark=spark)

    print("Building corpus statistics (offline phase)...")
    ud.build_corpus_statistics(
        corpus_tables, error_types=[ErrorType.UNIQUENESS], create_schema=False
    )

    # --- target table with one injected duplicate in an ID-like column ---
    target_values = [f"ICAO{900000 + i}" for i in range(100)]
    target_values[1] = target_values[0]
    spark.createDataFrame([(v,) for v in target_values], ["code"]).write.format("delta").mode(
        "overwrite"
    ).saveAsTable("spark_catalog.unidetect_demo.target")

    print("Scanning target table (online phase)...")
    detections = ud.detect(
        ["spark_catalog.unidetect_demo.target"], error_types=[ErrorType.UNIQUENESS]
    ).toPandas()

    for _, row in detections.iterrows():
        print(
            f"[{row['error_type']}] {row['table_id']} {row['column_names']} "
            f"lr_ratio={row['lr_ratio']:.4g} significant={row['is_significant']} "
            f"evidence={json.loads(row['evidence_json'])}"
        )

    spark.stop()


if __name__ == "__main__":
    main()
