"""Acceptance tests for the Auto-Validate verdict cache (OPE-86 / P-10 AV).

The optimized :meth:`AutoValidateAlgorithm.detect` computes the pattern verdict
once per *distinct* value and broadcasts it, instead of re-running
``_value_matches`` for every cell. These tests assert two things:

1. **Equivalence** -- the per-cell output equals the pre-optimization per-cell
   loop exactly. :func:`_per_cell_reference` re-implements ``detect`` as it was
   at ``011b59d^`` (the parent of the commit that introduced the cache) using
   the same production helpers, and builds real :class:`CellResult` objects, so
   the comparison covers row index, column name, algorithm, verdict, score
   **and** evidence.
2. **The cache invariant** -- ``_value_matches`` is invoked exactly once per
   distinct text value, and far fewer times than there are rows. OPE-86's
   before/after numbers are recorded in the PR description; the deterministic
   guard lives here instead of in a wall-clock assertion.

Blank strings follow the detector on ``main``: on a *feasible* column ``""`` is
a non-null value that fails the match, so it is emitted as an error cell; only
the *infeasible* path (:func:`_non_null_cells`) drops blanks. Both behaviors
are checked against the oracle rather than hardcoded.
"""

from __future__ import annotations

from collections.abc import Callable
from unittest.mock import patch

import pandas as pd
import pytest

from open_detect.algorithms.auto_validate.config import AutoValidateConfig
from open_detect.algorithms.auto_validate.detector import (
    AutoValidateAlgorithm,
    _feasible_evidence,
    _infeasible_evidence,
    _is_null,
    _non_null_cells,
    _value_matches,
    _value_matches_groups,
)
from open_detect.algorithms.auto_validate.fmdv import InferredPattern
from open_detect.algorithms.base import CellResult

CONFIG = AutoValidateConfig(m=1, tau=16)
TABLE_ID = "t1"


def _make_tiny_corpus() -> list[pd.Series]:
    return [
        pd.Series(["2024-01-15", "2024-02-20", "2024-03-10"]),
        pd.Series(["john@example.com", "jane@test.org", "admin@site.net"]),
        pd.Series(["New York", "London", "Tokyo"]),
    ]


def _detector() -> AutoValidateAlgorithm:
    detector = AutoValidateAlgorithm(CONFIG)
    detector.build_index(_make_tiny_corpus())
    return detector


def _detect(dirty: pd.DataFrame) -> tuple[CellResult, ...]:
    return _detector().detect(dirty, table_id=TABLE_ID).cells


def _per_cell_reference(dirty: pd.DataFrame) -> tuple[CellResult, ...]:
    """Pre-optimization ``detect``: one ``_value_matches`` call per cell.

    This is the literal per-cell loop from ``011b59d^`` (the commit before the
    verdict cache), reusing the same production helpers the cached path uses --
    ``_is_null``, ``_value_matches``, ``_non_null_cells``, ``_feasible_evidence``,
    ``_infeasible_evidence`` -- and building real :class:`CellResult` objects.
    The only difference from the optimized path is the missing dedup: the
    verdict is recomputed for every row.

    Neither branch treats empty strings specially, so the oracle stays faithful
    to the detector on ``main``. Blank cells are dropped only in the infeasible
    path, by :func:`_non_null_cells`.
    """
    detector = _detector()
    cells: list[CellResult] = []
    for col in dirty.columns:
        series = dirty[col]
        inferred = detector.infer_pattern(series)
        if inferred is not None:
            pattern = inferred.pattern
            fpr_t, cov_t, theta_c = inferred.fpr_t, inferred.cov_t, inferred.theta_c
            n_total = len(series) - sum(1 for v in series if _is_null(v))
            score = 1.0 - fpr_t if n_total > 0 else 0.0
            for idx, value in series.items():
                if _is_null(value):
                    continue
                is_error = not _value_matches(pattern, value)
                cells.append(
                    CellResult(
                        table_id=TABLE_ID,
                        row_index=idx,
                        column_name=col,
                        algorithm=detector.name,
                        is_error=is_error,
                        score=score if is_error else 0.0,
                        evidence=_feasible_evidence(
                            detector.config, pattern, fpr_t, cov_t, theta_c
                        ),
                    )
                )
        else:
            cells.extend(
                _non_null_cells(
                    series,
                    TABLE_ID,
                    col,
                    detector.name,
                    is_error=False,
                    score=0.0,
                    evidence=_infeasible_evidence(detector.config, None),
                )
            )
    return tuple(cells)


def _city_column(n: int) -> list[str]:
    cities = ["New York", "London", "Tokyo", "Paris"]
    return [cities[i % len(cities)] for i in range(n)]


#: ``_per_cell_reference`` must equal ``detect`` for the ``email`` column of
#: each of these frames (a ``city`` column is appended so multi-column detect is
#: exercised too). ``""`` appears in several cases on purpose, so blank-cell
#: behavior is checked by the equivalence itself on both the feasible and the
#: infeasible path.
EQUIVALENCE_CASES: list[tuple[str, list]] = [
    ("email_with_blank", ["john@example.com", "invalid-email", "", "john@example.com", None]),
    ("all_nan", [None, None, None]),
    ("single_repeated_value", ["a@b.com"] * 4),
    ("unhashable_values", [["a@b.com"], {"x": 1}, "", "valid@test.com", None]),
    ("blank_and_nan", ["", "", None]),
    ("mixed_types", [1, True, "1", 1.0, "a@b.com", "", None, pd.NA, [None], "invalid"]),
    ("list_like_nulls", ["valid@test.com", [None], None, "another@test.com", ""]),
    ("duplicates_and_blanks", ["a@b.com", "a@b.com", "", "bad", "", None, "a@b.com"]),
]


@pytest.mark.parametrize(
    "values",
    [pytest.param(v, id=name) for name, v in EQUIVALENCE_CASES],
)
def test_identical_to_per_cell_baseline(values: list) -> None:
    """The cached path must emit cells exactly equal to the per-cell loop.

    ``CellResult`` is a frozen dataclass whose ``__eq__`` compares every field
    (``evidence`` included), and the comparison is on the ordered tuple, so row
    index, column name, algorithm, verdict, score and evidence must all agree --
    not just counts or row-index sets.
    """
    dirty = pd.DataFrame({"email": values, "city": _city_column(len(values))})
    assert _detect(dirty) == _per_cell_reference(dirty)


def test_identical_to_per_cell_baseline_non_default_index() -> None:
    """Equivalence holds for a non-default (string) row index."""
    dirty = pd.DataFrame(
        {"email": ["a@b.com", "bad", "", None, "a@b.com"]},
        index=["r5", "r1", "r9", "r0", "r3"],
    )
    assert _detect(dirty) == _per_cell_reference(dirty)


def test_identical_to_per_cell_baseline_multi_column() -> None:
    """Equivalence across columns with *different* feasibility (both paths)."""
    dirty = pd.DataFrame(
        {
            "email": ["john@example.com", "", "invalid", "a@b.com"],
            "date": ["2024-01-15", "not-a-date", "", "2024-02-20"],
            "noise": [1, 2, 3, 4],
            "nothing": [None, None, None, None],
        }
    )
    assert _detect(dirty) == _per_cell_reference(dirty)


def _counting_value_matches_groups(call_counter: dict[str, int]) -> Callable:
    """Wrapper around ``_value_matches_groups`` that records how often it is called."""

    def counting(groups, text):
        call_counter["n"] += 1
        return _value_matches_groups(groups, text)

    return counting


#: Verdict produced by ``infer_pattern`` for :func:`_two_distinct_frame`, taken
#: from the real (``fmdv_vh``) inference instead of being re-run inside the
#: call-count tests. ``infer_pattern`` is the slow half of ``detect`` (~28s at
#: 100k rows, ~2.7s at 10k) and OPE-86 does not touch it, so re-running it there
#: would only add CI minutes without testing the cache. Stubbing it is what
#: leaves the *verdict loop* -- the code OPE-86 changed -- as the thing measured.
#: :func:`test_stubbed_pattern_matches_real_inference` pins this constant to the
#: real result, and :func:`test_verdict_cache_matches_per_cell_under_broadcasting`
#: / :func:`test_identical_to_per_cell_baseline` keep asserting full equivalence
#: against the oracle with the *real* inference (no stub).
#: For this test fixture (emails), all values share the same coarse signature,
#: so fmdv_vh returns a single string pattern (backward compat: one group, one segment).
STUBBED_INFERRED_PATTERN = InferredPattern(
    pattern="<alphanum>+<symbol>+<alphanum>+<symbol>+<alphanum>+",
    fpr_t=0.0,
    cov_t=2,
    theta_c=0.0,
    variant="fmdv_vh",
)


def _count_detect_calls(dirty: pd.DataFrame) -> tuple[int, int]:
    """Run ``detect`` with ``_value_matches_groups`` counted and ``infer_pattern`` stubbed.

    Returns ``(num_cells, num_value_matches_calls)``. ``infer_pattern`` never
    calls ``_value_matches_groups``, so the count isolates the verdict loop.
    """
    detector = _detector()
    call_counter: dict[str, int] = {"n": 0}
    with (
        patch.object(detector, "infer_pattern", return_value=STUBBED_INFERRED_PATTERN),
        patch(
            "open_detect.algorithms.auto_validate.detector._value_matches_groups",
            _counting_value_matches_groups(call_counter),
        ),
    ):
        cells = detector.detect(dirty, table_id=TABLE_ID).cells
    return len(cells), call_counter["n"]


def test_feasible_column_empty_string_is_error_cell() -> None:
    r"""On a feasible column, ``""`` is non-null and fails the match -> error cell.

    This replaces the earlier test that asserted the opposite while its fixture
    was actually infeasible.
    """
    dirty = pd.DataFrame(
        {"email": ["john@example.com", "invalid-email", "admin@site.net", "", None]}
    )
    assert _detector().infer_pattern(dirty["email"]) is not None, "fixture must be feasible"
    cells = _detect(dirty)
    assert {c.row_index for c in cells} == {0, 1, 2, 3}, "only None is skipped"
    assert {c.row_index for c in cells if c.is_error} == {1, 3}, "bad email and ''"
    assert cells == _per_cell_reference(dirty)


def test_empty_dataframe() -> None:
    assert _detector().detect(pd.DataFrame(), table_id=TABLE_ID).cells == ()


def test_infeasible_column_skips_empty_strings() -> None:
    """With no feasible pattern the column goes through ``_non_null_cells``,

    which drops nulls *and* blanks, so no cell is emitted here at all. This is
    an infeasible-path test; it says nothing about ``""`` on a feasible column.
    """
    dirty = pd.DataFrame({"email": ["", "", None, ""]})
    assert _detector().infer_pattern(dirty["email"]) is None, "fixture must be infeasible"
    assert _detect(dirty) == ()
    assert _detect(dirty) == _per_cell_reference(dirty)


def _two_distinct_frame(rows: int) -> pd.DataFrame:
    values = ["valid@test.com"] * (rows - 1) + ["invalid-email"]
    return pd.DataFrame({"email": values})


def test_stubbed_pattern_matches_real_inference() -> None:
    """The stub used by the call-count tests must be the real inference result.

    Otherwise those tests measure a verdict loop that production never runs.
    Checked at a size where the real ``fmdv_vh`` inference is fast; the 2000-row
    and 100k-row inferences of :func:`_two_distinct_frame` agree (both select
    ``<alphanum>+<symbol>+...`` with ``fpr_t=0.0``), so the constant is valid for
    the 100k-row fixture too.
    """
    dirty = _two_distinct_frame(2_000)
    real = _detector().infer_pattern(dirty["email"])
    assert real == STUBBED_INFERRED_PATTERN, (
        f"real inference is {real!r}; update STUBBED_INFERRED_PATTERN to match"
    )


def test_verdict_cache_invoked_exactly_once_per_distinct() -> None:
    """The cache invariant: ``_value_matches`` runs exactly once per distinct value.

    ``<= n_distinct`` would also pass had the cache been bypassed, so the
    assertion is strict equality. On a 100k-row, 2-distinct column that is 2
    calls, not 100k. ``infer_pattern`` is stubbed with the real result (pinned by
    :func:`test_stubbed_pattern_matches_real_inference`) so this measures the
    verdict loop that OPE-86 changed instead of paying ~28s for inference; the
    same equality is checked at small sizes in
    :func:`test_verdict_cache_reduces_value_matches_calls`.
    """
    rows = 100_000
    values = ["valid@test.com"] * (rows - 1) + ["invalid-email"]
    n_distinct = len({v for v in values if not _is_null(v)})

    n_cells, n_calls = _count_detect_calls(_two_distinct_frame(rows))

    assert n_cells == rows
    assert n_calls == n_distinct, f"expected {n_distinct} calls, got {n_calls}"
    assert n_calls < rows, "the cache must not fall back to per-cell matching"


@pytest.mark.parametrize("rows", [10, 100, 10_000])
def test_verdict_cache_reduces_value_matches_calls(rows: int) -> None:
    """The cache keeps the call count constant as the column grows."""
    n_cells, n_calls = _count_detect_calls(_two_distinct_frame(rows))
    assert n_cells == rows
    assert n_calls == 2, "two distinct values -> two verdicts, at any size"
    assert n_calls < rows, "the cache must not fall back to per-cell matching"


def test_verdict_cache_matches_per_cell_under_broadcasting() -> None:
    """Equivalence on the shape the cache targets, with the *real* inference.

    Few distinct values over many rows, with blanks, unhashables, list-like
    nulls and near-duplicate text mixed in so dedup on the *text* representation
    (not the raw value) is exercised. A non-default index stops duplicate row
    values from masking a mapping error, and the comparison is full ``CellResult``
    equality against the per-cell oracle.
    """
    base = [
        "valid@test.com",
        "",
        "nope",
        "valid@test.com",
        "valid@test.co",
        ["a@b.com"],
        None,
        [None],
        1,
        True,
    ]
    values = base * 200
    dirty = pd.DataFrame({"email": values}, index=[f"r{i}" for i in range(len(values))])
    cells = _detect(dirty)
    assert cells == _per_cell_reference(dirty)
    assert any(c.is_error for c in cells), "fixture must actually flag cells"
    # Same dedup key the detector uses: the text representation, not the raw
    # (possibly unhashable) value.
    distinct_texts = {v if isinstance(v, str) else str(v) for v in values if not _is_null(v)}
    assert 1 < len(distinct_texts) < len(values) // 2, (
        "fixture must be high-duplicate, i.e. the case the cache optimizes"
    )
