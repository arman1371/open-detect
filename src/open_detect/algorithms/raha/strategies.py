"""Error detection strategies (paper Section 4.1, "Automatic Algorithm Configuration").

Each function below is one *family* of Definition-1 strategies: it runs every
parameter/configuration in that family against a single column (or, for FD,
a column paired with every other column) and returns one boolean array per
strategy, ``True`` marking a cell as flagged by that strategy. These arrays
are later concatenated into each cell's feature vector (see ``features.py``).

We implement three of the paper's four strategy families -- outlier
detection, pattern violation detection, and rule violation detection.
Knowledge-base violation detection (Section 2.2, ``Katara``-style entity
lookups against DBpedia) needs a live external knowledge base and network
access, which is out of scope for a library meant to run against arbitrary,
possibly offline/private data; the paper itself notes Raha "is not limited to
these categories" (Section 2.2), and the feature-vector/clustering/labeling
machinery downstream treats strategy families uniformly, so a knowledge-base
family can be added later as another function following the same
``dict[str, np.ndarray[bool]]`` contract without touching the rest of the
pipeline.

Fidelity note on the histogram outlier strategy: the paper's Equation for
``s_tf`` normalizes term frequency by ``sum_i' TF(d[i',j])``, i.e. the sum of
*each row's own* frequency count -- algebraically this is ``sum_v count(v)^2``
over distinct values ``v``, not the column size. Plugging that literal
denominator into the paper's own worked example (Section 2.2, threshold
``tf=2/6``) does not reproduce the stated result, while the natural reading
"``TF(d[i,j])`` normalized by the number of rows", i.e. plain relative
frequency ``count(v) / |d|``, reproduces it exactly. We implement the latter;
this is the same class of PDF-math-extraction artifact documented in
``open_detect/algorithms/uni_detect/metrics/functional_dependency.py`` for the
Uni-Detect paper.

Performance note: factorize each column once with ``pd.factorize`` and reuse
the integer codes across every strategy that touches that column. This turns
group-building set-add loops into integer-indexed operations (``np.bincount``
and ``np.searchsorted``) and is what the paper calls the "factorize-once"
optimization (OPE-82 P-11). The per-cell flags are still materialized as
booleans -- the matrix is stored as ``float64`` in ``features.py`` because
``pdist`` requires a floating-point array.
"""

from __future__ import annotations

from collections import defaultdict

import numpy as np
import pandas as pd

from open_detect.text_utils import is_float_like

NULL_SENTINEL = "__open_detect_raha_null__"


def normalize_to_str(values: pd.Series) -> pd.Series:
    """Stringify a column, mapping every null-like value to one sentinel category.

    Grouping nulls into a single category (rather than dropping them, or
    letting ``NaN != NaN`` silently split them into their own singleton
    groups) matches how the paper's own running example treats a missing
    placeholder ("*" in Table 2) as an ordinary repeated value. Shared by the
    strategies below and by ``labeling.py``'s ground-truth comparison, so a
    "missing" cell is treated consistently everywhere in the pipeline.
    """
    return values.map(lambda v: NULL_SENTINEL if pd.isna(v) else str(v))


def _factorize_column(series: pd.Series) -> tuple[np.ndarray, np.ndarray]:
    """Stringify + factorize a single column in one pass.

    Mapping nulls to a sentinel before factorizing means they land on a real
    code instead of being silently dropped by pandas, matching how the paper's
    running example treats missing placeholders as ordinary repeated values.
    Returns ``(codes, uniques)`` where ``codes`` has length ``len(series)`` and
    ``uniques`` is a string array of length ``len(set(series))``.
    """
    raw = series.map(lambda v: NULL_SENTINEL if pd.isna(v) else str(v))
    codes, uniques = pd.factorize(raw)
    return codes, np.asarray(uniques)


def histogram_outlier_strategies(
    values: pd.Series, thresholds: tuple[float, ...]
) -> dict[str, np.ndarray]:
    """Histogram-modeling outlier strategies ``s_tf`` (Section 4.1).

    Flags a cell when its value's relative frequency in the column falls
    below ``tf`` -- i.e. it is a comparatively rare value.
    """
    codes, uniques = _factorize_column(values)
    n = len(values)
    if n == 0:
        return {}
    counts = np.bincount(codes, minlength=len(uniques)).astype(float)
    freq = counts[codes] / n
    return {f"outlier_tf<{t}": freq < t for t in thresholds}


def gaussian_outlier_strategies(
    values: pd.Series, thresholds: tuple[float, ...]
) -> dict[str, np.ndarray]:
    """Gaussian-modeling outlier strategies ``s_dist`` (Section 4.1).

    Applies only to (mostly) numeric columns -- returns no strategies
    otherwise, since "distance to the mean in standard deviations" is not
    meaningful for non-numeric data. Cells that fail to parse as numeric
    (including nulls, via :func:`_factorize_column`'s sentinel) are left
    unflagged by this family (the pattern-violation strategies below already
    expose non-numeric characters in an otherwise-numeric column).
    """
    codes, uniques = _factorize_column(values)
    parseable = np.array([is_float_like(u) for u in uniques])
    # "Mostly numeric" is judged by row share, not unique-value share, to
    # match the original ``raw.map(is_float_like).mean()`` semantics: a
    # column of 1000 "1"s and one "x" is mostly numeric even though only
    # 1/2 of its *distinct* values parse. ``row_counts`` holds the per-unique
    # row counts from ``np.bincount``.
    row_counts = np.bincount(codes, minlength=len(uniques))
    row_parseable_share = np.dot(parseable, row_counts) / len(values)
    if row_parseable_share < 0.5:
        return {}

    numeric = np.full(len(uniques), np.nan)
    numeric[parseable] = pd.to_numeric(uniques[parseable], errors="coerce")
    # Mean and std are computed over the *rows*, not the unique values, so a
    # constant column with a single numeric value still yields a strategy
    # (std = 0 -> every cell flagged as nothing, the paper's "no signal" case).
    row_numeric = numeric[codes]
    finite_mask = np.isfinite(row_numeric)
    if finite_mask.sum() < 2:
        return {}

    mean = row_numeric[finite_mask].mean()
    std = row_numeric[finite_mask].std(ddof=0)
    if not std:
        return {f"outlier_dist>{t}": np.zeros(len(values), dtype=bool) for t in thresholds}

    z = np.where(finite_mask, (np.abs(row_numeric - mean) / std), 0.0)

    return {f"outlier_dist>{t}": z > t for t in thresholds}


def pattern_character_strategies(values: pd.Series, max_characters: int) -> dict[str, np.ndarray]:
    """Bag-of-characters pattern-violation strategies ``s_ch`` (Section 4.1).

    One strategy per distinct character observed in the column, flagging
    cells that contain it -- e.g. a stray "-" in an otherwise digit-only
    column. ``max_characters`` bounds this to the most frequent characters so
    a free-text column does not explode the feature space.
    """
    codes, uniques = _factorize_column(values)
    n = len(values)
    if n == 0:
        return {}

    char_counts: dict[str, int] = defaultdict(int)
    unique_counts = np.bincount(codes, minlength=len(uniques))
    for i, u in enumerate(uniques):
        count = int(unique_counts[i])
        for ch in set(u):
            char_counts[ch] += count

    top_chars = sorted(char_counts, key=lambda ch: (-char_counts[ch], ch))[:max_characters]
    if not top_chars:
        return {}

    # Build the (n_rows, n_top_chars) presence matrix by broadcasting
    # unique-value codes against character membership.
    uniq_flags = np.zeros((len(uniques), len(top_chars)), dtype=bool)
    for j, ch in enumerate(top_chars):
        mask = np.fromiter((ch in set(u) for u in uniques), dtype=bool)
        uniq_flags[:, j] = mask

    return {f"pattern_contains[{ch!r}]": uniq_flags[codes, j] for j, ch in enumerate(top_chars)}


def fd_violation_strategies(df: pd.DataFrame, target_column: str) -> dict[str, np.ndarray]:
    """Rule-violation (functional dependency) strategies ``s_{a->a'}`` (Section 4.1).

    For every other column ``a`` as a candidate left-hand side, flags cells
    in ``target_column`` whose ``a``-group contains more than one distinct
    ``target_column`` value -- the same "ambiguous LHS group" notion of an FD
    violation used by
    ``open_detect.algorithms.uni_detect.metrics.functional_dependency``.

    We follow Section 4.1's formal definition, which assigns strategy
    ``s_{a->a'}`` to the right-hand-side column ``a'`` (``j = index of a'``).
    The paper's earlier, illustrative Section 2.2 example instead shows both
    directions of a two-column FD marked against the *same* column's feature
    vector, which is inconsistent with that formal definition; we take the
    formal one as authoritative, consistent with this codebase's general
    approach to such paper inconsistencies (see
    ``open_detect/algorithms/uni_detect/metrics/functional_dependency.py``).
    """
    rhs_codes, rhs_uniques = _factorize_column(df[target_column])
    n_lhs = len(rhs_uniques)  # distinct target values = number of RHS buckets
    strategies: dict[str, np.ndarray] = {}

    for other in df.columns:
        if other == target_column:
            continue
        lhs_codes, _lhs_uniques = _factorize_column(df[other])
        n_rhs = n_lhs  # constant across iterations; kept explicit for clarity

        # A functional dependency holds iff each distinct LHS code maps to
        # exactly one RHS code. ``pair = lhs * n_rhs + rhs`` is a bijective
        # encoding of ordered pairs into ints; ``np.unique(pair)`` yields
        # sorted unique pairs, and ``up // n_rhs`` recovers the LHS code of
        # each unique pair. ``np.bincount`` then counts how many RHS values
        # appear with each LHS value.
        pair = lhs_codes * n_rhs + rhs_codes
        up = np.unique(pair)
        violating_lhs = np.bincount(up // n_rhs, minlength=n_lhs) > 1
        strategies[f"fd[{other}->{target_column}]"] = violating_lhs[lhs_codes]

    return strategies
