.PHONY: all venv project install freeze test lint run

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

run:
	uv run python main.py

lint:
	uv run ruff check .
