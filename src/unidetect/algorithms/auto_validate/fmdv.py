"""FMDV and FMDV-H pattern inference (paper Eqns 5-7 and 12-16).

FMDV solves the basic problem: minimize FPR_T(h) over the *intersection* of
all P(v) in the query column, subject to FPR_T(h) <= r and Cov_T(h) >= m.
H(C) = ∩_{v∈C} P(v) \\ {".*"}.

FMDV-H generalizes the hypothesis space to the *union* of P(v) and adds a
theta-tolerance (Eqn 16): h must match at least (1-theta)|C| values.  This
allows non-conforming values such as "N/A" that would otherwise make H(C)
empty.  The paper says the decision version is NP-hard (Thm 1) and uses a
greedy; we solve the problem exactly by enumerating every distinct candidate
pattern that appears in at least one P(v) and selecting the argmin of
FPR_T among those satisfying all constraints.  Ties are broken
deterministically by (fpr_t ascending, generality_weight ascending, pattern
lexicographically) — the paper is silent on tie-breaking.

FMDV-V and FMDV-VH (vertical cuts, horizontal-then-vertical) are in
:mod:`fmdv_v`.
"""

from __future__ import annotations

import math
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any

import pandas as pd

from unidetect.algorithms.auto_validate.config import AutoValidateConfig
from unidetect.algorithms.auto_validate.hierarchy import matches
from unidetect.algorithms.auto_validate.index import PatternIndex
from unidetect.algorithms.auto_validate.patterns import patterns_of, sorted_patterns


@dataclass(frozen=True, slots=True)
class InferredPattern:
    """Result of running FMDV (any variant) on a single column."""

    pattern: str | Sequence[str]
    fpr_t: float
    cov_t: int
    theta_c: float
    variant: str


def fmdv(
    values: pd.Series,
    index: PatternIndex,
    config: AutoValidateConfig | None = None,
) -> InferredPattern | None:
    """Eqn 5-7: min FPR_T(h) over H(C) s.t. FPR_T(h) <= r, Cov_T(h) >= m.

    Returns ``None`` when no pattern satisfies both constraints.
    """
    config = config or AutoValidateConfig()
    clean = _clean(values)
    if not clean:
        return None

    candidate_set: set[str] = set()
    for v in clean:
        candidate_set |= patterns_of(v, config.tau)
    candidates = sorted_patterns(candidate_set)

    best: dict[str, Any] | None = None
    for pattern in candidates:
        entry = index.lookup(pattern)
        if entry is None:
            continue
        fpr_t, cov_t = entry
        if fpr_t > config.r or cov_t < config.m:
            continue
        # h must belong to H(C) = ∩P(v) \\ {".*"}, i.e. it must match every
        # value in the query column (Imp_D(h) == 0).
        n_match = sum(1 for v in clean if matches(pattern, v))
        if n_match != len(clean):
            continue
        # Deterministic ordering: minimize FPR_T, then corpus coverage (more
        # evidence = more trusted), then lexicographic.  The paper is silent
        # on tie-breaking; this is the library's choice.
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


def fmdv_h(
    values: pd.Series,
    index: PatternIndex,
    config: AutoValidateConfig | None = None,
) -> InferredPattern | None:
    """Eqn 12-16: min FPR_T over union P(v), with theta coverage on C.

    The hypothesis space is ∪P(v)\\{".*"} (not the intersection).  h must
    match at least ``(1-theta)|C|`` values of the query column.  We search
    the candidate set exactly; the paper's greedy is omitted in favour of a
    complete search over the candidate patterns, which is acceptable for the
    sizes encountered in practice and avoids the ambiguity of the greedy
    description in the paper-spec.
    """
    config = config or AutoValidateConfig()
    clean = _clean(values)
    if not clean:
        return None

    # Paper Eqn 16: h must match at least ceil((1-theta)|C|) values.  Ceiling
    # (not truncation) is required so that e.g. theta=0.1 over 3 values needs
    # all 3 matches, not merely 2.
    min_conforming = math.ceil((1.0 - config.theta) * len(clean))

    candidate_set: set[str] = set()
    for v in clean:
        candidate_set |= patterns_of(v, config.tau)
    candidates = sorted_patterns(candidate_set)

    best: dict[str, Any] | None = None
    for pattern in candidates:
        entry = index.lookup(pattern)
        if entry is None:
            continue
        fpr_t, cov_t = entry
        if fpr_t > config.r or cov_t < config.m:
            continue
        n_match = sum(1 for v in clean if matches(pattern, v))
        if n_match < min_conforming:
            continue
        imp = 1.0 - n_match / len(clean)
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
    theta_c = 1.0 - best["n_match"] / len(clean)
    return InferredPattern(
        pattern=best["pattern"],
        fpr_t=best["fpr_t"],
        cov_t=best["cov_t"],
        theta_c=theta_c,
        variant="fmdv_h",
    )


def _clean(values: pd.Series) -> list[str]:
    """Drop nulls and blanks, str()-convert, preserve order."""
    out: list[str] = []
    for v in values:
        if v is None:
            continue
        try:
            if pd.isna(v):
                continue
        except (TypeError, ValueError):
            pass
        text = v if isinstance(v, str) else str(v)
        if text:
            out.append(text)
    return out
