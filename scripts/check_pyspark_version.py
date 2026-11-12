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
        import tomli as tomllib
    except ImportError:
        print(
            "ERROR: tomllib (Python 3.11+) or tomli (Python 3.10) required to parse pyproject.toml"
        )
        print("Install tomli with: pip install tomli")
        sys.exit(1)


def main():
    with open("pyproject.toml", "rb") as f:
        data = tomllib.load(f)

    deps = data.get("project", {}).get("dependencies", [])
    pyspark = next((d for d in deps if d.lower().startswith("pyspark")), None)
    if pyspark is None:
        print("ERROR: pyspark not found in pyproject.toml dependencies")
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