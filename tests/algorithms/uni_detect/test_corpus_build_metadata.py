"""Unit tests for corpus/build_metadata.py (Spark mocked; no Java required)."""

from __future__ import annotations

import json
import logging
from unittest.mock import MagicMock

import pytest

from open_detect.algorithms.uni_detect.config import UniDetectConfig, UnityCatalogLocation
from open_detect.algorithms.uni_detect.corpus.build_metadata import (
    diff_fingerprints,
    property_key,
    read_build_config,
    verify_build_config,
    write_build_config,
)
from open_detect.core.enums import ErrorType
from open_detect.exceptions import ConfigurationError

FQN = "main.s.open_detect_corpus_stats"


def _config(**overrides) -> UniDetectConfig:
    return UniDetectConfig(location=UnityCatalogLocation("main", "s"), **overrides)


class FakeSpark:
    """Minimal ``spark.sql`` stand-in that stores/returns table properties."""

    def __init__(self, properties: dict[str, str] | None = None) -> None:
        self.properties = dict(properties or {})
        self.statements: list[str] = []

    def sql(self, statement: str):
        self.statements.append(statement)
        if statement.startswith("SHOW TBLPROPERTIES"):
            rows = [{"key": k, "value": v} for k, v in self.properties.items()]
            result = MagicMock()
            result.collect.return_value = rows
            return result
        if statement.startswith("ALTER TABLE"):
            body = statement.split("SET TBLPROPERTIES (", 1)[1].rstrip(")")
            for assignment in body.split(", '"):
                key, value = assignment.strip("'").split("' = '", 1)
                self.properties[key] = value.rstrip("'")
            return MagicMock()
        raise AssertionError(statement)


class TestRoundTrip:
    def test_build_config_survives_write_then_read(self):
        spark = FakeSpark()
        config = _config(epsilon=0.03, row_count_edges=(10, 20), token_length_edges=(3,))

        write_build_config(spark, FQN, [ErrorType.UNIQUENESS, ErrorType.SPELLING], config)

        for error_type in (ErrorType.UNIQUENESS, ErrorType.SPELLING):
            assert read_build_config(spark, FQN, error_type) == config.build_fingerprint()
        assert read_build_config(spark, FQN, ErrorType.NUMERIC_OUTLIER) is None

    def test_write_with_no_error_types_is_a_noop(self):
        spark = FakeSpark()
        write_build_config(spark, FQN, [], _config())
        assert spark.statements == []

    def test_matching_config_verifies(self):
        spark = FakeSpark()
        config = _config(epsilon=0.03)
        write_build_config(spark, FQN, [ErrorType.UNIQUENESS], config)
        verify_build_config(spark, FQN, ErrorType.UNIQUENESS, config)


class TestMismatch:
    def _built(self, **overrides) -> FakeSpark:
        spark = FakeSpark()
        write_build_config(spark, FQN, [ErrorType.UNIQUENESS], _config(**overrides))
        return spark

    def test_epsilon_and_edges_mismatch_raises_listing_fields(self):
        spark = self._built(epsilon=0.01, row_count_edges=(10, 20))
        active = _config(epsilon=0.05, row_count_edges=(10, 30))

        with pytest.raises(ConfigurationError) as excinfo:
            verify_build_config(spark, FQN, ErrorType.UNIQUENESS, active)

        message = str(excinfo.value)
        assert "epsilon" in message
        assert "row_count_edges" in message
        assert "prevalence_edges" not in message

    def test_override_logs_and_proceeds(self, caplog):
        spark = self._built(epsilon=0.01)
        active = _config(epsilon=0.05, allow_corpus_config_mismatch=True)

        with caplog.at_level(logging.WARNING):
            verify_build_config(spark, FQN, ErrorType.UNIQUENESS, active)

        assert any("epsilon" in r.getMessage() for r in caplog.records)

    def test_scoring_time_laplace_difference_only_warns(self, caplog):
        spark = self._built(laplace_smoothing=1.0)
        active = _config(laplace_smoothing=0.5)

        with caplog.at_level(logging.WARNING):
            verify_build_config(spark, FQN, ErrorType.UNIQUENESS, active)

        assert any("laplace_smoothing" in r.getMessage() for r in caplog.records)

    def test_alpha_is_not_part_of_the_fingerprint(self):
        spark = self._built(alpha=0.05)
        verify_build_config(spark, FQN, ErrorType.UNIQUENESS, _config(alpha=0.2))

    def test_other_error_types_are_checked_independently(self):
        spark = self._built(epsilon=0.01)
        spark.properties[property_key(ErrorType.SPELLING)] = json.dumps(
            _config(epsilon=0.5).build_fingerprint()
        )
        verify_build_config(spark, FQN, ErrorType.UNIQUENESS, _config(epsilon=0.01))
        with pytest.raises(ConfigurationError):
            verify_build_config(spark, FQN, ErrorType.SPELLING, _config(epsilon=0.01))


class TestLegacyCorpus:
    def test_missing_metadata_warns_without_raising(self, caplog):
        spark = FakeSpark({"delta.minReaderVersion": "1"})

        with caplog.at_level(logging.WARNING):
            verify_build_config(spark, FQN, ErrorType.UNIQUENESS, _config())

        assert any("legacy" in r.getMessage() for r in caplog.records)


def test_diff_fingerprints_reports_missing_fields():
    assert diff_fingerprints({"a": 1}, {"a": 1, "b": 2}) == {"b": (None, 2)}


class TestWiring:
    def test_store_load_verifies_build_config(self):
        from open_detect.algorithms.uni_detect.corpus.store import CorpusStatsStore

        spark = MagicMock()
        spark.catalog.tableExists.return_value = True
        spark.sql.return_value.collect.return_value = [
            {
                "key": property_key(ErrorType.UNIQUENESS),
                "value": json.dumps(_config(epsilon=0.5).build_fingerprint()),
            }
        ]
        store = CorpusStatsStore(spark, _config(epsilon=0.01))

        with pytest.raises(ConfigurationError, match="epsilon"):
            store.load(ErrorType.UNIQUENESS)
        spark.table.assert_not_called()

    def test_builder_write_persists_build_config_for_given_error_types(self):
        from open_detect.algorithms.uni_detect.corpus.builder import CorpusStatsBuilder

        spark = FakeSpark()
        spark.catalog = MagicMock()
        spark.catalog.tableExists.return_value = True
        config = _config(epsilon=0.07)
        stats = MagicMock()

        CorpusStatsBuilder(spark, config).write(stats, error_types=[ErrorType.SPELLING])

        stats.select.assert_not_called()
        stats.write.format.return_value.mode.return_value.option.assert_called_once_with(
            "replaceWhere", "error_type = 'spelling'"
        )
        assert read_build_config(spark, config.corpus_stats_fqn, ErrorType.SPELLING) == (
            config.build_fingerprint()
        )
