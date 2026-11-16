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

import hashlib
import heapq
from collections.abc import Sequence
from itertools import permutations
from typing import TYPE_CHECKING

from open_detect.algorithms.uni_detect.corpus.schema import (
    CORPUS_COLUMNS_SCHEMA,
    CORPUS_PAIRS_SCHEMA,
    TOKEN_STATS_SCHEMA,
)
from open_detect.algorithms.uni_detect.text_utils import infer_column_data_type
from open_detect.logging_utils import get_logger, log_duration

if TYPE_CHECKING:
    from pyspark.sql import DataFrame, SparkSession

# Config constant for repartition factor (requirement 4: repartition on spark.default.parallelism * k)
INGESTION_REPARTITION_FACTOR = 4

logger = get_logger(__name__)


def select_fd_column_pairs(
    table_id: str, column_names: Sequence[str], max_pairs: int
) -> list[tuple[int, int]]:
    """Pick the ordered ``(lhs_idx, rhs_idx)`` candidate pairs for one table.

    Both directions (A->B and B->A) are candidates. When there are more than
    ``max_pairs`` the survivors are those with the smallest stable hash of
    ``(table_id, lhs_name, rhs_name)``, so the selection depends only on the
    table and its column *names* -- not on column order -- and is identical
    across runs and processes (``hashlib``, unlike ``hash()``, is unsalted).
    """

    def sort_key(pair: tuple[int, int]) -> tuple[bytes, int, int]:
        lhs, rhs = pair
        digest = hashlib.sha256(
            f"{table_id}\x00{column_names[lhs]}\x00{column_names[rhs]}".encode()
        ).digest()
        return digest, lhs, rhs

    candidates = permutations(range(len(column_names)), 2)
    return heapq.nsmallest(max_pairs, candidates, key=sort_key)


def balanced_union(frames: list[DataFrame]) -> DataFrame:
    """Combine DataFrames with a balanced binary union tree.

    A naive ``reduce(lambda a, b: a.unionByName(b), frames)`` produces a
    left-deep plan whose depth equals the number of frames; on thousands of
    tables that is a quadratic plan-blow-up risk. This halves the depth at
    each level (``ceil(log2(N))`` total) by unioning the two halves of the
    list recursively. Pair/column content is unchanged -- only the plan shape
    differs.
    """
    if len(frames) == 1:
        return frames[0]
    mid = len(frames) // 2
    return balanced_union(frames[:mid]).unionByName(balanced_union(frames[mid:]))


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
        Caps the number of ordered LHS/RHS candidate pairs generated per
        table, avoiding an O(columns^2) blow-up on very wide tables. Over the
        cap, pairs are sampled deterministically (see
        :func:`select_fd_column_pairs`).
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

        Each source table is scanned ONCE: all per-column value arrays are
        computed in a single ``agg(collect_list(...))`` call, and the column
        rows are derived from that frame. This avoids O(columns) scans per table.
        """
        per_table_frames: list[DataFrame] = []
        with log_duration(logger, f"ingest_columns({len(table_names)} tables)"):
            for fqn in table_names:
                try:
                    frame = self._per_table_column_frame(fqn)
                except Exception:
                    logger.exception("Skipping table %s: failed to read/profile it", fqn)
                    continue
                if frame is not None:
                    per_table_frames.append(frame)

        if not per_table_frames:
            return self.spark.createDataFrame([], schema=CORPUS_COLUMNS_SCHEMA)
        # Use balanced union to avoid left-deep reduce(unionByName) plan blow-up
        return balanced_union(per_table_frames)

    def ingest_columns_with_pairs(self, table_names: Sequence[str]) -> tuple[DataFrame, DataFrame]:
        """Build both ``corpus_columns`` and ``corpus_column_pairs`` in a single scan per table.

        Returns a tuple of (columns_df, pairs_df) where both are built from the same single scan
        per table. This avoids re-scanning tables for FD pairs (requirement 2).
        """
        per_table_column_frames: list[DataFrame] = []
        per_table_pair_frames: list[DataFrame] = []
        with log_duration(logger, f"ingest_columns_with_pairs({len(table_names)} tables)"):
            for fqn in table_names:
                try:
                    column_frame, pair_frames = self._per_table_column_frame_with_pairs(fqn)
                except Exception:
                    logger.exception("Skipping table %s: failed to read/profile it", fqn)
                    continue
                if column_frame is not None:
                    per_table_column_frames.append(column_frame)
                per_table_pair_frames.extend(pair_frames)

        if not per_table_column_frames:
            columns_df = self.spark.createDataFrame([], schema=CORPUS_COLUMNS_SCHEMA)
        else:
            columns_df = balanced_union(per_table_column_frames)

        if not per_table_pair_frames:
            pairs_df = self.spark.createDataFrame([], schema=CORPUS_PAIRS_SCHEMA)
        else:
            pairs_df = balanced_union(per_table_pair_frames)

        return columns_df, pairs_df

    def _per_table_column_frame(self, fqn: str) -> DataFrame | None:
        """Build column frame for a single table (backward compatible)."""
        frame, _ = self._per_table_column_frame_with_pairs(fqn)
        return frame

    def _per_table_column_frame_with_pairs(
        self, fqn: str
    ) -> tuple[DataFrame | None, list[DataFrame]]:
        from pyspark.sql import functions as F

        df = self.spark.table(fqn)
        fields = df.schema.fields
        if not fields:
            return None, []

        # Single scan: collect every column's values in one ``agg`` call.
        # ``array_sort(collect_list(...))`` + ``slice`` reproduces the baseline
        # ``orderBy(value).limit(max_values_per_column)`` semantics (the N
        # smallest stringified values, in sorted order) without a per-column
        # scan, a window rank column, or a driver-side collect.
        col_names = [f.name for f in fields]
        cast_df = df.select(*[F.col(f"`{c}`").cast("string").alias(c) for c in col_names])
        agg_exprs = [
            F.slice(
                F.array_sort(F.collect_list(F.col(c))),
                1,
                self.max_values_per_column,
            ).alias(f"values_{idx}")
            for idx, c in enumerate(col_names)
        ]
        all_values_row = cast_df.agg(*agg_exprs).first()
        if all_values_row is None:
            return None, []

        num_rows = df.count()
        if num_rows == 0:
            return None, []

        # Build per-column rows from the single-scan result
        rows = []
        for idx, field in enumerate(fields):
            col_name = field.name
            values = all_values_row[f"values_{idx}"] or []
            # Infer column data type for P-14 tagging
            col_type = infer_column_data_type(values)
            rows.append(
                (
                    fqn,  # table_id
                    col_name,  # column_name
                    idx,  # column_index
                    num_rows,  # num_rows
                    values,  # values
                    col_type.value,  # column_data_type
                )
            )

        column_frame = self.spark.createDataFrame(rows, schema=CORPUS_COLUMNS_SCHEMA)
        pair_frames = self._build_column_pairs_from_single_scan(
            fqn, all_values_row, col_names, num_rows
        )
        return column_frame, pair_frames

    def _balanced_union(self, frames: list[DataFrame]) -> DataFrame:
        """Combine DataFrames with a balanced union tree to avoid left-deep plans."""
        return balanced_union(frames)

    def _build_column_pairs_from_single_scan(
        self, fqn: str, all_values_row, col_names, num_rows
    ) -> list[DataFrame]:
        """Build FD column pairs from the single-scan aggregation result (requirement 2).

        Uses the pre-collected value arrays from the single scan instead of re-scanning the table.
        """

        columns = col_names
        if len(columns) < 2:
            return []

        pairs = select_fd_column_pairs(fqn, columns, self.max_fd_column_pairs_per_table)
        if not pairs:
            return []

        frames: list[DataFrame] = []
        for lhs_idx, rhs_idx in pairs:
            lhs_col, rhs_col = columns[lhs_idx], columns[rhs_idx]
            # Get pre-collected values from the single scan result
            lhs_values = all_values_row[f"values_{lhs_idx}"] or []
            rhs_values = all_values_row[f"values_{rhs_idx}"] or []

            # Align by index (both arrays come from the same row order)
            min_len = min(len(lhs_values), len(rhs_values))
            lhs_values = lhs_values[:min_len]
            rhs_values = rhs_values[:min_len]

            # Filter out rows where either side is null
            aligned_pairs = [
                (lhs, rhs)
                for lhs, rhs in zip(lhs_values, rhs_values, strict=True)
                if lhs is not None and rhs is not None
            ][: self.max_values_per_column]

            if not aligned_pairs:
                continue

            lhs_vals, rhs_vals = zip(*aligned_pairs, strict=False)

            from pyspark.sql import Row

            per_pair = self.spark.createDataFrame(
                [
                    Row(
                        table_id=fqn,
                        lhs_column=lhs_col,
                        rhs_column=rhs_col,
                        rhs_column_index=rhs_idx,
                        num_rows=num_rows,
                        lhs_values=list(lhs_vals),
                        rhs_values=list(rhs_vals),
                    )
                ],
                schema=CORPUS_PAIRS_SCHEMA,
            )
            frames.append(per_pair)
        return frames

    def ingest_column_pairs(self, table_names: Sequence[str]) -> DataFrame:
        """Build the ``corpus_column_pairs`` DataFrame used for FD statistics.

        Builds one row per FD pair from the same table scan. Pair selection
        (``select_fd_column_pairs``) and per-pair null alignment (collecting
        ``(lhs, rhs)`` as a struct so both sides stay row-aligned) are preserved
        exactly; only the final per-table merge uses the balanced union tree
        instead of a left-deep ``reduce(unionByName)``.
        """
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
        # Balanced union tree (not left-deep reduce) to avoid plan blow-up on
        # many pairs/tables, matching ingest_columns. Pair content is unchanged.
        return self._balanced_union(per_pair_frames)

    def _per_table_pair_frames(self, fqn: str) -> list[DataFrame]:
        from pyspark.sql import functions as F

        df = self.spark.table(fqn)
        columns = [f.name for f in df.schema.fields]
        if len(columns) < 2:
            return []

        num_rows = df.count()
        if num_rows == 0:
            return []

        pairs = select_fd_column_pairs(fqn, columns, self.max_fd_column_pairs_per_table)
        if not pairs:
            return []

        frames: list[DataFrame] = []
        for lhs_idx, rhs_idx in pairs:
            lhs_col, rhs_col = columns[lhs_idx], columns[rhs_idx]
            # Collect (lhs, rhs) as one struct, keeping only rows where both
            # sides are non-null: collecting the columns independently drops
            # nulls independently, leaving arrays of different lengths whose
            # positions no longer refer to the same rows.
            sampled = (
                df.select(
                    F.col(f"`{lhs_col}`").cast("string").alias("lhs"),
                    F.col(f"`{rhs_col}`").cast("string").alias("rhs"),
                )
                .where(F.col("lhs").isNotNull() & F.col("rhs").isNotNull())
                .limit(self.max_values_per_column)
            )
            per_pair = sampled.agg(F.collect_list(F.struct("lhs", "rhs")).alias("pairs")).select(
                F.lit(fqn).alias("table_id"),
                F.lit(lhs_col).alias("lhs_column"),
                F.lit(rhs_col).alias("rhs_column"),
                F.lit(rhs_idx).alias("rhs_column_index"),
                F.lit(num_rows).alias("num_rows"),
                F.col("pairs.lhs").alias("lhs_values"),
                F.col("pairs.rhs").alias("rhs_values"),
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

        from open_detect.algorithms.uni_detect.text_utils import tokenize

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
