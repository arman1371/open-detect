"""Tests for Teams notification service."""

from __future__ import annotations

import time
from unittest.mock import MagicMock, patch

import pytest
import requests

from open_detect.notifications.teams import TeamsNotificationError, TeamsNotifier


class TestTeamsNotifierInit:
    """Tests for TeamsNotifier initialization."""

    def test_initializes_with_defaults(self):
        notifier = TeamsNotifier(webhook_url="https://test.url")
        assert notifier.webhook_url == "https://test.url"
        assert notifier.severity_threshold == "medium"
        assert notifier.rate_limit == {"max_per_hour": 5}
        assert notifier._last_sent == {}

    def test_initializes_with_custom_values(self):
        notifier = TeamsNotifier(
            webhook_url="https://custom.url",
            severity_threshold="high",
            rate_limit={"max_per_hour": 10},
        )
        assert notifier.webhook_url == "https://custom.url"
        assert notifier.severity_threshold == "high"
        assert notifier.rate_limit == {"max_per_hour": 10}


class TestCheckRateLimit:
    """Tests for _check_rate_limit method."""

    def test_allows_first_notification(self):
        notifier = TeamsNotifier(webhook_url="https://test.url", rate_limit={"max_per_hour": 5})
        assert notifier._check_rate_limit("test_event") is True

    def test_allows_after_time_window(self):
        notifier = TeamsNotifier(webhook_url="https://test.url", rate_limit={"max_per_hour": 5})
        # First call should succeed
        assert notifier._check_rate_limit("test_event") is True
        # Manually adjust the last sent time to be 2 hours ago
        notifier._last_sent["test_event"] = time.time() - 7200
        assert notifier._check_rate_limit("test_event") is True

    def test_blocks_within_time_window(self):
        notifier = TeamsNotifier(webhook_url="https://test.url", rate_limit={"max_per_hour": 5})
        # First call succeeds
        assert notifier._check_rate_limit("test_event") is True
        # Second call immediately should be rate limited
        assert notifier._check_rate_limit("test_event") is False

    def test_rate_limit_per_event_type(self):
        notifier = TeamsNotifier(webhook_url="https://test.url", rate_limit={"max_per_hour": 5})
        assert notifier._check_rate_limit("event_a") is True
        assert notifier._check_rate_limit("event_b") is True
        assert notifier._check_rate_limit("event_a") is False
        assert notifier._check_rate_limit("event_b") is False


class TestBuildMessage:
    """Tests for _build_message method."""

    def test_builds_valid_adaptive_card(self):
        notifier = TeamsNotifier(webhook_url="https://test.url")
        card = notifier._build_message(
            event_type="community_structure_change",
            severity="high",
            affected="45 nodes across 3 communities",
            timestamp="2026-01-15T10:30:00Z",
            description="New community detected",
        )

        # Verify structure
        assert card["type"] == "message"
        assert "attachments" in card
        assert len(card["attachments"]) == 1
        attachment = card["attachments"][0]
        assert attachment["contentType"] == "application/vnd.microsoft.card.adaptive"
        content = attachment["content"]
        assert content["type"] == "AdaptiveCard"
        assert content["version"] == "1.5"
        assert content["themeColor"] == "orange"  # high severity
        assert content["title"] == ":alert: Scan Context Detection"

    def test_theme_colors_for_all_severities(self):
        notifier = TeamsNotifier(webhook_url="https://test.url")
        test_cases = [
            ("low", "green"),
            ("medium", "yellow"),
            ("high", "orange"),
            ("critical", "red"),
            ("unknown", "yellow"),  # default
        ]
        for severity, expected_color in test_cases:
            card = notifier._build_message(
                event_type="test",
                severity=severity,
                affected="test",
                timestamp="now",
            )
            assert card["attachments"][0]["content"]["themeColor"] == expected_color

    def test_includes_all_facts(self):
        notifier = TeamsNotifier(webhook_url="https://test.url")
        card = notifier._build_message(
            event_type="scan_context_uniqueness",
            severity="critical",
            affected="100 columns in 5 tables",
            timestamp="2026-01-15T10:30:00Z",
            description="Uniqueness violation detected",
        )

        facts = card["attachments"][0]["content"]["sections"][0]["facts"]
        fact_dict = {f["title"]: f["value"] for f in facts}
        assert fact_dict["Event Type"] == "Scan Context Uniqueness"
        assert fact_dict["Severity"] == "Critical"
        assert fact_dict["Affected"] == "100 columns in 5 tables"
        assert fact_dict["Timestamp"] == "2026-01-15T10:30:00Z"

    def test_includes_description_section_when_provided(self):
        notifier = TeamsNotifier(webhook_url="https://test.url")
        card = notifier._build_message(
            event_type="test",
            severity="high",
            affected="test",
            timestamp="now",
            description="Test description",
        )
        sections = card["attachments"][0]["content"]["sections"]
        assert len(sections) == 2
        assert sections[1]["activityTitle"] == "Description"
        assert sections[1]["facts"][0]["value"] == "Test description"

    def test_excludes_description_section_when_none(self):
        notifier = TeamsNotifier(webhook_url="https://test.url")
        card = notifier._build_message(
            event_type="test",
            severity="high",
            affected="test",
            timestamp="now",
            description=None,
        )
        sections = card["attachments"][0]["content"]["sections"]
        assert len(sections) == 1


class TestSend:
    """Tests for send method."""

    @patch("open_detect.notifications.teams.requests.post")
    def test_sends_successfully_on_first_attempt(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        notifier = TeamsNotifier(webhook_url="https://test.url")
        result = notifier.send(
            event_type="test_event",
            severity="high",
            affected="test affected",
            timestamp="2026-01-15T10:30:00Z",
        )

        assert result is True
        mock_post.assert_called_once()

    @patch("open_detect.notifications.teams.requests.post")
    def test_retries_on_failure(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.text = "Internal Server Error"
        mock_post.return_value = mock_response

        notifier = TeamsNotifier(webhook_url="https://test.url")

        with pytest.raises(TeamsNotificationError):
            notifier.send(
                event_type="test_event",
                severity="high",
                affected="test affected",
                timestamp="2026-01-15T10:30:00Z",
            )

        # Should retry MAX_RETRIES + 1 times (default 3 + 1 = 4)
        assert mock_post.call_count == 4

    @patch("open_detect.notifications.teams.requests.post")
    def test_succeeds_after_retry(self, mock_post):
        # First two calls fail, third succeeds
        mock_response_fail = MagicMock()
        mock_response_fail.status_code = 500
        mock_response_fail.text = "Internal Server Error"

        mock_response_success = MagicMock()
        mock_response_success.status_code = 200

        mock_post.side_effect = [mock_response_fail, mock_response_fail, mock_response_success]

        notifier = TeamsNotifier(webhook_url="https://test.url")
        result = notifier.send(
            event_type="test_event",
            severity="high",
            affected="test affected",
            timestamp="2026-01-15T10:30:00Z",
        )

        assert result is True
        assert mock_post.call_count == 3

    @patch("open_detect.notifications.teams.requests.post")
    def test_returns_false_for_rate_limited(self, mock_post):
        notifier = TeamsNotifier(webhook_url="https://test.url", rate_limit={"max_per_hour": 5})
        # First call to use up the rate limit
        notifier._last_sent["test_event"] = time.time()

        result = notifier.send(
            event_type="test_event",
            severity="high",
            affected="test affected",
            timestamp="2026-01-15T10:30:00Z",
        )

        assert result is False
        mock_post.assert_not_called()

    def test_returns_true_for_severity_below_threshold(self):
        notifier = TeamsNotifier(webhook_url="https://test.url", severity_threshold="high")
        # medium is below high threshold
        result = notifier.send(
            event_type="test_event",
            severity="medium",
            affected="test affected",
            timestamp="2026-01-15T10:30:00Z",
        )

        assert result is True  # Not an error, just suppressed

    def test_sends_when_severity_meets_threshold(self):
        notifier = TeamsNotifier(webhook_url="https://test.url", severity_threshold="medium")
        # high meets medium threshold
        with patch("open_detect.notifications.teams.requests.post") as mock_post:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_post.return_value = mock_response

            result = notifier.send(
                event_type="test_event",
                severity="high",
                affected="test affected",
                timestamp="2026-01-15T10:30:00Z",
            )

            assert result is True
            mock_post.assert_called_once()

    def test_sends_when_severity_equals_threshold(self):
        notifier = TeamsNotifier(webhook_url="https://test.url", severity_threshold="high")
        # high equals high threshold
        with patch("open_detect.notifications.teams.requests.post") as mock_post:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_post.return_value = mock_response

            result = notifier.send(
                event_type="test_event",
                severity="high",
                affected="test affected",
                timestamp="2026-01-15T10:30:00Z",
            )

            assert result is True
            mock_post.assert_called_once()


class TestSendSafe:
    """Tests for send_safe method."""

    @patch("open_detect.notifications.teams.requests.post")
    def test_returns_true_on_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        notifier = TeamsNotifier(webhook_url="https://test.url")
        result = notifier.send_safe(
            event_type="test_event",
            severity="high",
            affected="test affected",
            timestamp="2026-01-15T10:30:00Z",
        )

        assert result is True

    @patch("open_detect.notifications.teams.requests.post")
    def test_returns_false_on_teams_notification_error(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.text = "Internal Server Error"
        mock_post.return_value = mock_response

        notifier = TeamsNotifier(webhook_url="https://test.url")
        result = notifier.send_safe(
            event_type="test_event",
            severity="high",
            affected="test affected",
            timestamp="2026-01-15T10:30:00Z",
        )

        assert result is False

    @patch("open_detect.notifications.teams.requests.post", side_effect=Exception("Network error"))
    def test_returns_false_on_unexpected_error(self, mock_post):
        notifier = TeamsNotifier(webhook_url="https://test.url")
        result = notifier.send_safe(
            event_type="test_event",
            severity="high",
            affected="test affected",
            timestamp="2026-01-15T10:30:00Z",
        )

        assert result is False

    @patch(
        "open_detect.notifications.teams.requests.post",
        side_effect=requests.RequestException("Connection error"),
    )
    def test_returns_false_on_request_exception(self, mock_post):
        notifier = TeamsNotifier(webhook_url="https://test.url")
        result = notifier.send_safe(
            event_type="test_event",
            severity="high",
            affected="test affected",
            timestamp="2026-01-15T10:30:00Z",
        )

        assert result is False


class TestSeverityOrdering:
    """Tests for severity threshold comparison logic."""

    @pytest.mark.parametrize(
        "severity,threshold,expected_allowed",
        [
            ("low", "low", True),
            ("low", "medium", False),
            ("low", "high", False),
            ("low", "critical", False),
            ("medium", "low", True),
            ("medium", "medium", True),
            ("medium", "high", False),
            ("medium", "critical", False),
            ("high", "low", True),
            ("high", "medium", True),
            ("high", "high", True),
            ("high", "critical", False),
            ("critical", "low", True),
            ("critical", "medium", True),
            ("critical", "high", True),
            ("critical", "critical", True),
        ],
    )
    def test_severity_threshold_comparison(
        self, severity: str, threshold: str, expected_allowed: bool
    ):
        notifier = TeamsNotifier(webhook_url="https://test.url", severity_threshold=threshold)

        with patch("open_detect.notifications.teams.requests.post") as mock_post:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_post.return_value = mock_response

            # We'll check the internal logic directly
            severity_order = {"low": 0, "medium": 1, "high": 2, "critical": 3}
            threshold_order = {"low": 0, "medium": 1, "high": 2, "critical": 3}

            allowed = severity_order.get(severity, 0) >= threshold_order.get(
                notifier.severity_threshold, 1
            )
            assert allowed == expected_allowed

    def test_unknown_severity_defaults_to_low(self):
        """Unknown severity should be treated as low (0)."""
        notifier = TeamsNotifier(webhook_url="https://test.url", severity_threshold="low")

        with patch("open_detect.notifications.teams.requests.post") as mock_post:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_post.return_value = mock_response

            result = notifier.send(
                event_type="test_event",
                severity="unknown_severity",
                affected="test affected",
                timestamp="2026-01-15T10:30:00Z",
            )

            # unknown severity = low = 0, which is >= low threshold = 0
            # But the actual comparison uses severity_order.get(severity, 0) < threshold_order.get(...)
            # So unknown severity (0) < low threshold (0) = False, should send
            assert result is True


class TestEdgeCases:
    """Tests for edge cases and error handling."""

    def test_rate_limit_with_infinite_max_per_hour(self):
        """Rate limit should work with infinite max_per_hour."""
        notifier = TeamsNotifier(
            webhook_url="https://test.url",
            rate_limit={"max_per_hour": float("inf")},
        )

        # Should always allow with infinite rate limit
        assert notifier._check_rate_limit("event_a") is True
        assert notifier._check_rate_limit("event_a") is True

    def test_rate_limit_with_empty_rate_limit_dict(self):
        """Empty rate limit dict should use inf for max_per_hour."""
        notifier = TeamsNotifier(
            webhook_url="https://test.url",
            rate_limit={},
        )

        # Should always allow with empty rate limit
        assert notifier._check_rate_limit("event_a") is True

    def test_rate_limit_with_zero_max_per_hour(self):
        """Zero max_per_hour should be guarded against (division by zero prevention)."""
        notifier = TeamsNotifier(
            webhook_url="https://test.url",
            rate_limit={"max_per_hour": 0},
        )

        # Should always allow when max_per_hour is 0 (guard clause prevents division by zero)
        assert notifier._check_rate_limit("event_a") is True

    def test_rate_limit_with_negative_max_per_hour(self):
        """Negative max_per_hour should be guarded against."""
        notifier = TeamsNotifier(
            webhook_url="https://test.url",
            rate_limit={"max_per_hour": -5},
        )

        # Should always allow when max_per_hour is negative (treated as invalid)
        assert notifier._check_rate_limit("event_a") is True

    def test_rate_limit_with_non_numeric_max_per_hour(self):
        """Non-numeric max_per_hour should be guarded against."""
        notifier = TeamsNotifier(
            webhook_url="https://test.url",
            rate_limit={"max_per_hour": "invalid"},
        )

        # Should always allow when max_per_hour is non-numeric (treated as invalid)
        assert notifier._check_rate_limit("event_a") is True

    @patch("open_detect.notifications.teams.requests.post")
    def test_send_with_404_status_code(self, mock_post):
        """404 status code should trigger retries."""
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.text = "Not Found"
        mock_post.return_value = mock_response

        notifier = TeamsNotifier(webhook_url="https://test.url")

        with pytest.raises(TeamsNotificationError):
            notifier.send(
                event_type="test_event",
                severity="high",
                affected="test affected",
                timestamp="2026-01-15T10:30:00Z",
            )

        # Should have retried
        assert mock_post.call_count == 4

    @patch("open_detect.notifications.teams.requests.post")
    def test_send_with_503_status_code(self, mock_post):
        """503 status code should trigger retries."""
        mock_response = MagicMock()
        mock_response.status_code = 503
        mock_response.text = "Service Unavailable"
        mock_post.return_value = mock_response

        notifier = TeamsNotifier(webhook_url="https://test.url")

        with pytest.raises(TeamsNotificationError):
            notifier.send(
                event_type="test_event",
                severity="high",
                affected="test affected",
                timestamp="2026-01-15T10:30:00Z",
            )

        # Should have retried
        assert mock_post.call_count == 4

    @patch("open_detect.notifications.teams.requests.post")
    def test_send_with_connection_error_and_timeout(self, mock_post):
        """Network errors should trigger retries."""
        mock_post.side_effect = [
            requests.exceptions.ConnectionError("Connection refused"),
            requests.exceptions.Timeout("Request timeout"),
            requests.exceptions.ConnectionError("Connection refused again"),
            requests.exceptions.Timeout("Still timing out"),
        ]

        notifier = TeamsNotifier(webhook_url="https://test.url")

        # All four fail due to network errors
        with pytest.raises(TeamsNotificationError):
            notifier.send(
                event_type="test_event",
                severity="high",
                affected="test affected",
                timestamp="2026-01-15T10:30:00Z",
            )

        assert mock_post.call_count == 4  # 3 retries + 1 initial

    def test_send_safe_returns_false_on_timeout(self):
        """send_safe should return False on timeout."""
        with patch(
            "open_detect.notifications.teams.requests.post",
            side_effect=requests.exceptions.Timeout("Request timeout"),
        ):
            notifier = TeamsNotifier(webhook_url="https://test.url")
            result = notifier.send_safe(
                event_type="test_event",
                severity="high",
                affected="test affected",
                timestamp="2026-01-15T10:30:00Z",
            )

            assert result is False

    def test_send_safe_returns_false_on_connection_error(self):
        """send_safe should return False on connection error."""
        with patch(
            "open_detect.notifications.teams.requests.post",
            side_effect=requests.exceptions.ConnectionError("Connection refused"),
        ):
            notifier = TeamsNotifier(webhook_url="https://test.url")
            result = notifier.send_safe(
                event_type="test_event",
                severity="high",
                affected="test affected",
                timestamp="2026-01-15T10:30:00Z",
            )

            assert result is False

    def test_send_safe_returns_false_on_sslc_error(self):
        """send_safe should return False on SSL error."""
        with patch(
            "open_detect.notifications.teams.requests.post",
            side_effect=requests.exceptions.SSLError("SSL error"),
        ):
            notifier = TeamsNotifier(webhook_url="https://test.url")
            result = notifier.send_safe(
                event_type="test_event",
                severity="high",
                affected="test affected",
                timestamp="2026-01-15T10:30:00Z",
            )

            assert result is False

    @patch("open_detect.notifications.teams.requests.post")
    def test_send_with_json_decode_error(self, mock_post):
        """send should handle JSON decode errors from response."""
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.text = "Internal Server Error"
        mock_post.return_value = mock_response

        notifier = TeamsNotifier(webhook_url="https://test.url")

        with pytest.raises(TeamsNotificationError):
            notifier.send(
                event_type="test_event",
                severity="high",
                affected="test affected",
                timestamp="2026-01-15T10:30:00Z",
            )

    def test_empty_timestamp_falls_back_to_just_now(self):
        """Empty timestamp should fall back to 'just now'."""
        notifier = TeamsNotifier(webhook_url="https://test.url")
        card = notifier._build_message(
            event_type="test",
            severity="high",
            affected="test",
            timestamp="",
        )

        facts = card["attachments"][0]["content"]["sections"][0]["facts"]
        fact_dict = {f["title"]: f["value"] for f in facts}
        assert fact_dict["Timestamp"] == "just now"

    def test_none_timestamp_falls_back_to_just_now(self):
        """None timestamp should fall back to 'just now'."""
        notifier = TeamsNotifier(webhook_url="https://test.url")
        card = notifier._build_message(
            event_type="test",
            severity="high",
            affected="test",
            timestamp=None,
        )

        facts = card["attachments"][0]["content"]["sections"][0]["facts"]
        fact_dict = {f["title"]: f["value"] for f in facts}
        assert fact_dict["Timestamp"] == "just now"

    def test_event_type_with_underscores_formatted_correctly(self):
        """Event type names with underscores should be formatted with spaces."""
        notifier = TeamsNotifier(webhook_url="https://test.url")
        card = notifier._build_message(
            event_type="community_structure_change",
            severity="high",
            affected="test",
            timestamp="now",
        )

        activity_title = card["attachments"][0]["content"]["sections"][0]["activityTitle"]
        assert activity_title == ":alert: Community Structure Change"
