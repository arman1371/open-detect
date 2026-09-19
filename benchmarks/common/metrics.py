"""Confusion-matrix scoring shared by every benchmark's evaluation targets.

Every benchmark reduces its evaluation to the same shape: a list of rows
each carrying a boolean ground truth and a boolean prediction. This module
is the one place that turns such a list into
precision/recall/F1/accuracy, so ``run_benchmark.py`` scripts don't
reimplement (and risk disagreeing on) the same arithmetic per benchmark.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence


def confusion_metrics(
    rows: Sequence[Mapping[str, object]],
    expected_key: str = "expected_significant",
    predicted_key: str = "predicted_significant",
) -> dict:
    """Precision/recall/F1/accuracy over ``rows``' boolean ``expected_key``/``predicted_key``."""
    tp = sum(1 for r in rows if r[expected_key] and r[predicted_key])
    fp = sum(1 for r in rows if not r[expected_key] and r[predicted_key])
    fn = sum(1 for r in rows if r[expected_key] and not r[predicted_key])
    tn = sum(1 for r in rows if not r[expected_key] and not r[predicted_key])
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
