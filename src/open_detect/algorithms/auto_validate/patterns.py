"""``P(v)``, the set of patterns consistent with a value (paper Section 2.1).

Enumeration follows Algorithm 1 (``GeneratePatterns``): emit the coarsest
pattern first and then progressively drill down into finer ones, rather than
enumerating the full cross-product. A complete product over the per-token
alternatives of a date-time value blows up combinatorially -- the paper
reports over 3 billion candidate patterns for one such column, which is why
``patterns_of`` caps the number of returned patterns and the caller can
restrict enumeration further with a coverage threshold.

Patterns are plain ``str`` objects. They are hashable, order deterministically
(coarsest first, then lexicographically), and render exactly as the paper
writes them.
"""

from __future__ import annotations

import heapq
import itertools
import logging
from collections.abc import Iterator

from open_detect.algorithms.auto_validate.hierarchy import (
    ROOT_PATTERN,
    Token,
    generality_weight,
    generalize,
    matches,
    tokenize,
)

logger = logging.getLogger(__name__)

#: Upper bound on ``len(patterns_of(v))``. The paper does not specify a cap;
#: without one, a date-time value yields millions of patterns per cell. The
#: enumeration order is coarse-first, so truncation drops only the most
#: specialized patterns, which are also the least likely to be chosen as a
#: validation pattern (FMDV minimizes FPR, which favors general patterns).
DEFAULT_MAX_PATTERNS = 2048

#: Cap on the number of alternative spellings explored per token, before the
#: cross-product is materialized. Keeps a single value with many tokens
#: tractable when its alternatives multiply out.
DEFAULT_MAX_ALTERNATIVES = 24


def _alternatives(token: Token) -> tuple[str, ...]:
    return token.generalizations()


def _ordered_alternatives(token: Token, max_alternatives: int) -> tuple[str, ...]:
    """Per-token generalizations, coarsest first and deduplicated."""
    seen: dict[str, None] = {}
    for alt in _alternatives(token):
        seen.setdefault(alt, None)
    ordered = sorted(seen, key=lambda alt: (generality_weight(alt), len(alt), alt))
    if len(ordered) > max_alternatives:
        logger.debug(
            "truncating %d token generalizations to %d for token %r",
            len(ordered),
            max_alternatives,
            token.text,
        )
    return tuple(ordered[:max_alternatives])


def iter_patterns(value: str, *, tau: int | None = None) -> Iterator[str]:
    """Yield the members of ``P(value)``, coarsest first, ``.*`` excluded.

    ``tau`` bounds the number of tokens considered; values with more tokens
    than ``tau`` contribute nothing, mirroring the offline pruning of paper
    Section 2.4 (``P(D) = union over v in D with t(v) < tau``).

    The two ends of the hierarchy -- the value's literal spelling and its
    fully-coarse form -- are always emitted, so both survive truncation even
    when a value's per-token alternatives multiply out past the cap.
    """
    tokens = tokenize(value)
    if tau is not None and len(tokens) >= tau:
        return
    if not tokens:
        return
    coarse = generalize(tokens)
    yield value
    if coarse != value:
        yield coarse
    skip = {ROOT_PATTERN, value, coarse}
    per_token = [_ordered_alternatives(token, DEFAULT_MAX_ALTERNATIVES) for token in tokens]
    widths = [len(alts) for alts in per_token]
    total = 1
    for width in widths:
        total *= width
        if total > 4 * DEFAULT_MAX_PATTERNS:
            # Too many combinations for a full product: fall back to a
            # best-first walk that stays within the cap without materializing
            # the cross-product.
            yield from _best_first_patterns(per_token, DEFAULT_MAX_PATTERNS, skip)
            return
    for combination in itertools.product(*per_token):
        pattern = "".join(combination)
        if pattern not in skip:
            yield pattern


def _best_first_patterns(
    per_token: list[tuple[str, ...]], limit: int, skip: frozenset[str] | set[str]
) -> Iterator[str]:
    """Enumerate patterns by ascending total generality, without a full product.

    Each position is a sorted list of alternatives, coarse first. A heap walks
    index tuples in order of summed generality weight, so the ``limit`` patterns
    yielded are the most general ones available. Patterns in ``skip`` -- the
    root and the two endpoints the caller already emitted -- are passed over.
    """
    weights = [[generality_weight(alt) for alt in alts] for alts in per_token]
    start = tuple(0 for _ in per_token)
    heap: list[tuple[int, tuple[int, ...]]] = [(0, start)]
    seen: set[tuple[int, ...]] = {start}
    emitted = 0
    while heap and emitted < limit:
        cost, indices = heapq.heappop(heap)
        pattern = "".join(per_token[i][j] for i, j in enumerate(indices))
        if pattern not in skip:
            yield pattern
            emitted += 1
        for i in range(len(indices)):
            nxt = list(indices)
            nxt[i] += 1
            if nxt[i] >= len(per_token[i]):
                continue
            key = tuple(nxt)
            if key in seen:
                continue
            seen.add(key)
            new_cost = cost - weights[i][indices[i]] + weights[i][nxt[i]]
            heapq.heappush(heap, (new_cost, key))


def patterns_of(
    value: str,
    tau: int | None = None,
    *,
    max_patterns: int = DEFAULT_MAX_PATTERNS,
) -> frozenset[str]:
    """The members of ``P(value)`` as a set, capped at ``max_patterns``.

    The cap is an implementation necessity, not a paper decision; it keeps
    ``|P(v)|`` bounded for long values. Because enumeration is coarse-first
    (Algorithm 1), truncation retains the general patterns that FMDV's
    minimize-FPR objective is most likely to select.
    """
    out: set[str] = set()
    for pattern in iter_patterns(value, tau=tau):
        out.add(pattern)
        if len(out) >= max_patterns:
            break
    return frozenset(out)


def sorted_patterns(patterns: frozenset[str] | set[str] | list[str]) -> tuple[str, ...]:
    """Deterministic ordering: coarsest pattern first, then lexicographic."""
    return tuple(sorted(patterns, key=lambda p: (generality_weight(p), len(p), p)))


def common_patterns(left: frozenset[str], right: frozenset[str]) -> frozenset[str]:
    """``P(a) ∩ P(b)`` -- the intersection FMDV's hypothesis space is built from."""
    return left & right


def any_pattern(patterns: frozenset[str]) -> str | None:
    """A deterministic representative of a hypothesis set, or ``None`` if empty."""
    ordered = sorted_patterns(patterns)
    return ordered[0] if ordered else None


def matching_pattern(patterns: frozenset[str], value: str) -> str | None:
    """The coarsest member of ``patterns`` that matches ``value``."""
    for pattern in sorted_patterns(patterns):
        if matches(pattern, value):
            return pattern
    return None
