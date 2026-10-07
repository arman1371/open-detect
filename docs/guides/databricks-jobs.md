# Running on Databricks

Uni-Detect is designed to run as scheduled Databricks jobs against Unity Catalog. The repository
ships a [Databricks Asset Bundle](https://docs.databricks.com/en/dev-tools/bundles/) and two
notebooks.

## Jobs

`databricks.yml` defines two jobs:

| Job | Phase | Default schedule |
|---|---|---|
| `build_corpus_statistics_job` | Offline: learn corpus statistics | Weekly, Sunday 03:00 UTC |
| `run_detection_job` | Online: scan target tables | On demand or scheduled |

Both are installed as console scripts by the wheel (`build_corpus_statistics_job`,
`run_detection_job`).

```bash
databricks bundle deploy -t dev
databricks bundle run build_corpus_statistics_job -t dev
databricks bundle run run_detection_job -t dev -- --target-tables main.sales.orders
```

Bundle variables (`unidetect_catalog`, `unidetect_schema`, `corpus_catalog`) set where the
library's tables live and which catalog is scanned for the corpus.

## Job arguments

=== "build_corpus_statistics_job"

    | Argument | Required | Description |
    |---|---|---|
    | `--catalog`, `--schema` | yes | Where `unidetect`'s own tables are created |
    | `--corpus-tables` | no | Comma-separated fully-qualified tables to use as the corpus |
    | `--corpus-catalog` | if no `--corpus-tables` | Catalog to scan for corpus tables |
    | `--corpus-schemas` | no | Comma-separated schemas within `--corpus-catalog` (default: all) |
    | `--error-types` | no | Comma-separated subset of `uniqueness,functional_dependency,numeric_outlier,spelling` |
    | `--epsilon`, `--alpha` | no | Defaults `0.01` and `0.05` |

=== "run_detection_job"

    | Argument | Required | Description |
    |---|---|---|
    | `--catalog`, `--schema` | yes | Where `unidetect`'s own tables live |
    | `--target-tables` | yes | Comma-separated fully-qualified tables to scan |
    | `--error-types` | no | Comma-separated subset of error types (default: all) |
    | `--alpha` | no | Significance level (default `0.05`) |
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
  with `SELECT` on the corpus and targets and `CREATE TABLE` on the `unidetect` schema.
