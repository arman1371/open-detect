.PHONY: install dev-install lint format type-check test test-fast cov build clean benchmark benchmark-real-world-gov benchmark-all

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
	uv run pytest tests/test_metrics.py tests/test_perturbation.py tests/test_featurization.py tests/test_config.py tests/test_text_utils.py

cov:
	uv run pytest --cov=unidetect --cov-report=term-missing --cov-report=html

benchmark:
	uv run python benchmarks/wiki_subset/run_benchmark.py

benchmark-real-world-gov:
	uv run python benchmarks/real_world_gov/run_benchmark.py

benchmark-all: benchmark benchmark-real-world-gov

build:
	uv build

clean:
	rm -rf build dist *.egg-info src/*.egg-info .pytest_cache .mypy_cache .ruff_cache htmlcov .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
