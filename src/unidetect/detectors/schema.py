"""Output schema shared by every detector's :meth:`~unidetect.detectors.base.BaseDetector.detect`."""

from __future__ import annotations

from pyspark.sql.types import (
    ArrayType,
    BooleanType,
    DoubleType,
    LongType,
    StringType,
    StructField,
    StructType,
)

CANDIDATE_SCHEMA = StructType(
    [
        StructField("candidate_id", StringType(), nullable=False),
        StructField("table_id", StringType(), nullable=False),
        StructField("column_names", ArrayType(StringType()), nullable=False),
        StructField("row_ids", ArrayType(StringType()), nullable=False),
        StructField("feature_bucket", StringType(), nullable=False),
        StructField("theta_before", DoubleType(), nullable=False),
        StructField("theta_after", DoubleType(), nullable=False),
        StructField("evidence_json", StringType(), nullable=False),
    ]
)

DETECTION_RESULT_SCHEMA = StructType(
    [
        StructField("candidate_id", StringType(), nullable=False),
        StructField("error_type", StringType(), nullable=False),
        StructField("table_id", StringType(), nullable=False),
        StructField("column_names", ArrayType(StringType()), nullable=False),
        StructField("row_ids", ArrayType(StringType()), nullable=False),
        StructField("lr_ratio", DoubleType(), nullable=False),
        StructField("surprisal", DoubleType(), nullable=False),
        StructField("is_significant", BooleanType(), nullable=False),
        StructField("support", LongType(), nullable=False),
        StructField("evidence_json", StringType(), nullable=False),
    ]
)
