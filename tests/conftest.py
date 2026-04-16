import pytest


@pytest.fixture
def sample_transactions():
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


@pytest.fixture
def empty_transactions():
    """Пустой список транзакций."""
    return []
