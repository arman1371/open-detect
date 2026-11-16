# PRD: User Feedback Tooltips

## 1. Summary
This document specifies the design and implementation of User Feedback Tooltips — contextual, interactive tooltips that appear when users hover over or interact with error detection results, validation scores, and pattern matches in the OpenDetect platform. These tooltips provide human-readable explanations of why a cell was flagged, what pattern was expected, and actionable guidance for fixing data quality issues.

## 2. Contacts

| Name | Role | Comment |
|------|------|---------|
| BackendPM | Product Manager | Owns the feature roadmap and prioritization |
| BackendDev | Backend Engineer | Implements API endpoints and tooltip data models |
| FrontendDev | Frontend Engineer | Builds tooltip UI components and interactions |
| CTO | Technical Lead | Reviews architecture and performance implications |
| UX Designer | Designer | Defines tooltip visual design and interaction patterns |

## 3. Background

### Context
OpenDetect is an automated data quality platform that detects errors in tabular data using pattern-based validation (Auto-Validate), spelling correction, numeric outlier detection, and functional dependency analysis. Currently, when OpenDetect flags a cell as an error, users only see:
- A boolean `is_error` flag
- A numeric `score` (confidence)
- Raw `evidence` JSON with pattern details

### Why Now?
1. **User Feedback from Beta**: Early users report that raw evidence is too technical — they need plain-language explanations to understand and act on detections.
2. **OPE-86/OPE-162 Completion**: The verdict-cache optimization (now merged) makes pattern inference fast enough to pre-compute tooltip content without latency penalties.
3. **Competitive Gap**: Competing tools (Great Expectations, Deequ) provide human-readable error messages; OpenDetect needs parity.

### What Changed?
- Pattern inference is now cached per distinct value (OPE-86), enabling O(1) tooltip content lookup
- The evidence structure is standardized across detectors (Auto-Validate, Spelling, Numeric, FD)

## 4. Objective

### Goal
Provide contextual, actionable tooltips that explain **why** a cell was flagged and **how** to fix it, reducing time-to-resolution for data quality issues by 50%.

### Benefits
- **For Data Engineers**: Faster debugging — no need to inspect raw JSON evidence
- **For Analysts**: Self-service understanding of data quality issues without engineering help
- **For OpenDetect**: Differentiation through superior UX; reduces support burden

### Success Metrics (OKRs)
| Key Result | Target | Measurement |
|------------|--------|-------------|
| Tooltip open rate on flagged cells | > 60% | Frontend telemetry |
| Time from detection to user acknowledgment | < 30 seconds | Event timestamps |
| "Helpful" rating on tooltip feedback | > 4.0 / 5.0 | In-tooltip survey |
| Support tickets about detection interpretation | -50% | Support system tags |

## 5. Market Segments

| Segment | Problems | Constraints |
|---------|----------|-------------|
| **Data Engineers** (primary) | Need to triage hundreds of flagged cells quickly; raw evidence is slow to parse | Must integrate with existing CLI/API workflows; cannot add latency to detection |
| **Data Analysts** (secondary) | See flagged cells in dashboards but don't understand pattern language | Read-only access; tooltips must work in embedded views |
| **Data Stewards** (tertiary) | Need to communicate issues to business stakeholders | Require exportable, shareable explanations |

## 6. Value Propositions

### Customer Jobs
| Job | Current Pain | Tooltip Solution |
|-----|--------------|------------------|
| "Understand why this email was rejected" | Raw regex pattern `<alphanum>+@<domain>+` is opaque | "Expected format: name@domain.com — got 'john@@example.com'" |
| "Fix this date format error" | Evidence shows `fpr_t=0.0, cov_t=2` — meaningless | "Expected YYYY-MM-DD — got '15/01/2024' (day/month/year)" |
| "Explain this outlier to my manager" | Must manually create explanation from score + evidence | One-click "Copy explanation" with business-friendly language |

### Competitive Advantages
- **Context-aware**: Tooltips adapt to detector type (Auto-Validate vs Spelling vs Numeric)
- **Action-oriented**: Every tooltip includes a suggested fix, not just diagnosis
- **Zero-latency**: Pre-computed during detection via verdict cache (OPE-86)

## 7. Solution

### 7.1 UX / Prototypes

#### Tooltip Trigger
- **Hover**: Show tooltip after 300ms delay on flagged cell (desktop)
- **Tap/Long-press**: Mobile/touch interaction
- **Keyboard**: Focus + `?` key for accessibility

#### Tooltip Anatomy
```
┌─────────────────────────────────────────────┐
│ 🔴 Error: Invalid Email Format              │  ← Title (severity + category)
├─────────────────────────────────────────────┤
│ Expected: name@domain.com                   │  ← Plain-language pattern
│ Received: john@@example.com                 │  ← Actual value (truncated)
│                                             │
│ 💡 Suggestion: Remove duplicate '@'         │  ← Actionable fix
│                                             │
│ [Details]  [Copy]  [Dismiss]               │  ← Actions
└─────────────────────────────────────────────┘
```

#### States
| State | Description |
|-------|-------------|
| Default | Title + expected/received + suggestion |
| Expanded | Click "Details" → shows pattern, score, evidence JSON |
| Copied | Toast confirmation "Explanation copied to clipboard" |
| Loading | Skeleton state if content not pre-computed (fallback) |

### 7.2 Key Features

#### F1: Pattern-to-Language Translation
- **Auto-Validate**: Convert inferred regex patterns to human-readable format
  - `<alphanum>+<symbol>+<alphanum>+<symbol>+<alphanum>+` → "word@domain.tld"
  - `<digit>{4}-<digit>{2}-<digit>{2}` → "YYYY-MM-DD"
- **Spelling**: Show nearest valid dictionary word + edit distance
- **Numeric**: Show expected range + actual value + z-score interpretation
- **FD**: Show functional dependency (A → B) + violating value pair

#### F2: Contextual Suggestion Engine
| Detector | Suggestion Template |
|----------|---------------------|
| Auto-Validate | "Remove extra character", "Use format X", "Value not in allowed set" |
| Spelling | "Did you mean 'X'? (edit distance: N)" |
| Numeric | "Value exceeds 3σ threshold — verify data entry" |
| FD | "Column B should be determined by A — check for duplicate A with different B" |

#### F3: Tooltip Content API
**Endpoint**: `GET /api/v1/detections/{detection_id}/tooltip`
```json
{
  "detection_id": "det_abc123",
  "title": "Invalid Email Format",
  "severity": "error",
  "category": "format",
  "expected_pattern": "name@domain.com",
  "received_value": "john@@example.com",
  "suggestion": "Remove duplicate '@' symbol",
  "details": {
    "inferred_pattern": "<alphanum>+@<domain>+",
    "false_positive_rate": 0.0,
    "coverage": 2,
    "theta_c": 0.0,
    "variant": "fmdv_vh"
  },
  "actions": ["copy_explanation", "view_evidence", "ignore_once"]
}
```

#### F4: Pre-computation at Detection Time
- During `detector.detect()`, compute tooltip content for each flagged cell
- Store in `CellResult.evidence.tooltip` field (extends existing evidence)
- Leverage OPE-86 verdict cache: tooltip content keyed by distinct value
- Fallback: compute on-demand via API if not pre-computed

#### F5: Accessibility & Internationalization
- ARIA labels for screen readers
- Keyboard navigation (focus trap within tooltip)
- i18n-ready: all strings externalized, support for RTL languages

### 7.3 Technology

#### Backend Changes
1. **Extend `CellResult` model** (`src/open_detect/algorithms/base.py`):
   ```python
   @dataclass(frozen=True)
   class CellResult:
       ...
       tooltip: TooltipContent | None = None
   
   @dataclass(frozen=True)
   class TooltipContent:
       title: str
       severity: Literal["error", "warning", "info"]
       category: str
       expected_pattern: str
       received_value: str
       suggestion: str
       details: dict  # detector-specific evidence
       actions: list[str]
   ```

2. **Add tooltip generators per detector** (`src/open_detect/algorithms/*/tooltips.py`):
   - `auto_validate/tooltips.py`: Pattern-to-language + suggestion
   - `spelling/tooltips.py`: Nearest word + edit distance
   - `numeric/tooltips.py`: Range + z-score interpretation
   - `fd/tooltips.py`: Dependency explanation

3. **API endpoint** (`src/open_detect/api/detections.py`):
   - `GET /detections/{id}/tooltip` — returns pre-computed or on-demand tooltip

4. **Verdict cache integration** (OPE-86):
   - Extend `_distinct_value_verdicts()` to also compute tooltip content
   - Store in `_tooltip_cache: dict[str, TooltipContent]`

#### Frontend Changes
1. **Tooltip React component** (`packages/ui/src/components/Tooltip.tsx`):
   - Reusable, accessible, animated
   - Props: `content`, `trigger`, `position`, `onAction`

2. **Detection table integration** (`packages/ui/src/pages/DetectionsTable.tsx`):
   - Attach tooltip to flagged cells
   - Handle keyboard/touch triggers

3. **Telemetry hooks** (`packages/ui/src/hooks/useTooltipTelemetry.ts`):
   - Track open rate, dwell time, action clicks

### 7.4 Assumptions
| Assumption | Validation Plan |
|------------|-----------------|
| Pattern-to-language translation covers 90%+ of real patterns | Test against production corpus patterns |
| Tooltip content adds < 5% to detection latency | Benchmark with 100k-row tables |
| Users prefer suggestions over raw evidence | A/B test: tooltip vs raw JSON in beta |
| Pre-computation memory overhead is acceptable | Profile memory on 1M distinct values |

## 8. Release

### Phase 1: Core Tooltip Engine (4 weeks)
- [ ] Extend `CellResult` with `tooltip` field
- [ ] Implement pattern-to-language for Auto-Validate (covers 70% of detections)
- [ ] Build backend tooltip API endpoint
- [ ] Create reusable frontend Tooltip component
- [ ] Integrate into detection results table
- [ ] Unit tests for tooltip generators

### Phase 2: Full Detector Coverage (3 weeks)
- [ ] Spelling detector tooltips
- [ ] Numeric outlier tooltips
- [ ] FD detector tooltips
- [ ] Raha detector tooltips
- [ ] Cross-detector tooltip consistency review

### Phase 3: Polish & Telemetry (2 weeks)
- [ ] Accessibility audit (WCAG 2.1 AA)
- [ ] i18n framework + English strings
- [ ] Telemetry dashboard (open rate, helpfulness)
- [ ] Performance optimization (cache hit rate > 95%)
- [ ] Documentation & developer guide

### Phase 4: Beta & Iterate (ongoing)
- [ ] Beta release to 3 design partners
- [ ] Collect feedback via in-tooltip survey
- [ ] Iterate on suggestion quality
- [ ] General availability

### Future Enhancements (Not in v1)
- **Smart grouping**: Cluster similar errors into one tooltip with "N cells affected"
- **Interactive fix**: "Apply suggestion" button that proposes data correction
- **Learning mode**: Tooltip improves based on user accept/reject of suggestions
- **Export**: "Download all explanations as CSV" for stakeholder reports