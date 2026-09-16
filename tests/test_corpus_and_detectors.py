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
def corpus_and_target_tables(spark, uc_location):
    """Builds a small but statistically meaningful synthetic corpus.

    The corpus contains many "boring" columns (common names/dates with
    occasional coincidental duplicates, chemical-formula-like short-distance
    string columns, multi-candidate vote columns with a dominant winner) so
    that the *background* statistics correctly treat the paper's
    false-positive examples as unsurprising, while still containing enough
    genuine near-constraints (ID-like unique columns, tight numeric
    columns, near-duplicate name pairs, near-FDs) that the true-positive
    examples stand out as surprising.
    """
    catalog, schema = uc_location.catalog, uc_location.schema
    tables: list[str] = []

    import random

    rnd = random.Random(42)

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
        n = rnd.randint(60, 300)
        values = [rnd.choice(common_names) for _ in range(n)]  # lots of natural collisions
        fqn = f"{catalog}.{schema}.corpus_names_{t}"
        _write_table(spark, fqn, [{"name": v} for v in values], ["name"])
        tables.append(fqn)

    # --- "boring" corpus tables: ID-like unique mixed-alphanumeric columns ---
    for t in range(10):
        n = rnd.randint(60, 300)
        values = [f"ICAO{rnd.randint(100000, 999999)}X{t}{i}" for i in range(n)]
        fqn = f"{catalog}.{schema}.corpus_ids_{t}"
        _write_table(spark, fqn, [{"code": v} for v in values], ["code"])
        tables.append(fqn)

    # --- "boring" corpus tables: many small-vote-share candidates (outlier baseline) ---
    for t in range(10):
        n = rnd.randint(20, 60)
        values = [round(rnd.uniform(0.1, 3.0), 2) for _ in range(n)]
        values[0] = round(rnd.uniform(20, 45), 2)  # one legitimately larger "winner"
        fqn = f"{catalog}.{schema}.corpus_votes_{t}"
        _write_table(spark, fqn, [{"pct": v} for v in values], ["pct"])
        tables.append(fqn)

    # --- "boring" corpus tables: roman-numeral-suffixed strings (spelling baseline) ---
    for t in range(10):
        n = rnd.randint(20, 80)
        romans = ["XIX", "XX", "XXI", "XXII", "XXIII", "XXIV"]
        values = [f"Super Bowl {rnd.choice(romans)}" for _ in range(n)]
        fqn = f"{catalog}.{schema}.corpus_spelling_{t}"
        _write_table(spark, fqn, [{"event": v} for v in values], ["event"])
        tables.append(fqn)

    # --- "boring" corpus tables: near-FD with no real relationship (large domain) ---
    for t in range(10):
        n = rnd.randint(60, 200)
        lhs = [str(rnd.randint(0, 10_000)) for _ in range(n)]
        rhs = [str(rnd.randint(0, 10_000)) for _ in range(n)]
        fqn = f"{catalog}.{schema}.corpus_fd_{t}"
        _write_table(
            spark, fqn, [{"a": a, "b": b} for a, b in zip(lhs, rhs, strict=True)], ["a", "b"]
        )
        tables.append(fqn)

    # --- genuine near-constraints, also placed in the corpus so the model has positives ---
    for t in range(5):
        n = rnd.randint(80, 150)
        values = [f"CODE{rnd.randint(0, 999999)}Z{t}{i}" for i in range(n)]
        values[1] = values[0]  # inject one true duplicate into an ID-like column
        fqn = f"{catalog}.{schema}.corpus_true_unique_violation_{t}"
        _write_table(spark, fqn, [{"code": v} for v in values], ["code"])
        tables.append(fqn)

    return {"catalog": catalog, "schema": schema, "corpus_tables": tables, "rnd": rnd}


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
        self, spark, corpus_and_target_tables, config
    ):
        catalog, schema = corpus_and_target_tables["catalog"], corpus_and_target_tables["schema"]
        corpus_tables = corpus_and_target_tables["corpus_tables"]

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
        self, spark, corpus_and_target_tables, config
    ):
        catalog, schema = corpus_and_target_tables["catalog"], corpus_and_target_tables["schema"]
        corpus_tables = corpus_and_target_tables["corpus_tables"]

        ud = UniDetect(config, spark=spark)
        ud.build_corpus_statistics(
            corpus_tables, error_types=[ErrorType.NUMERIC_OUTLIER], create_schema=False
        )

        # False positive (paper Fig. 2e): many small-share candidates, one legitimate winner
        fp_values = [round(v, 2) for v in [0.3, 0.4, 0.5, 0.6, 0.76, 0.9, 1.1, 1.2, 22.0]]
        fp_fqn = f"{catalog}.{schema}.target_fp_outlier"
        _write_table(spark, fp_fqn, [{"pct": v} for v in fp_values], ["pct"])

        # True positive (paper Fig. 4e): "8.716" typo'd in place of "8,716"
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
        self, spark, corpus_and_target_tables, config
    ):
        catalog, schema = corpus_and_target_tables["catalog"], corpus_and_target_tables["schema"]
        corpus_tables = corpus_and_target_tables["corpus_tables"]

        ud = UniDetect(config, spark=spark)
        ud.build_corpus_statistics(
            corpus_tables, error_types=[ErrorType.SPELLING], create_schema=False
        )

        # False positive (paper Fig. 2h): roman-numeral suffixes, syntactically close by design
        fp_values = ["Super Bowl XIX", "Super Bowl XX", "Super Bowl XXI", "Super Bowl XXII"] * 5
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
        self, spark, corpus_and_target_tables, config
    ):
        catalog, schema = corpus_and_target_tables["catalog"], corpus_and_target_tables["schema"]
        corpus_tables = corpus_and_target_tables["corpus_tables"]

        ud = UniDetect(config, spark=spark)
        ud.build_corpus_statistics(
            corpus_tables, error_types=[ErrorType.FUNCTIONAL_DEPENDENCY], create_schema=False
        )

        # False positive: large, unrelated random domains (paper's "population -> statistical area" case)
        rnd = corpus_and_target_tables["rnd"]
        n = 150
        fp_a = [str(rnd.randint(0, 100_000)) for _ in range(n)]
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

    def test_detect_unions_multiple_error_types(self, spark, corpus_and_target_tables, config):
        catalog, schema = corpus_and_target_tables["catalog"], corpus_and_target_tables["schema"]
        corpus_tables = corpus_and_target_tables["corpus_tables"]

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
        self, spark, corpus_and_target_tables, config
    ):
        catalog, schema = corpus_and_target_tables["catalog"], corpus_and_target_tables["schema"]
        corpus_tables = corpus_and_target_tables["corpus_tables"]

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
