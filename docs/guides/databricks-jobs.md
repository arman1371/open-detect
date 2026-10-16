# Running on Databricks

Uni-Detect is designed to run as scheduled Databricks jobs against Unity Catalog. The repository
ships a [Databricks Asset Bundle](https://docs.databricks.com/en/dev-tools/bundles/) and two
notebooks.

## Jobs

`databricks.yml` defines two jobs — one per phase. Each is installed under a primary name
and a backward-compatible alias; all four names are console scripts in the wheel.

| Job | Phase | Default schedule | Primary name | Alias |
|---|---|---|---|---|
| Offline: learn corpus statistics | build | Weekly, Sunday 03:00 UTC | `open_detect_build_corpus` | `build_corpus_statistics_job` |
| Online: scan target tables | detect | On demand or scheduled | `open_detect_run_detection` | `run_detection_job` |

The aliases exist because Databricks `python_wheel_tasks` reference entry-point names, and
existing bundles already call the old names. Both names for a phase resolve to the same
console script.

```bash
databricks bundle deploy -t dev
databricks bundle run build_corpus_statistics_job -t dev
databricks bundle run open_detect_build_corpus -t dev
databricks bundle run run_detection_job -t dev -- --target-tables main.sales.orders
databricks bundle run open_detect_run_detection -t dev -- --target-tables main.sales.orders
```

Bundle variables (`open_detect_catalog`, `open_detect_schema`, `corpus_catalog`) set where the
library's tables live and which catalog is scanned for the corpus.

## Job arguments

=== "build_corpus_statistics_job"

    | Argument | Required | Description |
    |---|---|---|
    | `--catalog`, `--schema` | yes | Where `open-detect`'s own tables are created |
    | `--corpus-tables` | no | Comma-separated fully-qualified tables to use as the corpus |
    | `--corpus-catalog` | if no `--corpus-tables` | Catalog to scan for corpus tables |
    | `--corpus-schemas` | no | Comma-separated schemas within `--corpus-catalog` (default: all) |
    | `--error-types` | no | Comma-separated subset of `uniqueness,functional_dependency,numeric_outlier,spelling` |
    | `--epsilon`, `--alpha` | no | Defaults `0.01` and `0.05` |

=== "run_detection_job"

    | Argument | Required | Description |
    |---|---|---|
    | `--catalog`, `--schema` | yes | Where `open-detect`'s own tables live |
    | `--target-tables` | yes | Comma-separated fully-qualified tables to scan |
    | `--error-types` | no | Comma-separated subset of error types (default: all) |
    | `--epsilon` | no | Maximum perturbation size (default `0.01`); must match the corpus build |
    | `--alpha` | no | Significance level (default `0.05`) |
    | `--allow-config-mismatch` | no | Log instead of failing when the corpus was built with a different epsilon/bucket configuration |
    | `--top-k` | no | Keep only the K most surprising results |
    | `--write-results` | no | Append results to the detections table |

## Notebooks

For interactive use, import `notebooks/01_build_corpus_statistics.py` and
`notebooks/02_run_detection.py`. They expose the same settings as widgets.

## Practical advice

- **Run the offline job first.** Detection raises `CorpusNotFoundError` until statistics exist.
- **Refresh on a schedule that matches how fast your data changes.** Weekly is a sensible default.
- **Use `--write-results` for monitoring.** Appending to the detections table gives you history
  you can chart and alert on.
- **Governed access.** Jobs read the tables they are told to scan, so run them under a principal
  with `SELECT` on the corpus and targets and `CREATE TABLE` on the `open-detect` schema.
