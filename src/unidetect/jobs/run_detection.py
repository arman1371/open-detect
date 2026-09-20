"""Databricks Job entrypoint: online Uni-Detect error scanning.

Example:

    databricks bundle run run_detection_job -- \\
        --catalog main --schema data_quality \\
        --target-tables main.sales.orders,main.sales.customers \\
        --error-types uniqueness,numeric_outlier \\
        --write-results
"""

from __future__ import annotations

import argparse
import sys

from unidetect.config import UniDetectConfig, UnityCatalogLocation
from unidetect.core.enums import ErrorType
from unidetect.logging_utils import get_logger
from unidetect.pipeline import UniDetect
from unidetect.spark_utils import get_spark

logger = get_logger(__name__)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--catalog", required=True, help="Unity Catalog catalog holding unidetect's tables"
    )
    parser.add_argument(
        "--schema", required=True, help="Unity Catalog schema holding unidetect's tables"
    )
    parser.add_argument(
        "--target-tables",
        required=True,
        help="Comma-separated fully-qualified tables to scan for errors",
    )
    parser.add_argument(
        "--error-types",
        default=",".join(e.value for e in ErrorType),
        help="Comma-separated subset of: " + ",".join(e.value for e in ErrorType),
    )
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument(
        "--top-k", type=int, default=None, help="Only keep the top-K most surprising results"
    )
    parser.add_argument(
        "--write-results",
        action="store_true",
        help="Append results to the configured detections table",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    spark = get_spark()

    target_tables = [t.strip() for t in args.target_tables.split(",") if t.strip()]
    error_types = [ErrorType(e.strip()) for e in args.error_types.split(",") if e.strip()]

    config = UniDetectConfig(
        location=UnityCatalogLocation(catalog=args.catalog, schema=args.schema), alpha=args.alpha
    )
    ud = UniDetect(config, spark=spark)
    detections = ud.detect(target_tables, error_types=error_types)

    if args.top_k:
        detections = detections.limit(args.top_k)

    significant = detections.where("is_significant = true")
    logger.info(
        "Scanned %d table(s); %d significant detection(s) at alpha=%.3f",
        len(target_tables),
        significant.count(),
        args.alpha,
    )
    detections.show(truncate=80)

    if args.write_results:
        ud.write_detections(detections, mode="append")
        logger.info("Wrote results to %s", config.detections_fqn)


if __name__ == "__main__":  # pragma: no cover
    main(sys.argv[1:])
