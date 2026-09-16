"""Uni-Detect: a unified, corpus-driven framework for automated error detection in tables.

Implementation of:
    Pei Wang and Yeye He. "Uni-Detect: A Unified Approach to Automated Error
    Detection in Tables." SIGMOD 2019.

The public entry point is :class:`unidetect.pipeline.UniDetect`.
"""

from unidetect.config import UniDetectConfig, UnityCatalogLocation
from unidetect.core.enums import ColumnDataType, ComparisonDirection, ErrorType
from unidetect.core.models import Candidate, Detection, FeatureBucket, MetricObservation

__all__ = [
    "ColumnDataType",
    "ComparisonDirection",
    "ErrorType",
    "Candidate",
    "Detection",
    "FeatureBucket",
    "MetricObservation",
    "UniDetectConfig",
    "UnityCatalogLocation",
]

__version__ = "0.1.0"


def __getattr__(name: str):
    # Lazy import: unidetect.pipeline.UniDetect requires pyspark, which is an
    # optional dependency (the pure-Python metrics/featurization modules do
    # not). Importing it eagerly here would break `import unidetect` for
    # users who only need the metric functions.
    if name == "UniDetect":
        from unidetect.pipeline import UniDetect

        return UniDetect
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
