"""Canonical Delta table schemas used by the corpus builder and store.

Keeping these as module-level constants (rather than re-deriving schemas ad
hoc in each job) means the builder, the store, and any downstream consumer
reading these UC tables directly all agree on column names and types.
"""

from __future__ import annotations

from pyspark.sql.types import (
    ArrayType,
    DoubleType,
    IntegerType,
    LongType,
    StringType,
    StructField,
    StructType,
)

#: One row per (table, column) in the background corpus T -- the canonical
#: representation every metric/featurization function in this package
#: consumes. Produced by :class:`unidetect.corpus.ingestion.CorpusIngestor`.
CORPUS_COLUMNS_SCHEMA = StructType(
    [
        StructField("table_id", StringType(), nullable=False),
        StructField("column_name", StringType(), nullable=False),
        StructField("column_index", IntegerType(), nullable=False),
        StructField("num_rows", IntegerType(), nullable=False),
        StructField("values", ArrayType(StringType()), nullable=False),
    ]
)

#: One row per (table, lhs-column, rhs-column) candidate FD pair.
CORPUS_PAIRS_SCHEMA = StructType(
    [
        StructField("table_id", StringType(), nullable=False),
        StructField("lhs_column", StringType(), nullable=False),
        StructField("rhs_column", StringType(), nullable=False),
        StructField("rhs_column_index", IntegerType(), nullable=False),
        StructField("num_rows", IntegerType(), nullable=False),
        StructField("lhs_values", ArrayType(StringType()), nullable=False),
        StructField("rhs_values", ArrayType(StringType()), nullable=False),
    ]
)

#: Global token -> number-of-distinct-corpus-tables-containing-it. Backs the
#: ``Prev(C)`` featurization dimension (paper Sec. 3.3).
TOKEN_STATS_SCHEMA = StructType(
    [
        StructField("token", StringType(), nullable=False),
        StructField("doc_frequency", LongType(), nullable=False),
    ]
)

#: The materialized "model": one row per corpus (column|pair) per error type,
#: recording its (feature_bucket, theta_before, theta_after) triple. This is
#: the "learning" phase's only output, and the only thing the online
#: detectors read (paper Sec. 2.2.3, "System Architecture").
CORPUS_STATS_SCHEMA = StructType(
    [
        StructField("error_type", StringType(), nullable=False),
        StructField("feature_bucket", StringType(), nullable=False),
        StructField("theta_before", DoubleType(), nullable=False),
        StructField("theta_after", DoubleType(), nullable=False),
        StructField("table_id", StringType(), nullable=True),
    ]
)
