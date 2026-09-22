"""Raha: A Configuration-Free Error Detection System (Mahdavi et al., SIGMOD 2019).

>>> from unidetect.algorithms.raha import RahaDetector, RahaConfig
>>> detector = RahaDetector(RahaConfig(labeling_budget=20))
>>> result = detector.detect(my_dataframe, table_id="orders")

See :mod:`unidetect.algorithms.raha.detector` for the full Algorithm-1
workflow and ``ARCHITECTURE.md`` for how each module maps onto the paper.
"""

from __future__ import annotations

from unidetect.algorithms.raha.config import RahaConfig
from unidetect.algorithms.raha.detector import RahaDetector
from unidetect.algorithms.raha.labeling import (
    CallableLabeler,
    GroundTruthLabeler,
    HeuristicLabeler,
    Labeler,
)

__all__ = [
    "CallableLabeler",
    "GroundTruthLabeler",
    "HeuristicLabeler",
    "Labeler",
    "RahaConfig",
    "RahaDetector",
]
