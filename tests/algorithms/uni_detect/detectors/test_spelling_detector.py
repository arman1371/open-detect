"""Source-row-id mapping for SpellingDetector (pure Python; no Spark required).

The mapping is now owned by the perturbation layer: ``PerturbationOutcome.row_ids``
carries the original 0-based positions of the dropped values (nulls included), so
``_build_row`` and these tests no longer re-derive the mapping and cannot drift
away from it.
"""

from __future__ import annotations

import hashlib
import json

import pytest

from open_detect.algorithms.uni_detect.config import UniDetectConfig, UnityCatalogLocation
from open_detect.algorithms.uni_detect.detectors.spelling import _build_row
from open_detect.algorithms.uni_detect.featurization import build_spelling_bucket
from open_detect.algorithms.uni_detect.perturbation import perturb_spelling


def _score(vals):
    """Run the same drop-nulls -> perturb sequence as ``compute``.

    ``vals`` is passed whole so the perturbation can map dropped indices back to
    original positions (nulls included); passing the pre-filtered list instead
    would silently lose that mapping.
    """
    outcome = perturb_spelling(vals, epsilon=0.1)
    return outcome, [str(i) for i in outcome.row_ids]


def _row(vals, cfg: UniDetectConfig, tid: str = "t", col: str = "c"):
    """Build a candidate row exactly as ``compute`` does, for end-to-end checks."""
    clean = [v for v in vals if v is not None]
    outcome = perturb_spelling(vals, epsilon=cfg.epsilon, max_block_size=cfg.max_mpd_block_size)
    bucket = build_spelling_bucket(
        values=clean,
        num_rows=len(vals),
        avg_differing_token_length=outcome.evidence.get("avg_differing_token_length", 0.0),
        row_count_edges=cfg.row_count_edges,
        token_length_edges=cfg.token_length_edges,
    )
    return _build_row(tid, col, vals, outcome, bucket, cfg)


def _positions_of(vals, value):
    return [str(i) for i, v in enumerate(vals) if v == value]


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


def test_build_row_maps_row_ids_via_original_positions():
    """End-to-end through ``_build_row`` for the leading-nulls scenario."""
    vals = ["zzzz", None, "appel", None, "appel", "appel", "apple", "kiwi", "plum"]
    cfg = UniDetectConfig(location=UnityCatalogLocation(catalog="t", schema="dq"), epsilon=0.1)
    row = _row(vals, cfg)
    assert row["row_ids"] == ["2", "4", "5"]
    assert row["candidate_id"].endswith("::spelling::2")


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


@pytest.mark.parametrize("mode", ["none", "hash", "drop"])
def test_evidence_honors_redact_mode(mode):
    """Spelling evidence must respect ``cfg.redact_evidence`` like the other detectors."""
    vals = ["zzzz", None, "appel", None, "appel", "apple", "kiwi", "plum"]
    cfg = UniDetectConfig(
        location=UnityCatalogLocation(catalog="t", schema="dq"), epsilon=0.1, redact_evidence=mode
    )
    row = _row(vals, cfg)
    evidence = json.loads(row["evidence_json"])
    assert "avg_differing_token_length" in evidence
    if mode == "none":
        assert evidence["pair"] == ["appel", "apple"]
    elif mode == "hash":
        assert evidence["pair"] == [
            hashlib.sha256(b"appel").hexdigest()[:16],
            hashlib.sha256(b"apple").hexdigest()[:16],
        ]
    else:  # drop
        assert "pair" not in evidence