"""Unit tests for logging_utils.py (no Spark required)."""

from __future__ import annotations

import logging

import pytest

from unidetect.logging_utils import get_logger, log_duration


class TestGetLogger:
    def test_namespaces_arbitrary_module_names(self):
        logger = get_logger("unidetect.corpus.builder")
        assert logger.name == "unidetect.corpus.builder"

    def test_prefixes_bare_module_names(self):
        logger = get_logger("some_module")
        assert logger.name == "unidetect.some_module"

    def test_root_logger_name_is_returned_unprefixed(self):
        logger = get_logger("unidetect")
        assert logger.name == "unidetect"


class TestLogDuration:
    def test_logs_started_and_completed(self, caplog):
        logger = get_logger("test_log_duration")
        with caplog.at_level(logging.INFO, logger=logger.name), log_duration(logger, "my_action"):
            pass
        messages = [r.getMessage() for r in caplog.records]
        assert any("my_action: started" in m for m in messages)
        assert any("my_action: completed" in m for m in messages)

    def test_reraises_and_logs_failure_on_exception(self, caplog):
        logger = get_logger("test_log_duration_failure")
        with (
            caplog.at_level(logging.INFO, logger=logger.name),
            pytest.raises(ValueError),
            log_duration(logger, "failing_action"),
        ):
            raise ValueError("boom")
        messages = [r.getMessage() for r in caplog.records]
        assert any("failing_action: failed" in m for m in messages)
