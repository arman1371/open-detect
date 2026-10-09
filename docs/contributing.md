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

## Commit conventions and releases

Releases are fully automated. The version number, the tag, the GitHub Release and
[`CHANGELOG.md`](changelog.md) are all derived from the commit messages on `main`, using
[Conventional Commits](https://www.conventionalcommits.org/) and
[python-semantic-release](https://python-semantic-release.readthedocs.io/).

### Writing commits and PR titles

Pull requests are **squash-merged**, so the **PR title becomes the commit message on `main`** and
is what decides the release. CI rejects PR titles that are not Conventional Commits.

```text
<type>(<optional scope>)<!>: <short imperative summary>
```

| Type | Release effect | Changelog section |
|---|---|---|
| `feat` | minor | Features |
| `fix` | patch | Bug Fixes |
| `perf` | patch | Performance Improvements |
| `docs` | none | Documentation |
| `refactor`, `revert` | none | Refactoring, Reverts |
| `build`, `ci`, `chore`, `style`, `test` | none | not listed |
| any type with `!` (e.g. `feat(api)!:`) or a `BREAKING CHANGE:` footer | see below | Breaking Changes |

Examples: `feat(raha): add a value-length strategy`, `fix: handle all-null columns`,
`feat(api)!: rename detect() to run()`.

A breaking change must be explained in the commit body, so put a `BREAKING CHANGE: ...` paragraph
in the PR description (it is copied into the squash commit) in addition to the `!` in the title.

**Versions below 1.0.0.** While the version is `0.y.z`, a breaking change bumps the **minor**
number (`0.2.0` to `0.3.0`) and `feat` also bumps minor, `fix`/`perf` bump patch. The jump to
`1.0.0` is deliberate: run the Release workflow manually with `force: major` when the public API
is ready to be called stable.

### How a release happens

1. A PR is squash-merged into `main`.
2. The **CI** workflow runs on `main`. If it passes, the **Release** workflow starts.
3. python-semantic-release looks at the commits since the last `v*` tag. If none of them is a
   `feat`, `fix`, `perf` or breaking change, nothing happens.
4. Otherwise it updates `version` in `pyproject.toml` and `uv.lock`, prepends the new section to
   `CHANGELOG.md`, commits `chore(release): vX.Y.Z [skip ci]`, tags `vX.Y.Z`, builds the sdist and
   wheel, creates the GitHub Release (notes are the changelog section, with a compare link) and
   attaches both files.
5. The docs site is redeployed so the [Changelog](changelog.md) page is current.

The `[skip ci]` marker on the release commit is what prevents the release from triggering itself.

To preview or force a release, open **Actions, Release, Run workflow**. It defaults to a dry run
that only reports the last tag and the next version in the job summary. Uncheck `dry_run` to
release for real, and use `force` to override the bump level. The same preview works locally
without any credentials:

```bash
uvx --from "python-semantic-release>=10,<11" semantic-release --noop version --print
```

### First release bootstrap

The project was at `0.2.0` before releases were automated. Create the baseline tag once, on the
commit that `0.2.0` describes, so the first automated release does not replay the whole history:

```bash
git tag -a v0.2.0 <commit-sha> -m "v0.2.0 baseline"
git push origin v0.2.0
```

(Already done for this repository: `v0.2.0` points at the project rename commit `46a1237`.)

The Release workflow refuses to run until a `v*` tag exists. After this, the first `feat` or
`fix` merged to `main` produces `v0.3.0` (or `v0.2.1`).

### Required repository settings

| Setting | Where | Value |
|---|---|---|
| Workflow permissions | Settings, Actions, General | **Read and write permissions** (the release job pushes a commit and a tag) |
| Merge method | Settings, General, Pull Requests | Allow **squash merging** only; "Default commit message" = **Pull request title** (or title and description) |
| Required status check | Settings, Branches (or Rules), `main` | Require **CI passed** (the single aggregate job in `ci.yml`) |
| Ruleset bypass for the release bot | Settings, Rules, Rulesets, `main` ruleset, Bypass list | Add **Deploy keys** with mode *Always allow*. The `main` ruleset requires PRs for everyone and `GITHUB_TOKEN` cannot be a bypass actor, so the release job pushes its commit and tag over SSH with a deploy key. |
| Deploy key + `RELEASE_DEPLOY_KEY` secret | Settings, Deploy keys; Settings, Secrets and variables, Actions | Generate a key pair (`ssh-keygen -t ed25519 -N "" -f release-key`), add `release-key.pub` as a deploy key with **Allow write access**, and store the private key as the secret `RELEASE_DEPLOY_KEY`. Rotate by repeating this and deleting the old key. |

### Publishing to PyPI (optional, off by default)

The `pypi` job in `release.yml` uses [trusted publishing](https://docs.pypi.org/trusted-publishers/)
(OIDC), so no API token is stored. It only runs when the repository variable `PUBLISH_TO_PYPI` is
`true`. One-time setup:

1. On PyPI, add a **pending publisher** for project `open-detect`: owner `arman1371`, repository
   `open-detect`, workflow `release.yml`, environment `pypi`.
2. In GitHub, create an environment named `pypi` (Settings, Environments), optionally with required
   reviewers.
3. Set the repository variable `PUBLISH_TO_PYPI` to `true` (Settings, Secrets and variables,
   Actions, Variables).

## Adding an algorithm

Follow [Writing your own algorithm](guides/writing-an-algorithm.md). To make it a built-in, put
it in `src/open_detect/algorithms/<name>/` and register it lazily in
`src/open_detect/algorithms/__init__.py` next to the existing three. Add a section to
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
