.PHONY: help uv project install freeze test lint format run

help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "Setup:"
	@echo "  uv       - Install uv package manager"
	@echo "  project  - Create venv and install dependencies"
	@echo "  install  - Install package in editable mode with dev deps"
	@echo "  freeze   - List installed packages"
	@echo ""
	@echo "Development:"
	@echo "  test     - Run tests"
	@echo "  lint     - Run ruff linter"
	@echo "  format   - Auto-fix lint issues"
	@echo "  run      - Run demo script"

uv:
	curl -LsSf https://astral.sh/uv/install.sh | sh

project:
	uv venv --clear
	uv sync --extra dev

install:
	uv pip install -e ".[dev]"

freeze:
	uv pip freeze

test:
	uv run pytest -v

lint:
	uv run ruff check .

format:
	uv run ruff check . --fix

run:
	uv run python main.py
