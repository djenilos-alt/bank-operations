import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number


class TestMaskingFunctions:

    def test_get_mask_card_number_valid(self):
        """Тест корректной маскировки номера карты."""
        result = get_mask_card_number("1234567890123456")
        assert result == "1234 56** **** 3456"

    def test_get_mask_card_number_with_spaces(self):
        """Тест маскировки карты с пробелами в номере."""
        result = get_mask_card_number("1234 5678 9012 3456")
        assert result == "1234 56** **** 3456"

    def test_get_mask_card_number_invalid_length(self):
        """Тест обработки некорректной длины номера карты."""
        with pytest.raises(ValueError, match="Card number must contain exactly 16 digits"):
            get_mask_card_number("123456789012345")

    def test_get_mask_card_number_non_digit(self):
        """Тест обработки нечислового номера карты."""
        with pytest.raises(ValueError, match="Card number must contain exactly 16 digits"):
            get_mask_card_number("1234abcd5678efgh")

    def test_get_mask_account_valid(self):
        """Тест корректной маскировки номера счёта."""
        result = get_mask_account("40702810500000000001")
        assert result == "**0001"

    def test_get_mask_account_with_spaces(self):
        """Тест маскировки счёта с пробелами."""
        result = get_mask_account("4070 2810 5000 0000 0001")
        assert result == "**0001"

    def test_get_mask_account_invalid_length(self):
        """Тест обработки некорректной длины номера счёта."""
        with pytest.raises(ValueError, match="Account number must contain exactly 20 digits"):
            get_mask_account("4070281050000000001")

    def test_get_mask_account_non_digit(self):
        """Тест обработки нечислового номера счёта."""
        with pytest.raises(ValueError, match="Account number must contain exactly 20 digits"):
            get_mask_account("4070abcd5000efghijkl")
