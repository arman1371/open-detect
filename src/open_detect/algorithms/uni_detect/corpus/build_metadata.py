"""Persist and verify the build-time configuration of the corpus-statistics table.

Epsilon and the bucket edges are baked into the materialized statistics, so
detecting with a different value silently compares apples to oranges. The
builder therefore records :meth:`UniDetectConfig.build_fingerprint` as a Delta
table property (one per error type, since error types are rebuilt
independently) and the store compares it against the active config on load.
"""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

from open_detect.exceptions import ConfigurationError
from open_detect.logging_utils import get_logger

if TYPE_CHECKING:
    from collections.abc import Iterable

    from pyspark.sql import SparkSession

    from open_detect.algorithms.uni_detect.config import UniDetectConfig
    from open_detect.core.enums import ErrorType

logger = get_logger(__name__)

PROPERTY_PREFIX = "open_detect.build_config."

#: Recorded for reference but applied at scoring time, not baked into the
#: stored statistics, so a difference is logged rather than rejected.
_SCORING_TIME_FIELDS = frozenset({"laplace_smoothing"})


def property_key(error_type: ErrorType) -> str:
    return f"{PROPERTY_PREFIX}{error_type.value}"


def diff_fingerprints(persisted: dict[str, Any], active: dict[str, Any]) -> dict[str, tuple]:
    """Return ``{field: (persisted_value, active_value)}`` for every differing field."""
    return {
        name: (persisted.get(name), active.get(name))
        for name in sorted(persisted.keys() | active.keys())
        if persisted.get(name) != active.get(name)
    }


def write_build_config(
    spark: SparkSession, table_fqn: str, error_types: Iterable[ErrorType], config: UniDetectConfig
) -> None:
    """Record ``config``'s fingerprint on ``table_fqn`` for each rebuilt error type."""
    payload = json.dumps(config.build_fingerprint(), sort_keys=True)
    assignments = ", ".join(f"'{property_key(et)}' = '{payload}'" for et in error_types)
    if assignments:
        spark.sql(f"ALTER TABLE {table_fqn} SET TBLPROPERTIES ({assignments})")


def read_build_config(
    spark: SparkSession, table_fqn: str, error_type: ErrorType
) -> dict[str, Any] | None:
    """Return the persisted fingerprint for ``error_type``, or ``None`` for legacy corpora."""
    key = property_key(error_type)
    for row in spark.sql(f"SHOW TBLPROPERTIES {table_fqn}").collect():
        if row["key"] == key:
            try:
                return json.loads(row["value"])
            except ValueError:
                logger.warning(
                    "Property %s on %s is not valid JSON (possibly redacted by Spark); "
                    "treating the corpus as having no persisted build configuration.",
                    key,
                    table_fqn,
                )
                return None
    return None


def verify_build_config(
    spark: SparkSession, table_fqn: str, error_type: ErrorType, config: UniDetectConfig
) -> None:
    """Raise :class:`ConfigurationError` if the corpus was built with an incompatible config."""
    persisted = read_build_config(spark, table_fqn, error_type)
    if persisted is None:
        logger.warning(
            "Corpus statistics %s (%s) carry no persisted build configuration (legacy corpus); "
            "cannot verify epsilon/bucket edges match. Rebuild the corpus to record them.",
            table_fqn,
            error_type.value,
        )
        return

    differing = diff_fingerprints(persisted, config.build_fingerprint())
    for name in _SCORING_TIME_FIELDS & differing.keys():
        built, active = differing.pop(name)
        logger.warning(
            "%s differs from the corpus build value (built=%r, active=%r); it is applied at "
            "scoring time so detection proceeds.",
            name,
            built,
            active,
        )
    if not differing:
        return

    details = "; ".join(
        f"{name}: built with {built!r}, active {active!r}"
        for name, (built, active) in differing.items()
    )
    message = (
        f"Corpus statistics {table_fqn!r} ({error_type.value}) were built with a different "
        f"configuration than the active detection config ({details}). Rebuild the corpus or "
        "align the detection settings."
    )
    if config.allow_corpus_config_mismatch:
        logger.warning("%s Proceeding because allow_corpus_config_mismatch is set.", message)
        return
    raise ConfigurationError(message)
