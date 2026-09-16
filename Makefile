.PHONY: install dev-install lint format type-check test test-fast cov build clean

install:
	pip install .

dev-install:
	pip install -e ".[dev]"

lint:
	ruff check src tests

format:
	ruff check --fix src tests
	black src tests

type-check:
	mypy src

test:
	pytest

test-fast:
	pytest tests/test_metrics.py tests/test_perturbation.py tests/test_featurization.py tests/test_config.py tests/test_text_utils.py

cov:
	pytest --cov=unidetect --cov-report=term-missing --cov-report=html

build:
	python -m build

clean:
	rm -rf build dist *.egg-info src/*.egg-info .pytest_cache .mypy_cache .ruff_cache htmlcov .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
