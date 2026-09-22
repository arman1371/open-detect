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
``unidetect/metrics/functional_dependency.py`` for the Uni-Detect paper.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterable

import numpy as np
import pandas as pd

from unidetect.text_utils import is_float_like

NULL_SENTINEL = "__unidetect_raha_null__"


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


def histogram_outlier_strategies(
    values: pd.Series, thresholds: Iterable[float]
) -> dict[str, np.ndarray]:
    """Histogram-modeling outlier strategies ``s_tf`` (Section 4.1).

    Flags a cell when its value's relative frequency in the column falls
    below ``tf`` -- i.e. it is a comparatively rare value.
    """
    raw = normalize_to_str(values)
    n = len(raw)
    if n == 0:
        return {}
    counts = raw.value_counts()
    freq = (raw.map(counts) / n).to_numpy()
    return {f"outlier_tf<{t}": freq < t for t in thresholds}


def gaussian_outlier_strategies(
    values: pd.Series, thresholds: Iterable[float]
) -> dict[str, np.ndarray]:
    """Gaussian-modeling outlier strategies ``s_dist`` (Section 4.1).

    Applies only to (mostly) numeric columns -- returns no strategies
    otherwise, since "distance to the mean in standard deviations" is not
    meaningful for non-numeric data. Cells that fail to parse as numeric are
    left unflagged by this family (the pattern-violation strategies below
    already expose non-numeric characters in an otherwise-numeric column).
    """
    raw = values.astype(str)
    parseable = raw.map(is_float_like)
    if parseable.mean() < 0.5:
        return {}

    numeric = pd.to_numeric(raw.where(parseable), errors="coerce")
    if numeric.count() < 2:
        return {}

    mean = numeric.mean()
    std = numeric.std(ddof=0)
    if not std:
        return {f"outlier_dist>{t}": np.zeros(len(values), dtype=bool) for t in thresholds}

    z = ((numeric - mean).abs() / std).fillna(0.0).to_numpy()
    return {f"outlier_dist>{t}": z > t for t in thresholds}


def pattern_character_strategies(values: pd.Series, max_characters: int) -> dict[str, np.ndarray]:
    """Bag-of-characters pattern-violation strategies ``s_ch`` (Section 4.1).

    One strategy per distinct character observed in the column, flagging
    cells that contain it -- e.g. a stray "-" in an otherwise digit-only
    column. ``max_characters`` bounds this to the most frequent characters so
    a free-text column does not explode the feature space.
    """
    raw = normalize_to_str(values)
    char_counts: dict[str, int] = defaultdict(int)
    per_row_chars = [set(s) for s in raw]
    for chars in per_row_chars:
        for ch in chars:
            char_counts[ch] += 1

    top_chars = sorted(char_counts, key=lambda ch: (-char_counts[ch], ch))[:max_characters]
    return {
        f"pattern_contains[{ch!r}]": np.array([ch in chars for chars in per_row_chars], dtype=bool)
        for ch in top_chars
    }


def fd_violation_strategies(df: pd.DataFrame, target_column: str) -> dict[str, np.ndarray]:
    """Rule-violation (functional dependency) strategies ``s_{a->a'}`` (Section 4.1).

    For every other column ``a`` as a candidate left-hand side, flags cells
    in ``target_column`` whose ``a``-group contains more than one distinct
    ``target_column`` value -- the same "ambiguous LHS group" notion of an FD
    violation used by ``unidetect.metrics.functional_dependency``.

    We follow Section 4.1's formal definition, which assigns strategy
    ``s_{a->a'}`` to the right-hand-side column ``a'`` (``j = index of a'``).
    The paper's earlier, illustrative Section 2.2 example instead shows both
    directions of a two-column FD marked against the *same* column's feature
    vector, which is inconsistent with that formal definition; we take the
    formal one as authoritative, consistent with this codebase's general
    approach to such paper inconsistencies (see
    ``unidetect/metrics/functional_dependency.py``).
    """
    target_raw = normalize_to_str(df[target_column]).to_numpy()
    strategies: dict[str, np.ndarray] = {}
    for other in df.columns:
        if other == target_column:
            continue
        lhs_raw = normalize_to_str(df[other]).to_numpy()
        groups: dict[str, set[str]] = defaultdict(set)
        for lhs_v, rhs_v in zip(lhs_raw, target_raw, strict=True):
            groups[lhs_v].add(rhs_v)
        flags = np.array([len(groups[lhs_v]) > 1 for lhs_v in lhs_raw], dtype=bool)
        strategies[f"fd[{other}->{target_column}]"] = flags
    return strategies
