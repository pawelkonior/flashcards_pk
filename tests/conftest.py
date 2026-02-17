from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from pathlib import Path

TEST_SCOPE_MARKERS = frozenset({"unit", "integration", "e2e"})


def pytest_addoption(parser: pytest.Parser) -> None:
    """Add CLI switches controlling which marker groups are included."""
    group = parser.getgroup("marker-policy")
    group.addoption(
        "--run-integration",
        action="store_true",
        default=False,
        help="Run tests marked as integration.",
    )
    group.addoption(
        "--run-e2e",
        action="store_true",
        default=False,
        help="Run tests marked as e2e.",
    )
    group.addoption(
        "--run-slow",
        action="store_true",
        default=False,
        help="Run tests marked as slow.",
    )


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    """Enforce marker policy and default skipping strategy."""
    run_integration = config.getoption("--run-integration")
    run_e2e = config.getoption("--run-e2e")
    run_slow = config.getoption("--run-slow")

    skip_integration = pytest.mark.skip(reason="Integration tests require --run-integration.")
    skip_e2e = pytest.mark.skip(reason="E2E tests require --run-e2e.")
    skip_slow = pytest.mark.skip(reason="Slow tests require --run-slow.")

    invalid_scope_marker: list[str] = []

    for item in items:
        marker_names = {marker.name for marker in item.iter_markers()}

        scope_markers = marker_names.intersection(TEST_SCOPE_MARKERS)
        if len(scope_markers) != 1:
            selected = ", ".join(sorted(scope_markers)) if scope_markers else "none"
            invalid_scope_marker.append(f"{item.nodeid} (scope markers: {selected})")

        if "integration" in marker_names and not run_integration:
            item.add_marker(skip_integration)
        if "e2e" in marker_names and not run_e2e:
            item.add_marker(skip_e2e)
        if "slow" in marker_names and not run_slow:
            item.add_marker(skip_slow)

    if invalid_scope_marker:
        failing_tests = "\n - ".join(sorted(invalid_scope_marker))
        raise pytest.UsageError(
            "Each test must declare exactly one scope marker: unit, integration, or e2e.\n"
            f"Invalid tests:\n - {failing_tests}"
        )


@pytest.fixture
def isolated_workdir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Run a test in a temporary CWD to avoid polluting repository files."""
    monkeypatch.chdir(tmp_path)
    return tmp_path
