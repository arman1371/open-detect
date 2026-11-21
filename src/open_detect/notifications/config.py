"""Configuration for Teams notification service.

Provides default configuration values and environment variable lookups
for the Teams notification integration.
"""

from __future__ import annotations

import os

from open_detect.logging_utils import get_logger

logger = get_logger(__name__)

# Valid severity levels
VALID_SEVERITIES = {"low", "medium", "high", "critical"}

# Default values
DEFAULT_SEVERITY_THRESHOLD = "medium"
DEFAULT_RATE_LIMIT = {"max_per_hour": 5}


def get_teams_webhook_url() -> str | None:
    """Get the Teams webhook URL from environment variables.

    Returns:
        Webhook URL if set, None otherwise
    """
    url = os.environ.get("TEAMS_WEBHOOK_URL")
    if url and not url.startswith("https://"):
        logger.warning(
            f"TEAMS_WEBHOOK_URL does not start with https://, this may be insecure: {url}"
        )
    return url


def get_teams_enabled() -> bool:
    """Check if Teams notifications are enabled.

    Returns:
        True if TEAMS_NOTIFICATION_ENABLED is set to a truthy value
    """
    val = os.environ.get("TEAMS_NOTIFICATION_ENABLED", "").lower()
    return val in ("true", "1", "yes", "on")


def get_severity_threshold() -> str:
    """Get the severity threshold for notifications.

    Returns:
        One of: low, medium, high, critical
    """
    val = os.environ.get("TEAMS_SEVERITY_THRESHOLD", DEFAULT_SEVERITY_THRESHOLD).lower()
    if val not in VALID_SEVERITIES:
        logger.warning(
            f"Invalid TEAMS_SEVERITY_THRESHOLD '{val}', "
            f"valid values: {sorted(VALID_SEVERITIES)}, "
            f"defaulting to '{DEFAULT_SEVERITY_THRESHOLD}'"
        )
        return DEFAULT_SEVERITY_THRESHOLD
    return val


def get_rate_limit() -> dict:
    """Get the rate limit configuration from environment.

    Returns:
        Dictionary with rate limit settings, e.g. {"max_per_hour": 5}
    """
    val = os.environ.get("TEAMS_RATE_LIMIT_MAX_PER_HOUR")
    if val:
        try:
            max_per_hour = int(val)
            if max_per_hour <= 0:
                logger.warning(
                    f"TEAMS_RATE_LIMIT_MAX_PER_HOUR must be positive, got {max_per_hour}, "
                    f"defaulting to {DEFAULT_RATE_LIMIT['max_per_hour']}"
                )
                return DEFAULT_RATE_LIMIT.copy()
            return {"max_per_hour": max_per_hour}
        except ValueError:
            logger.warning(
                f"Invalid TEAMS_RATE_LIMIT_MAX_PER_HOUR '{val}', must be integer, "
                f"defaulting to {DEFAULT_RATE_LIMIT['max_per_hour']}"
            )
            return DEFAULT_RATE_LIMIT.copy()
    return DEFAULT_RATE_LIMIT.copy()


def get_notification_config() -> dict:
    """Get the complete notification configuration.

    Returns:
        Dictionary with all configuration values
    """
    return {
        "webhook_url": get_teams_webhook_url(),
        "enabled": get_teams_enabled(),
        "severity_threshold": get_severity_threshold(),
        "rate_limit": get_rate_limit(),
    }