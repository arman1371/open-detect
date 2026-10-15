"""Minimum pairwise edit-distance (MPD) metric for spelling errors.

See paper Section 3.2 and Example 1. MPD is computed over the column's
*distinct* values: an exact repeat is a duplicate (the uniqueness error
class), not a misspelling, so it must not populate the MPD=0 bucket.

A naive implementation is O(n^2) string comparisons per column, which is
unacceptable at Databricks scale (columns with 10^4-10^6 distinct values are
common). Columns with at most ``max_block_size`` distinct values are
therefore compared exhaustively (exact), while larger columns use blocking:
candidate pairs are only compared when they share a key -- (first two
characters | last two characters) x (length bucket | length bucket shifted by
one), plus one key shared by all values of up to three characters -- and each
block is capped at ``max_block_size`` values. Any two values at edit distance
1 (one substitution, insertion or deletion) share at least one key, so MPD=1
-- the case the detector cares about most -- is found exactly. For larger distances the result is an upper bound on the
true MPD (a pair needing edits in both the prefix and the suffix can be
missed, and oversized blocks are stride-subsampled), which trades a small
amount of recall on adversarial inputs for near-linear expected runtime.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Sequence
from dataclasses import dataclass
from itertools import combinations

from rapidfuzz.distance import Levenshtein

from open_detect.algorithms.uni_detect.metrics.base import drop_nulls, require_min_size
from open_detect.exceptions import InsufficientDataError, ValidationError


@dataclass(frozen=True, slots=True)
class MPDResult:
    mpd: int
    index_u: int
    """Index (into the null-dropped, stringified input) of the first occurrence of ``value_u``."""
    index_v: int
    value_u: str
    value_v: str


_LENGTH_BUCKET_WIDTH = 3


_SHORT_MAX_LEN = 3


def _blocking_keys(s: str) -> set[tuple[str, str, int]]:
    """Keys under which ``s`` is compared; values at edit distance 1 always share one.

    For length >= 4 a single edit leaves the first two or the last two
    characters of both values intact, and changes the length by at most one,
    which moves the ``len // 3`` bucket only when ``len % 3 == 2`` -- in which
    case the shifted ``(len + 1) // 3`` bucket still agrees. Values of up to
    three characters have no intact prefix/suffix after an edit, so they also
    all share one "short" key.
    """
    lowered = s.lower()
    n = len(s)
    buckets = (n // _LENGTH_BUCKET_WIDTH, (n + 1) // _LENGTH_BUCKET_WIDTH)
    keys = {
        (kind, anchor, bucket)
        for kind, anchor in (("p", lowered[:2]), ("s", lowered[-2:]))
        for bucket in buckets
    }
    if n <= _SHORT_MAX_LEN:
        keys.add(("short", "", 0))
    return keys


def _closest_pair(
    clean: list[str], idxs: Sequence[int], best: MPDResult | None
) -> MPDResult | None:
    for i, j in combinations(idxs, 2):
        dist = Levenshtein.distance(clean[i], clean[j])
        if best is None or dist < best.mpd:
            best = MPDResult(mpd=dist, index_u=i, index_v=j, value_u=clean[i], value_v=clean[j])
            if dist <= 1:  # values are distinct, so 1 is the global minimum
                break
    return best


def _search_mpd(values: Sequence[object], max_block_size: int) -> tuple[MPDResult | None, int]:
    """Return ``(result, n_distinct)``; ``result`` is None when no pair can be compared."""
    stringified = [str(v) for v in drop_nulls(list(values))]
    first_index: dict[str, int] = {}
    for i, v in enumerate(stringified):
        first_index.setdefault(v, i)
    distinct = list(first_index)
    require_min_size(distinct, 2, "min_pairwise_edit_distance")
    # Work on the distinct values; map positions back to first occurrences at the end.
    positions = list(first_index.values())

    def _result(r: MPDResult) -> MPDResult:
        return MPDResult(
            mpd=r.mpd,
            index_u=positions[r.index_u],
            index_v=positions[r.index_v],
            value_u=r.value_u,
            value_v=r.value_v,
        )

    if len(distinct) <= max_block_size:
        best = _closest_pair(distinct, range(len(distinct)), None)
        if best is None:  # unreachable: >= 2 distinct values guarantees at least one pair
            raise InsufficientDataError("min_pairwise_edit_distance found no comparable value pair")
        return _result(best), len(distinct)

    blocks: dict[tuple[str, str, int], list[int]] = defaultdict(list)
    for i, v in enumerate(distinct):
        for key in _blocking_keys(v):
            blocks[key].append(i)

    best = None
    for idxs in blocks.values():
        if len(idxs) < 2:
            continue
        if len(idxs) > max_block_size:
            # Deterministic, stride-based subsample rather than random.sample,
            # so results are reproducible without seeding global RNG state.
            stride = len(idxs) // max_block_size + 1
            idxs = idxs[::stride]
        best = _closest_pair(distinct, idxs, best)
        if best is not None and best.mpd <= 1:
            return _result(best), len(distinct)

    return (_result(best) if best is not None else None), len(distinct)


def try_min_pairwise_edit_distance(
    values: Sequence[object],
    max_block_size: int = 500,
) -> MPDResult | None:
    """Like :func:`min_pairwise_edit_distance`, but return ``None`` when no pair can be compared.

    That happens when no two values share a blocking key and the column has
    more than ``max_block_size`` distinct values, so the exhaustive scan does
    not apply. Fewer than two distinct values still raises
    :class:`~open_detect.exceptions.InsufficientDataError`.
    """
    return _search_mpd(values, max_block_size)[0]


def min_pairwise_edit_distance(
    values: Sequence[object],
    max_block_size: int = 500,
) -> MPDResult:
    """``MPD(C) = min_{u != v in C} Edit(u, v)`` -- the closest pair of *distinct* values.

    Parameters
    ----------
    values:
        Column values; non-strings are stringified (``str(v)``) so this also
        works on mixed-alphanumeric columns. Exact repeats are collapsed
        before comparison; fewer than two distinct values raises
        :class:`~open_detect.exceptions.InsufficientDataError`.
    max_block_size:
        Columns with at most this many distinct values are compared
        exhaustively. Larger columns use blocking; blocks larger than this are
        deterministically subsampled, bounding worst-case cost to
        ``O(max_block_size^2)`` per block.

    Raises
    ------
    InsufficientDataError
        Fewer than two distinct non-null values.
    ValidationError
        No two values share a block and the column exceeds ``max_block_size``.
    """
    result, n_distinct = _search_mpd(values, max_block_size)
    if result is None:
        raise ValidationError(
            "min_pairwise_edit_distance found no comparable blocks and the "
            f"column ({n_distinct} distinct values) exceeds max_block_size={max_block_size}; "
            "increase max_block_size or pre-bucket the column."
        )
    return result


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
