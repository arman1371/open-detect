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
