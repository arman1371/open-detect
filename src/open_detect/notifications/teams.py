"""Teams notification service for Scan Context detection events.

Sends adaptive card formatted messages to Microsoft Teams channels via webhook URLs.
Supports severity filtering, rate limiting, and error handling with retries.
"""

from __future__ import annotations

import time
from typing import Any

import requests

from open_detect.logging_utils import get_logger

logger = get_logger(__name__)

# Default severity threshold: only notify on high and critical by default
DEFAULT_SEVERITY_THRESHOLD = "medium"

# Rate limiting: max notifications per time window per event type
DEFAULT_RATE_LIMIT = {"max_per_hour": 5}

# Retry configuration
MAX_RETRIES = 3
BASE_BACKOFF_SECONDS = 1.0


class TeamsNotificationError(RuntimeError):
    """Raised when Teams notification delivery fails after retries."""


class TeamsNotifier:
    """Sends notifications to Microsoft Teams via webhook."""

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
        self.webhook_url = webhook_url
        self.severity_threshold = severity_threshold
        self.rate_limit = rate_limit or DEFAULT_RATE_LIMIT
        self._last_sent: dict[str, float] = {}  # event_type -> timestamp

    def _check_rate_limit(self, event_type: str) -> bool:
        """Check if we should respect rate limiting for this event type.

        Returns True if the notification should proceed, False if rate limited.
        """
        now = time.time()
        last_sent = self._last_sent.get(event_type, 0)
        max_per_hour = self.rate_limit.get("max_per_hour", float("inf"))

        # Guard against division by zero or invalid rate limit values
        if max_per_hour <= 0:
            max_per_hour = float("inf")

        # Calculate how long since last send in hours
        elapsed_hours = (now - last_sent) / 3600

        # Avoid division by zero when max_per_hour is effectively infinite
        min_interval_hours = 0.0 if max_per_hour == float("inf") else 1 / max_per_hour

        if elapsed_hours < min_interval_hours:
            logger.debug(
                f"Rate limiting: skipping {event_type} notification, "
                f"last sent {elapsed_hours:.2f}h ago, need at least {min_interval_hours:.2f}h"
            )
            return False

        self._last_sent[event_type] = now
        return True

    def _build_message(
        self,
        event_type: str,
        severity: str,
        affected: str,
        timestamp: str,
        description: str | None = None,
    ) -> dict[str, Any]:
        # Build the adaptive card with proper type hints
        # Keep deprecated 'title' property for backward compatibility
        # and use activityTitle in sections as recommended
        card: dict[str, Any] = {
            "type": "message",
            "attachments": [
                {
                    "contentType": "application/vnd.microsoft.card.adaptive",
                    "content": {
                        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                        "type": "AdaptiveCard",
                        "version": "1.5",
                        "title": ":alert: Scan Context Detection",  # deprecated but kept for compatibility
                        "fallbackText": f":alert: Scan Context Detection - {event_type}",
                        "themeColor": "yellow",  # placeholder, will be updated
                        "sections": [
                            {
                                "activityTitle": f":alert: Scan Context Detection - {event_type.replace('_', ' ').title()}",
                                "activitySubtitle": f"Severity: {severity.title()}",
                                "facts": [
                                    {
                                        "title": "Event Type",
                                        "value": event_type.replace("_", " ").title(),
                                    },
                                    {
                                        "title": "Severity",
                                        "value": severity.title(),
                                    },
                                    {
                                        "title": "Affected",
                                        "value": affected,
                                    },
                                    {
                                        "title": "Timestamp",
                                        "value": timestamp if timestamp else "just now",
                                    },
                                ],
                                "markdown": True,
                            }
                        ],
                    },
                }
            ],
        }

        # Map severity to Teams theme color
        color_map = {
            "low": "green",
            "medium": "yellow",
            "high": "orange",
            "critical": "red",
        }
        color = color_map.get(severity, "yellow")
        card["attachments"][0]["content"]["themeColor"] = color

        if description:
            # Add description as an additional section
            sections = card["attachments"][0]["content"]["sections"]
            sections.append(
                {
                    "activityTitle": "Description",
                    "facts": [
                        {
                            "title": "Description",
                            "value": description,
                        }
                    ],
                    "markdown": True,
                }
            )

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
            True if notification was sent successfully, False otherwise

        Raises:
            TeamsNotificationError: If all retries exhausted
        """
        # Check rate limit
        if not self._check_rate_limit(event_type):
            logger.info(f"Rate limited: skipping {event_type} notification")
            return False

        # Check severity threshold
        severity_order = {"low": 0, "medium": 1, "high": 2, "critical": 3}
        threshold_order = {"low": 0, "medium": 1, "high": 2, "critical": 3}

        # Validate severity threshold; raise error for invalid configuration
        if self.severity_threshold not in threshold_order:
            raise ValueError(
                f"Invalid severity_threshold: '{self.severity_threshold}'. "
                f"Must be one of: low, medium, high, critical"
            )
        effective_threshold = threshold_order[self.severity_threshold]

        if severity_order.get(severity, 0) < effective_threshold:
            logger.debug(
                f"Severity {severity} below threshold {self.severity_threshold}, "
                f"skipping notification"
            )
            return True  # Not an error, just suppressed

        # Build the message payload
        payload = self._build_message(event_type, severity, affected, timestamp, description)

        # Send with retries
        backoff = BASE_BACKOFF_SECONDS  # Reset backoff at start
        for attempt in range(MAX_RETRIES + 1):
            try:
                response = requests.post(
                    self.webhook_url,
                    json=payload,
                    timeout=10,
                )

                if response.status_code == 200:
                    # Update last sent timestamp to reflect actual delivery time
                    self._last_sent[event_type] = time.time()
                    logger.info(f"Teams notification sent: {event_type} ({severity})")
                    return True
                else:
                    logger.warning(
                        f"Teams webhook returned status {response.status_code}: "
                        f"{response.text[:200]}"
                    )

            except requests.RequestException as e:
                logger.warning(
                    f"Teams webhook request failed (attempt {attempt + 1}/{MAX_RETRIES + 1}): {e}"
                )

            # Exponential backoff before retry
            if attempt < MAX_RETRIES:
                backoff = BASE_BACKOFF_SECONDS * (2**attempt)
                logger.info(f"Retrying in {backoff}s...")
                time.sleep(backoff)

        # All retries exhausted
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
            logger.error(f"Teams notification failed: {e}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error sending Teams notification: {e}")
            return False
