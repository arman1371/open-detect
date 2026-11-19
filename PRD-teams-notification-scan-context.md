# PRD: Teams Notification Trigger for Scan Context

## 1. Summary

This PRD defines the implementation of a Teams notification trigger for the Scan Context feature in OpenDetect. When a Scan Context detection event occurs, the system will automatically post a notification to Microsoft Teams, providing real-time alerts to on-call engineers and team members about detected anomalies, pattern changes, or significant events in the knowledge graph corpus. This integration enables faster response times and better visibility into detection events without requiring constant monitoring of logs or the UI.

## 2. Contacts

| Name | Role | Comment |
|------|------|---------|
| **BackendPM** | Product Manager | Defines feature priorities and acceptance criteria |
| **BackendDev** (bd7b3e13) | Backend Engineer | Implements the Teams notification integration |
| **CodeReviewer** | Code Reviewer | Validates implementation and ensures quality |
| **DevOps Engineer** | Infrastructure | Configures deployment pipelines and environment variables |
| **Product Designer** | Designer | Defines notification message format and user experience |
| **Security Lead** | Security | Reviews webhook security and access controls |

## 3. Background

### Current State
- OpenDetect processes and analyzes large corpora of documents using knowledge graph algorithms
- Detection events are generated through various algorithms (Raha, Uni-Detect, etc.)
- Events are currently logged and visible via the UI, but there is no real-time notification mechanism
- On-call engineers must manually monitor the system for significant detection events

### Why Teams Now
- The knowledge graph has grown to 193 files with ~161,403 words and 3019 nodes
- Community structure detection and pattern changes require timely human attention
- Current monitoring relies on periodic log checks or UI polling, which introduces delay
- Microsoft Teams is the primary communication channel for the engineering team
- Real-time notifications will improve incident response times and reduce mean time to awareness

### Technical Context
- Scan Context refers to the spatial/semantic context around detected features/patterns in the knowledge graph
- The graphify system already tracks communities, nodes, and edges across the corpus
- Existing webhook infrastructure may be available for extension
- The project uses Python with FastAPI/Flask backend patterns

## 4. Objective

**Primary Goal:** Enable real-time Microsoft Teams notifications for Scan Context detection events.

**Success Metrics:**
- [ ] 100% of critical Scan Context events trigger a Teams notification within 5 seconds of detection
- [ ] 0 false positive rate for Teams webhook deliveries (or documented acceptable rate)
- [ ] On-call engineers report reduced mean time to awareness (target: >50% reduction)
- [ ] No increase in CI/CD pipeline OOM incidents (memory capped at 3g for CI)
- [ ] All existing tests continue to pass (700+ test suite)

**Business Value:**
- Faster incident response when scan context patterns change significantly
- Better visibility into knowledge graph community structure updates
- Reduced operational overhead for on-call rotation
- Improved cross-team coordination during major detection events

## 5. Market Segment(s)

### Primary Users
- **On-call Engineers:** Receive immediate alerts about significant detection events
- **Backend Team:** Stay informed about system changes and pattern detections
- **Product Team:** Understand when major corpus changes occur that may affect roadmap
- **DevOps/Infra:** Monitor system health and detection pipeline status

### Constraints
- Teams integration must respect existing authentication and authorization models
- Notifications should be rate-limited to avoid alert fatigue
- Must comply with company security policies for external webhook integrations
- Should work across all deployment environments (development, staging, production)

### Assumptions
- The engineering team uses Microsoft Teams as primary communication channel
- Webhook-based integration is the preferred approach over bot framework
- Scan Context events are already being generated and tracked in the detection pipeline

## 6. Value Proposition(s)

### Customer/User Benefits
- **Immediate Awareness:** Teams notifications provide instant visibility into detection events
- **Reduced Context Switching:** Engineers stay in their workflow (Teams) rather than switching to monitoring tools
- **Better Coverage:** Notifications reach all team members, including those not actively monitoring the UI
- **Actionable Context:** Notifications include relevant details (event type, severity, affected areas) for quick triage

### Business Benefits
- **Decreased MTTA (Mean Time To Awareness):** Faster detection of significant events
- **Improved SLA:** Better response times to critical corpus changes
- **Operational Efficiency:** Reduced manual monitoring overhead
- **Enhanced Incident Response:** Teams enables threaded discussions and rapid coordination

### Competitive Differentiation
- Many code analysis tools lack real-time notification capabilities
- Integration with existing team communication platform (vs. requiring new tools)
- Leverages existing OpenDetect detection infrastructure

## 7. Solution

### 7.1 UX/Prototypes

**Notification Message Format:**
```
:alert: *Scan Context Detection*

*Event:* <event_type>
*Severity:* <low/medium/high/critical>
*Affected:* <graph_nodes_or_patterns>
*Timestamp:* <relative_time>

<optional: brief_description_or_action_item>
```

**Example:**
```
:alert: *Scan Context Detection*

*Event:* community_structure_change
*Severity:* high
*Affected:* 45 nodes across 3 communities in uni_detect
*Timestamp:* 2 minutes ago

New community detected in corpus_stats_builder - review recommended.
```

**Teams Message Card Layout:**
- Title: "Scan Context Detection"
- Theme color: amber (for medium) or red (for critical)
- Sections: event type, severity, affected areas, timestamp, description
- Action button: "View in OpenDetect" linking to the relevant graph view

### 7.2 Key Features

1. **Event-Driven Trigger**
   - Subscribe to Scan Context detection events from the existing pipeline
   - Fire on: community structure changes, significant pattern detections, anomaly alerts
   - configurable severity levels

2. **Teams Webhook Integration**
   - Outgoing webhook to Microsoft Teams webhook URL
   - Adaptive card format for rich message formatting
   - Fallback text for clients that don't render cards

3. **Configuration Options**
   - Enable/disable per-event-type
   - Severity threshold filtering (only notify on high/critical by default)
   - Custom webhook URL per environment (dev/staging/prod)
   - Rate limiting per time window to prevent flood

4. **Error Handling**
   - Retry logic with exponential backoff for failed webhook deliveries
   - Dead letter queue for permanently failed notifications
   - Metrics tracking: delivery success/failure rates, latency
   - Fallback to logging when webhook is unavailable

5. **Security**
   - Webhook URL stored in secret management (env vars or secret service)
   - HMAC signature verification for incoming webhook requests (if applicable)
   - Rate limiting to prevent webhook abuse
   - Environment-specific configuration

### 7.3 Technology Stack

- **Language:** Python 3.11+ (consistent with codebase)
- **Framework:** FastAPI or existing Flask patterns in the codebase
- **Dependencies:** `requests` for webhook calls, existing project dependencies
- **Environment Variables:** `TEAMS_WEBHOOK_URL`, `TEAMS_NOTIFICATION_ENABLED`, `TEAMS_SEVERITY_THRESHOLD`
- **Testing:** Existing pytest suite integration

### 7.4 Assumptions (Technical)
- The detection pipeline already emits events that can be tapped into
- Existing graphify infrastructure can identify the affected communities/nodes
- Teams webhook URLs can be configured per environment
- Rate limiting can be implemented without significant performance impact

### 7.5 Open Questions & Assumptions to Validate
- [ ] What exact event types should trigger notifications? (community_change? anomaly_detection? both?)
- [ ] What severity threshold makes sense? (default: notify on high/critical only?)
- [ ] Should notifications include links back to specific graph views?
- [ ] How should rate limiting be configured? (per user? per team? per time window?)
- [ ] What happens if the webhook fails? (retry? fallback to log?)

## 8. Release

### Version & Timeline
- **Target Version:** 0.5.0 (next minor release after core stabilization)
- **Estimated Development Time:** 3-5 business days
- **Dependencies:** None (builds on existing detection pipeline)

### First Version Scope
- [x] Basic Teams webhook integration with Adaptive Cards
- [x] Configurable severity threshold
- [x] Enable/disable per event type
- [x] Rate limiting (default: max 5 notifications per hour per event type)
- [x] Error handling with retries and dead letter queue
- [ ] Multi-tenant webhook configuration (stay tuned for v0.6.0)
- [ ] Advanced formatting options (stay tuned for v0.6.0)
- [ ] Bot integration with interactive cards (stay tuned for v0.7.0)

### Future Considerations (Post-MVP)
- Interactive buttons in Teams cards (acknowledge, investigate, resolve)
- Customizable message templates per team
- Integration with other notification channels (Slack, Email, PagerDuty)
- Analytics on notification effectiveness and alert fatigue metrics
- Webhook health monitoring and automatic fallback

### Release Checklist
- [ ] Code implementation with full test coverage
- [ ] Security review of webhook integration
- [ ] Documentation updated (usage, configuration, troubleshooting)
- [ ] Integration tests with mock Teams webhook
- [ ] Performance impact assessment (memory, latency)
- [ ] Feature flag for gradual rollout
- [ ] Update graphify graph after implementation (`graphify update .`)
- [ ] CHANGELOG entry
- [ ] PR created and reviewed by CodeReviewer
- [ ] Merge to main and deployment

---
*PRD generated using the create-prd skill template. Last updated: 2026-11-19*