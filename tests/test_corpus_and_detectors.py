"""End-to-end tests: ingest a tiny synthetic corpus into Delta tables, build
corpus statistics, then run each detector and check that the paper's
canonical true-positive examples are flagged while its canonical
false-positive examples are not.

These tests require a local Delta-enabled Spark session (see
``conftest.py::spark``) and are skipped automatically if one cannot be
started (e.g. no network access to resolve the Delta Maven artifact).
"""

from __future__ import annotations

import pytest

from unidetect.config import UniDetectConfig
from unidetect.core.enums import ErrorType
from unidetect.pipeline import UniDetect


def _write_table(spark, fqn: str, rows: list[dict], columns: list[str]) -> None:
    df = spark.createDataFrame([tuple(row[c] for c in columns) for row in rows], schema=columns)
    df.write.format("delta").mode("overwrite").saveAsTable(fqn)


@pytest.fixture
def corpus_tables_by_category(spark, uc_location):
    """Builds a small but statistically meaningful synthetic corpus, grouped by category.

    Each error-type test below builds corpus statistics from *only* the
    category (or categories) relevant to it, rather than the full mixed
    corpus. This matters at this test corpus's tiny scale (tens of tables,
    not the paper's 100M+): an unrelated category's columns can otherwise
    land in the same coarse feature bucket (e.g. two STRING columns of
    similar row-count) and dilute the very statistics a test is trying to
    isolate. A real deployment's corpus is large and diverse enough that
    featurization separates categories on its own; this grouping exists
    purely to keep *this* small test corpus's signal clean per assertion.
    """
    catalog, schema = uc_location.catalog, uc_location.schema

    import random

    # Each category gets its own, independently-seeded Random instance rather
    # than sharing one. A shared RNG's state after generating category A
    # depends on exactly how many random calls category A happened to make,
    # so any later change to an earlier category (more tables, a wider
    # range, ...) silently changes every later category's draws too -- which
    # is exactly what repeatedly broke the outlier and FD assertions here
    # while isolated single-category debugging (starting from a fresh seed)
    # kept passing. Independent seeds make each category's data reproducible
    # on its own.
    names_rnd = random.Random("uniqueness-names")
    ids_rnd = random.Random("uniqueness-ids")
    votes_rnd = random.Random("outlier-votes")
    figures_rnd = random.Random("outlier-figures")
    romans_rnd = random.Random("spelling-romans")
    long_names_rnd = random.Random("spelling-long-names")
    fd_rnd = random.Random("fd-corpus")
    fd_target_rnd = random.Random("fd-target")

    categories: dict[str, list[str]] = {
        "uniqueness": [],
        "outlier": [],
        "spelling": [],
        "fd": [],
    }

    # 20 distinct roman numerals so sampling without replacement produces
    # syntactically *close but not identical* pairs (MPD=1, e.g. "XIX"/"XX")
    # rather than exact duplicates. Exact duplicates give a trivial MPD=0
    # both in the corpus and in a naive false-positive target, which masks
    # the actual "close pair" false-positive pattern the paper describes
    # (Fig. 2h) and this test is meant to exercise.
    roman_numerals = [
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
    ]

    # --- "boring" corpus tables: common names with coincidental duplicates ---
    common_names = [
        "James Smith",
        "Mary Jones",
        "John Brown",
        "Patricia Davis",
        "Robert Miller",
        "Linda Wilson",
        "Michael Moore",
        "Barbara Taylor",
        "William Anderson",
        "Elizabeth Thomas",
    ]
    for t in range(10):
        n = names_rnd.randint(60, 300)
        values = [names_rnd.choice(common_names) for _ in range(n)]  # lots of natural collisions
        fqn = f"{catalog}.{schema}.corpus_names_{t}"
        _write_table(spark, fqn, [{"name": v} for v in values], ["name"])
        categories["uniqueness"].append(fqn)

    # --- "boring" corpus tables: ID-like unique mixed-alphanumeric columns ---
    for t in range(10):
        n = ids_rnd.randint(60, 300)
        values = [f"ICAO{ids_rnd.randint(100000, 999999)}X{t}{i}" for i in range(n)]
        fqn = f"{catalog}.{schema}.corpus_ids_{t}"
        _write_table(spark, fqn, [{"code": v} for v in values], ["code"])
        categories["uniqueness"].append(fqn)

    # Note: we deliberately do *not* inject extra "near-violation" columns
    # into the uniqueness corpus. Doing so would teach the corpus statistics
    # that a 0.99-before / 1.0-after transition is a *common* pattern for
    # mixed-alphanumeric columns, which directly weakens (and, at this test
    # corpus's tiny scale, can invert) the very surprise signal the
    # assertion below depends on. The `corpus_ids` columns already supply
    # the correct contrast on their own: real ID-like columns are almost
    # always *exactly* unique (before=after=1.0), so a column with
    # before=0.99 stands out as rare on its own, without needing synthetic
    # reinforcement.

    # --- "boring" corpus tables: many small-vote-share candidates (outlier baseline) ---
    # Row counts span from single digits up through the false-positive target's
    # own 44-candidate scale, and a wider table count keeps each row-count
    # sub-bucket adequately populated -- with too few samples per bucket, the
    # ratio becomes highly sensitive to which handful of tables happen to be
    # drawn (the same sparsity issue diagnosed for the "figures" category
    # below, just for this shape of column instead).
    for t in range(30):
        n = votes_rnd.randint(6, 60)
        values = [round(votes_rnd.uniform(0.1, 3.0), 2) for _ in range(n)]
        values[0] = round(votes_rnd.uniform(20, 45), 2)  # one legitimately larger "winner"
        fqn = f"{catalog}.{schema}.corpus_votes_{t}"
        _write_table(spark, fqn, [{"pct": v} for v in values], ["pct"])
        categories["outlier"].append(fqn)

    # --- "boring" corpus tables: clustered large-magnitude figures (outlier baseline) ---
    # The paper's own outlier target (Fig. 4e) lives in the thousands and has
    # a *low* value as its outlier -- the inverse shape of the "many small
    # values, one big winner" vote-share columns above, which land in a
    # different (data_type, log_fit) sub-cube. Without a background category
    # at this scale, that sub-cube would have zero corpus support and any
    # target landing there would be scored as trivially "unsurprising".
    # A *deterministic sweep* of spread (rather than randomized) matters here
    # specifically: the ratio's denominator counts corpus columns whose own
    # natural dispersion is at least as large as the target's post-
    # perturbation score, so if random draws happen not to cover that
    # score's range, the denominator silently collapses to zero (and the
    # Laplace-smoothed ratio degenerates to the default "no evidence, assume
    # normal" 1.0) regardless of how surprising the target actually is. A
    # linear sweep guarantees the full range is represented independent of
    # the random seed.
    for t in range(20):
        n = figures_rnd.randint(6, 20)
        base = figures_rnd.uniform(5000, 15000)
        spread = 300 + t * 400  # sweeps 300 .. ~8000
        values = [round(base + figures_rnd.uniform(-spread, spread), 2) for _ in range(n)]
        fqn = f"{catalog}.{schema}.corpus_figures_{t}"
        _write_table(spark, fqn, [{"amount": v} for v in values], ["amount"])
        categories["outlier"].append(fqn)

    # --- "boring" corpus tables: roman-numeral-suffixed strings (spelling baseline) ---
    for t in range(10):
        n = romans_rnd.randint(6, len(roman_numerals))
        values = [f"Super Bowl {r}" for r in romans_rnd.sample(roman_numerals, n)]
        fqn = f"{catalog}.{schema}.corpus_spelling_{t}"
        _write_table(spark, fqn, [{"event": v} for v in values], ["event"])
        categories["spelling"].append(fqn)

    # --- "boring" corpus tables: distinct long names, no natural close pairs ---
    # The paper's true-positive spelling target (Fig. 4g) has long ("Doeling"/
    # "Dowling"-length) tokens, a different token_length sub-cube than the short
    # roman-numeral tokens above. Without a background category at that token
    # length, that sub-cube would have zero corpus support and any target
    # landing there would be scored as trivially "unsurprising", regardless of
    # how large its own MPD jump is.
    long_names_pool = [
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
    ]
    # A pool of well-separated names alone leaves a coverage gap: the
    # true-positive target's *before* MPD is 1 (its injected close pair), but
    # every well-separated pool sample has its own natural MPD around 9-14,
    # so nothing in the corpus is ever "at least as close as 1" and the
    # ratio's denominator collapses to zero regardless of how the target's
    # own MPD is scored. Deterministically sweeping a constructed pair's edit
    # distance from 1 up guarantees the corpus has *some* entries at every
    # distance the target could land on, independent of the random seed.
    # The differing token itself is kept at a fixed 8-character length (not a
    # long, growing suffix) so it lands in the *same* token_length sub-cube
    # as the target's own "Doeling"/"Dowling"-length (7-char) differing
    # tokens -- a longer constructed token would land in a different bucket
    # and provide no coverage for the one that matters.
    for t in range(8):
        n = long_names_rnd.randint(6, len(long_names_pool))
        k = t + 1
        word_a = "abcdefgh"
        word_b = word_a[: 8 - k] + "z" * k
        values = long_names_rnd.sample(long_names_pool, max(n - 2, 4)) + [
            f"Corpustest {word_a}",
            f"Corpustest {word_b}",
        ]
        fqn = f"{catalog}.{schema}.corpus_long_names_{t}"
        _write_table(spark, fqn, [{"name": v} for v in values], ["name"])
        categories["spelling"].append(fqn)

    # --- "boring" corpus tables: near-FD with no real relationship (large domain) ---
    for t in range(10):
        n = fd_rnd.randint(60, 200)
        lhs = [str(fd_rnd.randint(0, 10_000)) for _ in range(n)]
        rhs = [str(fd_rnd.randint(0, 10_000)) for _ in range(n)]
        fqn = f"{catalog}.{schema}.corpus_fd_{t}"
        _write_table(
            spark, fqn, [{"a": a, "b": b} for a, b in zip(lhs, rhs, strict=True)], ["a", "b"]
        )
        categories["fd"].append(fqn)

    # --- "boring" corpus tables: near-perfect FD with a mixed-alphanumeric RHS ---
    # The true-positive target's RHS ("awardee-0", "awardee-1", ...) is
    # MIXED_ALPHANUMERIC, a different data_type sub-cube than the plain-integer
    # RHS columns above, which had zero support there. A deterministic sweep of
    # injected violation counts (0 up) guarantees corpus coverage across the
    # near-1.0 compliance-ratio range the target's own before-value could land
    # on, independent of the random seed.
    for t in range(10):
        n = 100 + t * 20
        domain = n // 3
        lhs = [str(i % domain) for i in range(n)]
        rhs = [f"item-{i % domain}" for i in range(n)]
        for i in range(t):
            rhs[i] = f"item-{(i + 1) % domain}-x"  # inject t violations
        fqn = f"{catalog}.{schema}.corpus_fd_labels_{t}"
        _write_table(
            spark, fqn, [{"a": a, "b": b} for a, b in zip(lhs, rhs, strict=True)], ["a", "b"]
        )
        categories["fd"].append(fqn)

    return {"catalog": catalog, "schema": schema, "categories": categories, "rnd": fd_target_rnd}


@pytest.fixture
def config(uc_location):
    return UniDetectConfig(
        location=uc_location,
        epsilon=0.05,
        alpha=0.2,
        max_mpd_block_size=200,
        max_fd_column_pairs_per_table=10,
        # The default prevalence edges (50, 100, 1000, ...) are tuned for a
        # web-scale corpus (paper: ~100M tables). This test's synthetic
        # corpus only has a few dozen tables, so a common token like "james"
        # (document frequency ~10, appearing in every "boring names" table)
        # and a random ID token (document frequency ~1, essentially unique)
        # would otherwise both fall into the same "(-inf,50]" bucket and
        # become statistically indistinguishable. Scaling the edges down to
        # match this corpus's size restores the intended separation -- a
        # real deployment tunes this the same way for its own corpus scale.
        prevalence_edges=(2, 5, 20, 100, 1000),
    )


class TestCorpusBuilderAndDetectors:
    def test_uniqueness_true_positive_and_false_positive(
        self, spark, corpus_tables_by_category, config
    ):
        catalog, schema = corpus_tables_by_category["catalog"], corpus_tables_by_category["schema"]
        corpus_tables = corpus_tables_by_category["categories"]["uniqueness"]

        ud = UniDetect(config, spark=spark)
        ud.build_corpus_statistics(
            corpus_tables, error_types=[ErrorType.UNIQUENESS], create_schema=False
        )

        # False-positive-shaped target: common names, one coincidental duplicate (paper Fig. 2a/2b)
        fp_values = [
            "James Smith",
            "Mary Jones",
            "John Brown",
            "Patricia Davis",
            "Robert Miller",
        ] * 20 + [
            "James Smith"
        ]  # 101 values, 1 duplicate -> ~99% unique
        fp_fqn = f"{catalog}.{schema}.target_fp_uniqueness"
        _write_table(spark, fp_fqn, [{"name": v} for v in fp_values], ["name"])

        # True-positive-shaped target: ID-like mixed-alphanumeric column w/ 1 duplicate (paper Fig. 4a/4b)
        tp_values = [f"ICAO{900000 + i}" for i in range(120)]
        tp_values[1] = tp_values[0]
        tp_fqn = f"{catalog}.{schema}.target_tp_uniqueness"
        _write_table(spark, tp_fqn, [{"code": v} for v in tp_values], ["code"])

        result = ud.detect([fp_fqn, tp_fqn], error_types=[ErrorType.UNIQUENESS]).toPandas()

        fp_row = result[result["table_id"] == fp_fqn]
        tp_row = result[result["table_id"] == tp_fqn]
        assert not fp_row.empty
        assert not tp_row.empty

        # The ID-like violation should be scored as *more* surprising (lower
        # lr_ratio) than the common-name coincidence -- the paper's central
        # claim for uniqueness detection.
        assert tp_row["lr_ratio"].iloc[0] < fp_row["lr_ratio"].iloc[0]

    def test_numeric_outlier_true_positive_and_false_positive(
        self, spark, corpus_tables_by_category, config
    ):
        catalog, schema = corpus_tables_by_category["catalog"], corpus_tables_by_category["schema"]
        corpus_tables = corpus_tables_by_category["categories"]["outlier"]

        ud = UniDetect(config, spark=spark)
        ud.build_corpus_statistics(
            corpus_tables, error_types=[ErrorType.NUMERIC_OUTLIER], create_schema=False
        )

        # False positive (paper Example 3/4/5, "C-"): 44 election candidates collapse
        # to this same worked example in the paper -- a handful of small values with
        # one legitimate larger value. Deliberately using the paper's own C-/C+ pair
        # (rather than independently-constructed examples) matters: both have the
        # *same* raw max-MAD score (~8.1, verified in test_metrics.py), which is
        # exactly the paper's point -- raw-score thresholding alone cannot tell them
        # apart, so any difference the assertion below observes must come from the
        # corpus-based reasoning, not from the two targets simply having different
        # raw scores to begin with (as happened with earlier hand-picked examples).
        fp_values = [43.0, 22.0, 9.0, 5.0, 0.76, 0.32, 0.30]
        fp_fqn = f"{catalog}.{schema}.target_fp_outlier"
        _write_table(spark, fp_fqn, [{"pct": v} for v in fp_values], ["pct"])

        # True positive (paper Example 3/4/5, "C+"): "8.716" typo'd in place of "8,716"
        tp_values = [8011.0, 8.716, 9954.0, 11895.0, 13329.0, 11352.0, 11709.0]
        tp_fqn = f"{catalog}.{schema}.target_tp_outlier"
        _write_table(spark, tp_fqn, [{"amount": v} for v in tp_values], ["amount"])

        result = ud.detect([fp_fqn, tp_fqn], error_types=[ErrorType.NUMERIC_OUTLIER]).toPandas()
        fp_row = result[result["table_id"] == fp_fqn]
        tp_row = result[result["table_id"] == tp_fqn]
        assert not fp_row.empty
        assert not tp_row.empty
        assert tp_row["lr_ratio"].iloc[0] < fp_row["lr_ratio"].iloc[0]

    def test_spelling_true_positive_and_false_positive(
        self, spark, corpus_tables_by_category, config
    ):
        catalog, schema = corpus_tables_by_category["catalog"], corpus_tables_by_category["schema"]
        corpus_tables = corpus_tables_by_category["categories"]["spelling"]

        ud = UniDetect(config, spark=spark)
        ud.build_corpus_statistics(
            corpus_tables, error_types=[ErrorType.SPELLING], create_schema=False
        )

        # False positive (paper Fig. 2h): distinct roman-numeral suffixes, syntactically
        # close by design but not misspellings -- exact duplicates would trivially give
        # MPD=0 without exercising the "close but distinct" pattern being tested.
        fp_values = [
            f"Super Bowl {r}" for r in ["XIX", "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI"]
        ]
        fp_fqn = f"{catalog}.{schema}.target_fp_spelling"
        _write_table(spark, fp_fqn, [{"event": v} for v in fp_values], ["event"])

        # True positive (paper Fig. 4g): one genuine misspelling among unrelated long names
        tp_values = [
            "Kevin Doeling",
            "Kevin Dowling",
            "Alan Myerson",
            "Rob Morrow",
            "Patricia Fairweather",
            "Montgomery Higginbotham",
            "Alexandra Winterbourne",
        ]
        tp_fqn = f"{catalog}.{schema}.target_tp_spelling"
        _write_table(spark, tp_fqn, [{"name": v} for v in tp_values], ["name"])

        result = ud.detect([fp_fqn, tp_fqn], error_types=[ErrorType.SPELLING]).toPandas()
        fp_row = result[result["table_id"] == fp_fqn]
        tp_row = result[result["table_id"] == tp_fqn]
        assert not fp_row.empty
        assert not tp_row.empty
        assert tp_row["lr_ratio"].iloc[0] < fp_row["lr_ratio"].iloc[0]

    def test_functional_dependency_true_positive_and_false_positive(
        self, spark, corpus_tables_by_category, config
    ):
        catalog, schema = corpus_tables_by_category["catalog"], corpus_tables_by_category["schema"]
        corpus_tables = corpus_tables_by_category["categories"]["fd"]

        ud = UniDetect(config, spark=spark)
        ud.build_corpus_statistics(
            corpus_tables, error_types=[ErrorType.FUNCTIONAL_DEPENDENCY], create_schema=False
        )

        # False positive: unrelated random columns with a domain small enough that
        # coincidental lhs collisions (and near-certain rhs mismatches) actually
        # occur (paper's "population -> statistical area" case) -- a domain as
        # large as the row count would make collisions vanishingly rare, giving
        # zero violating rows and thus no candidate for the detector to score.
        rnd = corpus_tables_by_category["rnd"]
        n = 150
        fp_a = [str(rnd.randint(0, 300)) for _ in range(n)]
        fp_b = [str(rnd.randint(0, 100_000)) for _ in range(n)]
        fp_fqn = f"{catalog}.{schema}.target_fp_fd"
        _write_table(
            spark, fp_fqn, [{"a": a, "b": b} for a, b in zip(fp_a, fp_b, strict=True)], ["a", "b"]
        )

        # True positive: near-perfect FD (paper Fig. 4c), one violating row
        tp_a = [str(i % 40) for i in range(120)]
        tp_b = [f"awardee-{i % 40}" for i in range(120)]
        tp_b[0] = "awardee-DIFFERENT"  # inject one violation
        tp_fqn = f"{catalog}.{schema}.target_tp_fd"
        _write_table(
            spark, tp_fqn, [{"a": a, "b": b} for a, b in zip(tp_a, tp_b, strict=True)], ["a", "b"]
        )

        result = ud.detect(
            [fp_fqn, tp_fqn], error_types=[ErrorType.FUNCTIONAL_DEPENDENCY]
        ).toPandas()
        fp_row = result[result["table_id"] == fp_fqn]
        tp_row = result[result["table_id"] == tp_fqn]
        assert not fp_row.empty
        assert not tp_row.empty
        assert tp_row["lr_ratio"].iloc[0] < fp_row["lr_ratio"].iloc[0]

    def test_detect_unions_multiple_error_types(self, spark, corpus_tables_by_category, config):
        catalog, schema = corpus_tables_by_category["catalog"], corpus_tables_by_category["schema"]
        corpus_tables = (
            corpus_tables_by_category["categories"]["uniqueness"]
            + corpus_tables_by_category["categories"]["outlier"]
        )

        ud = UniDetect(config, spark=spark)
        ud.build_corpus_statistics(
            corpus_tables,
            error_types=[ErrorType.UNIQUENESS, ErrorType.NUMERIC_OUTLIER],
            create_schema=False,
        )

        fqn = f"{catalog}.{schema}.target_multi"
        rows = [{"code": f"ICAO{900000+i}", "amount": float(1000 + i)} for i in range(60)]
        rows[1]["code"] = rows[0]["code"]
        _write_table(spark, fqn, rows, ["code", "amount"])

        result = ud.detect(
            [fqn], error_types=[ErrorType.UNIQUENESS, ErrorType.NUMERIC_OUTLIER]
        ).toPandas()
        assert set(result["error_type"].unique()) <= {"uniqueness", "numeric_outlier"}
        # results must be sorted ascending by lr_ratio
        assert list(result["lr_ratio"]) == sorted(result["lr_ratio"])

    def test_write_detections_round_trips_through_delta(
        self, spark, corpus_tables_by_category, config
    ):
        catalog, schema = corpus_tables_by_category["catalog"], corpus_tables_by_category["schema"]
        corpus_tables = corpus_tables_by_category["categories"]["uniqueness"]

        ud = UniDetect(config, spark=spark)
        ud.build_corpus_statistics(
            corpus_tables, error_types=[ErrorType.UNIQUENESS], create_schema=False
        )

        fqn = f"{catalog}.{schema}.target_writeback"
        rows = [{"code": f"ICAO{900000+i}"} for i in range(60)]
        rows[1]["code"] = rows[0]["code"]
        _write_table(spark, fqn, rows, ["code"])

        detections = ud.detect([fqn], error_types=[ErrorType.UNIQUENESS])
        ud.write_detections(detections, mode="overwrite")

        read_back = spark.table(config.detections_fqn)
        assert read_back.count() == detections.count()
