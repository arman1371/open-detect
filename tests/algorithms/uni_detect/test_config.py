"""Unit tests for config.py validation (no Spark required)."""

from __future__ import annotations

import json

import pytest

from open_detect.algorithms.uni_detect.config import UniDetectConfig, UnityCatalogLocation
from open_detect.algorithms.uni_detect.featurization import bucket_by_edges
from open_detect.exceptions import ConfigurationError


class TestUnityCatalogLocation:
    def test_table_builds_three_part_name(self):
        loc = UnityCatalogLocation(catalog="main", schema="data_quality")
        assert loc.table("open_detect_corpus_stats") == "main.data_quality.open_detect_corpus_stats"

    @pytest.mark.parametrize(
        "catalog,schema", [("", "s"), ("c", ""), ("bad-name", "s"), ("c", "bad name")]
    )
    def test_rejects_invalid_identifiers(self, catalog, schema):
        with pytest.raises(ConfigurationError):
            UnityCatalogLocation(catalog=catalog, schema=schema)


class TestUniDetectConfig:
    def _location(self):
        return UnityCatalogLocation(catalog="main", schema="data_quality")

    def test_defaults_are_valid(self):
        config = UniDetectConfig(location=self._location())
        assert 0 < config.epsilon <= 1
        assert 0 < config.alpha < 1

    @pytest.mark.parametrize("epsilon", [0, -0.1, 1.1])
    def test_rejects_invalid_epsilon(self, epsilon):
        with pytest.raises(ConfigurationError):
            UniDetectConfig(location=self._location(), epsilon=epsilon)

    @pytest.mark.parametrize("alpha", [0, 1, -0.1, 1.1])
    def test_rejects_invalid_alpha(self, alpha):
        with pytest.raises(ConfigurationError):
            UniDetectConfig(location=self._location(), alpha=alpha)

    @pytest.mark.parametrize("smoothing", [0, 0.0, -1.0, float("nan"), float("inf"), None])
    def test_rejects_invalid_laplace_smoothing(self, smoothing):
        with pytest.raises(ConfigurationError, match="laplace_smoothing"):
            UniDetectConfig(location=self._location(), laplace_smoothing=smoothing)

    def test_accepts_tiny_positive_laplace_smoothing(self):
        config = UniDetectConfig(location=self._location(), laplace_smoothing=1e-12)
        assert config.laplace_smoothing == 1e-12

    @pytest.mark.parametrize("name", ["row_count_edges", "prevalence_edges", "token_length_edges"])
    @pytest.mark.parametrize(
        "edges",
        [(), (5, 5), (10, 5), (1, 3, 2), (1, float("nan")), (1, float("inf")), (float("-inf"), 1)],
    )
    def test_rejects_invalid_edges(self, name, edges):
        with pytest.raises(ConfigurationError, match=name):
            UniDetectConfig(location=self._location(), **{name: edges})

    def test_accepts_single_edge_and_normalizes_lists_to_tuples(self):
        config = UniDetectConfig(location=self._location(), row_count_edges=[10])
        assert config.row_count_edges == (10,)

    def test_validated_edges_never_break_bucketing(self):
        config = UniDetectConfig(location=self._location(), row_count_edges=(10,))
        assert bucket_by_edges(5, config.row_count_edges) == "(-inf,10]"
        assert bucket_by_edges(50, config.row_count_edges) == "(10,inf)"

    def test_bucket_by_edges_tolerates_empty_edges(self):
        assert bucket_by_edges(5, ()) == "(-inf,inf)"

    def test_build_fingerprint_is_json_round_trippable(self):
        config = UniDetectConfig(location=self._location(), epsilon=0.02)
        fingerprint = config.build_fingerprint()
        assert json.loads(json.dumps(fingerprint)) == fingerprint
        assert fingerprint["epsilon"] == 0.02
        assert fingerprint["row_count_edges"] == list(config.row_count_edges)

    @pytest.mark.parametrize("max_mpd_block_size", [0, 1, -5])
    def test_rejects_too_small_max_mpd_block_size(self, max_mpd_block_size):
        with pytest.raises(ConfigurationError):
            UniDetectConfig(location=self._location(), max_mpd_block_size=max_mpd_block_size)

    @pytest.mark.parametrize("max_fd_column_pairs_per_table", [0, -1])
    def test_rejects_too_small_max_fd_column_pairs_per_table(self, max_fd_column_pairs_per_table):
        with pytest.raises(ConfigurationError):
            UniDetectConfig(
                location=self._location(),
                max_fd_column_pairs_per_table=max_fd_column_pairs_per_table,
            )

    def test_fully_qualified_table_names(self):
        config = UniDetectConfig(location=self._location())
        assert config.corpus_stats_fqn == "main.data_quality.open_detect_corpus_stats"
        assert config.token_stats_fqn == "main.data_quality.open_detect_token_stats"
        assert config.detections_fqn == "main.data_quality.open_detect_detections"


class TestRedactEvidence:
    def test_defaults_to_none(self):
        assert UniDetectConfig(location=UnityCatalogLocation("c", "s")).redact_evidence == "none"

    @pytest.mark.parametrize("mode", ["none", "hash", "drop"])
    def test_accepts_valid_modes(self, mode):
        cfg = UniDetectConfig(location=UnityCatalogLocation("c", "s"), redact_evidence=mode)
        assert cfg.redact_evidence == mode

    def test_rejects_unknown_mode(self):
        with pytest.raises(ConfigurationError, match="redact_evidence"):
            UniDetectConfig(location=UnityCatalogLocation("c", "s"), redact_evidence="mask")

    def test_not_part_of_build_fingerprint(self):
        loc = UnityCatalogLocation("c", "s")
        assert (
            UniDetectConfig(location=loc).build_fingerprint()
            == UniDetectConfig(location=loc, redact_evidence="drop").build_fingerprint()
        )
