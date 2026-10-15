"""Hygiene tests: evidence redaction, assert-free narrowing, table-name log levels (no Spark)."""

from __future__ import annotations

import json
import logging
from unittest.mock import MagicMock

import pytest

from open_detect.algorithms.uni_detect.config import UniDetectConfig, UnityCatalogLocation
from open_detect.algorithms.uni_detect.detectors.base import (
    BaseDetector,
    make_evidence_json,
    redact_evidence,
)
from open_detect.algorithms.uni_detect.pipeline import _require_columns
from open_detect.core.enums import ErrorType
from open_detect.exceptions import ConfigurationError

EVIDENCE = {
    "duplicate_values": ["alice@example.com", "alice@example.com"],
    "violating_examples": [("NYC", "NY"), ("NYC", "NJ")],
    "pair": ("Dowling", "Doeling"),
    "outlier_value": 99999.0,
    "num_duplicate_values": 2,
    "avg_differing_token_length": 7.0,
}
RAW_KEYS = {"duplicate_values", "violating_examples", "pair", "outlier_value"}


class TestRedactEvidence:
    def test_none_keeps_everything(self):
        assert json.loads(make_evidence_json(EVIDENCE)) == json.loads(
            json.dumps(EVIDENCE, default=str)
        )

    def test_drop_removes_raw_values_only(self):
        out = redact_evidence(EVIDENCE, "drop")
        assert RAW_KEYS.isdisjoint(out)
        assert out == {"num_duplicate_values": 2, "avg_differing_token_length": 7.0}

    def test_hash_replaces_raw_values_and_keeps_shape(self):
        out = redact_evidence(EVIDENCE, "hash")
        assert out["num_duplicate_values"] == 2
        assert out["duplicate_values"][0] == out["duplicate_values"][1]  # equality preserved
        assert out["duplicate_values"][0] != "alice@example.com"
        assert out["violating_examples"][0][0] == out["violating_examples"][1][0]
        assert isinstance(out["outlier_value"], str)
        serialized = make_evidence_json(EVIDENCE, "hash")
        for raw in ("alice@example.com", "Dowling", "NYC", "99999"):
            assert raw not in serialized

    def test_does_not_mutate_input(self):
        snapshot = json.dumps(EVIDENCE, default=str)
        redact_evidence(EVIDENCE, "hash")
        redact_evidence(EVIDENCE, "drop")
        assert json.dumps(EVIDENCE, default=str) == snapshot


class TestRequireColumns:
    def test_returns_dataframe(self):
        df = MagicMock()
        assert _require_columns(df) is df

    def test_raises_configuration_error_not_assertion(self):
        with pytest.raises(ConfigurationError):
            _require_columns(None)


class _NoCandidatesDetector(BaseDetector):
    error_type = ErrorType.UNIQUENESS

    def extract_candidates(self, table_names):
        candidates = MagicMock()
        candidates.count.return_value = 0
        return candidates


def test_table_names_logged_as_count_at_info_and_list_at_debug(caplog):
    config = UniDetectConfig(location=UnityCatalogLocation("c", "s"))
    detector = _NoCandidatesDetector(MagicMock(), config)
    tables = ["main.sales.orders", "main.sales.customers"]
    with caplog.at_level(logging.DEBUG, logger="open_detect"):
        detector.detect(tables)

    info = [r for r in caplog.records if r.levelno == logging.INFO]
    debug = [r for r in caplog.records if r.levelno == logging.DEBUG]
    assert not any("main.sales.orders" in r.getMessage() for r in info)
    assert any("2 table(s)" in r.getMessage() for r in info)
    assert any("main.sales.orders" in r.getMessage() for r in debug)
