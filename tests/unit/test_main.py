from typing import TYPE_CHECKING

import pytest

import flashcards.main as main_module

if TYPE_CHECKING:
    from pytest_mock import MockerFixture


@pytest.mark.unit
def test_main_configures_logging_and_emits_startup_log(mocker: MockerFixture) -> None:
    configure_logging = mocker.patch("flashcards.main.configure_logging")
    log_info = mocker.patch.object(main_module.logger, "info")

    main_module.main()

    configure_logging.assert_called_once_with()
    log_info.assert_called_once_with("Application started")
