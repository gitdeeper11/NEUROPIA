# NEUROPIA (E-LAB-10) Makefile

.PHONY: help install test lint format clean build deploy

help:
	@echo "Available commands:"
	@echo "  make install    - Install package in development mode"
	@echo "  make test       - Run tests"
	@echo "  make lint       - Run linters"
	@echo "  make format     - Format code"
	@echo "  make clean      - Clean build artifacts"
	@echo "  make build      - Build distribution packages"
	@echo "  make deploy     - Deploy to PyPI"

install:
	pip install -e .[dev]

test:
	pytest tests/ -v --cov=neuropia

lint:
	flake8 neuropia/
	mypy neuropia/

format:
	black neuropia/ tests/
	isort neuropia/ tests/

clean:
	rm -rf build/ dist/ *.egg-info .pytest_cache .coverage htmlcov
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

build: clean
	python -m build

deploy: build
	twine upload dist/*
