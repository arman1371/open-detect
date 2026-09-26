"""End-to-end tests for RahaDetector, using the paper's own running example
(Table 2, Mahdavi et al., SIGMOD'19) as the fixture dataset.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from unidetect.algorithms import get_algorithm
from unidetect.algorithms.raha import GroundTruthLabeler, RahaConfig, RahaDetector
from unidetect.exceptions import ConfigurationError

DIRTY = pd.DataFrame(
    {
        "Lord": ["Aragorn", "Sauron", "Gandalf", "Saruman", "Elrond", "Theoden"],
        "Kingdom": ["Minas Tirith", "Mordor", "MISSING", "MISSING", "123", "Shire"],
    }
)
CLEAN = pd.DataFrame(
    {
        "Lord": ["Aragorn", "Sauron", "Gandalf", "Saruman", "Elrond", "Theoden"],
        "Kingdom": ["Minas Tirith", "Mordor", "N/A", "Isengard", "Rivendell", "Rohan"],
    }
)


def test_registered_under_raha():
    detector = get_algorithm("raha")
    assert isinstance(detector, RahaDetector)


def test_empty_dataframe_returns_no_cells():
    detector = RahaDetector()
    result = detector.detect(pd.DataFrame(), table_id="empty")
    assert len(result) == 0


def test_recovers_known_errors_with_ground_truth_labeler():
    config = RahaConfig(labeling_budget=6, random_state=0)
    detector = RahaDetector(config)
    labeler = GroundTruthLabeler(CLEAN)

    result = detector.detect(DIRTY, table_id="lotr", labeler=labeler)

    assert len(result) == DIRTY.size
    assert {c.table_id for c in result} == {"lotr"}
    assert {c.algorithm for c in result} == {"raha"}

    kingdom_errors = {c.row_index for c in result.errors() if c.column_name == "Kingdom"}
    # With a full labeling budget covering every row, the ground-truth
    # labeler resolves every cell directly -- all 4 known Kingdom errors
    # (rows 2, 3, 4, 5) must be recovered exactly.
    assert kingdom_errors == {2, 3, 4, 5}

    lord_errors = {c.row_index for c in result.errors() if c.column_name == "Lord"}
    assert lord_errors == set()


def test_runs_end_to_end_with_default_heuristic_labeler():
    # No labeler supplied -> the zero-human HeuristicLabeler fallback must
    # still let the whole pipeline run without raising.
    detector = RahaDetector(RahaConfig(labeling_budget=3, random_state=0))
    result = detector.detect(DIRTY, table_id="lotr")
    assert len(result) == DIRTY.size
    for cell in result:
        assert 0.0 <= cell.score <= 1.0


def test_propagated_only_cells_emit_classifier_source_not_propagated():
    # A budget smaller than the table guarantees some cells are resolved
    # only by cluster propagation (never directly labeled). Per the paper
    # (Section 4.4), propagation output is training signal for the
    # per-column classifier, not a scored result in its own right -- so no
    # cell should ever surface evidence.source == "propagated".
    config = RahaConfig(labeling_budget=2, random_state=0)
    detector = RahaDetector(config)
    labeler = GroundTruthLabeler(CLEAN)

    result = detector.detect(DIRTY, table_id="lotr", labeler=labeler)

    sources = {c.evidence["source"] for c in result}
    assert "propagated" not in sources
    assert sources <= {"user_label", "classifier"}
    # With only 2 of 6 rows directly labeled, most cells must have fallen
    # through to the classifier tier -- otherwise this test would not be
    # exercising the propagated-only path at all.
    assert "classifier" in sources


def test_result_to_pandas_matches_shared_schema():
    detector = RahaDetector(RahaConfig(labeling_budget=6, random_state=0))
    result = detector.detect(DIRTY, table_id="lotr", labeler=GroundTruthLabeler(CLEAN))
    frame = result.to_pandas()
    assert list(frame.columns) == [
        "table_id",
        "row_index",
        "column_name",
        "algorithm",
        "is_error",
        "score",
        "evidence",
    ]
    assert len(frame) == DIRTY.size


def test_runs_past_the_dense_clustering_row_limit_without_crashing():
    # Regression test for OPE-22: RahaDetector.detect used to build a dense
    # O(n^2)-memory pairwise-distance array for every column on every
    # labeling iteration, which crashed with ArrayMemoryError on
    # realistically-sized tables (149GiB at 200,000 rows). Setting
    # `dense_clustering_row_limit` far below this fixture's row count
    # forces the sub-quadratic fallback path deterministically, without
    # needing an actual 200,000-row table to prove the crash is gone.
    rng = np.random.default_rng(0)
    n = 40
    dirty = pd.DataFrame(
        {
            "value": rng.integers(0, 5, size=n).astype(str),
            "flag": rng.choice(["yes", "no"], size=n),
        }
    )
    config = RahaConfig(labeling_budget=5, random_state=0, dense_clustering_row_limit=10)
    detector = RahaDetector(config)

    result = detector.detect(dirty, table_id="scale")

    assert len(result) == dirty.size
    for cell in result:
        assert isinstance(cell.is_error, bool)
        assert 0.0 <= cell.score <= 1.0
        assert not np.isnan(cell.score)


def test_dense_clustering_row_limit_rejects_non_positive_values():
    with pytest.raises(ConfigurationError):
        RahaConfig(dense_clustering_row_limit=0)
