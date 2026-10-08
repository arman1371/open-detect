"""Registry of pluggable error-detection algorithms.

>>> from open_detect.algorithms import list_algorithms, get_algorithm
>>> list_algorithms()
['raha', 'uni_detect']
>>> raha = get_algorithm("raha")          # open_detect.algorithms.raha.RahaDetector()
>>> result = raha.detect(my_dataframe, table_id="orders")
>>> result.errors()

See :mod:`open_detect.algorithms.base` for the shared :class:`ErrorDetectionAlgorithm`
contract and :mod:`open_detect.algorithms.registry` for how new algorithms (built-in
or third-party) get discovered.
"""

from __future__ import annotations

from open_detect.algorithms.base import AlgorithmResult, CellResult, ErrorDetectionAlgorithm
from open_detect.algorithms.registry import (
    UnknownAlgorithmError,
    get_algorithm,
    get_algorithm_class,
    list_algorithms,
    register_algorithm,
    register_lazy,
)


def _load_auto_validate() -> type[ErrorDetectionAlgorithm]:
    from open_detect.algorithms.auto_validate.detector import AutoValidateAlgorithm

    return AutoValidateAlgorithm


def _load_raha() -> type[ErrorDetectionAlgorithm]:
    from open_detect.algorithms.raha.detector import RahaDetector

    return RahaDetector


def _load_uni_detect() -> type[ErrorDetectionAlgorithm]:
    from open_detect.algorithms.uni_detect_algorithm import UniDetectAlgorithm

    return UniDetectAlgorithm


register_lazy("auto_validate", _load_auto_validate)
register_lazy("raha", _load_raha)
register_lazy("uni_detect", _load_uni_detect)

__all__ = [
    "AlgorithmResult",
    "CellResult",
    "ErrorDetectionAlgorithm",
    "UnknownAlgorithmError",
    "get_algorithm",
    "get_algorithm_class",
    "list_algorithms",
    "register_algorithm",
    "register_lazy",
]
