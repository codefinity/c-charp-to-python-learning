# AGENTS.md

Guidance for coding agents and contributors working in this repository.

## Project Purpose

This repo is a tutorial codebase that helps experienced C#/.NET developers become advanced, production-ready Python developers.

Key goals:
- Keep all concept examples runnable.
- Keep README links and code paths in sync.
- Preserve a clean learning progression from simple to advanced.

## Repository Layout

- `src/csharp_to_python_learning/concepts/`: Main tutorial concepts, grouped by numbered folders.
- `src/csharp_to_python_learning/python_only_features/`: Runnable Python-only feature examples.
- `src/csharp_to_python_learning/capstone/`: Final combined capstone example.
- `tests/`: Smoke tests for representative scripts.
- `scripts/scaffold_tutorial.py`: Source-of-truth scaffolder that can regenerate tutorial files and README.

## Python and Tooling

- Python version: `3.14.5` (see `.python-version`).
- Package/tool runner: `uv`.
- Lint/format: `ruff`.
- Tests: `pytest`.
- Optional static typing: `mypy`.

## Common Commands

- Install/sync environment:
  - `uv sync -p 3.14.5`
- Run tests:
  - `uv run -p 3.14.5 -m pytest`
- Lint:
  - `uv run -p 3.14.5 ruff check .`
- Format:
  - `uv run -p 3.14.5 ruff format .`
- Type-check:
  - `uv run -p 3.14.5 mypy src tests`
- Run one concept script:
  - `uv run -p 3.14.5 src/csharp_to_python_learning/concepts/<folder>/topic_xx_*.py`

## Change Rules

1. Keep examples runnable as standalone scripts.
2. When moving/renaming concept files or folders, update:
   - `README.md`
   - `tests/test_concept_smoke.py`
   - `scripts/scaffold_tutorial.py`
3. Do not leave broken README links.
4. Prefer minimal, focused changes over broad rewrites.
5. Keep content oriented to C# developers (comparisons and migration clarity).

## Scaffold Script Warning

`scripts/scaffold_tutorial.py` can overwrite large parts of the tutorial.

Only run it when you intentionally want regeneration. If you change structure manually, update the script to match so future runs do not undo your work.

## Before Finishing Any Change

Run, at minimum:
- `uv run -p 3.14.5 ruff check .`
- `uv run -p 3.14.5 -m pytest`

If typing-related code changed, also run:
- `uv run -p 3.14.5 mypy src tests`
