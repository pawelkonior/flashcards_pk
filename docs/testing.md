# Testing: pytest enterprise setup

## Zainstalowane pluginy

Projekt używa `pytest` oraz pluginów:
- `pytest-cov` (coverage + raport XML),
- `pytest-xdist` (równoległe uruchamianie testów),
- `pytest-mock` (mockowanie przez fixture `mocker`),
- `pytest-randomly` (losowa kolejność testów),
- `pytest-timeout` (twardy limit czasu testu).

## Konfiguracja centralna

Konfiguracja testów jest rozdzielona:
- `pytest.toml` (sekcja `[pytest]`) dla ustawień `pytest`,
- `pyproject.toml` (`[tool.coverage.run]` i `[tool.coverage.report]`) dla coverage.

Najważniejsze zasady:
- `--strict-config` i `--strict-markers` są zawsze włączone,
- coverage liczone dla `flashcards` z branch coverage,
- timeout domyślny: `20s`,
- minimalne pokrycie: `90%` (`fail_under = 90`).

## Polityka markerów

Każdy test musi mieć dokładnie marker zakresu:
- `@pytest.mark.unit`
- `@pytest.mark.integration`
- `@pytest.mark.e2e`

Dodatkowo możesz oznaczyć test jako:
- `@pytest.mark.slow`

Polityka jest egzekwowana w `tests/conftest.py`:
- brak markera zakresu kończy się błędem kolekcji,
- `integration`, `e2e` i `slow` są domyślnie pomijane.

## Komendy

Uruchomienie domyślne (tylko testy `unit`):

```bash
uv run pytest
```

Uruchomienie z `integration`:

```bash
uv run pytest --run-integration
```

Uruchomienie z `e2e`:

```bash
uv run pytest --run-e2e
```

Uruchomienie pełne (wszystkie markery):

```bash
uv run pytest --run-integration --run-e2e --run-slow
```

## Coverage: obliczanie i raport HTML

Coverage liczy się automatycznie przy `uv run pytest` (konfiguracja jest w `pytest.toml` i `pyproject.toml`).

Minimalna komenda:

```bash
uv run pytest
```

Wymuszenie raportu HTML:

```bash
uv run pytest --cov-report=html
```

Raport zostanie wygenerowany w katalogu `htmlcov/`.

Otworzenie raportu HTML (macOS):

```bash
open htmlcov/index.html
```

Jedna komenda: testy + HTML + otwarcie raportu:

```bash
uv run pytest --cov-report=html && open htmlcov/index.html
```

## Tox: enterprise orchestration

Projekt ma centralną konfigurację `tox` w `tox.toml` (tox 4 + `tox-uv`).

Dostępne środowiska:
- `py314` - testy na Python 3.14,
- `lint` - `ruff check` i `ruff format --check`,
- `type` - `ty check`,
- `docs` - build Sphinx z `-W`,
- `coverage` - testy + raporty coverage (terminal/XML/HTML).

Najczęstsze komendy:

```bash
uv run tox run
```

```bash
uv run tox run -m static
```

```bash
uv run tox run -e py314,coverage
```

```bash
uv run tox list
```

## Pre-commit / Pre-push hooks

Projekt używa `pre-commit` z lokalnymi hookami zdefiniowanymi w `.pre-commit-config.yaml`.

Hooki `pre-commit`:
- `ruff check --no-fix src tests`
- `ruff format --check src tests`
- `ty check src`

Hook `pre-push`:
- `pytest`

Instalacja hooków lokalnie:

```bash
uv run pre-commit install
uv run pre-commit install --hook-type pre-push
```

Ręczne uruchomienie:

```bash
uv run pre-commit run --all-files
```

```bash
uv run pre-commit run --all-files --hook-stage pre-push
```
