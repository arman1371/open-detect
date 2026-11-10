"""Verdict-cache tests for the Auto-Validate detector (OPE-86 / P-10 AV).

The detector now computes the pattern verdict once per distinct value and
broadcasts it, instead of re-running ``_value_matches`` for every cell.
These tests assert the per-cell output is unchanged (via a reference oracle)
and that the optimized path invokes ``_value_matches`` at most once per
distinct text value.
"""

from __future__ import annotations

import time
from unittest.mock import patch

import pandas as pd

from open_detect.algorithms.auto_validate.config import AutoValidateConfig
from open_detect.algorithms.auto_validate.detector import (
    AutoValidateAlgorithm,
    _is_null,
    _non_null_cells,
    _value_matches,
)


def _make_tiny_corpus() -> list[pd.Series]:
    return [
        pd.Series(["2024-01-15", "2024-02-20", "2024-03-10"]),
        pd.Series(["john@example.com", "jane@test.org", "admin@site.net"]),
        pd.Series(["New York", "London", "Tokyo"]),
    ]


def _detect_dirty(dirty: pd.DataFrame) -> list:
    config = AutoValidateConfig(m=1, tau=16)
    detector = AutoValidateAlgorithm(config)
    detector.build_index(_make_tiny_corpus())
    return detector.detect(dirty, table_id="t1").cells


def _per_cell_reference(dirty: pd.DataFrame) -> list:
    """Reference implementation: per-cell verdicts without dedup.

    This mimics the pre-optimization ``detect`` logic exactly (as on main branch):
    - For feasible columns: call ``_value_matches`` per non-null cell. Empty strings
      are NOT skipped - they fail the match and become errors (is_error=True).
    - For infeasible columns: use ``_non_null_cells`` which DOES skip empty strings.
    - Null handling uses ``_is_null`` for both paths.
    """
    config = AutoValidateConfig(m=1, tau=16)
    detector = AutoValidateAlgorithm(config)
    detector.build_index(_make_tiny_corpus())

    cells: list = []
    for col in dirty.columns:
        series = dirty[col]
        inferred = detector.infer_pattern(series)
        if inferred is None:
            # Infeasible column: use _non_null_cells which skips empty strings
            cells.extend(
                _non_null_cells(
                    series,
                    "t1",
                    col,
                    detector.name,
                    is_error=False,
                    score=0.0,
                    evidence={"pattern": None, "reason": "no_feasible_pattern"},
                )
            )
            continue
        pattern = inferred.pattern
        fpr_t, cov_t, theta_c = inferred.fpr_t, inferred.cov_t, inferred.theta_c
        n_total = len(series) - sum(1 for v in series if _is_null(v))
        score = 1.0 - fpr_t if n_total > 0 else 0.0
        for idx, value in series.items():
            if _is_null(value):
                continue
            # For feasible columns: do NOT skip empty strings (matching main branch behavior).
            # _value_matches returns False for empty strings -> is_error=True.
            is_error = not _value_matches(pattern, value)
            cells.append(
                type(
                    "CellResult",
                    (),
                    {
                        "table_id": "t1",
                        "row_index": idx,
                        "column_name": col,
                        "algorithm": detector.name,
                        "is_error": is_error,
                        "score": score if is_error else 0.0,
                        "evidence": {"pattern": pattern, "fpr_t": fpr_t, "cov_t": cov_t, "theta_c": theta_c},
                    },
                )()
            )
    return cells


def _cells_equal(cells1: list, cells2: list) -> bool:
    """Compare two cell lists by (row_index, column_name, is_error, score)."""
    if len(cells1) != len(cells2):
        return False
    # Sort by (column_name, row_index) for deterministic comparison
    cells1_sorted = sorted(cells1, key=lambda c: (c.column_name, c.row_index))
    cells2_sorted = sorted(cells2, key=lambda c: (c.column_name, c.row_index))
    for c1, c2 in zip(cells1_sorted, cells2_sorted):
        if c1.row_index != c2.row_index:
            return False
        if c1.column_name != c2.column_name:
            return False
        if c1.is_error != c2.is_error:
            return False
        if abs(c1.score - c2.score) > 1e-9:
            return False
    return True


def test_identical_to_per_cell_baseline():
    """Output must be identical to the per-cell reference oracle.

    The oracle runs the pre-optimization per-cell logic and asserts equality
    of (row_index, column_name, is_error, score) across all NaN, duplicates,
    empty strings, and mixed types.
    """
    dirty = pd.DataFrame(
        {
            "email": [
                "john@example.com",
                "invalid-email",
                "admin@site.net",
                "user@test.com",
                "john@example.com",  # duplicate
                None,
                "",  # empty string -> skipped (not a cell, matching _non_null_cells)
            ],
            "city": ["New York", "London", "Tokyo", "Paris", "New York", None, "London"],
        }
    )
    cells = _detect_dirty(dirty)
    reference = _per_cell_reference(dirty)
    assert _cells_equal(cells, reference), "Optimized output differs from per-cell reference"


def test_all_nan_column():
    dirty = pd.DataFrame({"email": [None, None, None]})
    cells = _detect_dirty(dirty)
    assert cells == ()


def test_single_value_column():
    dirty = pd.DataFrame({"email": ["a@b.com", "a@b.com", "a@b.com"]})
    cells = _detect_dirty(dirty)
    assert len(cells) == 3
    assert all(not c.is_error for c in cells)
    # Also verify score evidence
    assert all(c.score == 0.0 for c in cells)


def test_unhashable_values_handled():
    """Object columns with list/dict values must not crash and behave as before."""
    dirty = pd.DataFrame(
        {
            "email": [
                ["a@b.com"],  # unhashable
                {"x": 1},  # unhashable
                "valid@test.com",
            ]
        }
    )
    cells = _detect_dirty(dirty)
    assert len(cells) == 3
    # list/dict values are not str-matching patterns -> flagged as errors
    errors = [c for c in cells if c.is_error]
    assert len(errors) == 2
    assert {c.row_index for c in errors} == {0, 1}


def test_empty_dataframe():
    detector = AutoValidateAlgorithm()
    detector.build_index(_make_tiny_corpus())
    assert detector.detect(pd.DataFrame(), table_id="t1").cells == ()


def test_nan_and_empty_string_distinct_verdicts():
    """NaN is skipped; empty strings are skipped for infeasible columns
    (using _non_null_cells which skips empty strings)."""
    dirty = pd.DataFrame({"email": ["", "", None]})
    cells = _detect_dirty(dirty)
    # Infeasible column (no valid pattern) -> _non_null_cells path -> skips empty strings
    assert cells == ()


def test_mixed_type_column():
    """Mixed-type object columns [1, True, "1", 1.0, "a@b.com"] must produce
    output identical to the per-cell baseline.

    The per-cell baseline calls _value_matches per-cell without dedup.
    Rows with null values (None, pd.NA, [None]) are skipped.
    Non-null values that don't match the email pattern are errors.

    Row 4 ('a@b.com') matches the email pattern -> is_error=False.
    Rows 0-3 (1, True, "1", 1.0) do NOT match -> is_error=True.
    """
    dirty = pd.DataFrame(
        {
            "mixed": [
                1,
                True,
                "1",
                1.0,
                "a@b.com",
                None,
                pd.NA,
                [None],
            ]
        }
    )
    cells = _detect_dirty(dirty)
    reference = _per_cell_reference(dirty)
    assert _cells_equal(cells, reference), "Mixed-type column output differs from per-cell reference"


def test_stringdtype_and_pd_na_column():
    """StringDtype columns with pd.NA must be handled like NaN (skipped)."""
    dirty = pd.DataFrame(
        {
            "email": pd.array(["a@b.com", "invalid", pd.NA, ""], dtype="string"),
        }
    )
    cells = _detect_dirty(dirty)
    # pd.NA is skipped, empty string is treated as an error cell
    assert len(cells) == 3
    errors = [c for c in cells if c.is_error]
    assert len(errors) == 2
    # error rows are 1 ("invalid") and 3 (empty string)
    assert {errors[0].row_index, errors[1].row_index} == {1, 3}


def test_list_like_nulls_handled():
    """List-like nulls [None] are skipped by _is_null (not flagged as errors)."""
    dirty = pd.DataFrame(
        {
            "email": [
                "valid@test.com",
                [None],  # list-like null
                None,
                "another@test.com",
            ]
        }
    )
    cells = _detect_dirty(dirty)
    # [None] is skipped by _is_null, None is skipped, 2 valid remain
    assert len(cells) == 2
    assert all(not c.is_error for c in cells)


def test_verdict_cache_invoked_at_most_once_per_distinct():
    """The verdict cache invariant: _value_matches called <= n_distinct times.

    This is a deterministic, fast check replacing the wall-clock timing test.
    On a 100k-row, 2-distinct column, the cache ensures _value_matches is
    invoked at most twice (once per distinct text value), not 100k times.
    """
    n = 100_000
    values = ["valid@test.com"] * (n - 1) + ["invalid-email"]
    dirty = pd.DataFrame({"email": values})

    config = AutoValidateConfig(m=1, tau=16)
    detector = AutoValidateAlgorithm(config)
    detector.build_index(_make_tiny_corpus())

    # Patch _value_matches to count calls
    call_count = {"n": 0}

    def counting_matches(pattern, value):
        call_count["n"] += 1
        return _value_matches(pattern, value)

    with patch("open_detect.algorithms.auto_validate.detector._value_matches", counting_matches):
        cells = detector.detect(dirty, table_id="t1").cells

    assert len(cells) == n
    errors = [c for c in cells if c.is_error]
    assert len(errors) == 1
    assert errors[0].row_index == n - 1
    # The invariant: at most one call per distinct text value
    # (2 distinct: "valid@test.com" and "invalid-email")
    assert call_count["n"] <= 2, f"_value_matches called {call_count['n']} times, expected <= 2"


def test_before_after_timing_100k_rows():
    """Before/after timing on a high-duplicate column of 100k+ rows.

    Records the detect() duration for evidence in the PR. This is a benchmark,
    not a gate; the cache invariant test above is the actual guard.
    """
    n = 100_000
    values = ["valid@test.com"] * (n - 1) + ["invalid-email"]
    dirty = pd.DataFrame({"email": values})

    config = AutoValidateConfig(m=1, tau=16)
    detector = AutoValidateAlgorithm(config)
    detector.build_index(_make_tiny_corpus())

    start = time.perf_counter()
    cells = detector.detect(dirty, table_id="t1").cells
    elapsed = time.perf_counter() - start

    assert len(cells) == n
    errors = [c for c in cells if c.is_error]
    assert len(errors) == 1
    assert errors[0].row_index == n - 1
    # Print timing for PR evidence (not a gate)
    print(f"\nOPE-86 benchmark: detect 100k rows (2 distinct) took {elapsed:.3f}s")