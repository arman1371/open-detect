"""Notifications package for Open Detect."""

from open_detect.notifications.teams import (
    DEFAULT_RATE_LIMIT,
    DEFAULT_SEVERITY_THRESHOLD,
    SEVERITY_COLORS,
    SEVERITY_ORDER,
    VALID_SEVERITIES,
    SlidingWindowRateLimiter,
    TeamsNotificationError,
    TeamsNotifier,
)

__all__ = [
    "SEVERITY_COLORS",
    "SEVERITY_ORDER",
    "SlidingWindowRateLimiter",
    "TeamsNotificationError",
    "TeamsNotifier",
    "DEFAULT_RATE_LIMIT",
    "DEFAULT_SEVERITY_THRESHOLD",
    "VALID_SEVERITIES",
]
