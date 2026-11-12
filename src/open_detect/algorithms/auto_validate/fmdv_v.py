"""FMDV-V and FMDV-VH: vertical cuts + (optionally) horizontal cuts.

FMDV-V (Eqns 8-10) splits a composite column into vertical segments by
aligning coarse token-class signatures, then solving an m-segmentation
problem via DP (Eqn 11).  Each segment is solved with FMDV (single-pattern,
no horizontal tolerance).  Objective: **sum** of segment FPRs, NOT max
(paper-spec §8.3).

FMDV-VH applies FMDV-H horizontally first (tolerate non-conforming values
within each segment), then applies FMDV-V vertically.

## Alignment strategy

Values are tokenized with the shared tokenizer
(:func:`~open_detect.algorithms.auto_validate.hierarchy.tokenize`).  Two values
have the same *coarse signature* when their token-class sequences (one class
per token, not per character) are identical, so ``"Jan 5"`` and ``"Jan 15"``
fall in the same group.

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

from collections.abc import Callable, Sequence

import pandas as pd

from open_detect.algorithms.auto_validate.config import AutoValidateConfig
from open_detect.algorithms.auto_validate.fmdv import InferredPattern, _clean, min_conforming
from open_detect.algorithms.auto_validate.hierarchy import matches, tokenize
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

    # For each signature group, run DP to get its ordered segments.
    # We preserve one pattern per signature group (like fmdv_vh).
    all_patterns: list[InferredPattern] = []
    total_fpr = 0.0
    total_cov = 0
    total_theta_c_num = 0.0
    total_theta_c_den = 0.0

    for indices in sig_to_idx.values():
        group = [clean[i] for i in indices]
        seg = _segment_fmdv_v(group, index, config)
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

    # Preserve per-signature-group segment patterns as nested sequences
    # Each element of all_patterns is an InferredPattern whose .pattern is
    # a Sequence[str] of ordered segments for that signature group.
    group_patterns: list[Sequence[str]] = []
    for s in all_patterns:
        pat = s.pattern
        if isinstance(pat, str):
            # Single segment for this signature group
            group_patterns.append([pat])
        elif isinstance(pat, Sequence):
            # Multiple ordered segments for this signature group
            group_patterns.append(pat)  # type: ignore[arg-type]

    # For backward compatibility: when there's a single group with a single
    # segment, return the pattern as a string, not a nested list.
    if (
        len(group_patterns) == 1
        and len(group_patterns[0]) == 1
        and isinstance(group_patterns[0][0], str)
    ):
        pattern: str | Sequence[str] | list[Sequence[str]] = group_patterns[0][0]
    else:
        pattern = group_patterns

    return InferredPattern(
        pattern=pattern,
        fpr_t=min(1.0, total_fpr),
        cov_t=total_cov,
        theta_c=theta_c,
        variant="fmdv_v",
    )


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
    # Preserve per-signature-group segment patterns as nested sequences
    # Each element of all_patterns is an InferredPattern whose .pattern is
    # a Sequence[str] of ordered segments for that signature group.
    group_patterns: list[Sequence[str]] = []
    for s in all_patterns:
        pat = s.pattern
        # Filter to only include patterns that are Sequence[str] (not str, not list[Sequence[str]]).
        # pat could be: str (fmdv/fmdv_h), Sequence[str] (fmdv_v, fmdv_vh single group), or list[Sequence[str]] (fmdv_vh multiple groups).
        # We want to keep Sequence[str] which includes list[str] but not list[Sequence[str]].
        # Check: if it's a non-string sequence, and if it's a list, ensure its first element is a string (not a sequence).
        if isinstance(pat, Sequence) and not isinstance(pat, str):
            if (
                isinstance(pat, list)
                and pat
                and isinstance(pat[0], Sequence)
                and not isinstance(pat[0], str)
            ):
                # This is list[Sequence[str]] (nested groups) - skip, we handle at outer level
                continue
            # This is Sequence[str] (could be list[str] or tuple[str, ...]) - keep
            group_patterns.append(pat)  # type: ignore[arg-type]
    # For backward compatibility: when there's a single group with a single
    # segment, return the pattern as a string, not a nested list.
    if (
        len(group_patterns) == 1
        and len(group_patterns[0]) == 1
        and isinstance(group_patterns[0][0], str)
    ):
        pattern: str | Sequence[str] | list[Sequence[str]] = group_patterns[0][0]
    else:
        pattern = group_patterns
    return InferredPattern(
        pattern=pattern,
        fpr_t=min(1.0, total_fpr),
        cov_t=total_cov,
        theta_c=theta_c,
        variant="fmdv_vh",
    )


def _coarse_signature(value: str) -> tuple[str, ...]:
    """Token-class sequence of ``value``: one class per token, not per character."""
    return tuple(token.char_class for token in tokenize(value))


def _segment_dp(
    values: list[str],
    index: PatternIndex,
    config: AutoValidateConfig,
    variant: str,
    solve_segment: Callable[[list[str], PatternIndex, AutoValidateConfig], InferredPattern | None],
) -> InferredPattern | None:
    """Run the shared vertical-cut DP over token positions and aggregate the segments.

    ``values`` must share one token-class signature, so token position ``p``
    lines up across all values.  A segment ``(i, j)`` is the column slice of
    tokens ``i..j-1`` of every value, rejoined into a string.  ``solve_segment``
    is the per-segment FMDV variant (single-segment FMDV for ``fmdv_v``; FMDV-H
    for ``fmdv_vh``).  Returns ``None`` when no feasible segmentation exists.
    """
    if not values:
        return None
    token_rows = [[token.text for token in tokenize(v)] for v in values]
    n_tokens = len(token_rows[0])
    if any(len(row) != n_tokens for row in token_rows):
        raise ValueError("values must share a token-class signature")

    # Paper Def. 2 enforces e_i - s_i < tau (strict), so the widest admissible
    # segment is tau-1 tokens.  Only that band of start positions is ever
    # looked at, so dp/parent are 1-D arrays indexed by segment end.
    max_width = config.tau - 1

    memo: dict[tuple[int, int], InferredPattern | None] = {}

    def segment(i: int, j: int) -> InferredPattern | None:
        key = (i, j)
        if key not in memo:
            memo[key] = solve_segment(["".join(row[i:j]) for row in token_rows], index, config)
        return memo[key]

    inf = float("inf")
    # dp[j]: minimal summed FPR of a segmentation of tokens 0..j-1.
    dp = [inf] * (n_tokens + 1)
    parent = [-1] * (n_tokens + 1)
    dp[0] = 0.0
    for j in range(1, n_tokens + 1):
        for i in range(max(0, j - max_width), j):
            if dp[i] == inf:
                continue
            seg = segment(i, j)
            if seg is None:
                continue
            cost = dp[i] + seg.fpr_t
            if cost < dp[j]:
                dp[j] = cost
                parent[j] = i

    if dp[n_tokens] == inf:
        return None

    best_segments: list[InferredPattern] = []
    j = n_tokens
    while j > 0:
        i = parent[j]
        seg = segment(i, j)
        assert seg is not None
        best_segments.append(seg)
        j = i
    best_segments.reverse()

    total_fpr = min(1.0, sum(s.fpr_t for s in best_segments))
    total_cov = sum(s.cov_t for s in best_segments)
    theta_c = sum(s.theta_c * s.cov_t for s in best_segments) / total_cov if total_cov else 0.0
    # Preserve segment groups: each vertical segmentation produces ordered
    # segments that must ALL match (AND logic). For backward compatibility,
    # return a single string when there's only one segment.
    segment_patterns = [s.pattern for s in best_segments if isinstance(s.pattern, str)]
    if len(segment_patterns) == 1:
        pattern: str | Sequence[str] | list[Sequence[str]] = segment_patterns[0]
    else:
        pattern = segment_patterns
    return InferredPattern(
        pattern=pattern,
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
        if not all(matches(pattern, v) for v in values):
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
    required = min_conforming(config.theta, len(values))

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
        if n_match < required:
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
