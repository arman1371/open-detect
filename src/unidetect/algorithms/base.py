"""Algorithm-agnostic contract every registered error-detection algorithm implements.

This package turns ``unidetect`` from a single-paper implementation into a
library of interchangeable error-detection algorithms: :class:`~unidetect.pipeline.UniDetect`
(Wang & He, SIGMOD'19) and Raha (Mahdavi et al., SIGMOD'19) today, more in the
future. The two papers have genuinely different operating models -- Uni-Detect
scores tables already registered in Unity Catalog against a large background
corpus via a distributed offline/online split, while Raha trains one
classifier per column of a single in-memory table from a handful of user
labels. :class:`ErrorDetectionAlgorithm` does not try to paper over that
difference: it only fixes the *output* contract (:class:`AlgorithmResult`), so
results from different algorithms can be compared, unioned, or displayed
uniformly regardless of how each algorithm computes them. Each algorithm's
``detect`` signature documents its own expected input shape.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, ClassVar

if TYPE_CHECKING:
    import pandas as pd

#: Columns of the flattened, algorithm-agnostic cell-level result table.
CELL_RESULT_COLUMNS = (
    "table_id",
    "row_index",
    "column_name",
    "algorithm",
    "is_error",
    "score",
    "evidence",
)


@dataclass(frozen=True, slots=True)
class CellResult:
    """A single (row, column) cell's verdict from one algorithm.

    ``score`` is algorithm-specific in scale and direction (e.g. Uni-Detect's
    surprisal is unbounded and higher-is-worse, Raha's is a classifier
    probability in ``[0, 1]``) -- it is meant for *within-algorithm* ranking,
    not for comparing raw scores across algorithms. ``is_error`` is the
    normalized, comparable signal.
    """

    table_id: str
    row_index: Any
    column_name: str
    algorithm: str
    is_error: bool
    score: float
    evidence: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "table_id": self.table_id,
            "row_index": self.row_index,
            "column_name": self.column_name,
            "algorithm": self.algorithm,
            "is_error": self.is_error,
            "score": self.score,
            "evidence": self.evidence,
        }


@dataclass(frozen=True, slots=True)
class AlgorithmResult:
    """The common return type of every :meth:`ErrorDetectionAlgorithm.detect` call."""

    algorithm: str
    cells: tuple[CellResult, ...]

    def __len__(self) -> int:
        return len(self.cells)

    def __iter__(self):
        return iter(self.cells)

    def errors(self) -> tuple[CellResult, ...]:
        """Cells flagged ``is_error`` (the normalized, cross-algorithm signal)."""
        return tuple(c for c in self.cells if c.is_error)

    def to_pandas(self) -> pd.DataFrame:
        """Flatten to the shared cell-level schema (:data:`CELL_RESULT_COLUMNS`)."""
        import pandas as pd

        return pd.DataFrame([c.to_dict() for c in self.cells], columns=list(CELL_RESULT_COLUMNS))

    @classmethod
    def union(cls, results: list[AlgorithmResult], algorithm: str = "ensemble") -> AlgorithmResult:
        """Concatenate several algorithms' results into one comparable result set."""
        cells = tuple(cell for result in results for cell in result.cells)
        return cls(algorithm=algorithm, cells=cells)


class ErrorDetectionAlgorithm(ABC):
    """Base class every registered error-detection algorithm subclasses.

    Subclasses declare a unique :attr:`name` (the registry key, e.g.
    ``"raha"``) and implement :meth:`detect`. Construction is algorithm-owned
    -- pass whatever configuration object the algorithm needs (e.g.
    ``RahaConfig``, ``UniDetectConfig``) to ``__init__``.
    """

    name: ClassVar[str]

    @abstractmethod
    def detect(self, data: Any, *, table_id: str = "table", **kwargs: Any) -> AlgorithmResult:
        """Run this algorithm and return a normalized :class:`AlgorithmResult`.

        Parameters
        ----------
        data:
            Algorithm-specific input (a ``pandas.DataFrame`` for a
            single-table algorithm like Raha, a sequence of Unity Catalog
            table names for a corpus-driven algorithm like Uni-Detect). See
            the concrete subclass's docstring for what it expects.
        table_id:
            Identifier stamped onto every result cell. Ignored by algorithms
            (like Uni-Detect) whose input already carries its own table
            identity.
        """
