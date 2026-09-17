"""Unit tests for config.py validation (no Spark required)."""

from __future__ import annotations

import pytest

from unidetect.config import UniDetectConfig, UnityCatalogLocation
from unidetect.exceptions import ConfigurationError


class TestUnityCatalogLocation:
    def test_table_builds_three_part_name(self):
        loc = UnityCatalogLocation(catalog="main", schema="data_quality")
        assert loc.table("unidetect_corpus_stats") == "main.data_quality.unidetect_corpus_stats"

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

    def test_fully_qualified_table_names(self):
        config = UniDetectConfig(location=self._location())
        assert config.corpus_stats_fqn == "main.data_quality.unidetect_corpus_stats"
        assert config.token_stats_fqn == "main.data_quality.unidetect_token_stats"
        assert config.detections_fqn == "main.data_quality.unidetect_detections"
