"""Tests for UniDetect.build_corpus_statistics covering ingest, token stats, and cleanup."""

from unittest.mock import MagicMock
import pytest

from open_detect.algorithms.uni_detect.pipeline import UniDetect
from open_detect.algorithms.uni_detect.config import UniDetectConfig, UnityCatalogLocation
from open_detect.algorithms.uni_detect.core.enums import ErrorType

def _config() -> UniDetectConfig:
    return UniDetectConfig(location=UnityCatalogLocation(catalog="c", schema="s"))


def test_build_corpus_statistics_calls_ingest_and_unpersist(monkeypatch):
    """Ensure ingest_columns is called, result is cached, and unpersisted after processing."""
    # Mock Spark and the ingestor
    mock_spark = MagicMock()
    mock_ingestor = MagicMock()
    mock_columns_df = MagicMock()
    # cache() returns the same mock, unpersist will be tracked
    mock_columns_df.cache.return_value = mock_columns_df
    mock_ingestor.ingest_columns.return_value = mock_columns_df
    # Patch CorpusIngestor to return our mock ingestor
    monkeypatch.setattr(
        "open_detect.algorithms.uni_detect.pipeline.CorpusIngestor",
        lambda *args, **kwargs: mock_ingestor,
    )
    # Patch CorpusStatsBuilder to a simple mock with write method
    mock_builder = MagicMock()
    monkeypatch.setattr(
        "open_detect.algorithms.uni_detect.pipeline.CorpusStatsBuilder",
        lambda *args, **kwargs: mock_builder,
    )
    # Create UniDetect instance with mocked Spark
    ud = UniDetect(_config(), spark=mock_spark)
    # Run with a single error type that only needs columns
    ud.build_corpus_statistics(["t1"], error_types=[ErrorType.UNIQUENESS])

    # Verify ingest_columns was called and cache/unpersist flow executed
    mock_ingestor.ingest_columns.assert_called_once_with(["t1"])
    mock_columns_df.cache.assert_called_once()
    mock_columns_df.unpersist.assert_called_once()


def test_build_corpus_statistics_token_path(monkeypatch):
    """When an error type needs tokens, build_token_stats is invoked."""
    mock_spark = MagicMock()
    mock_ingestor = MagicMock()
    mock_columns_df = MagicMock()
    mock_columns_df.cache.return_value = mock_columns_df
    mock_ingestor.ingest_columns.return_value = mock_columns_df
    # token stats path
    mock_token_stats = MagicMock()
    mock_ingestor.build_token_stats.return_value = mock_token_stats
    # Patch ingestor
    monkeypatch.setattr(
        "open_detect.algorithms.uni_detect.pipeline.CorpusIngestor",
        lambda *args, **kwargs: mock_ingestor,
    )
    # Mock builder
    mock_builder = MagicMock()
    monkeypatch.setattr(
        "open_detect.algorithms.uni_detect.pipeline.CorpusStatsBuilder",
        lambda *args, **kwargs: mock_builder,
    )
    ud = UniDetect(_config(), spark=mock_spark)
    # Use an error type that requires token stats (functional dependency)
    ud.build_corpus_statistics(
        ["t1"],
        error_types=[ErrorType.FUNCTIONAL_DEPENDENCY],
    )
    # Verify token stats building was called
    mock_ingestor.build_token_stats.assert_called_once()
    # Ensure columns were still cached and unpersisted
    mock_columns_df.cache.assert_called_once()
    mock_columns_df.unpersist.assert_called_once()


def test_detect_exception_calls_release(monkeypatch):
    """If a detector raises, all detectors' release() should be invoked."""
    mock_spark = MagicMock()
    ud = UniDetect(_config(), spark=mock_spark)
    # Prepare detectors: one will raise, others are normal
    good_detector = MagicMock()
    good_detector.detect.return_value = MagicMock()
    bad_detector = MagicMock()
    bad_detector.detect.side_effect = RuntimeError("boom")
    ud._detectors = {
        ErrorType.UNIQUENESS: good_detector,
        ErrorType.SPELLING: bad_detector,
    }
    # Expect RuntimeError when calling detect
    with pytest.raises(RuntimeError):
        ud.detect(["t1"], error_types=[ErrorType.UNIQUENESS, ErrorType.SPELLING])
    # Both detectors should have release called
    good_detector.release.assert_called_once()
    bad_detector.release.assert_called_once()
