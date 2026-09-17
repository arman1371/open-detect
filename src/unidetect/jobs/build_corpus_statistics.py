"""Databricks Job entrypoint: offline Uni-Detect corpus-statistics build.

Intended to run as a Python-file/wheel task on a Databricks Job (see
``databricks.yml``). Example:

    databricks bundle run build_corpus_statistics_job -- \\
        --catalog main --schema data_quality \\
        --corpus-catalog main --corpus-schemas sales,marketing \\
        --error-types uniqueness,numeric_outlier,spelling,functional_dependency

If ``--corpus-tables`` is omitted, every table across ``--corpus-schemas``
(or every schema in ``--corpus-catalog`` if that is also omitted) is used as
the background corpus ``T`` -- i.e. "everything this catalog already
governs" (see ``unidetect/catalog.py::list_tables_matching``).
"""

from __future__ import annotations

import argparse
import sys

from unidetect.catalog import list_tables_matching
from unidetect.config import UniDetectConfig, UnityCatalogLocation
from unidetect.core.enums import ErrorType
from unidetect.logging_utils import get_logger
from unidetect.pipeline import UniDetect
from unidetect.spark_utils import get_spark

logger = get_logger(__name__)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--catalog", required=True, help="Unity Catalog catalog for unidetect's own tables"
    )
    parser.add_argument(
        "--schema", required=True, help="Unity Catalog schema for unidetect's own tables"
    )
    parser.add_argument(
        "--corpus-tables",
        default=None,
        help="Comma-separated list of fully-qualified table names to use as the corpus. "
        "If omitted, --corpus-catalog/--corpus-schemas are scanned instead.",
    )
    parser.add_argument("--corpus-catalog", default=None, help="Catalog to scan for corpus tables")
    parser.add_argument(
        "--corpus-schemas",
        default=None,
        help="Comma-separated schemas within --corpus-catalog to scan",
    )
    parser.add_argument(
        "--error-types",
        default=",".join(e.value for e in ErrorType),
        help="Comma-separated subset of: " + ",".join(e.value for e in ErrorType),
    )
    parser.add_argument("--epsilon", type=float, default=0.01)
    parser.add_argument("--alpha", type=float, default=0.05)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    spark = get_spark()

    if args.corpus_tables:
        corpus_tables = [t.strip() for t in args.corpus_tables.split(",") if t.strip()]
    else:
        if not args.corpus_catalog:
            raise SystemExit("Either --corpus-tables or --corpus-catalog must be provided")
        schemas = (
            [s.strip() for s in args.corpus_schemas.split(",")] if args.corpus_schemas else None
        )
        corpus_tables = list_tables_matching(spark, args.corpus_catalog, schemas)

    if not corpus_tables:
        raise SystemExit("No corpus tables resolved; nothing to build statistics from.")

    error_types = [ErrorType(e.strip()) for e in args.error_types.split(",") if e.strip()]

    config = UniDetectConfig(
        location=UnityCatalogLocation(catalog=args.catalog, schema=args.schema),
        epsilon=args.epsilon,
        alpha=args.alpha,
    )
    logger.info(
        "Building corpus statistics for %d tables, error types=%s -> %s",
        len(corpus_tables),
        [e.value for e in error_types],
        config.corpus_stats_fqn,
    )
    ud = UniDetect(config, spark=spark)
    ud.build_corpus_statistics(corpus_tables, error_types=error_types)
    logger.info("Done.")


if __name__ == "__main__":
    main(sys.argv[1:])
