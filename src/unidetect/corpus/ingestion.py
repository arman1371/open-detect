"""Turn a set of Unity Catalog tables into the canonical corpus representation.

The paper's corpus ``T`` is 100M+ tables scraped from the web. The natural
Databricks/Unity-Catalog analogue -- and the one this library targets -- is
the set of tables an organization already has registered in Unity Catalog
(a whole catalog, a set of schemas, or an explicit allow-list). For most
enterprises this is thousands to millions of governed tables spanning many
domains, which plays the same statistical role T does in the paper: a large
background sample of "what clean tables look like" to reason against.

:class:`CorpusIngestor` reads each source table *once*, using Spark's own
``limit`` push-down to bound how many values are materialized per column
(avoiding driver-side collection and unbounded executor memory use on wide
or skewed tables), and writes the canonical ``corpus_columns`` /
``corpus_column_pairs`` representations that every metric/featurization
function in this package consumes.
"""

from __future__ import annotations

from collections.abc import Sequence
from itertools import combinations
from typing import TYPE_CHECKING

from unidetect.corpus.schema import CORPUS_COLUMNS_SCHEMA, CORPUS_PAIRS_SCHEMA, TOKEN_STATS_SCHEMA
from unidetect.logging_utils import get_logger, log_duration

if TYPE_CHECKING:
    from pyspark.sql import DataFrame, SparkSession

logger = get_logger(__name__)


class CorpusIngestor:
    """Builds ``corpus_columns``, ``corpus_column_pairs`` and ``token_stats``.

    Parameters
    ----------
    spark:
        An active, Unity-Catalog-enabled :class:`SparkSession`.
    max_values_per_column:
        Upper bound on how many (stringified) values are materialized per
        corpus column. Uses ``DataFrame.limit`` *before* aggregation, so cost
        is bounded regardless of the source table's true size.
    max_fd_column_pairs_per_table:
        Caps the number of LHS/RHS candidate pairs generated per table,
        avoiding an O(columns^2) blow-up on very wide tables.
    """

    def __init__(
        self,
        spark: SparkSession,
        max_values_per_column: int = 20_000,
        max_fd_column_pairs_per_table: int = 200,
    ) -> None:
        self.spark = spark
        self.max_values_per_column = max_values_per_column
        self.max_fd_column_pairs_per_table = max_fd_column_pairs_per_table

    def ingest_columns(self, table_names: Sequence[str]) -> DataFrame:
        """Build the ``corpus_columns`` DataFrame from a list of UC table FQNs.

        Each source table is scanned once for its row count and once (via a
        bounded ``limit``) per column for its sampled values; all per-column
        aggregations are lazy Spark transformations unioned together, so the
        only action taken here (besides the row counts) is whatever the
        caller triggers downstream (e.g. a Delta write).
        """
        from functools import reduce

        per_column_frames: list[DataFrame] = []
        with log_duration(logger, f"ingest_columns({len(table_names)} tables)"):
            for fqn in table_names:
                try:
                    frames = self._per_table_column_frames(fqn)
                except Exception:
                    logger.exception("Skipping table %s: failed to read/profile it", fqn)
                    continue
                per_column_frames.extend(frames)

        if not per_column_frames:
            return self.spark.createDataFrame([], schema=CORPUS_COLUMNS_SCHEMA)
        return reduce(lambda a, b: a.unionByName(b), per_column_frames)

    def _per_table_column_frames(self, fqn: str) -> list[DataFrame]:
        from pyspark.sql import functions as F

        df = self.spark.table(fqn)
        num_rows = df.count()
        if num_rows == 0:
            return []

        frames: list[DataFrame] = []
        for idx, field in enumerate(df.schema.fields):
            col = field.name
            sampled = df.select(F.col(f"`{col}`").cast("string").alias("v")).limit(
                self.max_values_per_column
            )
            per_col = sampled.agg(F.collect_list("v").alias("values")).select(
                F.lit(fqn).alias("table_id"),
                F.lit(col).alias("column_name"),
                F.lit(idx).alias("column_index"),
                F.lit(num_rows).alias("num_rows"),
                "values",
            )
            frames.append(per_col)
        return frames

    def ingest_column_pairs(self, table_names: Sequence[str]) -> DataFrame:
        """Build the ``corpus_column_pairs`` DataFrame used for FD statistics."""
        from functools import reduce

        per_pair_frames: list[DataFrame] = []
        with log_duration(logger, f"ingest_column_pairs({len(table_names)} tables)"):
            for fqn in table_names:
                try:
                    frames = self._per_table_pair_frames(fqn)
                except Exception:
                    logger.exception("Skipping table %s: failed to read/profile it", fqn)
                    continue
                per_pair_frames.extend(frames)

        if not per_pair_frames:
            return self.spark.createDataFrame([], schema=CORPUS_PAIRS_SCHEMA)
        return reduce(lambda a, b: a.unionByName(b), per_pair_frames)

    def _per_table_pair_frames(self, fqn: str) -> list[DataFrame]:
        from pyspark.sql import functions as F

        df = self.spark.table(fqn)
        columns = [f.name for f in df.schema.fields]
        if len(columns) < 2:
            return []
        num_rows = df.count()
        if num_rows == 0:
            return []

        pairs = list(combinations(range(len(columns)), 2))[: self.max_fd_column_pairs_per_table]
        frames: list[DataFrame] = []
        for lhs_idx, rhs_idx in pairs:
            lhs_col, rhs_col = columns[lhs_idx], columns[rhs_idx]
            sampled = df.select(
                F.col(f"`{lhs_col}`").cast("string").alias("lhs"),
                F.col(f"`{rhs_col}`").cast("string").alias("rhs"),
            ).limit(self.max_values_per_column)
            per_pair = sampled.agg(
                F.collect_list("lhs").alias("lhs_values"),
                F.collect_list("rhs").alias("rhs_values"),
            ).select(
                F.lit(fqn).alias("table_id"),
                F.lit(lhs_col).alias("lhs_column"),
                F.lit(rhs_col).alias("rhs_column"),
                F.lit(rhs_idx).alias("rhs_column_index"),
                F.lit(num_rows).alias("num_rows"),
                "lhs_values",
                "rhs_values",
            )
            frames.append(per_pair)
        return frames

    def build_token_stats(self, corpus_columns: DataFrame) -> DataFrame:
        """Global token -> distinct-table document-frequency (``Prev(C)`` input).

        A token's document frequency is the number of *distinct tables* (not
        rows/values) it appears in, matching the paper's ``Prev`` definition
        (Sec. 3.3: "the number of times the tokens in C occur in other
        tables").
        """
        from pyspark.sql import functions as F

        from unidetect.text_utils import tokenize

        tokenize_udf = F.udf(lambda s: tokenize(s) if s else [], "array<string>")

        exploded = (
            corpus_columns.select("table_id", F.explode("values").alias("value"))
            .where(F.col("value").isNotNull())
            .select("table_id", F.explode(tokenize_udf(F.lower(F.col("value")))).alias("token"))
            .dropDuplicates(["table_id", "token"])
        )
        return exploded.groupBy("token").agg(F.count("*").alias("doc_frequency"))

    @staticmethod
    def token_stats_schema():
        return TOKEN_STATS_SCHEMA
