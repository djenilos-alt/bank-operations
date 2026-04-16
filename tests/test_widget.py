import pytest

from src.widget import get_date
from src.widget import mask_account_card


class TestWidgetFunctions:

    def test_mask_account_card_card(self):
        """Тест маскировки номера карты."""
        result = mask_account_card("Visa Platinum 7000792289606361")
        assert result == "Visa Platinum 7000 79** **** 6361"

        result = mask_account_card("Maestro 1596837868705199")
        assert result == "Maestro 1596 83** **** 5199"

        result = mask_account_card("MasterCard 7158300734726758")
        assert result == "MasterCard 7158 30** **** 6758"

        result = mask_account_card("Visa Classic 6831982476737658")
        assert result == "Visa Classic 6831 98** **** 7658"

        result = mask_account_card("Visa Gold 5999414228426353")
        assert result == "Visa Gold 5999 41** **** 6353"

    def test_mask_account_card_account_lowercase(self):
        """Тест маскировки номера счёта (строчная буква)."""
        result = mask_account_card("счет 73654108430135874305")
        assert result == "счет **4305"

    def test_mask_account_card_account_uppercase(self):
        """Тест маскировки номера счёта (заглавная буква)."""
        result = mask_account_card("Счет 64686473678894779589")
        assert result == "Счет **9589"

    def test_mask_account_card_account_cyrillic(self):
        """Тест маскировки номера счёта с кириллической «ё»."""
        result = mask_account_card("Счёт 35383033474447895560")
        assert result == "Счёт **5560"

    def test_get_date_valid(self):
        """Тест корректного преобразования даты."""
        result = get_date("2024-03-11T02:26:18.671407")
        assert result == "11.03.2024"

    def test_get_date_invalid(self):
        """Тест обработки некорректной даты."""
        result = get_date("invalid-date-format")
        assert result == "invalid-date-format"


def test_get_date_invalid_input(self):
    """Тест обработки некорректной даты."""
    result = get_date("invalid-date")
    assert result == "invalid-date"

    result = get_date(None)
    assert result is None
