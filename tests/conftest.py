import pytest


@pytest.fixture
def sample_card_numbers():
    """Фикстура с тестовыми номерами карт."""
    return ["1234567890123456", "4000008000000000", "5555444433332222"]


@pytest.fixture
def sample_account_numbers():
    """Фикстура с тестовыми номерами счетов."""
    return ["73654108430135874305", "64686473678894779589", "35383033474447895560"]


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
def sample_transactions():
    return [...]


@pytest.fixture
def another_sample_transactions():
    return [...]
