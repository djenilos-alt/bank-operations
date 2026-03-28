import pytest
from src.widget import mask_account_card, get_date


class TestWidgetFunctions:

    def test_mask_account_card_card(self):
        """Тест маскировки номера карты."""
        result = mask_account_card("Visa Platinum 7000792289606361")
        assert result == "Visa Platinum 7000 79** **** 6361"

        result = mask_account_card("Maestro 1596837868705199")
        assert result == "Maestro 1596 83** **** 5199"

    def test_mask_account_card_account(self):
        """Тест маскировки номера счёта."""
        result = mask_account_card("Счёт 73654108430135874305")
        assert result == "Счёт **4305"

        result = mask_account_card("Счёт 64686473678894779589")
        assert result == "Счёт **9589"

    def test_get_date_valid(self):
        """Тест корректного преобразования даты."""
        result = get_date("2024-03-11T02:26:18.671407")
        assert result == "11.03.2024"

    def test_get_date_invalid(self):
        """Тест обработки некорректной даты."""
        result = get_date("invalid-date-format")
        assert result == "invalid-date-format"