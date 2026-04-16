def filter_by_currency(transactions: list, currency: str) -> iter:
    """
    Фильтрует транзакции по валюте.

    Args:
        transactions (list): Список словарей с транзакциями.
        currency (str): Валюта для фильтрации (например, 'USD').

    Yields:
        dict: Транзакция с указанной валютой.
    """
    for transaction in transactions:
        if transaction.get('currency') == currency:
            yield transaction


def transaction_descriptions(transactions: list) -> iter:
    """
    Генерирует описания транзакций.

    Args:
        transactions (list): Список словарей с транзакциями.

    Yields:
        str: Описание транзакции в формате:
            "Операция {id}: {description} на сумму {amount} {currency}"
    """
    for transaction in transactions:
        description = transaction.get('description', 'Без описания')
        amount = transaction.get('amount', '0')
        curr = transaction.get('currency', 'N/A')
        trans_id = transaction.get('id', 'Unknown')
        yield f"Операция {trans_id}: {description} на сумму {amount} {curr}"

def card_number_generator(start: int, stop: int) -> iter:
    """
    Генерирует номера карт в формате XXXX XXXX XXXX XXXX.

    Args:
        start (int): Начальное число для генерации.
        stop (int): Конечное число для генерации (не включается).

    Yields:
        str: Номер карты в формате 'XXXX XXXX XXXX XXXX'.
    """
    for num in range(start, stop):
        # Форматируем число до 16 цифр с ведущими нулями
        card_num = f"{num:016d}"
        # Разбиваем на группы по 4 цифры
        formatted = f"{card_num[:4]} {card_num[4:8]} {card_num[8:12]} {card_num[12:]}"
        yield formatted