"""Uni-Detect (Wang & He, SIGMOD 2019): corpus-driven, Spark/Unity Catalog-native.

Public names are exported lazily so that ``import open_detect.algorithms.uni_detect``
(and anything that merely resolves its submodules, e.g. ``.config``) does not import
pyspark.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from open_detect.algorithms.uni_detect.algorithm import UniDetectAlgorithm
    from open_detect.algorithms.uni_detect.pipeline import UniDetect

__all__ = ["UniDetect", "UniDetectAlgorithm"]


def __getattr__(name: str) -> Any:
    if name == "UniDetect":
        from open_detect.algorithms.uni_detect.pipeline import UniDetect

        return UniDetect
    if name == "UniDetectAlgorithm":
        from open_detect.algorithms.uni_detect.algorithm import UniDetectAlgorithm

        return UniDetectAlgorithm
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
