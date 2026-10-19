# Workflow tool requirements

Hash-pinned requirements for tools installed in privileged workflows (`release.yml`,
`update-knowledge-graph.yml`). Installed with `--require-hashes`, so a tampered or newly
published release of the tool or any transitive dependency cannot be pulled in silently.

Regenerate after editing a `.in` file (or let Dependabot do it):

```sh
cd .github/requirements
uv pip compile --universal --generate-hashes --python-version 3.11 --no-header --no-annotate graphify.in -o graphify.txt
uv pip compile --universal --generate-hashes --python-version 3.11 --no-header --no-annotate semantic-release.in -o semantic-release.txt
```
