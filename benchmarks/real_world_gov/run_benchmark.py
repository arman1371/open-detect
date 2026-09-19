"""Runs the real_world_gov benchmark: builds corpus statistics from the
*clean* version of 5 real government open-data tables (see ``README.md``)
and scores UniDetect's detections on their *dirty* (really-corrupted)
counterparts against ``clean_changes.csv``'s cell-level ground truth.

Usage::

    uv run python benchmarks/real_world_gov/run_benchmark.py
    uv run python benchmarks/real_world_gov/run_benchmark.py --update-baseline

Writes ``results/latest.json`` and, when a baseline exists, prints a
version-over-version comparison (also appended to ``$GITHUB_STEP_SUMMARY``
when running in GitHub Actions). Requires JDK 17 locally, same as
``benchmarks/run_benchmark.py`` -- see that script's module docstring and
this benchmark's ``README.md`` for why (and how ``results/baseline.json``
was produced without it).
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

BENCHMARK_DIR = Path(__file__).parent
REPO_ROOT = BENCHMARK_DIR.parent.parent

sys.path.insert(0, str(REPO_ROOT / "benchmarks"))
sys.path.insert(0, str(BENCHMARK_DIR))
from dataset_utils import DATASETS, dataset_paths, load_changes, load_csv  # noqa: E402

from common.metrics import confusion_metrics  # noqa: E402
from common.spark_session import SparkUnavailable, git_commit, spark_session  # noqa: E402

RESULTS_DIR = BENCHMARK_DIR / "results"
BASELINE_FILE = RESULTS_DIR / "baseline.json"
LATEST_FILE = RESULTS_DIR / "latest.json"

TEST_CATALOG = "spark_catalog"
TEST_SCHEMA = "unidetect_benchmark_real"


def _build_config(uc_location):
    from unidetect.config import UniDetectConfig

    return UniDetectConfig(
        location=uc_location,
        # Same values as benchmarks/run_benchmark.py's wiki_subset config,
        # for the same reason: this benchmark's background corpus is a
        # handful of small real tables, not the paper's web-scale crawl.
        epsilon=0.05,
        alpha=0.2,
        max_mpd_block_size=200,
        max_fd_column_pairs_per_table=200,
        prevalence_edges=(2, 5, 20, 100, 1000),
    )


def _register_table(spark, fqn: str, header: list[str], rows: list[list]):
    df = spark.createDataFrame([tuple(row) for row in rows], schema=header)
    df.write.format("delta").mode("overwrite").saveAsTable(fqn)


def run() -> dict:
    from unidetect.config import UnityCatalogLocation
    from unidetect.core.enums import ErrorType
    from unidetect.pipeline import UniDetect

    uc_location = UnityCatalogLocation(catalog=TEST_CATALOG, schema=TEST_SCHEMA)
    config = _build_config(uc_location)

    with spark_session(TEST_CATALOG, TEST_SCHEMA) as spark:
        ud = UniDetect(config, spark=spark)

        clean_fqns: dict[str, str] = {}
        dirty_fqns: dict[str, str] = {}
        error_counts: dict[str, dict[str, int]] = {}
        num_rows_by_dataset: dict[str, int] = {}
        headers: dict[str, list[str]] = {}

        for name in DATASETS:
            clean_path, dirty_path, changes_path = dataset_paths(name)
            clean_header, clean_rows = load_csv(clean_path)
            dirty_header, dirty_rows = load_csv(dirty_path)
            assert clean_header == dirty_header

            clean_fqn = f"{TEST_CATALOG}.{TEST_SCHEMA}.clean_{name}".replace("-", "_").replace(
                ".", "_"
            )
            dirty_fqn = f"{TEST_CATALOG}.{TEST_SCHEMA}.dirty_{name}".replace("-", "_").replace(
                ".", "_"
            )
            _register_table(spark, clean_fqn, clean_header, clean_rows)
            _register_table(spark, dirty_fqn, dirty_header, dirty_rows)

            clean_fqns[name] = clean_fqn
            dirty_fqns[name] = dirty_fqn
            error_counts[name] = load_changes(changes_path)
            num_rows_by_dataset[name] = len(clean_rows)
            headers[name] = clean_header

        # Offline: learn "what these clean government tables typically look
        # like" from the clean versions.
        ud.build_corpus_statistics(list(clean_fqns.values()), error_types=list(ErrorType))

        # Online: score the dirty (really-corrupted) versions against it.
        detections = ud.detect(list(dirty_fqns.values()), error_types=list(ErrorType)).toPandas()

        fqn_to_dataset = {fqn: name for name, fqn in dirty_fqns.items()}

        # (dataset, column) -> the best (lowest lr_ratio) detection that
        # touched that column, across every error type and every candidate
        # (single-column ones directly, FD pairs via either side).
        per_column: dict[tuple[str, str], dict] = {}
        for _, row in detections.iterrows():
            dataset = fqn_to_dataset[row["table_id"]]
            for col in row["column_names"]:
                key = (dataset, col)
                existing = per_column.get(key)
                if existing is None or row["lr_ratio"] < existing["lr_ratio"]:
                    per_column[key] = row

        targets: list[dict] = []
        for name in DATASETS:
            for col in headers[name]:
                hit = per_column.get((name, col))
                error_count = error_counts[name].get(col, 0)
                targets.append(
                    {
                        "id": f"{name}::{col}",
                        "dataset": name,
                        "column": col,
                        "num_rows": num_rows_by_dataset[name],
                        "error_count": error_count,
                        "expected_significant": error_count > 0,
                        "predicted_significant": bool(hit is not None and hit["is_significant"]),
                        "lr_ratio": float(hit["lr_ratio"]) if hit is not None else None,
                        "matched_error_type": hit["error_type"] if hit is not None else None,
                    }
                )

    overall = confusion_metrics(targets)
    by_dataset = {
        name: confusion_metrics([t for t in targets if t["dataset"] == name]) for name in DATASETS
    }

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "git_commit": git_commit(REPO_ROOT),
        "dataset": "real_world_gov",
        "source": "https://github.com/LUH-DBS/Matelda/tree/main/datasets/DGov_NTR",
        "datasets_used": list(DATASETS),
        "targets": targets,
        "metrics": {
            "overall": overall,
            "by_dataset": by_dataset,
        },
    }


def _print_comparison(current: dict, baseline: dict | None) -> str:
    lines = ["## real_world_gov benchmark results", ""]
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
    for name in current["datasets_used"]:
        cur = current["metrics"]["by_dataset"].get(name, {})
        base = baseline["metrics"]["by_dataset"].get(name) if baseline else None
        _row(name, cur, base)

    text = "\n".join(lines)
    print(text)
    return text


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--update-baseline",
        action="store_true",
        help="Overwrite results/baseline.json with this run's results.",
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

        subprocess.run(
            [sys.executable, str(BENCHMARK_DIR / "generate_report.py")],
            cwd=REPO_ROOT,
            check=True,
        )
        print(
            "Regenerated results/REPORT.md and results/charts/ -- "
            "remember to `git add` them alongside baseline.json"
        )


if __name__ == "__main__":
    main()
