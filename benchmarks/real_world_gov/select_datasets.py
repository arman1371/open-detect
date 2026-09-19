"""Reproduces how this benchmark's 5 datasets were picked from Matelda's DGov_NTR corpus.

Source: https://github.com/LUH-DBS/Matelda/tree/main/datasets/DGov_NTR --
143 real government open-data tables, each shipped as a
``clean.csv``/``dirty.csv``/``clean_changes.csv`` triple (see
``README.md`` and ``dataset_utils.py`` for the format). This script is
provenance/documentation, not something CI runs: it requires a local
checkout of that repository and only needs to be re-run if the benchmark's
dataset selection is deliberately changed.

Selection method, in order:

1. List every subdirectory of ``datasets/DGov_NTR`` that has all three
   required files.
2. Keep only those whose ``dirty.csv`` is at most ``MAX_DIRTY_BYTES``
   (300 KB) -- a CI/repo-size bound applied *before* sampling, the same
   "small enough to check in and run on every push" reasoning
   ``benchmarks/README.md`` gives for the wiki_subset benchmark, not a
   content-based filter. 122 of the 143 datasets pass this bound.
3. Sort the survivors by name (for a deterministic input order) and draw 5
   with ``random.Random(SEED).sample(...)``.

Usage::

    git clone --depth 1 --filter=blob:none --sparse \\
        https://github.com/LUH-DBS/matelda /tmp/matelda
    git -C /tmp/matelda sparse-checkout set datasets/DGov_NTR
    uv run python benchmarks/real_world_gov/select_datasets.py /tmp/matelda
    # add --copy to also (re)populate benchmarks/real_world_gov/data/
"""

from __future__ import annotations

import argparse
import random
import shutil
from pathlib import Path

#: Fixed so the selection is reproducible; not tuned against the outcome.
SEED = 20240919
NUM_DATASETS = 5
MAX_DIRTY_BYTES = 300_000
REQUIRED_FILES = ("clean.csv", "dirty.csv", "clean_changes.csv")

THIS_DIR = Path(__file__).parent
DATA_DIR = THIS_DIR / "data"


def candidates(dgov_ntr_dir: Path) -> list[str]:
    names = []
    for d in sorted(dgov_ntr_dir.iterdir()):
        if not d.is_dir() or not all((d / f).exists() for f in REQUIRED_FILES):
            continue
        if (d / "dirty.csv").stat().st_size <= MAX_DIRTY_BYTES:
            names.append(d.name)
    return sorted(names)


def select(dgov_ntr_dir: Path) -> list[str]:
    pool = candidates(dgov_ntr_dir)
    return sorted(random.Random(SEED).sample(pool, NUM_DATASETS))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "matelda_root", type=Path, help="Path to a local checkout of LUH-DBS/Matelda"
    )
    parser.add_argument(
        "--copy",
        action="store_true",
        help="Also copy the selected datasets' CSVs into benchmarks/real_world_gov/data/",
    )
    args = parser.parse_args()

    dgov_ntr_dir = args.matelda_root / "datasets" / "DGov_NTR"
    pool = candidates(dgov_ntr_dir)
    print(f"{len(pool)} candidate datasets (<= {MAX_DIRTY_BYTES:,} bytes of dirty.csv)")

    chosen = select(dgov_ntr_dir)
    print(f"Selected {len(chosen)} with seed={SEED}:")
    for name in chosen:
        print(f"  - {name}")

    if args.copy:
        for name in chosen:
            src = dgov_ntr_dir / name
            dst = DATA_DIR / name
            dst.mkdir(parents=True, exist_ok=True)
            for f in REQUIRED_FILES:
                shutil.copyfile(src / f, dst / f)
        print(f"\nCopied into {DATA_DIR}")


if __name__ == "__main__":
    main()
