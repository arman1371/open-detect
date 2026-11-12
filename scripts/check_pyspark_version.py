#!/usr/bin/env python3
"""
Check that pyproject.toml has the correct pyspark version constraint (>=3.5,<4.0)
in the dependency-groups.dev section.
"""

import re
import sys

try:
    import tomllib
except ImportError:
    try:
        import tomli as tomllib
    except ImportError:
        print("ERROR: tomllib (Python 3.11+) or tomli (Python 3.10) required to parse pyproject.toml")
        sys.exit(1)


def main():
    with open("pyproject.toml", "rb") as f:
        data = tomllib.load(f)

    # Check dependency-groups.dev for pyspark constraint
    dev_deps = data.get("dependency-groups", {}).get("dev", [])
    pyspark_found = False
    pyspark_correct = False

    for dep in dev_deps:
        if dep.startswith("pyspark"):
            pyspark_found = True
            # Check if it matches >=3.5,<4.0
            if re.match(r"pyspark>=3\.5,<4\.0", dep):
                pyspark_correct = True
            else:
                print(f"ERROR: pyspark version constraint in pyproject.toml is incorrect: {dep}")
                print("Expected: pyspark>=3.5,<4.0")
                sys.exit(1)

    if not pyspark_found:
        print("ERROR: pyspark not found in dependency-groups.dev")
        sys.exit(1)

    if pyspark_correct:
        print("OK: pyspark version constraint is correct (>=3.5,<4.0)")


if __name__ == "__main__":
    main()
