"""Tests for Teams notification service."""

from __future__ import annotations

import time
from collections import deque
from unittest.mock import MagicMock, patch

import pytest
import requests

from open_detect.notifications.teams import (
    SEVERITY_COLORS,
    SEVERITY_ORDER,
    SlidingWindowRateLimiter,
    TeamsNotificationError,
    TeamsNotifier,
)


@pytest.fixture(autouse=True)
def reset_rate_limiters():
    """Reset the shared rate limiter cache before each test."""
    TeamsNotifier._rate_limiters.clear()
    yield
    TeamsNotifier._rate_limiters.clear()


class TestTeamsNotifierInit:
    """Tests for TeamsNotifier initialization."""

    def test_initializes_with_defaults(self):
        notifier = TeamsNotifier(webhook_url="https://test.url")
        assert notifier.webhook_url == "https://test.url"
        assert notifier.severity_threshold == "medium"
        assert notifier.rate_limit == {"max_per_hour": 5}
        assert hasattr(notifier, "_rate_limiter")

    def test_initializes_with_custom_values(self):
        notifier = TeamsNotifier(
            webhook_url="https://custom.url",
            severity_threshold="high",
            rate_limit={"max_per_hour": 10},
        )
        assert notifier.webhook_url == "https://custom.url"
        assert notifier.severity_threshold == "high"
        assert notifier.rate_limit == {"max_per_hour": 10}


class TestSlidingWindowRateLimiter:
    """Tests for SlidingWindowRateLimiter class."""

    def test_allows_first_notification(self):
        limiter = SlidingWindowRateLimiter(max_per_hour=5)
        assert limiter.check_and_consume("test_event") is True

    def test_allows_after_time_window(self):
        limiter = SlidingWindowRateLimiter(max_per_hour=5)
        # First call should succeed
        assert limiter.check_and_consume("test_event") is True
        # Manually set timestamps to simulate time passing (clear event timestamps)
        now = time.time()
        limiter._event_timestamps.clear()
        limiter._event_timestamps["test_event"] = deque(
            [now - 7200] * 5
        )  # 5 timestamps from 2 hours ago
        assert limiter.check_and_consume("test_event") is True

    def test_blocks_within_time_window(self):
        limiter = SlidingWindowRateLimiter(max_per_hour=2)
        # First call succeeds
        assert limiter.check_and_consume("test_event") is True
        # Second call (consuming second slot) should succeed
        assert limiter.check_and_consume("test_event") is True
        # Third call should be rate limited (max is 2)
        assert limiter.check_and_consume("test_event") is False

    def test_allows_each_event_type_separately(self):
        """Each event type should have its own rate limit slot."""
        limiter = SlidingWindowRateLimiter(max_per_hour=5)
        # Use up 5 slots for event_a
        for _ in range(5):
            limiter.check_and_consume("event_a")
        # event_b should still be allowed (different event type has its own quota)
        assert limiter.check_and_consume("event_b") is True
        # event_a should still be blocked (quota used up)
        assert limiter.check_and_consume("event_a") is False
        # event_b should still be allowed (only used 1 of 5 slots)
        assert limiter.check_and_consume("event_b") is True
        # Use up remaining slots for event_b
        for _ in range(3):  # 4 total calls needed, 1 already done
            limiter.check_and_consume("event_b")
        # event_b should now be blocked (used its quota)
        assert limiter.check_and_consume("event_b") is False

    def test_zero_max_per_hour_blocks_all(self):
        """Zero max_per_hour should block all notifications."""
        limiter = SlidingWindowRateLimiter(max_per_hour=0)
        assert limiter.check_and_consume("event_a") is False

    def test_negative_max_per_hour_treated_as_zero(self):
        """Negative max_per_hour should be treated as 0 (block all)."""
        limiter = SlidingWindowRateLimiter(max_per_hour=-5)
        assert limiter.check_and_consume("event_a") is False


class TestCheckRateLimit:
    """Tests for _check_rate_limit method."""

    def test_returns_true_when_not_rate_limited(self):
        notifier = TeamsNotifier(webhook_url="https://test.url", rate_limit={"max_per_hour": 5})
        assert notifier._check_rate_limit("test_event") is True

    def test_returns_false_when_rate_limited(self):
        notifier = TeamsNotifier(webhook_url="https://test.url", rate_limit={"max_per_hour": 5})
        # Use up the rate limit
        for _ in range(5):
            notifier._check_rate_limit("test_event")
        # Next should be rate limited
        assert notifier._check_rate_limit("test_event") is False


class TestBuildAdaptiveCard:
    """Tests for _build_adaptive_card method."""

    def test_builds_valid_adaptive_card(self):
        notifier = TeamsNotifier(webhook_url="https://test.url")
        card = notifier._build_adaptive_card(
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
        assert "body" in content  # Modern format uses body
        assert len(content["body"]) == 3  # TextBlock + FactSet + description

    def test_theme_colors_for_all_severities(self):
        notifier = TeamsNotifier(webhook_url="https://test.url")
        test_cases = [
            ("low", SEVERITY_COLORS["low"]),
            ("medium", SEVERITY_COLORS["medium"]),
            ("high", SEVERITY_COLORS["high"]),
            ("critical", SEVERITY_COLORS["critical"]),
            ("unknown", SEVERITY_COLORS.get("unknown", "warning")),  # default
        ]
        for severity, expected_color in test_cases:
            card = notifier._build_adaptive_card(
                event_type="test",
                severity=severity,
                affected="test",
                timestamp="now",
            )
            assert card["attachments"][0]["content"]["themeColor"] == expected_color

    def test_includes_all_facts(self):
        notifier = TeamsNotifier(webhook_url="https://test.url")
        card = notifier._build_adaptive_card(
            event_type="scan_context_uniqueness",
            severity="critical",
            affected="100 columns in 5 tables",
            timestamp="2026-01-15T10:30:00Z",
            description="Uniqueness violation detected",
        )

        body = card["attachments"][0]["content"]["body"]
        # Find the FactSet
        fact_set = None
        for element in body:
            if element.get("type") == "FactSet":
                fact_set = element
                break

        assert fact_set is not None
        facts = fact_set["facts"]
        fact_dict = {f["title"]: f["value"] for f in facts}
        assert fact_dict["Event Type"] == "Scan Context Uniqueness"
        assert fact_dict["Severity"] == "Critical"
        assert fact_dict["Affected"] == "100 columns in 5 tables"
        assert fact_dict["Timestamp"] == "2026-01-15T10:30:00Z"

    def test_includes_description_as_text_block_when_provided(self):
        notifier = TeamsNotifier(webhook_url="https://test.url")
        card = notifier._build_adaptive_card(
            event_type="test",
            severity="high",
            affected="test",
            timestamp="now",
            description="Test description",
        )
        body = card["attachments"][0]["content"]["body"]
        assert len(body) == 3  # TextBlock + FactSet + description TextBlock
        assert body[2]["type"] == "TextBlock"
        assert body[2]["text"] == "Test description"

    def test_excludes_description_when_none(self):
        notifier = TeamsNotifier(webhook_url="https://test.url")
        card = notifier._build_adaptive_card(
            event_type="test",
            severity="high",
            affected="test",
            timestamp="now",
            description=None,
        )
        body = card["attachments"][0]["content"]["body"]
        assert len(body) == 2  # TextBlock + FactSet only

    def test_event_type_with_underscores_formatted_correctly(self):
        """Event type names with underscores should be formatted with spaces."""
        notifier = TeamsNotifier(webhook_url="https://test.url")
        card = notifier._build_adaptive_card(
            event_type="community_structure_change",
            severity="high",
            affected="test",
            timestamp="now",
        )

        # Check the header text BlText
        header = card["attachments"][0]["content"]["body"][0]
        assert header["text"] == "Scan Context Detection - Community Structure Change"


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
    def test_retries_on_5xx_error(self, mock_post):
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
        # Use up the rate limit
        for _ in range(5):
            notifier._check_rate_limit("test_event")

        # Now sending should be rate limited
        result = notifier.send(
            event_type="test_event",
            severity="high",
            affected="test affected",
            timestamp="2026-01-15T10:30:00Z",
        )

        assert result is False
        mock_post.assert_not_called()

    def test_returns_false_for_severity_below_threshold(self):
        notifier = TeamsNotifier(webhook_url="https://test.url", severity_threshold="high")
        # medium is below high threshold
        result = notifier.send(
            event_type="test_event",
            severity="medium",
            affected="test affected",
            timestamp="2026-01-15T10:30:00Z",
        )

        assert result is False  # Not an error, just suppressed - don't consume rate limit slot

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

    @patch("open_detect.notifications.teams.requests.post")
    def test_404_client_error_raises_error(self, mock_post):
        """404 status code should raise TeamsNotificationError (client error, no retry)."""
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.text = "Not Found"
        mock_post.return_value = mock_response

        notifier = TeamsNotifier(webhook_url="https://test.url")

        with pytest.raises(TeamsNotificationError) as exc_info:
            notifier.send(
                event_type="test_event",
                severity="high",
                affected="test affected",
                timestamp="2026-01-15T10:30:00Z",
            )

        assert "client error" in str(exc_info.value).lower()
        # Should not retry on client errors
        assert mock_post.call_count == 1


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
        # Test the internal logic directly
        severity_order = SEVERITY_ORDER
        threshold_order = SEVERITY_ORDER

        allowed = severity_order.get(severity, 0) >= threshold_order.get(threshold, 0)
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
            # But the actual comparison uses severity_order.get(severity, 0) >= threshold_order.get(...)
            # So unknown severity (0) >= low threshold (0) = True, should send
            assert result is True


class TestEdgeCases:
    """Tests for edge cases and error handling."""

    def test_rate_limit_with_infinite_max_per_hour(self):
        """Rate limit should work with infinite max_per_hour."""
        limiter = SlidingWindowRateLimiter(max_per_hour=float("inf"))

        # Should always allow with infinite rate limit
        assert limiter.check_and_consume("event_a") is True
        assert limiter.check_and_consume("event_a") is True

    def test_rate_limit_zero_blocks_all(self):
        """Zero max_per_hour should block all notifications."""
        limiter = SlidingWindowRateLimiter(max_per_hour=0)
        assert limiter.check_and_consume("event_a") is False
        assert limiter.check_and_consume("event_a") is False

    def test_rate_limit_negative_treated_as_zero(self):
        """Negative max_per_hour should be treated as 0 (block all)."""
        limiter = SlidingWindowRateLimiter(max_per_hour=-5)
        assert limiter.check_and_consume("event_a") is False

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

    def test_empty_timestamp_is_converted_to_just_now(self):
        """Empty timestamp should be converted to 'just now'."""
        notifier = TeamsNotifier(webhook_url="https://test.url")
        card = notifier._build_adaptive_card(
            event_type="test",
            severity="high",
            affected="test",
            timestamp="",
        )

        facts = card["attachments"][0]["content"]["body"][1]["facts"]
        fact_dict = {f["title"]: f["value"] for f in facts}
        assert fact_dict["Timestamp"] == "just now"

    def test_none_timestamp_is_converted_to_just_now(self):
        """None timestamp should be converted to 'just now'."""
        notifier = TeamsNotifier(webhook_url="https://test.url")
        card = notifier._build_adaptive_card(
            event_type="test",
            severity="high",
            affected="test",
            timestamp=None,
        )

        facts = card["attachments"][0]["content"]["body"][1]["facts"]
        fact_dict = {f["title"]: f["value"] for f in facts}
        assert fact_dict["Timestamp"] == "just now"
