# Quickstart

## Install dependencies

```bash
uv sync --all-groups
```

## Run the application

```bash
PYTHONPATH=src uv run python -m flashcards.main
```

## Build documentation

```bash
uv run sphinx-build -b html docs docs/_build/html
```

Generated HTML will be available in `docs/_build/html`.

## Build and open docs index (macOS)

```bash
uv run sphinx-build -b html docs docs/_build/html && open docs/_build/html/index.html
```

## Live preview with auto-rebuild

```bash
uv run sphinx-autobuild docs docs/_build/html --open-browser
```

Stop with `Ctrl+C`.

## Run test suite

```bash
uv run pytest
```

## Coverage HTML report (macOS)

```bash
uv run pytest --cov-report=html && open htmlcov/index.html
```

## Full validation via tox

```bash
uv run tox run
```

## Install git hooks (pre-commit + pre-push)

```bash
uv run pre-commit install
uv run pre-commit install --hook-type pre-push
```
