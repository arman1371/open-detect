"""Compatibility tests for the benchmark ``KnownIndexLabeler`` (Java-free).

The wiki_subset benchmark's synthetic targets carry ``injected_row_indices``
as *positional* indices, so the local ``KnownIndexLabeler`` must accept Raha's
optional third ``position`` argument (BUG-10) and still work when the detector
calls it with only ``(df, row_index)`` -- the two-argument form documented in
``docs/guides/custom-labelers.md``.
"""

from __future__ import annotations

import pandas as pd

from open_detect.algorithms.raha.labeling import Labeler


class KnownIndexLabeler(Labeler):
    """Local re-implementation of the labeler in ``run_benchmark.py``."""

    def __init__(self, target_column: str, injected_indices: set[int]) -> None:
        self._target_column = target_column
        self._injected_indices = injected_indices

    def label_tuple(self, df, row_index, position=None):
        key = position if position is not None else row_index
        is_error = key in self._injected_indices
        return {col: (is_error if col == self._target_column else False) for col in df.columns}


def test_two_argument_call_still_works():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    labeler = KnownIndexLabeler("a", {1})
    assert labeler.label_tuple(df, 1) == {"a": True, "b": False}
    assert labeler.label_tuple(df, 0) == {"a": False, "b": False}


def test_position_argument_takes_precedence():
    # On a non-default index the label and the position differ; the injected
    # indices are positional, so the labeler must use ``position`` when given.
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}, index=[10, 20, 30])
    labeler = KnownIndexLabeler("a", {1})
    assert labeler.label_tuple(df, 20, position=1) == {"a": True, "b": False}
    assert labeler.label_tuple(df, 10, position=0) == {"a": False, "b": False}


def test_callable_labeler_still_accepts_position_argument():
    # Regression: the Labeler interface gained a third ``position`` argument,
    # but a plain ``CallableLabeler`` callback written against the documented
    # two-argument contract must not break when the detector passes one.
    from open_detect.algorithms.raha.labeling import CallableLabeler

    def fn(df, row_index):
        return {"a": True}

    labeler = CallableLabeler(fn)
    df = pd.DataFrame({"a": [1, 2]})
    assert labeler.label_tuple(df, 0, position=0) == {"a": True}