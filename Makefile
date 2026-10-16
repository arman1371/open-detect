.PHONY: install dev-install lint format type-check test test-fast cov build clean benchmark benchmark-real-world-gov benchmark-all benchmark-profile benchmark-diff

install:
	uv sync --no-dev

dev-install:
	uv sync

lint:
	uv run ruff check src tests benchmarks

format:
	uv run ruff check --fix src tests benchmarks
	uv run black src tests benchmarks

type-check:
	uv run mypy src

test:
	uv run pytest

test-fast:
	uv run pytest tests --deselect tests/algorithms/uni_detect/test_corpus_and_detectors.py --deselect tests/algorithms/uni_detect/test_corpus_edge_cases.py

cov:
	uv run pytest --cov=open_detect --cov-report=term-missing --cov-report=html

benchmark:
	uv run python benchmarks/wiki_subset/run_benchmark.py

benchmark-real-world-gov:
	uv run python benchmarks/real_world_gov/run_benchmark.py

benchmark-all: benchmark benchmark-real-world-gov

# Opt-in perf profile: Uni-Detect detections snapshot + Spark job counts per phase
# (writes benchmarks/*/results/profile/$(PROFILE_NAME)/{detections.csv,perf.json}).
# `make benchmark-profile PROFILE_NAME=baseline` regenerates the committed baseline.
PROFILE_NAME ?= latest

benchmark-profile:
	uv run python benchmarks/wiki_subset/run_benchmark.py --profile-dir benchmarks/wiki_subset/results/profile/$(PROFILE_NAME)
	uv run python benchmarks/real_world_gov/run_benchmark.py --profile-dir benchmarks/real_world_gov/results/profile/$(PROFILE_NAME)

# Diff the latest profile run against the committed baseline snapshot; non-zero exit on any
# difference. The baseline snapshot is the committed ``benchmarks/*/results/profile/baseline``
# directory (regenerate with ``make benchmark-profile PROFILE_NAME=baseline``); the latest run
# writes ``benchmarks/*/results/profile/latest``. Datasets without a committed baseline or a
# latest run are skipped rather than failing the whole target.
benchmark-diff:
	@for ds in wiki_subset real_world_gov; do \
	  base="benchmarks/$$ds/results/profile/baseline"; \
	  latest="benchmarks/$$ds/results/profile/latest"; \
	  if [ -f "$$base/detections.csv" ] && [ -f "$$latest/detections.csv" ]; then \
	    uv run python benchmarks/common/snapshot.py diff "$$base" "$$latest" || exit 1; \
	  else \
	    echo "SKIP $$ds: missing baseline or latest profile snapshot"; \
	  fi; \
	done

# Convenience: diff the latest run against itself (sanity check that the diff tool reads the
# profile dir layout written by ``make benchmark-profile``).
benchmark-diff-selfcheck:
	uv run python benchmarks/common/snapshot.py diff benchmarks/wiki_subset/results/profile/latest benchmarks/wiki_subset/results/profile/latest
	uv run python benchmarks/common/snapshot.py diff benchmarks/real_world_gov/results/profile/latest benchmarks/real_world_gov/results/profile/latest

build:
	uv build

clean:
	rm -rf build dist *.egg-info src/*.egg-info .pytest_cache .mypy_cache .ruff_cache htmlcov .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
