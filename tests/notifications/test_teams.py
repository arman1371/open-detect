"""Tests for Teams notifier."""

from __future__ import annotations

import time
from unittest.mock import MagicMock, patch

import pytest
import requests

from open_detect.notifications.teams import (
    DEFAULT_RATE_LIMIT,
    DEFAULT_SEVERITY_THRESHOLD,
    MAX_RETRIES,
    SEVERITY_ORDER,
    SlidingWindowRateLimiter,
    TeamsNotificationError,
    TeamsNotifier,
)


@pytest.fixture(autouse=True)
def reset_rate_limiters():
    """Reset shared rate limiters between tests to ensure isolation."""
    # Clear the class-level shared rate limiters
    TeamsNotifier._rate_limiters.clear()
    yield
    TeamsNotifier._rate_limiters.clear()


class TestSlidingWindowRateLimiter:
    """Tests for SlidingWindowRateLimiter."""

    def test_allows_within_limit(self):
        """Should allow notifications within the limit."""
        limiter = SlidingWindowRateLimiter(max_per_hour=5)
        for _ in range(5):
            assert limiter.check_and_consume("test_event") is True

    def test_blocks_at_limit(self):
        """Should block when at the limit."""
        limiter = SlidingWindowRateLimiter(max_per_hour=2)
        assert limiter.check_and_consume("test_event") is True
        assert limiter.check_and_consume("test_event") is True
        assert limiter.check_and_consume("test_event") is False

    def test_allows_after_window_expires(self):
        """Should allow after timestamps expire."""
        limiter = SlidingWindowRateLimiter(max_per_hour=2)
        # Manually add old timestamps
        limiter._timestamps.append(time.time() - 7200)  # 2 hours ago
        assert limiter.check_and_consume("test_event") is True
        assert limiter.check_and_consume("test_event") is True

    def test_infinite_limit_allows_all(self):
        """Infinite limit should allow all."""
        limiter = SlidingWindowRateLimiter(max_per_hour=float("inf"))
        for _ in range(100):
            assert limiter.check_and_consume("test_event") is True

    def test_zero_limit_blocks_all(self):
        """Zero limit should block all."""
        limiter = SlidingWindowRateLimiter(max_per_hour=0)
        assert limiter.check_and_consume("test_event") is False

    def test_negative_limit_blocks_all(self):
        """Negative limit should block all."""
        limiter = SlidingWindowRateLimiter(max_per_hour=-1)
        assert limiter.check_and_consume("test_event") is False


class TestTeamsNotifierInit:
    """Tests for TeamsNotifier.__init__."""

    def test_valid_severity_threshold(self):
        """Should accept valid severity thresholds."""
        for threshold in SEVERITY_ORDER:
            notifier = TeamsNotifier(
                webhook_url="https://webhook.url",
                severity_threshold=threshold,
            )
            assert notifier.severity_threshold == threshold

    def test_invalid_severity_threshold_defaults(self, caplog):
        """Invalid severity threshold should default to medium with warning."""
        notifier = TeamsNotifier(
            webhook_url="https://webhook.url",
            severity_threshold="invalid",
        )
        assert notifier.severity_threshold == DEFAULT_SEVERITY_THRESHOLD
        assert "Invalid severity_threshold" in caplog.text

    def test_warns_on_non_https_url(self, caplog):
        """Should warn on non-HTTPS webhook URL."""
        TeamsNotifier(webhook_url="http://insecure.url")
        assert "does not use HTTPS" in caplog.text

    def test_rate_limit_uses_default_when_none(self):
        """Should use default rate limit when None provided."""
        notifier = TeamsNotifier(webhook_url="https://webhook.url")
        assert notifier.rate_limit == DEFAULT_RATE_LIMIT

    def test_shared_rate_limiter_across_instances(self):
        """Multiple notifiers with same max_per_hour should share rate limiter."""
        notifier1 = TeamsNotifier(
            webhook_url="https://webhook1.url",
            rate_limit={"max_per_hour": 5},
        )
        notifier2 = TeamsNotifier(
            webhook_url="https://webhook2.url",
            rate_limit={"max_per_hour": 5},
        )
        assert notifier1._rate_limiter is notifier2._rate_limiter

    def test_different_rate_limits_get_different_limiters(self):
        """Different max_per_hour should get different limiters."""
        notifier1 = TeamsNotifier(
            webhook_url="https://webhook1.url",
            rate_limit={"max_per_hour": 5},
        )
        notifier2 = TeamsNotifier(
            webhook_url="https://webhook2.url",
            rate_limit={"max_per_hour": 10},
        )
        assert notifier1._rate_limiter is not notifier2._rate_limiter


class TestTeamsNotifierShouldNotify:
    """Tests for severity threshold checking."""

    def test_allows_at_threshold(self):
        """Should allow severity at threshold."""
        notifier = TeamsNotifier(
            webhook_url="https://webhook.url",
            severity_threshold="medium",
        )
        assert notifier._should_notify("medium") is True
        assert notifier._should_notify("high") is True
        assert notifier._should_notify("critical") is True

    def test_blocks_below_threshold(self):
        """Should block severity below threshold."""
        notifier = TeamsNotifier(
            webhook_url="https://webhook.url",
            severity_threshold="high",
        )
        assert notifier._should_notify("low") is False
        assert notifier._should_notify("medium") is False
        assert notifier._should_notify("high") is True
        assert notifier._should_notify("critical") is True

    def test_unknown_severity_treated_as_low(self):
        """Unknown severity should be treated as low (0)."""
        notifier = TeamsNotifier(
            webhook_url="https://webhook.url",
            severity_threshold="medium",
        )
        assert notifier._should_notify("unknown") is False


class TestTeamsNotifierBuildAdaptiveCard:
    """Tests for _build_adaptive_card method."""

    def test_card_has_correct_structure(self):
        """Adaptive card should have correct structure."""
        notifier = TeamsNotifier(webhook_url="https://webhook.url")
        card = notifier._build_adaptive_card(
            event_type="test_event",
            severity="high",
            affected="Test affected",
            timestamp="2024-01-01T12:00:00Z",
        )

        assert card["type"] == "message"
        assert "attachments" in card
        assert len(card["attachments"]) == 1
        attachment = card["attachments"][0]
        assert attachment["contentType"] == "application/vnd.microsoft.card.adaptive"
        content = attachment["content"]
        assert content["type"] == "AdaptiveCard"
        assert content["version"] == "1.5"
        assert "$schema" in content
        assert "body" in content
        assert isinstance(content["body"], list)

    def test_card_body_has_textblock_and_factset(self):
        """Card body should have TextBlock and FactSet elements."""
        notifier = TeamsNotifier(webhook_url="https://webhook.url")
        card = notifier._build_adaptive_card(
            event_type="test_event",
            severity="high",
            affected="Test affected",
            timestamp="2024-01-01T12:00:00Z",
        )

        body = card["attachments"][0]["content"]["body"]
        # First element should be TextBlock
        assert body[0]["type"] == "TextBlock"
        assert "Test Event" in body[0]["text"]
        # Second element should be FactSet
        assert body[1]["type"] == "FactSet"
        facts = body[1]["facts"]
        assert len(facts) == 4
        fact_titles = [f["title"] for f in facts]
        assert "Event Type" in fact_titles
        assert "Severity" in fact_titles
        assert "Affected" in fact_titles
        assert "Timestamp" in fact_titles

    def test_card_includes_description_when_provided(self):
        """Card should include description TextBlock when provided."""
        notifier = TeamsNotifier(webhook_url="https://webhook.url")
        card = notifier._build_adaptive_card(
            event_type="test_event",
            severity="high",
            affected="Test affected",
            timestamp="2024-01-01T12:00:00Z",
            description="Custom description",
        )

        body = card["attachments"][0]["content"]["body"]
        # Should have 3 elements: TextBlock, FactSet, TextBlock (description)
        assert len(body) == 3
        assert body[2]["type"] == "TextBlock"
        assert body[2]["text"] == "Custom description"
        assert body[2]["wrap"] is True

    def test_card_excludes_description_when_none(self):
        """Card should not include description when None."""
        notifier = TeamsNotifier(webhook_url="https://webhook.url")
        card = notifier._build_adaptive_card(
            event_type="test_event",
            severity="high",
            affected="Test affected",
            timestamp="2024-01-01T12:00:00Z",
            description=None,
        )

        body = card["attachments"][0]["content"]["body"]
        assert len(body) == 2  # TextBlock + FactSet only

    def test_card_color_maps_to_severity(self):
        """Card theme color should map to severity."""
        notifier = TeamsNotifier(webhook_url="https://webhook.url")
        for severity, expected_color in [
            ("low", "good"),
            ("medium", "warning"),
            ("high", "attention"),
            ("critical", "bad"),
        ]:
            card = notifier._build_adaptive_card(
                event_type="test_event",
                severity=severity,
                affected="Test affected",
                timestamp="2024-01-01T12:00:00Z",
            )
            assert card["attachments"][0]["content"]["themeColor"] == expected_color


class TestTeamsNotifierSend:
    """Tests for send method."""

    @patch("open_detect.notifications.teams.requests.post")
    def test_sends_successfully(self, mock_post):
        """Should send successfully on 200 response."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        notifier = TeamsNotifier(webhook_url="https://webhook.url")
        result = notifier.send(
            event_type="test_event",
            severity="high",
            affected="Test affected",
            timestamp="2024-01-01T12:00:00Z",
        )

        assert result is True
        mock_post.assert_called_once()

    @patch("open_detect.notifications.teams.requests.post")
    def test_blocks_on_severity_below_threshold(self, mock_post):
        """Should not send when severity below threshold."""
        notifier = TeamsNotifier(
            webhook_url="https://webhook.url",
            severity_threshold="high",
        )
        result = notifier.send(
            event_type="test_event",
            severity="medium",
            affected="Test affected",
            timestamp="2024-01-01T12:00:00Z",
        )

        assert result is False  # Suppressed, not an error
        mock_post.assert_not_called()

    @patch("open_detect.notifications.teams.requests.post")
    def test_blocks_on_rate_limit(self, mock_post):
        """Should not send when rate limited."""
        notifier = TeamsNotifier(
            webhook_url="https://webhook.url",
            rate_limit={"max_per_hour": 1},
        )
        # First send succeeds
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        result1 = notifier.send(
            event_type="test_event",
            severity="high",
            affected="Test affected",
            timestamp="2024-01-01T12:00:00Z",
        )
        assert result1 is True

        # Second send should be rate limited
        result2 = notifier.send(
            event_type="test_event",
            severity="high",
            affected="Test affected",
            timestamp="2024-01-01T12:00:00Z",
        )
        assert result2 is False
        assert mock_post.call_count == 1  # Only called once

    @patch("open_detect.notifications.teams.requests.post")
    def test_retries_on_429(self, mock_post):
        """Should retry on 429 (rate limited) response."""
        mock_response_429 = MagicMock()
        mock_response_429.status_code = 429
        mock_response_200 = MagicMock()
        mock_response_200.status_code = 200
        mock_post.side_effect = [mock_response_429, mock_response_200]

        notifier = TeamsNotifier(webhook_url="https://webhook.url")
        with patch("open_detect.notifications.teams.time.sleep"):
            result = notifier.send(
                event_type="test_event",
                severity="high",
                affected="Test affected",
                timestamp="2024-01-01T12:00:00Z",
            )

        assert result is True
        assert mock_post.call_count == 2

    @patch("open_detect.notifications.teams.requests.post")
    def test_does_not_retry_on_400(self, mock_post):
        """Should not retry on 400 (client error)."""
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad request"
        mock_post.return_value = mock_response

        notifier = TeamsNotifier(webhook_url="https://webhook.url")
        with pytest.raises(TeamsNotificationError, match="client error"):
            notifier.send(
                event_type="test_event",
                severity="high",
                affected="Test affected",
                timestamp="2024-01-01T12:00:00Z",
            )

        assert mock_post.call_count == 1  # No retries

    @patch("open_detect.notifications.teams.requests.post")
    def test_does_not_retry_on_404(self, mock_post):
        """Should not retry on 404 (not found)."""
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.text = "Not found"
        mock_post.return_value = mock_response

        notifier = TeamsNotifier(webhook_url="https://webhook.url")
        with pytest.raises(TeamsNotificationError, match="client error"):
            notifier.send(
                event_type="test_event",
                severity="high",
                affected="Test affected",
                timestamp="2024-01-01T12:00:00Z",
            )

        assert mock_post.call_count == 1

    @patch("open_detect.notifications.teams.requests.post")
    def test_retries_on_500(self, mock_post):
        """Should retry on 500 (server error)."""
        mock_response_500 = MagicMock()
        mock_response_500.status_code = 500
        mock_response_200 = MagicMock()
        mock_response_200.status_code = 200
        mock_post.side_effect = [mock_response_500, mock_response_200]

        notifier = TeamsNotifier(webhook_url="https://webhook.url")
        with patch("open_detect.notifications.teams.time.sleep"):
            result = notifier.send(
                event_type="test_event",
                severity="high",
                affected="Test affected",
                timestamp="2024-01-01T12:00:00Z",
            )

        assert result is True
        assert mock_post.call_count == 2

    @patch("open_detect.notifications.teams.requests.post")
    def test_retries_on_network_error(self, mock_post):
        """Should retry on network errors."""
        mock_post.side_effect = [
            requests.ConnectionError("Network error"),
            MagicMock(status_code=200),
        ]

        notifier = TeamsNotifier(webhook_url="https://webhook.url")
        with patch("open_detect.notifications.teams.time.sleep"):
            result = notifier.send(
                event_type="test_event",
                severity="high",
                affected="Test affected",
                timestamp="2024-01-01T12:00:00Z",
            )

        assert result is True
        assert mock_post.call_count == 2

    @patch("open_detect.notifications.teams.requests.post")
    def test_exhausts_retries_then_raises(self, mock_post):
        """Should raise TeamsNotificationError after exhausting retries."""
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_post.return_value = mock_response

        notifier = TeamsNotifier(webhook_url="https://webhook.url")
        with (
            patch("open_detect.notifications.teams.time.sleep"),
            pytest.raises(TeamsNotificationError, match="after 4 attempts"),
        ):
            notifier.send(
                event_type="test_event",
                severity="high",
                affected="Test affected",
                timestamp="2024-01-01T12:00:00Z",
            )

        assert mock_post.call_count == MAX_RETRIES + 1  # Initial + retries


class TestTeamsNotifierSendSafe:
    """Tests for send_safe method."""

    def test_returns_true_on_success(self):
        """Should return True on successful send."""
        notifier = TeamsNotifier(webhook_url="https://webhook.url")
        with patch.object(notifier, "send", return_value=True):
            result = notifier.send_safe(
                event_type="test_event",
                severity="high",
                affected="Test affected",
                timestamp="2024-01-01T12:00:00Z",
            )
            assert result is True

    def test_returns_false_on_teams_notification_error(self, caplog):
        """Should return False and log error on TeamsNotificationError."""
        notifier = TeamsNotifier(webhook_url="https://webhook.url")
        with patch.object(notifier, "send", side_effect=TeamsNotificationError("Failed")):
            result = notifier.send_safe(
                event_type="test_event",
                severity="high",
                affected="Test affected",
                timestamp="2024-01-01T12:00:00Z",
            )
            assert result is False
            assert "Teams notification failed" in caplog.text
            assert "TeamsNotificationError" in caplog.text

    def test_returns_false_on_unexpected_error(self, caplog):
        """Should return False and log error on unexpected exception."""
        notifier = TeamsNotifier(webhook_url="https://webhook.url")
        with patch.object(notifier, "send", side_effect=ValueError("Unexpected")):
            result = notifier.send_safe(
                event_type="test_event",
                severity="high",
                affected="Test affected",
                timestamp="2024-01-01T12:00:00Z",
            )
            assert result is False
            assert "Unexpected error sending Teams notification" in caplog.text
            assert "ValueError" in caplog.text

    def test_does_not_log_webhook_url(self, caplog):
        """Should not log the webhook URL in error messages."""
        notifier = TeamsNotifier(webhook_url="https://secret.webhook.url/token")
        with patch.object(notifier, "send", side_effect=TeamsNotificationError("Failed")):
            notifier.send_safe(
                event_type="test_event",
                severity="high",
                affected="Test affected",
                timestamp="2024-01-01T12:00:00Z",
            )
            assert "secret.webhook.url" not in caplog.text
            assert "token" not in caplog.text


class TestTeamsNotifierEdgeCases:
    """Edge case tests."""

    def test_severity_threshold_validation_in_send(self, caplog):
        """Invalid severity_threshold from config should be handled in send."""
        notifier = TeamsNotifier(
            webhook_url="https://webhook.url",
            severity_threshold="invalid",
        )
        # The threshold gets corrected in __init__, but test the send path
        with patch("open_detect.notifications.teams.requests.post") as mock_post:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_post.return_value = mock_response

            result = notifier.send(
                event_type="test_event",
                severity="high",
                affected="Test affected",
                timestamp="2024-01-01T12:00:00Z",
            )
            assert result is True
            # Should have defaulted to medium
            assert notifier.severity_threshold == DEFAULT_SEVERITY_THRESHOLD

    def test_shared_rate_limiter_across_different_webhooks(self):
        """Rate limiter should be shared across different webhook URLs with same limit."""
        notifier1 = TeamsNotifier(
            webhook_url="https://webhook1.url",
            rate_limit={"max_per_hour": 2},
        )
        notifier2 = TeamsNotifier(
            webhook_url="https://webhook2.url",
            rate_limit={"max_per_hour": 2},
        )

        with patch("open_detect.notifications.teams.requests.post") as mock_post:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_post.return_value = mock_response

            # First notifier sends 2 (at limit)
            notifier1.send("event", "high", "affected", "timestamp")
            notifier1.send("event", "high", "affected", "timestamp")

            # Second notifier should be rate limited
            result = notifier2.send("event", "high", "affected", "timestamp")
            assert result is False
