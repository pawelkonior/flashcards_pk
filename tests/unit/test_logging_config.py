import logging
from logging.handlers import RotatingFileHandler
from typing import TYPE_CHECKING

import pytest
from pythonjsonlogger import json

from flashcards.logging_config import configure_logging, get_standard_formatter

if TYPE_CHECKING:
    from pathlib import Path


@pytest.mark.unit
def test_get_standard_formatter_returns_json_formatter() -> None:
    formatter = get_standard_formatter()

    assert isinstance(formatter, json.JsonFormatter)


@pytest.mark.unit
def test_configure_logging_uses_log_level_and_creates_file_handler(
    monkeypatch: pytest.MonkeyPatch, isolated_workdir: Path
) -> None:
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")

    configure_logging()

    root_logger = logging.getLogger()
    handler_types = {type(handler) for handler in root_logger.handlers}

    assert root_logger.level == logging.DEBUG
    assert logging.StreamHandler in handler_types
    assert RotatingFileHandler in handler_types

    logging.getLogger(__name__).info("test-log-line")
    assert (isolated_workdir / "app.log").exists()
