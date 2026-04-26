import pytest

from src.generators import card_number_generator
from src.generators import filter_by_currency
from src.generators import transaction_descriptions


class TestGenerators:

    @pytest.fixture
    def sample_transactions(self):
        """Фикстура с тестовыми транзакциями."""
        return [
            {
                'id': '1',
                'amount': '100',
                'currency': 'USD',
                'description': 'Покупка в магазине'
            },
            {
                'id': '2',
                'amount': '200',
                'currency': 'EUR',
                'description': 'Оплата услуг'
            },
            {
                'id': '3',
                'amount': '150',
                'currency': 'USD',
                'description': 'Перевод другу'
            }
        ]

    @pytest.mark.parametrize("currency,expected_count", [
        ('USD', 2),
        ('EUR', 1),
        ('RUB', 0),
        ('', 0)
    ])
    def test_filter_by_currency_parametrized(self, sample_transactions, currency, expected_count):
        """Параметризованный тест фильтрации по валюте."""
        result = list(filter_by_currency(sample_transactions, currency))
        assert len(result) == expected_count

    def test_filter_by_currency_empty_list(self):
        """Тест фильтрации пустого списка."""
        result = list(filter_by_currency([], 'USD'))
        assert result == []

    def test_transaction_descriptions_basic(self, sample_transactions):
        """Тест генерации описаний транзакций."""
        descriptions = list(transaction_descriptions(sample_transactions))
        assert len(descriptions) == 3
        assert descriptions[0].startswith("Операция 1: Покупка в магазине")
        assert "100 USD" in descriptions[0]

    def test_transaction_descriptions_empty_list(self):
        """Тест генератора описаний для пустого списка."""
        descriptions = list(transaction_descriptions([]))
        assert descriptions == []

    def test_transaction_descriptions_missing_fields(self):
        """Тест обработки транзакций с отсутствующими полями."""
        transactions = [
            {'id': '1'},
            {'id': '2', 'description': 'Без суммы'}
        ]
        descriptions = list(transaction_descriptions(transactions))
        assert len(descriptions) == 2
        assert "Без описания" in descriptions[0]
        assert "0 N/A" in descriptions[1]

    @pytest.mark.parametrize("start,stop,expected_first,expected_last", [
        (1, 2, "0000 0000 0000 0001", "0000 0000 0000 0001"),
        (9999999999999998, 10000000000000000, "9999 9999 9999 9998", "9999 9999 9999 9999")
    ])
    def test_card_number_generator_parametrized(
        self, start, stop, expected_first, expected_last
    ):
        """Параметризованный тест генератора номеров карт."""
        generator = card_number_generator(start, stop)
        numbers = list(generator)

        if numbers:
            assert numbers[0] == expected_first
            assert numbers[-1] == expected_last

    def test_card_number_generator_empty_range(self):
        """Тест генератора с пустым диапазоном."""
        generator = card_number_generator(100, 100)
        numbers = list(generator)
        assert numbers == []
