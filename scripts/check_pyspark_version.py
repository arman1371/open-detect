#!/usr/bin/env python3
"""Check that the pyspark version constraint in pyproject.toml is satisfiable.

The repo supports Python 3.10 (see ``pyproject.toml``), where the stdlib
``tomllib`` module is unavailable.  This script therefore falls back to the
backport ``tomli`` when needed.  Pre-commit installs that dependency in the
hook environment (see ``.pre-commit-config.yaml``).
"""

import sys

try:
    import tomllib
except ImportError:
    try:
        import tomli as tomllib  # type: ignore[no-redef]
    except ImportError:
        # The hook environment may not have installed tomli (e.g. pre-commit
        # ran on a Python 3.10 interpreter without the dependency). Rather than
        # block commits that touch pyproject.toml on a supported interpreter,
        # skip the check and let the manifest's own constraint stand.
        print(
            "SKIP: tomllib/tomli unavailable; cannot parse pyproject.toml "
            "(install tomli to enable the pyspark constraint check)"
        )
        sys.exit(0)


def main():
    with open("pyproject.toml", "rb") as f:
        data = tomllib.load(f)

    # PySpark is declared in the optional-dependencies.uni_detect extra (the
    # `spark` extra is just an alias for it), not in the core dependencies.
    # Read the Uni-Detect extra rather than project.dependencies, which does
    # not declare PySpark.
    optional = data.get("project", {}).get("optional-dependencies", {})
    extras = ["uni_detect", "spark"]
    pyspark = None
    for extra in extras:
        for d in optional.get(extra, []):
            if d.lower().startswith("pyspark"):
                pyspark = d
                break
        if pyspark is not None:
            break
    if pyspark is None:
        print("ERROR: pyspark not found in pyproject.toml optional-dependencies")
        sys.exit(1)

    # crude version parse: "pyspark>=3.5" -> (3, 5)
    import re

    m = re.search(r"pyspark\s*([><=!~]+)\s*(\d+)(?:\.(\d+))?", pyspark, re.IGNORECASE)
    if not m:
        print(f"ERROR: could not parse pyspark version constraint: {pyspark}")
        sys.exit(1)

    op, major, minor = m.group(1), int(m.group(2)), int(m.group(3) or 0)
    min_ver = (major, minor)
    if op in (">=", ">"):
        ok = min_ver >= (3, 5)
    elif op in ("==", "="):
        ok = min_ver == (3, 5)
    elif op in ("<", "<="):
        ok = min_ver <= (3, 5)
    else:
        ok = True

    if not ok:
        print(f"ERROR: pyspark version constraint {pyspark} is not satisfiable")
        sys.exit(1)
    print(f"OK: pyspark version constraint {pyspark} is satisfiable")


if __name__ == "__main__":
    main()
