"""Renders a benchmark results JSON (see ``run_benchmark.py``) as a
human-readable Markdown report with SVG charts, so people can see the
WIKI-subset benchmark results at a glance without reading raw JSON.

Usage::

    uv run python benchmarks/wiki_subset/generate_report.py
    uv run python benchmarks/wiki_subset/generate_report.py --input benchmarks/wiki_subset/results/latest.json

Defaults to rendering ``results/baseline.json`` (the checked-in reference
run) into ``results/REPORT.md`` and ``results/charts/*.svg``. Pure stdlib --
no plotting library required.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

BENCHMARK_DIR = Path(__file__).parent
RESULTS_DIR = BENCHMARK_DIR / "results"
BASELINE_FILE = RESULTS_DIR / "baseline.json"

sys.path.insert(0, str(BENCHMARK_DIR.parent))
from common.charts import AQUA, BLUE, ORANGE, grouped_bar_chart  # noqa: E402

ERROR_TYPES = [
    "uniqueness",
    "numeric_outlier",
    "spelling",
    "functional_dependency",
]

#: Display order for severity levels, easiest-to-call to hardest. Kept in
#: sync with ``run_benchmark.py::SEVERITIES`` and ``generate_dataset.py``.
SEVERITIES = ["paper_example", "obvious", "moderate", "subtle", "clean"]

SEVERITY_LABELS = {
    "paper_example": "paper example",
    "obvious": "obvious corruption",
    "moderate": "moderate corruption",
    "subtle": "subtle corruption",
    "clean": "clean (no injection)",
}


def _overall_metrics_chart(results: dict) -> str:
    overall = results["metrics"]["overall"]
    groups = ["Precision", "Recall", "F1", "Accuracy"]
    keys = ["precision", "recall", "f1", "accuracy"]
    colors = {"score": BLUE}
    series = {"score": [overall[k] for k in keys]}
    return grouped_bar_chart(
        groups,
        series,
        colors,
        title="Overall metrics",
        subtitle=f"n = {overall['n']} evaluation targets",
        y_max=1.0,
    )


def _f1_by_error_type_chart(results: dict) -> str:
    by_type = results["metrics"]["by_error_type"]
    groups = ["overall"] + ERROR_TYPES
    values = [results["metrics"]["overall"]["f1"]] + [
        by_type.get(et, {}).get("f1", 0.0) for et in ERROR_TYPES
    ]
    return grouped_bar_chart(
        groups,
        {"F1": values},
        {"F1": AQUA},
        title="F1 score by error type",
        y_max=1.0,
    )


def _severity_chart(results: dict) -> str:
    # Precision/recall are degenerate for severity tiers that are entirely
    # one ground-truth class ("obvious"/"moderate"/"subtle" contain only
    # true-positive targets; "clean" contains only true-negative targets),
    # so plotting them per severity would show a meaningless 0/1 artifact
    # rather than a real precision or recall measurement. Accuracy is
    # well-defined in every tier -- it reduces to recall on a pure-TP tier
    # and to the true-negative rate on the pure-FP "clean" tier -- so it's
    # the one metric that is comparable across the whole severity axis.
    by_severity = results["metrics"].get("by_severity", {})
    groups = [s for s in SEVERITIES if s in by_severity]
    return grouped_bar_chart(
        [SEVERITY_LABELS.get(s, s) for s in groups],
        {"Accuracy": [by_severity[s]["accuracy"] for s in groups]},
        {"Accuracy": AQUA},
        title="Accuracy by corruption severity",
        subtitle="How detection holds up as injected errors get harder to spot "
        "(or, for 'clean', how often genuinely clean data is left alone)",
        y_max=1.0,
    )


def _ranking_chart(results: dict) -> str:
    ranking = results["metrics"]["ranking"]
    groups = [et for et in ERROR_TYPES if et in ranking]
    tp_vals = [ranking[et]["true_positive_lr_ratio"] for et in groups]
    fp_vals = [ranking[et]["false_positive_lr_ratio"] for et in groups]
    return grouped_bar_chart(
        groups,
        {"true error (lower = more surprising)": tp_vals, "false positive": fp_vals},
        {
            "true error (lower = more surprising)": BLUE,
            "false positive": ORANGE,
        },
        title="Detection ranking: lr_ratio",
        subtitle="A correctly ranked pair has a shorter blue bar than orange",
        value_fmt=lambda v: f"{v:.3f}",
    )


def _fmt_pct(value: float) -> str:
    return f"{value:.3f}"


def _metrics_table_row(label: str, m: dict) -> str:
    return (
        f"| {label} | {m['n']} | {_fmt_pct(m['precision'])} | {_fmt_pct(m['recall'])} | "
        f"{_fmt_pct(m['f1'])} | {_fmt_pct(m['accuracy'])} |"
    )


def render_markdown(results: dict) -> str:
    overall = results["metrics"]["overall"]
    by_type = results["metrics"]["by_error_type"]
    ranking = results["metrics"]["ranking"]

    lines: list[str] = []
    lines.append("# WIKI-subset benchmark results")
    lines.append("")
    lines.append(
        "Human-readable view of the checked-in benchmark run. "
        "See [README.md](../README.md) for how this benchmark works "
        "and how to regenerate this file."
    )
    lines.append("")
    lines.append(f"**Generated at:** {results.get('generated_at', 'unknown')}  ")
    lines.append(f"**Commit:** `{results.get('git_commit', 'unknown')}`  ")
    lines.append(f"**Dataset:** {results.get('dataset', 'unknown')}")
    lines.append("")

    lines.append("## Overall")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|---|---|")
    lines.append(f"| Targets evaluated | {overall['n']} |")
    lines.append(f"| Precision | {_fmt_pct(overall['precision'])} |")
    lines.append(f"| Recall | {_fmt_pct(overall['recall'])} |")
    lines.append(f"| F1 | {_fmt_pct(overall['f1'])} |")
    lines.append(f"| Accuracy | {_fmt_pct(overall['accuracy'])} |")
    lines.append("")
    lines.append("![Overall metrics](charts/overall_metrics.svg)")
    lines.append("")

    lines.append("## By error type")
    lines.append("")
    lines.append("| Error type | n | Precision | Recall | F1 | Accuracy |")
    lines.append("|---|---|---|---|---|---|")
    lines.append(_metrics_table_row("**overall**", overall))
    for et in ERROR_TYPES:
        if et in by_type:
            lines.append(_metrics_table_row(f"`{et}`", by_type[et]))
    lines.append("")
    lines.append("![F1 by error type](charts/f1_by_error_type.svg)")
    lines.append("")

    by_severity = results["metrics"].get("by_severity", {})
    if by_severity:
        lines.append("## By corruption severity")
        lines.append("")
        lines.append(
            "How detection holds up as injected errors get harder to spot. "
            "`paper_example` are the paper's own canonical worked examples "
            "(a mix of true- and false-positive shapes); `obvious`/`moderate`/`subtle` "
            "are true-positive targets with graded, programmatically-injected "
            "corruption; `clean` are false-positive shapes with no injected error at "
            "all. Precision/recall are not shown here because most of these tiers are "
            "single-class by construction (see [README.md](../README.md)) "
            "-- accuracy is the one metric that is meaningful across all of them."
        )
        lines.append("")
        lines.append("| Severity | n | TP | FP | FN | TN | Accuracy |")
        lines.append("|---|---|---|---|---|---|---|")
        for severity in SEVERITIES:
            if severity not in by_severity:
                continue
            m = by_severity[severity]
            lines.append(
                f"| `{severity}` | {m['n']} | {m['true_positive']} | {m['false_positive']} | "
                f"{m['false_negative']} | {m['true_negative']} | {_fmt_pct(m['accuracy'])} |"
            )
        lines.append("")
        lines.append("![Accuracy by corruption severity](charts/severity_accuracy.svg)")
        lines.append("")

    lines.append("## Ranking correctness")
    lines.append("")
    lines.append(
        "For each error type: is the true-positive (genuine error) target scored "
        "as *more surprising* (lower `lr_ratio`) than the false-positive target? "
        "This is the paper's central claim."
    )
    lines.append("")
    lines.append("| Error type | TP lr_ratio | FP lr_ratio | Correctly ranked |")
    lines.append("|---|---|---|---|")
    for et in ERROR_TYPES:
        if et in ranking:
            info = ranking[et]
            mark = "✅" if info["correctly_ranked"] else "❌"
            lines.append(
                f"| `{et}` | {info['true_positive_lr_ratio']:.4f} | "
                f"{info['false_positive_lr_ratio']:.4f} | {mark} |"
            )
    lines.append("")
    lines.append("![Detection ranking](charts/ranking_lr_ratio.svg)")
    lines.append("")

    lines.append("## Evaluation targets")
    lines.append("")
    lines.append(
        "| Target | Error type | Severity | Expected | Predicted | lr_ratio | Result | "
        "Description |"
    )
    lines.append("|---|---|---|---|---|---|---|---|")
    for t in results["targets"]:
        result_mark = "✅" if t["predicted_significant"] == t["expected_significant"] else "❌"
        lr = f"{t['lr_ratio']:.4f}" if t.get("lr_ratio") is not None else "n/a"
        lines.append(
            f"| `{t['id']}` | `{t['error_type']}` | `{t.get('severity', 'unknown')}` | "
            f"{t['expected_significant']} | {t['predicted_significant']} | {lr} | "
            f"{result_mark} | {t['description']} |"
        )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("_Regenerate this file (and the charts above) from a results JSON with:_")
    lines.append("")
    lines.append("```bash")
    lines.append("uv run python benchmarks/wiki_subset/generate_report.py")
    lines.append("```")
    lines.append("")

    return "\n".join(lines)


def write_report(results: dict, output_dir: Path) -> None:
    charts_dir = output_dir / "charts"
    charts_dir.mkdir(parents=True, exist_ok=True)

    (charts_dir / "overall_metrics.svg").write_text(_overall_metrics_chart(results) + "\n")
    (charts_dir / "f1_by_error_type.svg").write_text(_f1_by_error_type_chart(results) + "\n")
    if results["metrics"].get("by_severity"):
        (charts_dir / "severity_accuracy.svg").write_text(_severity_chart(results) + "\n")
    (charts_dir / "ranking_lr_ratio.svg").write_text(_ranking_chart(results) + "\n")

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
