"""Tests for notifications config module."""

from __future__ import annotations

import os
from unittest.mock import patch

import pytest

from open_detect.notifications.config import (
    DEFAULT_RATE_LIMIT,
    DEFAULT_SEVERITY_THRESHOLD,
    get_notification_config,
    get_rate_limit,
    get_severity_threshold,
    get_teams_enabled,
    get_teams_webhook_url,
)


class TestGetTeamsWebhookUrl:
    """Tests for get_teams_webhook_url."""

    def test_returns_url_when_set(self):
        with patch.dict(os.environ, {"TEAMS_WEBHOOK_URL": "https://webhook.url"}):
            assert get_teams_webhook_url() == "https://webhook.url"

    def test_returns_none_when_not_set(self):
        with patch.dict(os.environ, {}, clear=True):
            assert get_teams_webhook_url() is None

    def test_warns_when_not_https(self, caplog):
        with patch.dict(os.environ, {"TEAMS_WEBHOOK_URL": "http://insecure.url"}):
            get_teams_webhook_url()
            assert "does not start with https://" in caplog.text


class TestGetTeamsEnabled:
    """Tests for get_teams_enabled."""

    @pytest.mark.parametrize("val", ["true", "True", "1", "yes", "on"])
    def test_true_values(self, val):
        with patch.dict(os.environ, {"TEAMS_NOTIFICATION_ENABLED": val}):
            assert get_teams_enabled() is True

    @pytest.mark.parametrize("val", ["false", "0", "no", "off", ""])
    def test_false_values(self, val):
        with patch.dict(os.environ, {"TEAMS_NOTIFICATION_ENABLED": val}):
            assert get_teams_enabled() is False

    def test_default_false(self):
        with patch.dict(os.environ, {}, clear=True):
            assert get_teams_enabled() is False


class TestGetSeverityThreshold:
    """Tests for get_severity_threshold."""

    @pytest.mark.parametrize("val", ["low", "medium", "high", "critical"])
    def test_valid_values(self, val):
        with patch.dict(os.environ, {"TEAMS_SEVERITY_THRESHOLD": val}):
            assert get_severity_threshold() == val

    def test_case_insensitive(self):
        with patch.dict(os.environ, {"TEAMS_SEVERITY_THRESHOLD": "HIGH"}):
            assert get_severity_threshold() == "high"

    def test_default_medium(self):
        with patch.dict(os.environ, {}, clear=True):
            assert get_severity_threshold() == DEFAULT_SEVERITY_THRESHOLD

    def test_invalid_defaults_to_medium(self, caplog):
        with patch.dict(os.environ, {"TEAMS_SEVERITY_THRESHOLD": "invalid"}):
            result = get_severity_threshold()
            assert result == DEFAULT_SEVERITY_THRESHOLD
            assert "Invalid TEAMS_SEVERITY_THRESHOLD" in caplog.text


class TestGetRateLimit:
    """Tests for get_rate_limit."""

    def test_valid_integer(self):
        with patch.dict(os.environ, {"TEAMS_RATE_LIMIT_MAX_PER_HOUR": "10"}):
            result = get_rate_limit()
            assert result == {"max_per_hour": 10}

    def test_default_five(self):
        with patch.dict(os.environ, {}, clear=True):
            result = get_rate_limit()
            assert result == DEFAULT_RATE_LIMIT.copy()

    def test_zero_defaults_to_five(self, caplog):
        with patch.dict(os.environ, {"TEAMS_RATE_LIMIT_MAX_PER_HOUR": "0"}):
            result = get_rate_limit()
            assert result == DEFAULT_RATE_LIMIT.copy()
            assert "must be positive" in caplog.text

    def test_negative_defaults_to_five(self, caplog):
        with patch.dict(os.environ, {"TEAMS_RATE_LIMIT_MAX_PER_HOUR": "-1"}):
            result = get_rate_limit()
            assert result == DEFAULT_RATE_LIMIT.copy()
            assert "must be positive" in caplog.text

    def test_non_integer_defaults_to_five(self, caplog):
        with patch.dict(os.environ, {"TEAMS_RATE_LIMIT_MAX_PER_HOUR": "abc"}):
            result = get_rate_limit()
            assert result == DEFAULT_RATE_LIMIT.copy()
            assert "must be integer" in caplog.text

    def test_returns_copy_not_same_dict(self):
        with patch.dict(os.environ, {}, clear=True):
            result1 = get_rate_limit()
            result2 = get_rate_limit()
            assert result1 is not result2
            assert result1 == result2


class TestGetNotificationConfig:
    """Tests for get_notification_config."""

    def test_returns_all_keys(self):
        with patch.dict(
            os.environ,
            {
                "TEAMS_WEBHOOK_URL": "https://webhook.url",
                "TEAMS_NOTIFICATION_ENABLED": "true",
                "TEAMS_SEVERITY_THRESHOLD": "high",
                "TEAMS_RATE_LIMIT_MAX_PER_HOUR": "10",
            },
        ):
            config = get_notification_config()
            assert config["webhook_url"] == "https://webhook.url"
            assert config["enabled"] is True
            assert config["severity_threshold"] == "high"
            assert config["rate_limit"] == {"max_per_hour": 10}

    def test_all_defaults(self):
        with patch.dict(os.environ, {}, clear=True):
            config = get_notification_config()
            assert config["webhook_url"] is None
            assert config["enabled"] is False
            assert config["severity_threshold"] == DEFAULT_SEVERITY_THRESHOLD
            assert config["rate_limit"] == DEFAULT_RATE_LIMIT.copy()

    def test_returns_new_dict_each_call(self):
        with patch.dict(os.environ, {}, clear=True):
            config1 = get_notification_config()
            config2 = get_notification_config()
            assert config1 is not config2
            assert config1 == config2
