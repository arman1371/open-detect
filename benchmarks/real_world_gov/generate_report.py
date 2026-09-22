"""Renders a real_world_gov results JSON (see ``run_benchmark.py``) as a
human-readable Markdown report with SVG charts, comparing every algorithm
that was run.

Usage::

    uv run python benchmarks/real_world_gov/generate_report.py
    uv run python benchmarks/real_world_gov/generate_report.py --input results/latest.json

Defaults to rendering ``results/baseline.json`` into ``results/REPORT.md``
and ``results/charts/*.svg``. Pure stdlib -- no plotting library required.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

BENCHMARK_DIR = Path(__file__).parent
RESULTS_DIR = BENCHMARK_DIR / "results"
BASELINE_FILE = RESULTS_DIR / "baseline.json"

sys.path.insert(0, str(BENCHMARK_DIR.parent))
from common.charts import AQUA, grouped_bar_chart  # noqa: E402
from common.comparison import comparison_charts, comparison_table_markdown  # noqa: E402


def _slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")


def _by_dataset_chart(entry: dict, datasets: list[str]) -> str:
    by_dataset = entry["metrics"]["by_dataset"]
    return grouped_bar_chart(
        [_short_name(d) for d in datasets],
        {"F1": [by_dataset.get(d, {}).get("f1", 0.0) for d in datasets]},
        {"F1": AQUA},
        title="F1 score by dataset",
        y_max=1.0,
        width=760,
    )


def _short_name(dataset: str) -> str:
    return dataset if len(dataset) <= 24 else dataset[:21] + "..."


def _fmt_pct(value: float) -> str:
    return f"{value:.3f}"


def _metrics_table_row(label: str, m: dict) -> str:
    return (
        f"| {label} | {m['n']} | {_fmt_pct(m['precision'])} | {_fmt_pct(m['recall'])} | "
        f"{_fmt_pct(m['f1'])} | {_fmt_pct(m['accuracy'])} |"
    )


def _algorithm_section(name: str, entry: dict, datasets: list[str]) -> list[str]:
    overall = entry["metrics"]["overall"]
    by_dataset = entry["metrics"]["by_dataset"]
    slug = _slug(name)
    is_raha = name == "raha"

    lines: list[str] = []
    lines.append(f"## `{name}`")
    lines.append("")
    duration = entry.get("duration_seconds")
    if duration is not None:
        lines.append(f"**Duration:** {duration:.2f}s  ")
    elif entry.get("duration_note"):
        lines.append(f"**Duration:** not measured -- {entry['duration_note']}  ")
    lines.append("")

    lines.append("| Metric | Value |")
    lines.append("|---|---|")
    lines.append(f"| Columns evaluated | {overall['n']} |")
    lines.append(f"| Precision | {_fmt_pct(overall['precision'])} |")
    lines.append(f"| Recall | {_fmt_pct(overall['recall'])} |")
    lines.append(f"| F1 | {_fmt_pct(overall['f1'])} |")
    lines.append(f"| Accuracy | {_fmt_pct(overall['accuracy'])} |")
    lines.append("")
    lines.append(f"![F1 by dataset ({name})](charts/f1_by_dataset_{slug}.svg)")
    lines.append("")

    lines.append("### By dataset (column-level)")
    lines.append("")
    if is_raha:
        lines.append(
            'Column-level: a column is "predicted significant" if *any* of its cells '
            "was flagged -- the same granularity Uni-Detect's own output has, used for the "
            'apples-to-apples comparison above. See "Cell-level" below for Raha\'s native, '
            "per-cell granularity (the same one the paper's own Table 5 reports)."
        )
        lines.append("")
    lines.append("| Dataset | n | Precision | Recall | F1 | Accuracy |")
    lines.append("|---|---|---|---|---|---|")
    lines.append(_metrics_table_row("**overall**", overall))
    for name_ in datasets:
        if name_ in by_dataset:
            lines.append(_metrics_table_row(f"`{name_}`", by_dataset[name_]))
    lines.append("")

    if is_raha and entry.get("cell_metrics"):
        cell_overall = entry["cell_metrics"]["overall"]
        cell_by_dataset = entry["cell_metrics"]["by_dataset"]
        lines.append("### By dataset (cell-level)")
        lines.append("")
        lines.append(
            "Precision/recall/F1 over every individual `(row, column)` cell against "
            "`clean_changes.csv` -- Raha's native evaluation granularity, and typically a "
            "more informative number than the column-level reduction above, since a real, "
            "historically-corrupted column in this benchmark often has a double-digit-percent "
            "error rate: getting the column-level call right only requires flagging *one* of "
            "many erroneous cells."
        )
        lines.append("")
        lines.append("| Dataset | n | Precision | Recall | F1 | Accuracy |")
        lines.append("|---|---|---|---|---|---|")
        lines.append(_metrics_table_row("**overall**", cell_overall))
        for name_ in datasets:
            if name_ in cell_by_dataset:
                lines.append(_metrics_table_row(f"`{name_}`", cell_by_dataset[name_]))
        lines.append("")

    lines.append("### Evaluated columns (column-level)")
    lines.append("")
    if is_raha:
        lines.append("| Dataset | Column | Rows | Errors | Expected | Predicted | Score | Result |")
        lines.append("|---|---|---|---|---|---|---|---|")
        for t in entry["targets"]:
            result_mark = "✅" if t["predicted_significant"] == t["expected_significant"] else "❌"
            lines.append(
                f"| `{t['dataset']}` | `{t['column']}` | {t['num_rows']} | {t['error_count']} | "
                f"{t['expected_significant']} | {t['predicted_significant']} | "
                f"{t['score']:.3f} | {result_mark} |"
            )
    else:
        lines.append(
            "| Dataset | Column | Rows | Errors | Expected | Predicted | lr_ratio | Matched via | Result |"
        )
        lines.append("|---|---|---|---|---|---|---|---|---|")
        for t in entry["targets"]:
            result_mark = "✅" if t["predicted_significant"] == t["expected_significant"] else "❌"
            lr = f"{t['lr_ratio']:.4f}" if t.get("lr_ratio") is not None else "n/a"
            matched = t.get("matched_error_type") or "n/a"
            lines.append(
                f"| `{t['dataset']}` | `{t['column']}` | {t['num_rows']} | {t['error_count']} | "
                f"{t['expected_significant']} | {t['predicted_significant']} | {lr} | `{matched}` | "
                f"{result_mark} |"
            )
    lines.append("")
    return lines


def render_markdown(results: dict) -> str:
    algorithms = results["algorithms"]
    datasets = results["datasets_used"]

    lines: list[str] = []
    lines.append("# real_world_gov benchmark results")
    lines.append("")
    lines.append(
        "Human-readable view of the checked-in benchmark run. "
        "See [README.md](README.md) for how this benchmark works, where its "
        "5 datasets came from, and how to regenerate this file."
    )
    lines.append("")
    lines.append(f"**Generated at:** {results.get('generated_at', 'unknown')}  ")
    lines.append(f"**Commit:** `{results.get('git_commit', 'unknown')}`  ")
    lines.append(f"**Source:** {results.get('source', 'unknown')}")
    lines.append("")

    lines.append("## Algorithm comparison")
    lines.append("")
    lines.append(
        "Every algorithm below scores the same set of (dataset, column) targets "
        "against the same `clean_changes.csv` ground truth (see [README.md](README.md) "
        "for how each algorithm's per-column verdict is derived), so the comparison is "
        "apples-to-apples on effectiveness. Duration is each algorithm's own wall-clock "
        "time to go from loaded data to predictions (see README for exactly what is/isn't "
        "included, and why one algorithm's duration may be unmeasured in a given run)."
    )
    lines.append("")
    lines.append(comparison_table_markdown(algorithms))
    lines.append("")
    lines.append("![F1 by algorithm](charts/algorithm_f1_comparison.svg)")
    lines.append("")
    if any(e.get("duration_seconds") is not None for e in algorithms.values()):
        lines.append("![Duration by algorithm](charts/algorithm_duration_comparison.svg)")
        lines.append("")

    for name, entry in algorithms.items():
        lines.extend(_algorithm_section(name, entry, datasets))

    lines.append("---")
    lines.append("")
    lines.append("_Regenerate this file (and the charts above) from a results JSON with:_")
    lines.append("")
    lines.append("```bash")
    lines.append("uv run python benchmarks/real_world_gov/generate_report.py")
    lines.append("```")
    lines.append("")

    return "\n".join(lines)


def write_report(results: dict, output_dir: Path) -> None:
    charts_dir = output_dir / "charts"
    charts_dir.mkdir(parents=True, exist_ok=True)

    algorithms = results["algorithms"]
    datasets = results["datasets_used"]

    f1_chart, duration_chart = comparison_charts(algorithms)
    (charts_dir / "algorithm_f1_comparison.svg").write_text(f1_chart + "\n")
    if duration_chart is not None:
        (charts_dir / "algorithm_duration_comparison.svg").write_text(duration_chart + "\n")

    for name, entry in algorithms.items():
        chart = _by_dataset_chart(entry, datasets)
        (charts_dir / f"f1_by_dataset_{_slug(name)}.svg").write_text(chart + "\n")

    (output_dir / "REPORT.md").write_text(render_markdown(results) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        default=str(BASELINE_FILE),
        help="Path to a benchmark results JSON (default: results/baseline.json).",
    )
    parser.add_argument(
        "--output-dir",
        default=str(RESULTS_DIR),
        help="Directory to write REPORT.md and charts/ into (default: results).",
    )
    args = parser.parse_args()

    results = json.loads(Path(args.input).read_text())
    output_dir = Path(args.output_dir)
    write_report(results, output_dir)
    print(f"Wrote {output_dir / 'REPORT.md'} and {output_dir / 'charts'}/*.svg")


if __name__ == "__main__":
    main()
