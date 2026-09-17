"""Runs the WIKI-subset benchmark: builds corpus statistics from
``benchmarks/data/wiki_subset/corpus`` and scores the labeled targets in
``benchmarks/data/wiki_subset/eval/targets.json`` against their known ground
truth (see ``benchmarks/README.md`` for the full picture).

Usage::

    uv run python benchmarks/run_benchmark.py
    uv run python benchmarks/run_benchmark.py --update-baseline

Writes ``benchmarks/results/latest.json`` and, when a baseline exists,
prints a version-over-version comparison (also appended to
``$GITHUB_STEP_SUMMARY`` when running in GitHub Actions).
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

BENCHMARK_DIR = Path(__file__).parent
REPO_ROOT = BENCHMARK_DIR.parent
DATA_DIR = BENCHMARK_DIR / "data" / "wiki_subset"
CORPUS_DIR = DATA_DIR / "corpus"
TARGETS_FILE = DATA_DIR / "eval" / "targets.json"
RESULTS_DIR = BENCHMARK_DIR / "results"
BASELINE_FILE = RESULTS_DIR / "baseline.json"
LATEST_FILE = RESULTS_DIR / "latest.json"

TEST_CATALOG = "spark_catalog"
TEST_SCHEMA = "unidetect_benchmark"

ERROR_TYPES = [
    "uniqueness",
    "numeric_outlier",
    "spelling",
    "functional_dependency",
]


class SparkUnavailable(Exception):
    """Raised only when a local Delta-enabled Spark session cannot be started at all.

    Kept narrow and distinct from any other exception so that a real failure
    *during* the benchmark (a bad detector result, an OOM, a bug) fails the
    script loudly instead of being swallowed as if the environment simply
    lacked Spark/Delta -- see ``main()``.
    """


def _git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], cwd=REPO_ROOT, text=True
        ).strip()
    except Exception:  # noqa: BLE001
        return "unknown"


@contextmanager
def _spark_session() -> Iterator[Any]:
    os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
    os.environ.setdefault("PYSPARK_DRIVER_PYTHON", sys.executable)

    from delta import configure_spark_with_delta_pip
    from pyspark.sql import SparkSession

    warehouse_dir = tempfile.mkdtemp(prefix="unidetect-benchmark-warehouse-")
    builder = (
        SparkSession.builder.master("local[2]")
        .appName("unidetect-benchmark")
        .config("spark.sql.warehouse.dir", warehouse_dir)
        .config("spark.sql.shuffle.partitions", "2")
        .config("spark.ui.enabled", "false")
        # Default driver heap is too small for this benchmark's run:
        # unidetect.corpus.store.CorpusStatsStore.load_token_stats_map()
        # calls `.orderBy(...).limit(max_tokens)` with a default
        # max_tokens of 5,000,000, and Spark's TakeOrderedAndProjectExec
        # pre-sizes an ordering buffer proportional to that limit
        # regardless of the token table's actual (tiny) size -- an
        # OutOfMemoryError on the default heap, not a sign of anything
        # wrong with this benchmark's data or config.
        .config("spark.driver.memory", "3g")
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
    )
    try:
        session = configure_spark_with_delta_pip(builder).getOrCreate()
        session.sparkContext.setLogLevel("ERROR")
        session.sql(f"CREATE NAMESPACE IF NOT EXISTS {TEST_CATALOG}.{TEST_SCHEMA}")
    except Exception as exc:  # noqa: BLE001
        shutil.rmtree(warehouse_dir, ignore_errors=True)
        raise SparkUnavailable(str(exc)) from exc

    try:
        yield session
    finally:
        session.stop()
        shutil.rmtree(warehouse_dir, ignore_errors=True)


def _load_corpus_tables(spark, error_type: str) -> list[str]:
    import csv as csv_module

    fqns: list[str] = []
    category_dir = CORPUS_DIR / error_type
    for csv_path in sorted(category_dir.glob("*.csv")):
        with csv_path.open(newline="", encoding="utf-8") as fh:
            reader = csv_module.reader(fh)
            header = next(reader)
            rows = [tuple(row) for row in reader]
        table_name = csv_path.stem
        fqn = f"{TEST_CATALOG}.{TEST_SCHEMA}.corpus_{error_type}_{table_name}"
        df = spark.createDataFrame(rows, schema=header)
        if error_type == "numeric_outlier":
            from pyspark.sql import functions as F

            df = df.withColumn(header[0], F.col(header[0]).cast("double"))
        df.write.format("delta").mode("overwrite").saveAsTable(fqn)
        fqns.append(fqn)
    return fqns


def _load_targets(spark) -> list[dict]:
    targets = json.loads(TARGETS_FILE.read_text())
    for target in targets:
        fqn = f"{TEST_CATALOG}.{TEST_SCHEMA}.target_{target['id']}"
        df = spark.createDataFrame([tuple(r) for r in target["rows"]], schema=target["columns"])
        if target["error_type"] == "numeric_outlier":
            from pyspark.sql import functions as F

            col = target["columns"][0]
            df = df.withColumn(col, F.col(col).cast("double"))
        df.write.format("delta").mode("overwrite").saveAsTable(fqn)
        target["_fqn"] = fqn
    return targets


def _build_config(uc_location):
    from unidetect.config import UniDetectConfig

    return UniDetectConfig(
        location=uc_location,
        epsilon=0.05,
        alpha=0.2,
        max_mpd_block_size=200,
        max_fd_column_pairs_per_table=10,
        # Scaled down from the web-scale defaults to match this benchmark's
        # tens-of-tables corpus, the same reasoning
        # ``tests/test_corpus_and_detectors.py::config`` documents.
        prevalence_edges=(2, 5, 20, 100, 1000),
    )


def _confusion_metrics(rows: list[dict]) -> dict:
    tp = sum(1 for r in rows if r["expected_significant"] and r["predicted_significant"])
    fp = sum(1 for r in rows if not r["expected_significant"] and r["predicted_significant"])
    fn = sum(1 for r in rows if r["expected_significant"] and not r["predicted_significant"])
    tn = sum(1 for r in rows if not r["expected_significant"] and not r["predicted_significant"])
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0.0
    accuracy = (tp + tn) / len(rows) if rows else 0.0
    return {
        "n": len(rows),
        "true_positive": tp,
        "false_positive": fp,
        "false_negative": fn,
        "true_negative": tn,
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
        "accuracy": round(accuracy, 4),
    }


def run() -> dict:
    from unidetect.config import UnityCatalogLocation
    from unidetect.core.enums import ErrorType
    from unidetect.pipeline import UniDetect

    uc_location = UnityCatalogLocation(catalog=TEST_CATALOG, schema=TEST_SCHEMA)
    config = _build_config(uc_location)

    with _spark_session() as spark:
        ud = UniDetect(config, spark=spark)
        targets = _load_targets(spark)

        for error_type in ERROR_TYPES:
            corpus_tables = _load_corpus_tables(spark, error_type)
            ud.build_corpus_statistics(
                corpus_tables,
                error_types=[ErrorType(error_type)],
                create_schema=False,
            )

        target_rows: list[dict] = []
        for error_type in ERROR_TYPES:
            type_targets = [t for t in targets if t["error_type"] == error_type]
            if not type_targets:
                continue
            fqns = [t["_fqn"] for t in type_targets]
            result = ud.detect(fqns, error_types=[ErrorType(error_type)]).toPandas()
            for target in type_targets:
                rows = result[result["table_id"] == target["_fqn"]]
                predicted_significant = (
                    bool(rows["is_significant"].any()) if not rows.empty else False
                )
                lr_ratio = float(rows["lr_ratio"].min()) if not rows.empty else None
                target_rows.append(
                    {
                        "id": target["id"],
                        "error_type": error_type,
                        "description": target["description"],
                        "expected_significant": target["expected_significant"],
                        "predicted_significant": predicted_significant,
                        "lr_ratio": lr_ratio,
                    }
                )

    overall = _confusion_metrics(target_rows)
    by_type = {
        error_type: _confusion_metrics([r for r in target_rows if r["error_type"] == error_type])
        for error_type in ERROR_TYPES
    }

    ranking: dict[str, dict] = {}
    for error_type in ERROR_TYPES:
        type_rows = [r for r in target_rows if r["error_type"] == error_type]
        tp_rows = [r for r in type_rows if r["expected_significant"] and r["lr_ratio"] is not None]
        fp_rows = [
            r for r in type_rows if not r["expected_significant"] and r["lr_ratio"] is not None
        ]
        if tp_rows and fp_rows:
            tp_ratio = min(r["lr_ratio"] for r in tp_rows)
            fp_ratio = min(r["lr_ratio"] for r in fp_rows)
            ranking[error_type] = {
                "true_positive_lr_ratio": tp_ratio,
                "false_positive_lr_ratio": fp_ratio,
                "correctly_ranked": tp_ratio < fp_ratio,
            }

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "git_commit": _git_commit(),
        "dataset": "wiki_subset",
        "targets": target_rows,
        "metrics": {
            "overall": overall,
            "by_error_type": by_type,
            "ranking": ranking,
        },
    }


def _print_comparison(current: dict, baseline: dict | None) -> str:
    lines = ["## WIKI-subset benchmark results", ""]
    lines.append(f"Commit: `{current['git_commit']}`  ")
    if baseline:
        lines.append(f"Baseline commit: `{baseline.get('git_commit', 'unknown')}`")
    lines.append("")
    header = "| Metric | Current | Baseline | Delta |" if baseline else "| Metric | Current |"
    sep = "|---|---|---|---|" if baseline else "|---|---|"
    lines.append(header)
    lines.append(sep)

    def _row(label: str, cur_metrics: dict, base_metrics: dict | None) -> None:
        for key in ("precision", "recall", "f1", "accuracy"):
            cur_val = cur_metrics.get(key, 0.0)
            if baseline and base_metrics is not None:
                base_val = base_metrics.get(key, 0.0)
                delta = cur_val - base_val
                arrow = "▲" if delta > 1e-9 else ("▼" if delta < -1e-9 else "=")
                lines.append(
                    f"| {label} {key} | {cur_val:.3f} | {base_val:.3f} | {arrow} {delta:+.3f} |"
                )
            else:
                lines.append(f"| {label} {key} | {cur_val:.3f} |")

    base_overall = baseline["metrics"]["overall"] if baseline else None
    _row("overall", current["metrics"]["overall"], base_overall)
    for error_type in ERROR_TYPES:
        cur = current["metrics"]["by_error_type"].get(error_type, {})
        base = baseline["metrics"]["by_error_type"].get(error_type) if baseline else None
        _row(error_type, cur, base)

    lines.append("")
    lines.append("| Error type | correctly ranked (TP more surprising than FP) |")
    lines.append("|---|---|")
    for error_type, info in current["metrics"]["ranking"].items():
        lines.append(f"| {error_type} | {'yes' if info['correctly_ranked'] else 'NO'} |")

    text = "\n".join(lines)
    print(text)
    return text


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--update-baseline",
        action="store_true",
        help="Overwrite benchmarks/results/baseline.json with this run's results.",
    )
    args = parser.parse_args()

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    try:
        import delta  # noqa: F401
        import pyspark  # noqa: F401
    except ImportError:
        print(
            "pyspark/delta-spark not installed; skipping benchmark "
            "(run `uv sync` or `uv sync --group dev` first).",
            file=sys.stderr,
        )
        sys.exit(0)

    try:
        results = run()
    except SparkUnavailable as exc:
        print(f"Could not start a local Delta-enabled Spark session; skipping: {exc}")
        sys.exit(0)

    LATEST_FILE.write_text(json.dumps(results, indent=2) + "\n")

    baseline = json.loads(BASELINE_FILE.read_text()) if BASELINE_FILE.exists() else None
    summary = _print_comparison(results, baseline)

    step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if step_summary:
        with open(step_summary, "a", encoding="utf-8") as fh:
            fh.write(summary + "\n")

    if args.update_baseline:
        BASELINE_FILE.write_text(json.dumps(results, indent=2) + "\n")
        print(f"\nUpdated {BASELINE_FILE}")


if __name__ == "__main__":
    main()
