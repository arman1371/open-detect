"""Minimum pairwise edit-distance (MPD) metric for spelling errors.

See paper Section 3.2 and Example 1. A naive implementation is O(n^2) string
comparisons per column, which is unacceptable at Databricks scale (columns
with 10^4-10^6 distinct values are common). We instead block candidate pairs
by (first two characters, length bucket) -- true near-duplicates almost
always share a prefix and a similar length -- and only compare within a
block, capping block size so a single pathological block cannot blow up
runtime. This trades a small amount of recall on adversarial inputs for
near-linear expected runtime, which is the right trade-off for an automated,
unattended detector.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Sequence
from dataclasses import dataclass
from itertools import combinations

from rapidfuzz.distance import Levenshtein

from unidetect.metrics.base import drop_nulls, require_min_size


@dataclass(frozen=True, slots=True)
class MPDResult:
    mpd: int
    index_u: int
    """Index (into the null-dropped, stringified input) of the first value in the closest pair."""
    index_v: int
    value_u: str
    value_v: str


def _length_bucket(n: int, width: int = 3) -> int:
    return n // width


def _blocking_key(s: str) -> tuple[str, int]:
    prefix = s[:2].lower() if s else ""
    return prefix, _length_bucket(len(s))


def min_pairwise_edit_distance(
    values: Sequence[object],
    max_block_size: int = 500,
) -> MPDResult:
    """``MPD(C) = min_{u != v in C} Edit(u, v)`` -- the closest pair by edit distance.

    Parameters
    ----------
    values:
        Column values; non-strings are stringified (``str(v)``) so this also
        works on mixed-alphanumeric columns.
    max_block_size:
        Blocks larger than this are randomly (but deterministically)
        subsampled before the pairwise comparison, bounding worst-case cost
        to ``O(max_block_size^2)`` per block.
    """
    clean = [str(v) for v in drop_nulls(list(values))]
    require_min_size(clean, 2, "min_pairwise_edit_distance")

    blocks: dict[tuple[str, int], list[int]] = defaultdict(list)
    for i, v in enumerate(clean):
        blocks[_blocking_key(v)].append(i)

    best: MPDResult | None = None
    for idxs in blocks.values():
        if len(idxs) < 2:
            continue
        if len(idxs) > max_block_size:
            # Deterministic, stride-based subsample rather than random.sample,
            # so results are reproducible without seeding global RNG state.
            stride = len(idxs) // max_block_size + 1
            idxs = idxs[::stride]
        for i, j in combinations(idxs, 2):
            dist = Levenshtein.distance(clean[i], clean[j])
            if best is None or dist < best.mpd:
                best = MPDResult(mpd=dist, index_u=i, index_v=j, value_u=clean[i], value_v=clean[j])
            if best.mpd == 0:
                return best

    if best is None:
        # No two values shared a block (e.g. every value has a unique
        # prefix/length combination): fall back to a bounded global scan so
        # small columns still get an exact answer.
        if len(clean) <= max_block_size:
            for i, j in combinations(range(len(clean)), 2):
                dist = Levenshtein.distance(clean[i], clean[j])
                if best is None or dist < best.mpd:
                    best = MPDResult(
                        mpd=dist, index_u=i, index_v=j, value_u=clean[i], value_v=clean[j]
                    )
        else:
            raise ValueError(
                "min_pairwise_edit_distance found no comparable blocks and the "
                f"column ({len(clean)} values) exceeds max_block_size={max_block_size}; "
                "increase max_block_size or pre-bucket the column."
            )
    assert best is not None  # len(clean) >= 2 (require_min_size) guarantees at least one pair
    return best


def differing_token_lengths(value_u: str, value_v: str) -> list[int]:
    """Lengths of whitespace-delimited tokens that differ between two values.

    Used by the spelling featurization dimension (paper Sec. 3.2): edits on
    long tokens ("Doeling"/"Dowling") are more likely genuine typos than
    edits on short ones ("XXI"/"XXII").
    """
    tokens_u = value_u.split()
    tokens_v = value_v.split()
    lengths: list[int] = []
    for tu, tv in zip(tokens_u, tokens_v, strict=False):
        if tu != tv:
            lengths.append(max(len(tu), len(tv)))
    if len(tokens_u) != len(tokens_v):
        extra = (
            tokens_u[len(tokens_v) :]
            if len(tokens_u) > len(tokens_v)
            else tokens_v[len(tokens_u) :]
        )
        lengths.extend(len(t) for t in extra)
    if not lengths:
        lengths.append(max(len(value_u), len(value_v)))
    return lengths
