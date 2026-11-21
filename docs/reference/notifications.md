# Teams Notifications

Uni-Detect can send detection event notifications to Microsoft Teams via webhook.

## Configuration

Enable and configure Teams notifications using environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `TEAMS_WEBHOOK_URL` | Microsoft Teams incoming webhook URL | Required for notifications |
| `TEAMS_NOTIFICATION_ENABLED` | Enable/disable notifications (`true`, `1`, `yes`, `on`) | `false` |
| `TEAMS_SEVERITY_THRESHOLD` | Minimum severity to notify (`low`, `medium`, `high`, `critical`) | `medium` |
| `TEAMS_RATE_LIMIT_MAX_PER_HOUR` | Maximum notifications per hour | `5` |

## Severity Levels

Notifications can be filtered by severity:

- **low**: Informational events
- **medium**: Standard detection events (default threshold)
- **high**: Important anomalies requiring attention
- **critical**: Critical issues requiring immediate action

Only events at or above the configured threshold will be sent.

## Rate Limiting

Notifications are rate-limited to prevent spam:
- Default: 5 notifications per hour
- Uses a sliding window algorithm for smooth limiting
- Rate limit is shared across all detectors and detection runs

## Adaptive Card Format

Notifications use Microsoft Teams Adaptive Cards with:
- Event type and severity
- Affected tables/columns summary
- Timestamp (UTC)
- Optional custom description
- Color-coded by severity (green/warning/attention/bad)

## Usage

```python
from open_detect import UniDetectConfig, UnityCatalogLocation
from open_detect.algorithms.uni_detect.pipeline import UniDetect

config = UniDetectConfig(location=UnityCatalogLocation("main", "data_quality"))
ud = UniDetect(config)

# Run detection with notification parameters
detections = ud.detect(
    table_names=["main.sales.orders"],
    severity="high",
    description="Daily data quality scan",
)
```

## Error Handling

Notifications are best-effort side effects:
- Network failures, webhook errors, or misconfiguration will **never** break the detection run
- Errors are logged but don't raise exceptions
- Failed deliveries are retried with exponential backoff (up to 3 retries)
- Permanent errors (4xx except 429) are not retried

## Security

- Webhook URLs must use HTTPS
- Webhook URLs are never logged (only error types are logged)
- Invalid rate limit values fall back to defaults with warnings