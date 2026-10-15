"""open_detect: a library of pluggable, paper-backed error detection algorithms.

Multiple table error-detection algorithms live side by side here, each in its
own subpackage under ``open_detect.algorithms``, sharing a common result
contract (:class:`~open_detect.algorithms.base.AlgorithmResult`) so they can be
selected, compared, or extended uniformly:

- **Uni-Detect** (Wang & He, SIGMOD 2019) -- corpus-driven, Spark/Unity
  Catalog-native. See :class:`open_detect.algorithms.uni_detect.pipeline.UniDetect`.
- **Raha** (Mahdavi et al., SIGMOD 2019) -- semi-supervised, single-table,
  pandas-native. See :class:`open_detect.algorithms.raha.RahaDetector`.

>>> from open_detect.algorithms import get_algorithm
>>> raha = get_algorithm("raha")
>>> result = raha.detect(my_dataframe, table_id="orders")

Third-party algorithms can register themselves via the ``open_detect.algorithms``
entry-point group -- see :mod:`open_detect.algorithms.registry`.
"""

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _pkg_version

from open_detect.algorithms.uni_detect.config import UniDetectConfig, UnityCatalogLocation
from open_detect.core.enums import ColumnDataType, ComparisonDirection, ErrorType
from open_detect.core.models import Candidate, Detection, FeatureBucket, MetricObservation
from open_detect.exceptions import (
    ConfigurationError,
    CorpusNotFoundError,
    DataQualityError,
    IndexNotBuiltError,
    InsufficientDataError,
    OpenDetectError,
    UnityCatalogError,
    UnknownAlgorithmError,
    ValidationError,
)

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
    "UniDetect",
    "ConfigurationError",
    "CorpusNotFoundError",
    "DataQualityError",
    "IndexNotBuiltError",
    "InsufficientDataError",
    "OpenDetectError",
    "UnityCatalogError",
    "UnknownAlgorithmError",
    "ValidationError",
    "get_algorithm",
    "list_algorithms",
]

try:
    __version__ = _pkg_version("open-detect")
except PackageNotFoundError:  # source tree without install
    __version__ = "0+unknown"


def __getattr__(name: str):
    # Lazy imports: open_detect.algorithms.uni_detect.pipeline.UniDetect requires pyspark and
    # open_detect.algorithms.raha requires scikit-learn, both optional
    # dependencies the pure-Python core (metrics/featurization/enums) does
    # not need. Importing either eagerly here would break `import open_detect`
    # for users who only need one algorithm, or neither.
    if name == "UniDetect":
        from open_detect.algorithms.uni_detect.pipeline import UniDetect

        return UniDetect
    if name in ("get_algorithm", "list_algorithms"):
        from open_detect import algorithms

        return getattr(algorithms, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
