from datetime import datetime
from typing import Any


def sort_by_date(


    transactions: list[dict[str, Any]],
    reverse_order: bool = False
) -> list[dict[str, Any]]:
    """Сортирует транзакции по дате."""
    # код функции
    pass
    """
    Сортирует транзакции по дате.

    Args:
        transactions (list): Список транзакций с полем 'date'.
        reverse_order (bool): Если True — сортировка по убыванию, иначе по возрастанию.

    Returns:
        list: Отсортированный список транзакций.
    """
    def parse_date(transaction):
        # Парсим строку даты в объект datetime
        return datetime.fromisoformat(transaction['date'])

    # Сортируем транзакции по дате
    sorted_transactions = sorted(
        transactions,
        key=parse_date,
        reverse=reverse_order
    )
    return sorted_transactions
