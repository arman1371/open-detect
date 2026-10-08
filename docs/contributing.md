# Contributing

The project uses [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/arman1371/open-detect
cd open-detect
uv sync                # installs runtime + dev dependencies
```

## Everyday commands

| Command | Does |
|---|---|
| `make test` | Full test suite. Spark/Delta integration tests skip themselves if no local Delta-enabled Spark session can start. |
| `make test-fast` | Pure-Python unit tests only. No JVM needed. |
| `make lint` | `ruff check` |
| `make format` | `ruff --fix` and `black` |
| `make type-check` | `mypy src` |
| `make cov` | Tests with a coverage report |

Run Spark integration tests under **JDK 17**.

## Adding an algorithm

Follow [Writing your own algorithm](guides/writing-an-algorithm.md). To make it a built-in, put
it in `src/unidetect/algorithms/<name>/` and register it lazily in
`src/unidetect/algorithms/__init__.py` next to the existing three. Add a section to
`ARCHITECTURE.md` mapping the paper to the code, and add it to the benchmarks.

## Working on these docs

The site is built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and the API
reference is generated from docstrings by [mkdocstrings](https://mkdocstrings.github.io/).

```bash
python -m pip install -r docs/requirements.txt
mkdocs serve            # live-reloading preview at http://127.0.0.1:8000
mkdocs build --strict   # what CI runs; fails on broken links and unresolved references
```

- Pages live in `docs/`; navigation is in `mkdocs.yml`.
- The [Architecture](architecture.md) page is the repository's `ARCHITECTURE.md`, included as is.
  Edit that file, not the page.
- Reference pages use `::: module.path` directives. A new public class or function needs a
  directive to appear.
- Prefer examples you have run. Keep output blocks in sync with what the code prints.

The site is published to GitHub Pages by `.github/workflows/docs.yml` on every push to `main`
that touches docs, `mkdocs.yml`, `ARCHITECTURE.md` or `src/`.

## Knowledge graph automation

`.github/workflows/update-knowledge-graph.yml` runs `graphify update .` on every push to `main`
and opens (or updates) a single PR from branch `chore/update-knowledge-graph` that refreshes
`graphify-out/graph.json`, `graph.html` and `GRAPH_REPORT.md`. The PR is set to squash
auto-merge, so it lands once the required `SonarQube Quality Gate` check passes. The workflow
never pushes to `main`.

**One-time repository setup**

- Settings > General > Pull Requests: enable **Allow auto-merge** and **Allow squash merging**.
- Create a [fine-grained personal access token](https://github.com/settings/personal-access-tokens)
  limited to this repository only, with **Contents: Read and write** and **Pull requests: Read and
  write** (Metadata: Read is automatic) and nothing else. Use the longest expiry allowed
  (at most one year), and store it as the repository secret **`GRAPH_PR_TOKEN`**.
- Rotate the token before it expires: generate a new one, update the secret, and record the next
  renewal date here. If the token lapses, the workflow fails at the pull request step.

A PAT (or GitHub App token) is required because PRs created with the default `GITHUB_TOKEN` do not
trigger other workflows, so the required Sonar check would never run. A GitHub App with the same
two permissions plus `actions/create-github-app-token` is the stronger long-term option: its
tokens are short-lived and not tied to a person.

**Loop prevention**

- The push trigger uses `paths-ignore: graphify-out/**`, so merging the graph PR (which only touches
  `graphify-out/`) does not re-run the workflow. Pushes that also change other files still trigger it.
- The job is skipped when the head commit message starts with `chore: update knowledge graph`,
  except for manual `workflow_dispatch` runs.
