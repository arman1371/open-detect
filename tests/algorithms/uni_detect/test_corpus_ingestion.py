"""Tests for corpus/ingestion.py: FD pair selection and null-aligned pair collection."""

from __future__ import annotations

import random

import pytest

from open_detect.algorithms.uni_detect.corpus.ingestion import (
    CorpusIngestor,
    select_fd_column_pairs,
)


class TestSelectFdColumnPairs:
    def test_both_directions_are_candidates(self):
        pairs = select_fd_column_pairs("t", ["a", "b", "c"], max_pairs=100)
        assert sorted(pairs) == [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]

    def test_cap_is_respected(self):
        pairs = select_fd_column_pairs("t", [f"c{i}" for i in range(10)], max_pairs=7)
        assert len(pairs) == 7
        assert len(set(pairs)) == 7

    def test_selection_is_independent_of_column_order(self):
        names = [f"col_{i}" for i in range(12)]
        shuffled = names[:]
        random.Random(1).shuffle(shuffled)

        def by_name(cols):
            return {
                (cols[lhs], cols[rhs])
                for lhs, rhs in select_fd_column_pairs("t", cols, max_pairs=20)
            }

        assert by_name(names) == by_name(shuffled)

    def test_selection_is_deterministic_and_depends_on_table(self):
        names = [f"col_{i}" for i in range(12)]
        first = select_fd_column_pairs("t1", names, max_pairs=20)
        assert first == select_fd_column_pairs("t1", names, max_pairs=20)
        assert set(first) != set(select_fd_column_pairs("t2", names, max_pairs=20))

    def test_single_column_has_no_pairs(self):
        assert select_fd_column_pairs("t", ["a"], max_pairs=10) == []


@pytest.fixture
def pair_table(spark, uc_location):
    fqn = f"{uc_location.catalog}.{uc_location.schema}.ingest_null_pairs"
    rows = [
        ("a", "x"),
        (None, "y"),  # null only in lhs
        ("b", None),  # null only in rhs
        (None, None),  # null in both
        ("c", "z"),
        ("a", "x"),
    ]
    spark.createDataFrame(rows, schema="lhs string, rhs string").write.format("delta").mode(
        "overwrite"
    ).saveAsTable(fqn)
    return fqn


class TestIngestColumnPairsNullAlignment:
    def test_nulls_drop_whole_rows_so_arrays_stay_aligned(self, spark, pair_table):
        pairs = CorpusIngestor(spark, max_fd_column_pairs_per_table=10).ingest_column_pairs(
            [pair_table]
        )
        by_direction = {(r["lhs_column"], r["rhs_column"]): r for r in pairs.collect()}

        assert set(by_direction) == {("lhs", "rhs"), ("rhs", "lhs")}
        forward = by_direction[("lhs", "rhs")]
        assert len(forward["lhs_values"]) == len(forward["rhs_values"]) == 3
        assert sorted(zip(forward["lhs_values"], forward["rhs_values"], strict=True)) == [
            ("a", "x"),
            ("a", "x"),
            ("c", "z"),
        ]
        backward = by_direction[("rhs", "lhs")]
        assert sorted(zip(backward["lhs_values"], backward["rhs_values"], strict=True)) == [
            ("x", "a"),
            ("x", "a"),
            ("z", "c"),
        ]
        assert forward["num_rows"] == 6
