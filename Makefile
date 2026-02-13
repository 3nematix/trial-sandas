.PHONY: all venv project install freeze test lint

all: venv project

venv:
	uv venv --clear

project:
	uv sync --extra dev

install:
	uv pip install -e ".[dev]"

freeze:
	uv pip freeze

test:
	uv run pytest -v

lint:
	uv run ruff check .
