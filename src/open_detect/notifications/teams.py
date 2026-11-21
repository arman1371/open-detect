"""Teams notification service for Scan Context detection events.

Sends adaptive card formatted messages to Microsoft Teams channels via webhook URLs.
Supports severity filtering, rate limiting, and error handling with retries.
"""

from __future__ import annotations

import time
from collections import deque
from threading import Lock
from typing import Any

import requests

from open_detect.logging_utils import get_logger

logger = get_logger(__name__)

# Default severity threshold: only notify on medium, high, and critical by default
DEFAULT_SEVERITY_THRESHOLD = "medium"

# Rate limiting: max notifications per time window per event type
DEFAULT_RATE_LIMIT = {"max_per_hour": 5}

# Retry configuration
MAX_RETRIES = 3
BASE_BACKOFF_SECONDS = 1.0

# Severity ordering - single source of truth
SEVERITY_ORDER = {"low": 0, "medium": 1, "high": 2, "critical": 3}

# Color mapping for Teams theme colors
SEVERITY_COLORS = {
    "low": "good",
    "medium": "warning",
    "high": "attention",
    "critical": "bad",
}

# Valid severity levels
VALID_SEVERITIES = set(SEVERITY_ORDER.keys())


class TeamsNotificationError(RuntimeError):
    """Raised when Teams notification delivery fails after retries."""


class SlidingWindowRateLimiter:
    """Thread-safe sliding window rate limiter for Teams notifications.

    Implements a true "N per hour" rate limit using a deque of timestamps.
    """

    def __init__(self, max_per_hour: int | float) -> None:
        """Initialize the rate limiter.

        Args:
            max_per_hour: Maximum notifications allowed per hour. If <= 0, blocks all.
        """
        if max_per_hour <= 0:
            max_per_hour = 0  # 0 means block all
        self.max_per_hour = max_per_hour
        self._timestamps: deque[float] = deque()
        self._lock = Lock()

    def check_and_consume(self, event_type: str) -> bool:
        """Check if we can send a notification and consume a slot if allowed.

        Args:
            event_type: The type of event (used for logging)

        Returns:
            True if notification should proceed, False if rate limited
        """
        # Block all if max_per_hour is 0 or negative
        if self.max_per_hour <= 0:
            logger.debug(f"Rate limited (max_per_hour <= 0): skipping {event_type} notification")
            return False

        now = time.time()
        window_start = now - 3600  # 1 hour ago

        with self._lock:
            # Remove expired timestamps
            while self._timestamps and self._timestamps[0] < window_start:
                self._timestamps.popleft()

            # Check if we're at the limit
            if len(self._timestamps) >= self.max_per_hour:
                oldest = self._timestamps[0]
                wait_seconds = (oldest + 3600) - now
                logger.debug(
                    f"Rate limited: skipping {event_type} notification, "
                    f"{len(self._timestamps)}/{self.max_per_hour} used, "
                    f"next slot in {wait_seconds:.0f}s"
                )
                return False

            # Consume slot
            self._timestamps.append(now)
            logger.debug(
                f"Rate limit check passed: {event_type} notification, "
                f"{len(self._timestamps)}/{self.max_per_hour} used this hour"
            )
            return True


class TeamsNotifier:
    """Sends notifications to Microsoft Teams via webhook.

    Uses a shared rate limiter at the class level so that multiple instances
    (e.g., created per detector call) share the same rate limit state.
    """

    # Shared rate limiter across all instances (keyed by max_per_hour)
    _rate_limiters: dict[int, SlidingWindowRateLimiter] = {}
    _rate_limiter_lock = Lock()

    def __init__(
        self,
        webhook_url: str,
        severity_threshold: str = DEFAULT_SEVERITY_THRESHOLD,
        rate_limit: dict[str, int] | None = None,
    ) -> None:
        """Initialize the Teams notifier.

        Args:
            webhook_url: Microsoft Teams webhook URL
            severity_threshold: Minimum severity to notify on (low, medium, high, critical)
            rate_limit: Rate limit configuration, e.g. {"max_per_hour": 5}
        """
        if not webhook_url.startswith("https://"):
            logger.warning(f"Webhook URL does not use HTTPS: {webhook_url}")
        self.webhook_url = webhook_url

        # Validate severity threshold
        if severity_threshold not in VALID_SEVERITIES:
            logger.warning(
                f"Invalid severity_threshold '{severity_threshold}', default to 'medium'"
            )
            severity_threshold = DEFAULT_SEVERITY_THRESHOLD
        self.severity_threshold = severity_threshold

        self.rate_limit = rate_limit or DEFAULT_RATE_LIMIT
        max_per_hour = self.rate_limit.get("max_per_hour", 5)
        if max_per_hour <= 0:
            max_per_hour = 5

        # Get or create shared rate limiter
        with self._rate_limiter_lock:
            if max_per_hour not in self._rate_limiters:
                self._rate_limiters[max_per_hour] = SlidingWindowRateLimiter(max_per_hour)
            self._rate_limiter = self._rate_limiters[max_per_hour]

    def _should_notify(self, severity: str) -> bool:
        """Check if severity meets the threshold."""
        effective_threshold = SEVERITY_ORDER[self.severity_threshold]
        return SEVERITY_ORDER.get(severity, 0) >= effective_threshold

    def _check_rate_limit(self, event_type: str) -> bool:
        """Check if we should respect rate limiting for this event type.

        Returns True if the notification should proceed, False if rate limited.
        """
        return self._rate_limiter.check_and_consume(event_type)

    def _build_adaptive_card(
        self,
        event_type: str,
        severity: str,
        affected: str,
        timestamp: str,
        description: str | None = None,
    ) -> dict[str, Any]:
        """Build a proper Adaptive Card payload for Teams.

        Adaptive Cards use a body array of elements (TextBlock, FactSet, etc.),
        not the legacy MessageCard sections format.

        Args:
            event_type: Type of detection event
            severity: Severity level (low, medium, high, critical)
            affected: Description of affected nodes/patterns
            timestamp: When the event occurred
            description: Optional additional description

        Returns:
            Adaptive card payload dictionary
        """
        color = SEVERITY_COLORS.get(severity, "warning")

        # Build the adaptive card body with proper elements
        body: list[dict[str, Any]] = [
            {
                "type": "TextBlock",
                "text": f"Scan Context Detection - {event_type.replace('_', ' ').title()}",
                "weight": "Bolder",
                "size": "Medium",
                "color": color,
            },
            {
                "type": "FactSet",
                "facts": [
                    {"title": "Event Type", "value": event_type.replace("_", " ").title()},
                    {"title": "Severity", "value": severity.title()},
                    {"title": "Affected", "value": affected},
                    {"title": "Timestamp", "value": timestamp},
                ],
            },
        ]

        if description:
            body.append(
                {
                    "type": "TextBlock",
                    "text": description,
                    "wrap": True,
                    "size": "Small",
                }
            )

        card: dict[str, Any] = {
            "type": "message",
            "attachments": [
                {
                    "contentType": "application/vnd.microsoft.card.adaptive",
                    "content": {
                        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                        "type": "AdaptiveCard",
                        "version": "1.5",
                        "fallbackText": f"Scan Context Detection - {event_type}",
                        "themeColor": color,
                        "body": body,
                    },
                }
            ],
        }

        return card

    def send(
        self,
        event_type: str,
        severity: str,
        affected: str,
        timestamp: str,
        description: str | None = None,
    ) -> bool:
        """Send a Teams notification.

        Args:
            event_type: Type of detection event
            severity: Severity level (low, medium, high, critical)
            affected: Description of affected nodes/patterns
            timestamp: When the event occurred
            description: Optional additional description

        Returns:
            True if notification was sent successfully, False if rate limited or suppressed

        Raises:
            TeamsNotificationError: If all retries exhausted
        """
        # Check severity threshold first (before rate limiting)
        if not self._should_notify(severity):
            logger.debug(
                f"Severity {severity} below threshold {self.severity_threshold}, "
                f"skipping notification"
            )
            return False  # Not an error, just suppressed - don't consume rate limit slot

        # Check rate limit
        if not self._check_rate_limit(event_type):
            return False

        # Build the message payload
        payload = self._build_adaptive_card(event_type, severity, affected, timestamp, description)

        # Send with retries - only retry on transient errors (429, 5xx, network)
        last_exception = None
        for attempt in range(MAX_RETRIES + 1):
            try:
                response = requests.post(
                    self.webhook_url,
                    json=payload,
                    timeout=10,
                )

                if response.status_code == 200:
                    logger.info(f"Teams notification sent: {event_type} ({severity})")
                    return True
                elif 400 <= response.status_code < 500:
                    # Client errors (4xx) are permanent - don't retry
                    # Exception: 429 (rate limited) should be retried
                    if response.status_code == 429:
                        logger.warning(
                            f"Teams webhook rate limited (429), "
                            f"will retry (attempt {attempt + 1}/{MAX_RETRIES + 1})"
                        )
                    else:
                        logger.error(
                            f"Teams webhook returned client error {response.status_code}: "
                            f"{response.text[:200]}"
                        )
                        raise TeamsNotificationError(
                            f"Teams webhook client error: {response.status_code}"
                        )
                else:
                    # Server errors (5xx) - retry
                    logger.warning(
                        f"Teams webhook returned server error {response.status_code}: "
                        f"{response.text[:200]}"
                    )

            except requests.RequestException as e:
                logger.warning(
                    f"Teams webhook request failed (attempt {attempt + 1}/{MAX_RETRIES + 1}): {e}"
                )
                last_exception = e

            # Exponential backoff before retry
            if attempt < MAX_RETRIES:
                backoff = BASE_BACKOFF_SECONDS * (2**attempt)
                logger.info(f"Retrying in {backoff}s...")
                time.sleep(backoff)

        # All retries exhausted
        if last_exception:
            raise TeamsNotificationError(
                f"Failed to send Teams notification after {MAX_RETRIES + 1} attempts: {last_exception}"
            ) from last_exception
        raise TeamsNotificationError(
            f"Failed to send Teams notification after {MAX_RETRIES + 1} attempts"
        )

    def send_safe(
        self,
        event_type: str,
        severity: str,
        affected: str,
        timestamp: str,
        description: str | None = None,
    ) -> bool:
        """Send a Teams notification safely, catching and logging errors.

        Args:
            event_type: Type of detection event
            severity: Severity level (low, medium, high, critical)
            affected: Description of affected nodes/patterns
            timestamp: When the event occurred
            description: Optional additional description

        Returns:
            True if notification was sent successfully, False otherwise
        """
        try:
            return self.send(event_type, severity, affected, timestamp, description)
        except TeamsNotificationError as e:
            # Log without exposing the webhook URL
            logger.error(f"Teams notification failed: {type(e).__name__}")
            return False
        except Exception as e:
            # Log without exposing the webhook URL
            logger.error(f"Unexpected error sending Teams notification: {type(e).__name__}")
            return False