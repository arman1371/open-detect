"""FMDV-V and FMDV-VH: vertical cuts + (optionally) horizontal cuts.

FMDV-V (Eqns 8-10) splits a composite column into vertical segments by
aligning coarse token-class signatures, then solving an m-segmentation
problem via DP (Eqn 11).  Each segment is solved with FMDV (single-pattern,
no horizontal tolerance).  Objective: **sum** of segment FPRs, NOT max
(paper-spec §8.3).

FMDV-VH applies FMDV-H horizontally first (tolerate non-conforming values
within each segment), then applies FMDV-V vertically.

## Alignment strategy

Values are tokenized into **coarse** token classes (``<symbol>``, ``<num>``,
``<letter>``).  Two values have the same *coarse signature* when their
token-class sequences are identical.

- **Exact MSA** (the ideal): multi-sequence alignment (Carrillo & Lipman
  1988) over the token sequences.  Exponential in the worst case.
- **Our approach**: group values by coarse signature.  Within each group,
  all values already share the same class sequence, so positional
  alignment is exact — no gaps are needed.  We run DP separately on each
  group and return the best segment pattern from each group.  Values whose
  coarse signature is unique (appears only once) are treated as a single
  segment group.  When no group admits a feasible FMDV pattern, the
  function returns ``None``.

This is exact when all values share one coarse signature (the typical case
for homogeneous machine-generated data, per the paper's own assumption)
and an approximation otherwise.  Documented as a fidelity note.
"""

from __future__ import annotations

import math
from collections.abc import Callable

import pandas as pd

from open_detect.algorithms.auto_validate.config import AutoValidateConfig
from open_detect.algorithms.auto_validate.fmdv import InferredPattern, _clean
from open_detect.algorithms.auto_validate.hierarchy import matches
from open_detect.algorithms.auto_validate.index import PatternIndex
from open_detect.algorithms.auto_validate.patterns import patterns_of, sorted_patterns


def fmdv_v(
    values: pd.Series,
    index: PatternIndex,
    config: AutoValidateConfig | None = None,
) -> InferredPattern | None:
    """Eqn 8-11: vertical cuts via DP on coarse-aligned token segments."""
    config = config or AutoValidateConfig()
    clean = _clean(values)
    if not clean:
        return None

    # Group by coarse token signature.
    sig_to_idx: dict[tuple[str, ...], list[int]] = {}
    for i, v in enumerate(clean):
        sig = _coarse_signature(v)
        sig_to_idx.setdefault(sig, []).append(i)

    best_overall: InferredPattern | None = None
    for indices in sig_to_idx.values():
        group = [clean[i] for i in indices]
        if len(group) == 0:
            continue
        seg = _segment_fmdv_v(group, index, config)
        if seg is None:
            continue
        if best_overall is None or _infer_cmp(seg, best_overall) < 0:
            best_overall = seg

    return best_overall


def fmdv_vh(
    values: pd.Series,
    index: PatternIndex,
    config: AutoValidateConfig | None = None,
) -> InferredPattern | None:
    """FMDV-VH: horizontal cut first (theta), then vertical cuts.

    We apply FMDV-H tolerance to *each* vertical segment separately.  Values
    are partitioned by coarse signature, and within each segment group we
    run the horizontal-tolerant DP (:func:`_segment_fmdv_vh`).  The result
    aggregates per-segment patterns.
    """
    config = config or AutoValidateConfig()
    clean = _clean(values)
    if not clean:
        return None

    sig_to_idx: dict[tuple[str, ...], list[int]] = {}
    for i, v in enumerate(clean):
        sig = _coarse_signature(v)
        sig_to_idx.setdefault(sig, []).append(i)

    all_patterns: list[InferredPattern] = []
    total_fpr = 0.0
    total_cov = 0
    total_theta_c_num = 0.0
    total_theta_c_den = 0.0

    for indices in sig_to_idx.values():
        group = [clean[i] for i in indices]
        seg = _segment_fmdv_vh(group, index, config)
        if seg is None:
            continue
        all_patterns.append(seg)
        total_fpr += seg.fpr_t
        total_cov += seg.cov_t
        total_theta_c_num += seg.theta_c * seg.cov_t  # proportional contribution
        total_theta_c_den += seg.cov_t

    if not all_patterns:
        return None
    theta_c = total_theta_c_num / total_theta_c_den if total_theta_c_den else 0.0
    patterns = [s.pattern for s in all_patterns]
    return InferredPattern(
        pattern=patterns[0] if len(patterns) == 1 else patterns,  # type: ignore[arg-type]
        fpr_t=total_fpr,
        cov_t=total_cov,
        theta_c=theta_c,
        variant="fmdv_vh",
    )


def _coarse_signature(value: str) -> tuple[str, ...]:
    """Coarse token class sequence: <symbol>, <num>, or <letter> per run."""
    return tuple(_coarse_class(ch) for ch in value)


def _coarse_class(ch: str) -> str:
    if ch.isdigit():
        return "<num>"
    if ch.isalpha():
        return "<letter>"
    return "<symbol>"


def _segment_dp(
    values: list[str],
    index: PatternIndex,
    config: AutoValidateConfig,
    variant: str,
    solve_segment: Callable[[list[str], PatternIndex, AutoValidateConfig], InferredPattern | None],
) -> InferredPattern | None:
    """Run the shared vertical-cut DP and aggregate the chosen segments.

    ``solve_segment`` is the per-segment FMDV variant (single-segment FMDV for
    ``fmdv_v``; FMDV-H for ``fmdv_vh``).  Returns ``None`` when no feasible
    segmentation exists.
    """
    n = len(values)
    if n == 0:
        return None

    INF = float("inf")
    dp: list[list[float]] = [[INF] * n for _ in range(n)]
    parent: list[list[int | None]] = [[None] * n for _ in range(n)]

    # Paper Def. 2 enforces e_i - s_i < tau (strict), so the widest admissible
    # segment is tau-1 tokens.  A segment of exactly tau tokens is not
    # permitted; skip both the no-split leaf and any split candidate wider
    # than tau-1.
    max_width = config.tau - 1

    for length in range(1, n + 1):
        if length > max_width:
            continue
        for i in range(0, n - length + 1):
            j = i + length - 1
            seg = solve_segment(values[i : j + 1], index, config)
            best_cost = seg.fpr_t if seg else INF

            for t in range(i, j):
                left = dp[i][t]
                right = dp[t + 1][j]
                if left < INF and right < INF and left + right < best_cost:
                    best_cost = left + right
                    parent[i][j] = t
            dp[i][j] = best_cost

    if dp[0][n - 1] >= INF:
        return None

    segments: list[list[str]] = []
    i, j = 0, n - 1
    while i <= j:
        p = parent[i][j]
        if p is None:
            segments.append(values[i : j + 1])
            i = j + 1
        else:
            segments.append(values[i : p + 1])
            i = p + 1

    total_fpr = 0.0
    total_cov = 0
    best_segments: list[InferredPattern] = []
    for seg_vals in segments:
        seg = solve_segment(seg_vals, index, config)
        if seg is None:
            return None
        total_fpr += seg.fpr_t
        total_cov += seg.cov_t
        best_segments.append(seg)

    theta_c = sum(s.theta_c * s.cov_t for s in best_segments) / total_cov if total_cov else 0.0
    patterns = [s.pattern for s in best_segments]
    return InferredPattern(
        pattern=patterns[0] if len(patterns) == 1 else patterns,  # type: ignore[arg-type]
        fpr_t=total_fpr,
        cov_t=total_cov,
        theta_c=theta_c,
        variant=variant,
    )


def _segment_fmdv_v(
    values: list[str],
    index: PatternIndex,
    config: AutoValidateConfig,
) -> InferredPattern | None:
    """Run FMDV-V on a single coarse-signature group via DP."""
    return _segment_dp(values, index, config, "fmdv_v", _fmdv_single_segment)


def _segment_fmdv_vh(
    values: list[str],
    index: PatternIndex,
    config: AutoValidateConfig,
) -> InferredPattern | None:
    """FMDV-VH within a single coarse-signature group: horizontal first, then DP."""
    return _segment_dp(values, index, config, "fmdv_vh", _fmdv_h_single)


def _fmdv_single_segment(
    values: list[str],
    index: PatternIndex,
    config: AutoValidateConfig,
) -> InferredPattern | None:
    """FMDV over a single segment (no horizontal tolerance)."""
    if not values:
        return None
    candidate_set: set[str] = set()
    for v in values:
        candidate_set |= patterns_of(v, config.tau)
    candidates = sorted_patterns(candidate_set)

    best: dict | None = None
    for pattern in candidates:
        entry = index.lookup(pattern)
        if entry is None:
            continue
        fpr_t, cov_t = entry
        if fpr_t > config.r or cov_t < config.m:
            continue
        n_match = sum(1 for v in values if matches(pattern, v))
        if n_match != len(values):
            continue
        key = (fpr_t, -cov_t, pattern)
        if best is None or key < best["key"]:
            best = {"key": key, "pattern": pattern, "fpr_t": fpr_t, "cov_t": cov_t}

    if best is None:
        return None
    return InferredPattern(
        pattern=best["pattern"],
        fpr_t=best["fpr_t"],
        cov_t=best["cov_t"],
        theta_c=0.0,
        variant="fmdv",
    )


def _fmdv_h_single(
    values: list[str],
    index: PatternIndex,
    config: AutoValidateConfig,
) -> InferredPattern | None:
    """FMDV-H over a single segment (with horizontal theta tolerance)."""
    if not values:
        return None
    # Paper Eqn 16: h must match at least ceil((1-theta)|C|) values.
    min_conforming = math.ceil((1.0 - config.theta) * len(values))

    candidate_set: set[str] = set()
    for v in values:
        candidate_set |= patterns_of(v, config.tau)
    candidates = sorted_patterns(candidate_set)

    best: dict | None = None
    for pattern in candidates:
        entry = index.lookup(pattern)
        if entry is None:
            continue
        fpr_t, cov_t = entry
        if fpr_t > config.r or cov_t < config.m:
            continue
        n_match = sum(1 for v in values if matches(pattern, v))
        if n_match < min_conforming:
            continue
        imp = 1.0 - n_match / len(values)
        key = (fpr_t, imp, -cov_t, pattern)
        if best is None or key < best["key"]:
            best = {
                "key": key,
                "pattern": pattern,
                "fpr_t": fpr_t,
                "cov_t": cov_t,
                "n_match": n_match,
            }

    if best is None:
        return None
    theta_c = 1.0 - best["n_match"] / len(values)
    return InferredPattern(
        pattern=best["pattern"],
        fpr_t=best["fpr_t"],
        cov_t=best["cov_t"],
        theta_c=theta_c,
        variant="fmdv_h",
    )


def _infer_cmp(a: InferredPattern, b: InferredPattern) -> int:
    """Compare two InferredPatterns by (fpr_t, theta_c, cov_t desc, variant)."""
    if a.fpr_t < b.fpr_t:
        return -1
    if a.fpr_t > b.fpr_t:
        return 1
    if a.theta_c < b.theta_c:
        return -1
    if a.theta_c > b.theta_c:
        return 1
    if a.cov_t != b.cov_t:
        return -1 if a.cov_t > b.cov_t else 1
    return -1 if a.variant < b.variant else (1 if a.variant > b.variant else 0)
