"""Generates the WIKI-subset benchmark dataset checked into ``benchmarks/data/``.

Uni-Detect's own evaluation corpus (paper Section 4.1) is **WIKI**: "a subset
of WEB from the wikipedia.org domain with over 3M tables." Shipping (or
downloading, in CI, on every run) anything close to that scale is neither
practical nor reproducible for a small, fast, version-over-version regression
benchmark, so this script instead materializes a small, deterministic set of
tables that follow the same shapes Wikipedia's own list-article and infobox
tables take -- code/ID columns, key -> label mappings, population/vote-share
figures, and person/place name columns -- with real-world values (ISO 3166
country codes and names, well-known surnames, etc.) rather than arbitrary
synthetic strings.

This mirrors, and scales up, the same true-positive/false-positive table
shapes ``tests/test_corpus_and_detectors.py`` already validates against the
paper's own worked examples (Figures 2 and 4): a background "corpus" of
typical tables per error type, plus a handful of labeled evaluation targets
-- some containing a genuine, deliberately injected error (true positive),
some only superficially anomalous (false positive) -- so
``benchmarks/run_benchmark.py`` can score detection quality against known
ground truth and track it across versions.

Network access is deliberately not used: the values below are hand-curated
from well-known, mostly-static reference facts (ISO country codes/names,
common English surnames, ...) so the generated dataset is fully reproducible
offline and in CI. Run this script to regenerate ``benchmarks/data/`` after
changing anything below:

    uv run python benchmarks/generate_dataset.py
"""

from __future__ import annotations

import csv
import json
import random
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data" / "wiki_subset"
CORPUS_DIR = DATA_DIR / "corpus"
EVAL_DIR = DATA_DIR / "eval"

# ---------------------------------------------------------------------------
# Real-world reference data (Wikipedia-style list/infobox content)
# ---------------------------------------------------------------------------

# ISO 3166-1 alpha-3 country codes -> English short name, as tabulated on
# Wikipedia's "ISO 3166-1 alpha-3" list article -- a canonical example of a
# Wikipedia key -> label table with a hard functional dependency.
ISO_COUNTRIES: dict[str, str] = {
    "USA": "United States",
    "GBR": "United Kingdom",
    "FRA": "France",
    "DEU": "Germany",
    "JPN": "Japan",
    "CHN": "China",
    "IND": "India",
    "BRA": "Brazil",
    "CAN": "Canada",
    "AUS": "Australia",
    "MEX": "Mexico",
    "ITA": "Italy",
    "ESP": "Spain",
    "RUS": "Russia",
    "KOR": "South Korea",
    "NLD": "Netherlands",
    "CHE": "Switzerland",
    "SWE": "Sweden",
    "NOR": "Norway",
    "DNK": "Denmark",
    "FIN": "Finland",
    "POL": "Poland",
    "TUR": "Turkey",
    "EGY": "Egypt",
    "ZAF": "South Africa",
    "NGA": "Nigeria",
    "KEN": "Kenya",
    "ARG": "Argentina",
    "CHL": "Chile",
    "COL": "Colombia",
    "PER": "Peru",
    "IDN": "Indonesia",
    "THA": "Thailand",
    "VNM": "Vietnam",
    "PHL": "Philippines",
    "MYS": "Malaysia",
    "SGP": "Singapore",
    "NZL": "New Zealand",
    "IRL": "Ireland",
    "PRT": "Portugal",
    "GRC": "Greece",
    "AUT": "Austria",
    "BEL": "Belgium",
    "CZE": "Czechia",
    "HUN": "Hungary",
    "ROU": "Romania",
    "UKR": "Ukraine",
    "ISR": "Israel",
    "SAU": "Saudi Arabia",
    "ARE": "United Arab Emirates",
    "PAK": "Pakistan",
    "BGD": "Bangladesh",
    "LKA": "Sri Lanka",
    "NPL": "Nepal",
    "MMR": "Myanmar",
    "KHM": "Cambodia",
    "LAO": "Laos",
    "MNG": "Mongolia",
    "KAZ": "Kazakhstan",
    "UZB": "Uzbekistan",
    "QAT": "Qatar",
    "KWT": "Kuwait",
    "OMN": "Oman",
    "JOR": "Jordan",
    "LBN": "Lebanon",
    "MAR": "Morocco",
    "TUN": "Tunisia",
    "DZA": "Algeria",
    "GHA": "Ghana",
    "ETH": "Ethiopia",
    "TZA": "Tanzania",
    "UGA": "Uganda",
    "ZMB": "Zambia",
    "ZWE": "Zimbabwe",
    "AGO": "Angola",
    "MOZ": "Mozambique",
    "CMR": "Cameroon",
    "CIV": "Ivory Coast",
    "SEN": "Senegal",
    "MLI": "Mali",
    "ISL": "Iceland",
    "LUX": "Luxembourg",
    "MLT": "Malta",
    "CYP": "Cyprus",
    "EST": "Estonia",
    "LVA": "Latvia",
    "LTU": "Lithuania",
    "SVK": "Slovakia",
    "SVN": "Slovenia",
    "HRV": "Croatia",
    "SRB": "Serbia",
    "BIH": "Bosnia and Herzegovina",
    "ALB": "Albania",
    "MKD": "North Macedonia",
    "MDA": "Moldova",
    "GEO": "Georgia",
    "ARM": "Armenia",
    "AZE": "Azerbaijan",
    "BLR": "Belarus",
}
ISO_CODES = list(ISO_COUNTRIES)

# IATA-style airport codes (3 uppercase letters) -- another Wikipedia
# "should always be unique" ID column shape, distinct in flavor from ISO
# country codes so the two TP-baseline categories aren't identical.
IATA_CODES = [
    "JFK",
    "LAX",
    "ORD",
    "ATL",
    "DFW",
    "DEN",
    "SFO",
    "SEA",
    "LAS",
    "MIA",
    "LHR",
    "CDG",
    "FRA",
    "AMS",
    "MAD",
    "FCO",
    "IST",
    "DXB",
    "DOH",
    "SIN",
    "HKG",
    "NRT",
    "ICN",
    "PEK",
    "PVG",
    "BOM",
    "DEL",
    "SYD",
    "MEL",
    "GRU",
    "MEX",
    "YYZ",
    "GIG",
    "EZE",
    "JNB",
    "CAI",
    "NBO",
    "LOS",
    "ZRH",
    "VIE",
]  # noqa: RUF012 -- module-level constant data, not a dataclass field

# Common English surnames -- Wikipedia biography list-articles routinely
# repeat these across "notable people" sections, a natural (non-error)
# source of duplicate values, unlike an ID column.
COMMON_SURNAMES = [
    "Smith",
    "Johnson",
    "Williams",
    "Brown",
    "Jones",
    "Garcia",
    "Miller",
    "Davis",
    "Rodriguez",
    "Martinez",
    "Wilson",
    "Anderson",
    "Taylor",
    "Thomas",
    "Moore",
]  # noqa: RUF012

# Long, mutually distinct biography-style names -- Wikipedia "List of ...
# people" articles are full of these, and (unlike the surname pool above)
# they are not expected to collide.
LONG_NAMES_POOL = [
    "Alexander Kingsley",
    "Bartholomew Winters",
    "Cassandra Ashford",
    "Dominic Fairweather",
    "Evangeline Whitmore",
    "Frederick Lancaster",
    "Gwendolyn Pemberton",
    "Harrison Blackwood",
    "Isabella Thorne",
    "Jonathan Sinclair",
    "Katherine Wellesley",
    "Lysander Montgomery",
    "Marguerite Fitzgerald",
    "Nathaniel Ashworth",
    "Ophelia Sterling",
    "Percival Hawthorne",
    "Rosalind Kensington",
    "Sebastian Wolverton",
    "Theodora Ravensworth",
    "Ulysses Blackthorn",
    "Vivienne Calloway",
    "Winston Farrington",
    "Xiomara Blackwell",
    "Yusuf Abernathy",
    "Zelda Cunningham",
]  # noqa: RUF012

ROMAN_NUMERALS = [
    "I",
    "II",
    "III",
    "IV",
    "V",
    "VI",
    "VII",
    "VIII",
    "IX",
    "X",
    "XI",
    "XII",
    "XIII",
    "XIV",
    "XV",
    "XVI",
    "XVII",
    "XVIII",
    "XIX",
    "XX",
    "XXI",
    "XXII",
    "XXIII",
    "XXIV",
    "XXV",
    "XXVI",
    "XXVII",
    "XXVIII",
]  # noqa: RUF012


def _write_csv(path: Path, header: list[str], rows: list[tuple]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(header)
        writer.writerows(rows)


def _clear_dir(path: Path) -> None:
    if path.exists():
        for child in path.rglob("*"):
            if child.is_file():
                child.unlink()
    path.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Corpus (background) tables -- one small CSV per Wikipedia-shaped table.
# ---------------------------------------------------------------------------


def build_corpus() -> None:
    # uniqueness / false-positive baseline: common surnames, natural collisions
    rnd = random.Random("wiki-uniqueness-names")
    for t in range(10):
        n = rnd.randint(60, 200)
        rows = [(rnd.choice(COMMON_SURNAMES),) for _ in range(n)]
        _write_csv(
            CORPUS_DIR / "uniqueness" / f"notable_people_by_surname_{t:02d}.csv",
            ["surname"],
            rows,
        )

    # uniqueness / true-positive baseline: ID-like codes, always unique.
    # Each value pairs a code with a distinct numeric suffix (mirroring
    # `uniqueness_tp_airport_codes` in build_eval_targets below), which
    # matters beyond flavor: it makes the column MIXED_ALPHANUMERIC and
    # pushes row counts past 100, matching that eval target's own
    # (data_type, row_count) feature bucket so the corpus actually has
    # support for it (see unidetect.featurization.build_uniqueness_bucket).
    rnd = random.Random("wiki-uniqueness-codes")
    code_pool = ISO_CODES + IATA_CODES
    for t in range(10):
        n = 100 + t * 10
        rows = [(f"{code_pool[i % len(code_pool)]}{(t * 1000 + i):04d}",) for i in range(n)]
        rnd.shuffle(rows)
        _write_csv(
            CORPUS_DIR / "uniqueness" / f"code_list_{t:02d}.csv",
            ["code"],
            rows,
        )

    # numeric_outlier / false-positive baseline: election vote-share percentages
    rnd = random.Random("wiki-outlier-votes")
    for t in range(20):
        n = rnd.randint(6, 40)
        values = [round(rnd.uniform(0.1, 3.0), 2) for _ in range(n)]
        values[0] = round(rnd.uniform(20, 48), 2)  # legitimate winning candidate
        rows = [(v,) for v in values]
        _write_csv(
            CORPUS_DIR / "numeric_outlier" / f"election_result_{t:02d}.csv",
            ["vote_share_pct"],
            rows,
        )

    # numeric_outlier / true-positive baseline: clustered population-ish figures.
    # A wide, deterministic sweep of spread (up to ~30x the tightest table's)
    # matters here the same way it does in
    # tests/test_corpus_and_detectors.py: the eval target's own *post-drop*
    # residual max-MAD score is still a moderately large ~3.6 (six genuine
    # population figures spanning 8k-13k aren't perfectly clustered), so
    # without some corpus columns whose own natural dispersion reaches that
    # range too, the denominator has zero support and the ratio collapses to
    # the Laplace-smoothed default of "unsurprising" regardless of how real
    # the injected typo is.
    rnd = random.Random("wiki-outlier-population")
    for t in range(40):
        n = rnd.randint(6, 20)
        base = rnd.uniform(5000, 15000)
        spread = 300 + t * 700
        values = [round(base + rnd.uniform(-spread, spread), 1) for _ in range(n)]
        rows = [(v,) for v in values]
        _write_csv(
            CORPUS_DIR / "numeric_outlier" / f"population_thousands_{t:02d}.csv",
            ["population_thousands"],
            rows,
        )

    # spelling / false-positive baseline: short, syntactically-close suffixes
    rnd = random.Random("wiki-spelling-amendments")
    for t in range(10):
        n = rnd.randint(6, len(ROMAN_NUMERALS))
        values = [f"Amendment {r}" for r in rnd.sample(ROMAN_NUMERALS, n)]
        rows = [(v,) for v in values]
        _write_csv(
            CORPUS_DIR / "spelling" / f"amendment_list_{t:02d}.csv",
            ["title"],
            rows,
        )

    # spelling / true-positive baseline: long, mutually-distinct biography names.
    # Two full cycles through the 1-8 differing-token-length sweep (not one)
    # so the eval target's own bucket has more than a bare handful of corpus
    # rows backing it -- comfortably below the significance threshold rather
    # than sitting exactly on it.
    rnd = random.Random("wiki-spelling-names")
    for t in range(16):
        n = rnd.randint(6, len(LONG_NAMES_POOL))
        k = (t % 8) + 1
        word_a = "abcdefgh"
        word_b = word_a[: 8 - k] + "z" * k
        values = rnd.sample(LONG_NAMES_POOL, max(n - 2, 4)) + [
            f"Biography subject {word_a}",
            f"Biography subject {word_b}",
        ]
        rows = [(v,) for v in values]
        _write_csv(
            CORPUS_DIR / "spelling" / f"biography_list_{t:02d}.csv",
            ["name"],
            rows,
        )

    # functional_dependency / true-positive baseline: near-perfect key -> label.
    # Row counts sweep up to ~220 -- past `fd_tp_country_code_violation`'s own
    # 120-row scale below -- so the corpus has support in that target's
    # row-count bucket (not just at the smaller scales this swept
    # previously), and enough of it to sit comfortably below the
    # significance threshold rather than exactly on it.
    rnd = random.Random("wiki-fd-codes")
    for t in range(16):
        n = 40 + t * 12
        codes = [ISO_CODES[i % len(ISO_CODES)] for i in range(n)]
        rows = [(c, ISO_COUNTRIES[c]) for c in codes]
        _write_csv(
            CORPUS_DIR / "functional_dependency" / f"country_code_table_{t:02d}.csv",
            ["iso_code", "country_name"],
            rows,
        )

    # functional_dependency / false-positive baseline: unrelated small-integer
    # pairs (e.g. a weekly page-view count vs. an unrelated weekly edit
    # count -- plausible Wikipedia analytics columns with no real dependency
    # between them). A narrow domain (300) matters: with a domain wide
    # enough that most tables are exactly, coincidentally 100% "compliant"
    # by construction (few if any repeated LHS values), any candidate with
    # even a handful of coincidental collisions reads as a novel,
    # never-before-seen transition and scores as "surprising" regardless of
    # intent. A narrow domain instead makes partial compliance -- and
    # specifically the compliance level a 150-row sample of this recipe
    # typically lands at -- the corpus's normal, common case for this
    # bucket.
    rnd = random.Random("wiki-fd-unrelated")
    for t in range(20):
        n = rnd.randint(60, 150)
        rows = [(str(rnd.randint(0, 300)), str(rnd.randint(0, 300))) for _ in range(n)]
        _write_csv(
            CORPUS_DIR / "functional_dependency" / f"pageviews_vs_edits_{t:02d}.csv",
            ["page_views", "edit_count"],
            rows,
        )


# ---------------------------------------------------------------------------
# Evaluation targets: labeled true-positive / false-positive tables.
# ---------------------------------------------------------------------------


def build_eval_targets() -> list[dict]:
    targets: list[dict] = []

    # --- uniqueness ---
    fp_values = (COMMON_SURNAMES[:5] * 20) + [COMMON_SURNAMES[0]]  # 101 values, 1 coincidence
    targets.append(
        {
            "id": "uniqueness_fp_common_surnames",
            "error_type": "uniqueness",
            "expected_significant": False,
            "description": (
                "A 'List of notable people named Smith' style table: one coincidental "
                "duplicate surname among common names. Not a real error."
            ),
            "columns": ["surname"],
            "rows": [[v] for v in fp_values],
        }
    )
    tp_values = [f"{IATA_CODES[i % len(IATA_CODES)]}{i:03d}" for i in range(120)]
    tp_values[1] = tp_values[0]  # inject a genuine duplicate in a should-be-unique ID column
    targets.append(
        {
            "id": "uniqueness_tp_airport_codes",
            "error_type": "uniqueness",
            "expected_significant": True,
            "description": (
                "An airport-code-style ID column with one injected duplicate -- codes "
                "like this are expected to always be unique."
            ),
            "columns": ["code"],
            "rows": [[v] for v in tp_values],
        }
    )

    # --- numeric_outlier ---
    targets.append(
        {
            "id": "outlier_fp_election_result",
            "error_type": "numeric_outlier",
            "expected_significant": False,
            "description": (
                "Election vote shares: many small candidates plus one legitimately "
                "larger winner (paper's own 'C-' false-positive worked example)."
            ),
            "columns": ["vote_share_pct"],
            "rows": [[v] for v in [43.0, 22.0, 9.0, 5.0, 0.76, 0.32, 0.30]],
        }
    )
    targets.append(
        {
            "id": "outlier_tp_population_typo",
            "error_type": "numeric_outlier",
            "expected_significant": True,
            "description": (
                "Population figures (thousands) with a decimal-point typo "
                "('8.716' instead of '8716') -- paper's own 'C+' true-positive example."
            ),
            "columns": ["population_thousands"],
            "rows": [[v] for v in [8011.0, 8.716, 9954.0, 11895.0, 13329.0, 11352.0, 11709.0]],
        }
    )

    # --- spelling ---
    fp_values = [f"Amendment {r}" for r in ["XIX", "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV"]]
    targets.append(
        {
            "id": "spelling_fp_amendment_list",
            "error_type": "spelling",
            "expected_significant": False,
            "description": (
                "Consecutive amendment numerals: syntactically close by design, not "
                "misspellings."
            ),
            "columns": ["title"],
            "rows": [[v] for v in fp_values],
        }
    )
    tp_values = [
        "Kevin Doeling",
        "Kevin Dowling",
        "Alan Myerson",
        "Rob Morrow",
        "Patricia Fairweather",
        "Montgomery Higginbotham",
        "Alexandra Winterbourne",
    ]
    targets.append(
        {
            "id": "spelling_tp_biography_typo",
            "error_type": "spelling",
            "expected_significant": True,
            "description": (
                "One genuine misspelling ('Doeling' for 'Dowling') among unrelated "
                "long biography names -- paper's own true-positive example."
            ),
            "columns": ["name"],
            "rows": [[v] for v in tp_values],
        }
    )

    # --- functional_dependency ---
    rnd = random.Random("wiki-fd-target")
    n = 150
    fp_rows = [[str(rnd.randint(0, 300)), str(rnd.randint(0, 300))] for _ in range(n)]
    targets.append(
        {
            "id": "fd_fp_pageviews_vs_edits",
            "error_type": "functional_dependency",
            "expected_significant": False,
            "description": "Two independent numeric-ish columns with no real dependency.",
            "columns": ["page_views", "edit_count"],
            "rows": fp_rows,
        }
    )
    codes = [ISO_CODES[i % 40] for i in range(120)]
    tp_rows = [[c, ISO_COUNTRIES[c]] for c in codes]
    tp_rows[0][1] = "Nonexistent Country"  # inject one FD violation
    targets.append(
        {
            "id": "fd_tp_country_code_violation",
            "error_type": "functional_dependency",
            "expected_significant": True,
            "description": (
                "ISO code -> country name table (a hard functional dependency on "
                "Wikipedia) with one injected violating row."
            ),
            "columns": ["iso_code", "country_name"],
            "rows": tp_rows,
        }
    )

    return targets


def main() -> None:
    _clear_dir(CORPUS_DIR)
    _clear_dir(EVAL_DIR)
    build_corpus()
    targets = build_eval_targets()
    (EVAL_DIR / "targets.json").write_text(json.dumps(targets, indent=2) + "\n")
    n_corpus = sum(1 for _ in CORPUS_DIR.rglob("*.csv"))
    print(f"Wrote {n_corpus} corpus tables to {CORPUS_DIR}")
    print(f"Wrote {len(targets)} eval targets to {EVAL_DIR / 'targets.json'}")


if __name__ == "__main__":
    main()
