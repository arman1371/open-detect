"""unidetect: a library of pluggable, paper-backed error detection algorithms.

Multiple table error-detection algorithms live side by side here, each in its
own subpackage under ``unidetect.algorithms``, sharing a common result
contract (:class:`~unidetect.algorithms.base.AlgorithmResult`) so they can be
selected, compared, or extended uniformly:

- **Uni-Detect** (Wang & He, SIGMOD 2019) -- corpus-driven, Spark/Unity
  Catalog-native. See :class:`unidetect.pipeline.UniDetect`.
- **Raha** (Mahdavi et al., SIGMOD 2019) -- semi-supervised, single-table,
  pandas-native. See :class:`unidetect.algorithms.raha.RahaDetector`.

>>> from unidetect.algorithms import get_algorithm
>>> raha = get_algorithm("raha")
>>> result = raha.detect(my_dataframe, table_id="orders")

Third-party algorithms can register themselves via the ``unidetect.algorithms``
entry-point group -- see :mod:`unidetect.algorithms.registry`.
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
    "UniDetect",
    "get_algorithm",
    "list_algorithms",
]

__version__ = "0.2.0"


def __getattr__(name: str):
    # Lazy imports: unidetect.pipeline.UniDetect requires pyspark and
    # unidetect.algorithms.raha requires scikit-learn, both optional
    # dependencies the pure-Python core (metrics/featurization/enums) does
    # not need. Importing either eagerly here would break `import unidetect`
    # for users who only need one algorithm, or neither.
    if name == "UniDetect":
        from unidetect.pipeline import UniDetect

        return UniDetect
    if name in ("get_algorithm", "list_algorithms"):
        from unidetect import algorithms

        return getattr(algorithms, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
