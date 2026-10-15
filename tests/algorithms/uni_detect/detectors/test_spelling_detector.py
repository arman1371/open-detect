"""Original-row-id mapping for SpellingDetector (pure Python; no Spark required)."""

from __future__ import annotations

import pytest

from open_detect.algorithms.uni_detect.detectors.spelling import (
    _drop_nulls,
    _original_row_ids,
)
from open_detect.algorithms.uni_detect.perturbation import perturb_spelling


def _score(vals):
    """Run the same drop-nulls -> perturb -> map-back sequence as ``compute``."""
    clean, positions = _drop_nulls(vals)
    outcome = perturb_spelling(clean, epsilon=0.1)
    return outcome, _original_row_ids(outcome.dropped_indices, positions)


def _positions_of(vals, value):
    return [str(i) for i, v in enumerate(vals) if v == value]


def test_drop_nulls_returns_original_positions():
    clean, positions = _drop_nulls([None, "a", None, "b"])
    assert clean == ["a", "b"]
    assert positions == [1, 3]


def test_leading_nulls_map_to_original_positions():
    vals = [None, None, "apple", "apple", "appel", "banana", "cherry", "grape"]
    outcome, ids = _score(vals)
    assert outcome.dropped_indices == (0, 1)
    assert ids == ["2", "3"]


def test_duplicates_map_every_occurrence_in_ascending_order():
    vals = ["zzzz", None, "appel", None, "appel", "appel", "apple", "kiwi", "plum"]
    outcome, ids = _score(vals)
    assert len(ids) == 3
    assert ids == _positions_of(vals, "appel")
    assert ids == sorted(ids, key=int)
    assert outcome.dropped_indices == (1, 2, 3)


def test_nulls_interleaved_between_duplicates():
    vals = ["zzzz", None, "appel", None, None, "appel", None, "appel", "apple", "kiwi", "plum"]
    _, ids = _score(vals)
    assert ids == ["2", "5", "7"]


def test_no_nulls_is_identity_mapping():
    vals = ["apple", "apple", "appel", "banana", "cherry", "grape"]
    outcome, ids = _score(vals)
    assert ids == [str(i) for i in outcome.dropped_indices]
    assert ids == ["0", "1"]


@pytest.mark.parametrize("n_leading_nulls", [0, 1, 3])
def test_candidate_id_suffix_uses_first_mapped_row_id(n_leading_nulls):
    vals = [None] * n_leading_nulls + ["apple", "apple", "appel", "banana", "cherry", "grape"]
    _, ids = _score(vals)
    assert ids[0] == str(n_leading_nulls)
