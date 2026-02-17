import pytest

from flashcards.example import add


@pytest.mark.unit
def test_add_returns_sum_for_positive_numbers() -> None:
    assert add(2, 3) == 5


@pytest.mark.unit
def test_add_handles_negative_numbers() -> None:
    assert add(-5, 2) == -3
