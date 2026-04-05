from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional


def filter_by_state(transactions_list: List[Dict[str, str]], state_value: str = "EXECUTED") -> List[Dict[str, str]]:
    """
    Фильтрует список транзакций по значению поля state.

    Args:
        transactions_list (List[Dict[str, str]]): Список словарей с транзакциями.
            Каждый словарь должен содержать ключ 'state'.
        state_value (str): Значение поля state для фильтрации.
            По умолчанию — 'EXECUTED'.

    Returns:
        List[Dict[str, str]]: Отфильтрованный список транзакций, содержащих только
            элементы с указанным значением state.

    Example:
        >>> transactions = [
        ...     {'id': '441945886', 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041'},
        ...     {'id': '41428829', 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}
        ... ]
        >>> filter_by_state(transactions)
        [{'id': '441945886', 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041'}]
    """
    return [transaction for transaction in transactions_list if transaction.get("state") == state_value]


def sort_by_date(transactions_list: List[Dict[str, str]], reverse_order: bool = True) -> List[Dict[str, str]]:
    """
    Сортирует список транзакций по дате в указанном порядке.

    Args:
        transactions_list (List[Dict[str, str]]): Список словарей с транзакциями.
            Каждый словарь должен содержать ключ 'date' в формате ISO.
        reverse_order (bool): Порядок сортировки:
            True — убывание (новые транзакции первыми),
            False — возрастание (старые транзакции первыми).

    Returns:
        List[Dict[str, str]]: Отсортированный список транзакций.

    Example:
        >>> transactions = [
        ...     {'id': '441945886', 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041'},
        ...     {'id': '41428829', 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}
        ... ]
        >>> sort_by_date(transactions)
        [{'id': '441945886', 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041'},
         {'id': '41428829', 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}]
    """

    def parse_transaction_date(date_string: str) -> Optional[datetime]:
        """Парсит строку даты в объект datetime."""
        try:
            return datetime.fromisoformat(date_string)
        except (ValueError, TypeError):
            return None

    # Фильтруем транзакции с корректными датами
    valid_transactions = [
        transaction
        for transaction in transactions_list
        if "date" in transaction and parse_transaction_date(transaction["date"]) is not None
    ]

    return sorted(valid_transactions, key=lambda x: parse_transaction_date(x["date"]), reverse=reverse_order)
