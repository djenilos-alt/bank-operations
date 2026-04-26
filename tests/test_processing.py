import pytest

from src.processing import sort_by_date


class TestProcessing:

    @pytest.fixture
    def sample_transactions(self):
        """Фикстура с тестовыми транзакциями, содержащими даты."""
        return [
            {
                'id': '1',
                'date': '2023-01-15T10:00:00',
                'amount': '100',
                'currency': 'USD',
                'description': 'Покупка в магазине'
            },
            {
                'id': '2',
                'date': '2023-03-20T15:30:00',
                'amount': '200',
                'currency': 'EUR',
                'description': 'Оплата услуг'
            },
            {
                'id': '3',
                'date': '2022-12-01T09:15:00',
                'amount': '150',
                'currency': 'USD',
                'description': 'Перевод другу'
            }
        ]

    @pytest.mark.parametrize("reverse_order,expected_order", [
        (False, ['2022-12-01', '2023-01-15', '2023-03-20']),  # По возрастанию
        (True, ['2023-03-20', '2023-01-15', '2022-12-01'])   # По убыванию
    ])
    def test_sort_by_date_parametrized(self, sample_transactions, reverse_order, expected_order):
        """Параметризованный тест сортировки по дате."""
        result = sort_by_date(sample_transactions, reverse_order)

        # Извлекаем даты из результата (оставляем только дату без времени)
        dates = [transaction['date'][:10] for transaction in result]

        # Проверяем, что порядок дат соответствует ожидаемому
        assert dates == expected_order

    def test_sort_by_date_empty_list(self):
        """Тест сортировки пустого списка транзакций."""
        result = sort_by_date([])
        assert result == []

    def test_sort_by_date_single_transaction(self, sample_transactions):
        """Тест сортировки списка с одной транзакцией."""
        single_transaction = [sample_transactions[0]]
        result = sort_by_date(single_transaction)
        assert len(result) == 1
        assert result[0]['id'] == '1'
