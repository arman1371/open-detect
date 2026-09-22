"""Feature vector generation (paper Section 4.2).

Combines every strategy family's output into one feature matrix per column,
``V_j`` in the paper's notation -- one row per data cell, one column per
error detection strategy that applies to that column.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from unidetect.algorithms.raha.config import RahaConfig
from unidetect.algorithms.raha.strategies import (
    fd_violation_strategies,
    gaussian_outlier_strategies,
    histogram_outlier_strategies,
    pattern_character_strategies,
)


@dataclass(frozen=True, slots=True)
class ColumnFeatures:
    """A single column's feature matrix ``V_j`` and the strategy each column came from."""

    column_name: str
    feature_names: tuple[str, ...]
    matrix: np.ndarray  # shape (n_rows, n_features), dtype=float64, values in {0.0, 1.0}


def build_column_features(df: pd.DataFrame, column_name: str, config: RahaConfig) -> ColumnFeatures:
    """Run every applicable strategy family on ``column_name`` and assemble ``V_j``.

    Constant columns (a strategy that fires on every cell, or none) are
    dropped, per the paper's post-processing step: "we post-process the
    feature vectors of each data column to remove non-informative features
    that are constant for all the data cells of the data column" (Section 4.2).
    """
    values = df[column_name]
    strategies: dict[str, np.ndarray] = {}
    strategies.update(histogram_outlier_strategies(values, config.tf_thresholds))
    strategies.update(gaussian_outlier_strategies(values, config.dist_thresholds))
    strategies.update(pattern_character_strategies(values, config.max_pattern_characters))
    strategies.update(fd_violation_strategies(df, column_name))

    n = len(df)
    names: list[str] = []
    columns: list[np.ndarray] = []
    for name, flags in strategies.items():
        if flags.any() and not flags.all():
            names.append(name)
            columns.append(flags)

    matrix = (
        np.column_stack(columns).astype(np.float64)
        if columns
        else np.zeros((n, 0), dtype=np.float64)
    )
    return ColumnFeatures(column_name=column_name, feature_names=tuple(names), matrix=matrix)


def build_all_features(df: pd.DataFrame, config: RahaConfig) -> dict[str, ColumnFeatures]:
    """:func:`build_column_features` for every column of ``df``."""
    return {col: build_column_features(df, col, config) for col in df.columns}
