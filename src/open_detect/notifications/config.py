"""Configuration for Teams notification service.

Provides default configuration values and environment variable lookups
for the Teams notification integration.
"""

from __future__ import annotations

import os
from typing import Optional


def get_teams_webhook_url() -> Optional[str]:
    """Get the Teams webhook URL from environment variables.

    Returns:
        Webhook URL if set, None otherwise
    """
    return os.environ.get("TEAMS_WEBHOOK_URL")


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
    return os.environ.get("TEAMS_SEVERITY_THRESHOLD", "medium")


def get_rate_limit() -> dict:
    """Get the rate limit configuration from environment.

    Returns:
        Dictionary with rate limit settings, e.g. {"max_per_hour": 5}
    """
    val = os.environ.get("TEAMS_RATE_LIMIT_MAX_PER_HOUR")
    if val:
        return {"max_per_hour": int(val)}
    return {"max_per_hour": 5}


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