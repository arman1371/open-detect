"""Tests for notifications config module."""

from __future__ import annotations

import os
from unittest.mock import patch

import pytest

from open_detect.notifications.config import (
    get_notification_config,
    get_rate_limit,
    get_severity_threshold,
    get_teams_enabled,
    get_teams_webhook_url,
)


class TestGetTeamsWebhookUrl:
    """Tests for get_teams_webhook_url."""

    def test_returns_webhook_url_when_set(self):
        with patch.dict(os.environ, {"TEAMS_WEBHOOK_URL": "https://webhook.url"}):
            assert get_teams_webhook_url() == "https://webhook.url"

    def test_returns_none_when_not_set(self):
        with patch.dict(os.environ, {}, clear=True):
            assert get_teams_webhook_url() is None

    def test_returns_empty_when_empty_string(self):
        with patch.dict(os.environ, {"TEAMS_WEBHOOK_URL": ""}):
            assert get_teams_webhook_url() == ""


class TestGetTeamsEnabled:
    """Tests for get_teams_enabled."""

    @pytest.mark.parametrize("val", ["true", "True", "TRUE", "1", "yes", "on"])
    def test_returns_true_for_truthy_values(self, val):
        with patch.dict(os.environ, {"TEAMS_NOTIFICATION_ENABLED": val}):
            assert get_teams_enabled() is True

    @pytest.mark.parametrize("val", ["false", "False", "0", "no", "off", ""])
    def test_returns_false_for_falsy_values(self, val):
        with patch.dict(os.environ, {"TEAMS_NOTIFICATION_ENABLED": val}):
            assert get_teams_enabled() is False

    def test_returns_false_when_not_set(self):
        with patch.dict(os.environ, {}, clear=True):
            assert get_teams_enabled() is False


class TestGetSeverityThreshold:
    """Tests for get_severity_threshold."""

    @pytest.mark.parametrize("val", ["low", "medium", "high", "critical"])
    def test_returns_env_value_when_set(self, val):
        with patch.dict(os.environ, {"TEAMS_SEVERITY_THRESHOLD": val}):
            assert get_severity_threshold() == val

    def test_returns_default_when_not_set(self):
        with patch.dict(os.environ, {}, clear=True):
            assert get_severity_threshold() == "medium"


class TestGetRateLimit:
    """Tests for get_rate_limit."""

    def test_returns_parsed_value_when_set(self):
        with patch.dict(os.environ, {"TEAMS_RATE_LIMIT_MAX_PER_HOUR": "10"}):
            assert get_rate_limit() == {"max_per_hour": 10}

    def test_returns_default_when_not_set(self):
        with patch.dict(os.environ, {}, clear=True):
            assert get_rate_limit() == {"max_per_hour": 5}

    def test_returns_default_when_invalid(self):
        """Test that invalid rate limit value raises ValueError."""
        with (
            patch.dict(os.environ, {"TEAMS_RATE_LIMIT_MAX_PER_HOUR": "not_a_number"}),
            pytest.raises(ValueError),
        ):
            get_rate_limit()


class TestGetNotificationConfig:
    """Tests for get_notification_config."""

    def test_returns_complete_config(self):
        with patch.dict(
            os.environ,
            {
                "TEAMS_WEBHOOK_URL": "https://test.url",
                "TEAMS_NOTIFICATION_ENABLED": "true",
                "TEAMS_SEVERITY_THRESHOLD": "high",
                "TEAMS_RATE_LIMIT_MAX_PER_HOUR": "3",
            },
        ):
            config = get_notification_config()
            assert config["webhook_url"] == "https://test.url"
            assert config["enabled"] is True
            assert config["severity_threshold"] == "high"
            assert config["rate_limit"] == {"max_per_hour": 3}

    def test_returns_defaults_when_not_set(self):
        with patch.dict(os.environ, {}, clear=True):
            config = get_notification_config()
            assert config["webhook_url"] is None
            assert config["enabled"] is False
            assert config["severity_threshold"] == "medium"
            assert config["rate_limit"] == {"max_per_hour": 5}

    def test_mixed_env_values(self):
        """Test with mixed explicit and default values."""
        with patch.dict(
            os.environ,
            {
                "TEAMS_WEBHOOK_URL": "https://custom.webhook.url",
                "TEAMS_NOTIFICATION_ENABLED": "false",
                # TEAMS_SEVERITY_THRESHOLD not set - should use default
                # TEAMS_RATE_LIMIT_MAX_PER_HOUR not set - should use default
            },
            clear=True,
        ):
            config = get_notification_config()
            assert config["webhook_url"] == "https://custom.webhook.url"
            assert config["enabled"] is False
            assert config["severity_threshold"] == "medium"  # default
            assert config["rate_limit"] == {"max_per_hour": 5}  # default
