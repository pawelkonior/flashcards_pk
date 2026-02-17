# Jak dodać Sphinx krok po kroku

Ta strona pokazuje, jak od zera dodać dokumentację Sphinx do projektu Python w układzie `src/`.

## 1. Dodaj zależności developerskie

Zainstaluj Sphinx i dodatki:

```bash
uv add --dev sphinx furo myst-parser sphinx-copybutton sphinx-autodoc-typehints sphinx-autobuild
```

Co robią te pakiety:
- `sphinx`: generator dokumentacji.
- `furo`: nowoczesny motyw HTML.
- `myst-parser`: obsługa Markdown (`.md`) w dokumentacji.
- `sphinx-copybutton`: przycisk kopiowania przy blokach kodu.
- `sphinx-autodoc-typehints`: lepsza prezentacja adnotacji typów.
- `sphinx-autobuild`: automatyczny rebuild i podgląd live w przeglądarce.

## 2. Utwórz katalog `docs/`

Minimalna struktura:

```text
docs/
  conf.py
  index.rst
  api.rst
  quickstart.md
  _static/
  _templates/
```

## 3. Skonfiguruj `conf.py`

Najważniejsze elementy konfiguracji:
- dodanie `src` do `sys.path`, aby autodoc widział moduły projektu,
- włączenie rozszerzeń `autodoc`, `autosummary`, `napoleon`, `myst_parser`,
- ustawienie motywu HTML, np. `furo`.

W tym repo gotowa konfiguracja jest w `docs/conf.py`.

## 4. Dodaj strony i spis treści

W `docs/index.rst` dodaj wpisy do `toctree`, np.:

```rst
.. toctree::
   :maxdepth: 2

   quickstart
   sphinx_setup
   api
```

## 5. Dodaj dokumentację API przez autodoc

W `docs/api.rst` możesz dokumentować moduły:

```rst
.. automodule:: flashcards.main
   :members:
```

## 6. Zbuduj dokumentację

```bash
uv run sphinx-build -b html docs docs/_build/html
```

Wynik znajdziesz w `docs/_build/html/index.html`.

## 6a. Zbuduj i od razu otwórz `index.html` (macOS)

```bash
uv run sphinx-build -b html docs docs/_build/html && open docs/_build/html/index.html
```

## 6b. Uruchom tryb live (auto-rebuild)

```bash
uv run sphinx-autobuild docs docs/_build/html --open-browser
```

Przerwij działanie poleceniem `Ctrl+C`.

## 7. Opcjonalnie: Makefile

Dla wygody możesz budować dokumentację krótszą komendą:

```bash
make -C docs html
```

## 8. Dodaj build docs do `.gitignore`

Warto zignorować katalog z wygenerowanym HTML:

```text
docs/_build/
```
