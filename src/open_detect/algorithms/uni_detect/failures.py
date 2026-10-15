"""Executor-side failure accounting shared by the corpus builder and detectors.

Per-column scoring functions run inside ``mapInPandas`` on Spark executors.
A corpus/target column that legitimately cannot be scored (malformed values,
mismatched array lengths, a degenerate statistic) is skipped, but never
silently: each skip is counted in a driver-created Spark accumulator, and the
driver logs one WARNING summary and enforces
``UniDetectConfig.max_failure_ratio`` once the action has completed.

Only :data:`EXPECTED_ROW_ERRORS` are treated as skippable; anything else is a
bug and propagates, failing the Spark job.

Accumulator updates made inside transformations can over-count if a task is
retried or a stage recomputed (callers cache the result before the action to
avoid recomputation); the ratio is therefore approximate, which is adequate
for a quality gate.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, TypeVar

from open_detect.exceptions import DataQualityError, InsufficientDataError
from open_detect.logging_utils import get_logger

if TYPE_CHECKING:
    from pyspark import SparkContext

logger = get_logger(__name__)

T = TypeVar("T")

#: Exceptions a single corpus/target item may legitimately raise while being scored.
#: ``UnicodeError`` and ``json``/parse errors are ``ValueError`` subclasses;
#: ``ArithmeticError`` covers degenerate statistics (e.g. ``ZeroDivisionError``).
EXPECTED_ROW_ERRORS: tuple[type[Exception], ...] = (ValueError, KeyError, ArithmeticError)

#: Raised when an item simply has too little usable data to score (e.g. a text column
#: handed to the numeric-outlier metric). That is "not applicable", not a data-quality
#: failure, so it is counted separately and excluded from the failure ratio.
NOT_APPLICABLE_ERRORS: tuple[type[Exception], ...] = (InsufficientDataError,)

#: Upper bound on how many distinct exception type names a WARNING lists.
MAX_REPORTED_EXCEPTION_TYPES = 5


@dataclass
class FailureCounts:
    """Mutable counts of attempted / skipped items plus skipped exception types.

    ``processed`` counts items that were scored or failed (``skipped``);
    ``not_applicable`` items are tracked separately and excluded from the ratio.
    """

    processed: int = 0
    skipped: int = 0
    not_applicable: int = 0
    by_type: dict[str, int] = field(default_factory=dict)

    @property
    def failure_ratio(self) -> float:
        return self.skipped / self.processed if self.processed else 0.0

    def record_success(self) -> None:
        self.processed += 1

    def record_skip(self, exc: BaseException) -> None:
        self.processed += 1
        self.skipped += 1
        name = type(exc).__name__
        self.by_type[name] = self.by_type.get(name, 0) + 1

    def record_not_applicable(self) -> None:
        self.not_applicable += 1

    def merge(self, other: FailureCounts) -> None:
        self.processed += other.processed
        self.skipped += other.skipped
        self.not_applicable += other.not_applicable
        for name, n in other.by_type.items():
            self.by_type[name] = self.by_type.get(name, 0) + n

    def attempt(self, fn: Callable[..., T], /, *args: object, **kwargs: object) -> T | None:
        """Call ``fn``; count a success, or count and swallow an expected error.

        Returns ``None`` when the call was skipped. Exceptions outside
        :data:`EXPECTED_ROW_ERRORS` / :data:`NOT_APPLICABLE_ERRORS` propagate untouched.
        """
        try:
            result = fn(*args, **kwargs)
        except NOT_APPLICABLE_ERRORS:
            self.record_not_applicable()
            return None
        except EXPECTED_ROW_ERRORS as exc:
            self.record_skip(exc)
            return None
        self.record_success()
        return result


class FailureCountsAccumulatorParam:
    """Spark ``AccumulatorParam`` (duck-typed) that merges :class:`FailureCounts`."""

    def zero(self, value: FailureCounts) -> FailureCounts:  # noqa: ARG002
        return FailureCounts()

    def addInPlace(self, value1: FailureCounts, value2: FailureCounts) -> FailureCounts:  # noqa: N802
        value1.merge(value2)
        return value1


class FailureTracker:
    """Driver-created handle: executors ``flush`` local counts, the driver ``check``s them."""

    def __init__(self, spark_context: SparkContext, label: str, max_failure_ratio: float) -> None:
        self.label = label
        self.max_failure_ratio = max_failure_ratio
        # Duck-typed param: subclassing pyspark's AccumulatorParam would make pyspark a hard import.
        self._accumulator = spark_context.accumulator(
            FailureCounts(),
            FailureCountsAccumulatorParam(),  # type: ignore[arg-type]
        )

    def flush(self, counts: FailureCounts) -> None:
        """Executor side: add one batch's local counts to the accumulator."""
        self._accumulator.add(counts)

    def check(self) -> FailureCounts:
        """Driver side, after the action: log totals once and enforce the threshold."""
        counts = self._accumulator.value
        check_failure_threshold(counts, label=self.label, max_failure_ratio=self.max_failure_ratio)
        return counts


def check_failure_threshold(counts: FailureCounts, *, label: str, max_failure_ratio: float) -> None:
    """Log a single WARNING if anything was skipped; raise if the ratio is too high."""
    if counts.not_applicable:
        logger.info(
            "%s: %d items had too little data to score and were not counted as failures",
            label,
            counts.not_applicable,
        )
    if counts.skipped == 0:
        return
    top = sorted(counts.by_type.items(), key=lambda kv: (-kv[1], kv[0]))
    shown = ", ".join(f"{name}={n}" for name, n in top[:MAX_REPORTED_EXCEPTION_TYPES])
    if len(top) > MAX_REPORTED_EXCEPTION_TYPES:
        shown += f", ... (+{len(top) - MAX_REPORTED_EXCEPTION_TYPES} more types)"
    logger.warning(
        "%s: skipped %d of %d items (%.2f%%) that failed to score; exception types: %s",
        label,
        counts.skipped,
        counts.processed,
        100 * counts.failure_ratio,
        shown,
    )
    if counts.failure_ratio > max_failure_ratio:
        raise DataQualityError(
            f"{label}: {counts.skipped} of {counts.processed} items failed to score "
            f"({counts.failure_ratio:.2%}), above max_failure_ratio={max_failure_ratio:.2%}. "
            f"Exception types: {shown}"
        )
