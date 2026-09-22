"""Standalone quickstart: run Raha against a small dirty in-memory table.

Run with `python examples/raha_quickstart.py` from a Python environment that
has `unidetect[raha]` installed (adds scikit-learn + scipy; see README).
Unlike Uni-Detect, Raha needs no Spark session and no background corpus --
just the table itself, plus a handful of labels.
"""

from __future__ import annotations

import pandas as pd

from unidetect.algorithms.raha import GroundTruthLabeler, RahaConfig, RahaDetector


def main() -> None:
    # The paper's own running example (Table 2), plus a couple of extra rows
    # so clustering has more than one tuple per cluster to work with.
    dirty = pd.DataFrame(
        {
            "Lord": ["Aragorn", "Sauron", "Gandalf", "Saruman", "Elrond", "Theoden", "Bilbo"],
            "Kingdom": ["Minas Tirith", "Mordor", "MISSING", "MISSING", "123", "Shire", "Shire"],
        }
    )
    clean = pd.DataFrame(
        {
            "Lord": ["Aragorn", "Sauron", "Gandalf", "Saruman", "Elrond", "Theoden", "Bilbo"],
            "Kingdom": ["Minas Tirith", "Mordor", "N/A", "Isengard", "Rivendell", "Rohan", "Shire"],
        }
    )

    detector = RahaDetector(RahaConfig(labeling_budget=6, random_state=0))
    # GroundTruthLabeler is for evaluation, since `clean` is known here. For a
    # real, unlabeled dataset, pass a CallableLabeler wired to a person instead.
    labeler = GroundTruthLabeler(clean)

    result = detector.detect(dirty, table_id="lord_of_the_rings", labeler=labeler)

    print(f"Scanned {len(result)} cells, flagged {len(result.errors())} as errors:")
    for cell in result.errors():
        print(
            f"  row={cell.row_index} column={cell.column_name!r} "
            f"score={cell.score:.2f} source={cell.evidence['source']}"
        )


if __name__ == "__main__":
    main()
