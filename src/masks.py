def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты по правилу XXXX XX** **** XXXX.

    Args:
        card_number (str): Номер карты в виде строки (16 цифр)

    Returns:
        str: Замаскированный номер карты в формате "XXXX XX** **** XXXX"

    Raises:
        ValueError: Если номер карты не содержит ровно 16 цифр

    Example:
        >>> get_mask_card_number("1234567890123456")
        '1234 56** **** 3456'
    """
    # Удаляем пробелы и проверяем длину
    cleaned = card_number.replace(" ", "")

    if len(cleaned) != 16 or not cleaned.isdigit():
        raise ValueError("Card number must contain exactly 16 digits")

    # Применяем маску по правилу: XXXX XX** **** XXXX
    part1 = cleaned[:4]  # Первые 4 цифры
    part2 = cleaned[4:6] + "**"  # Следующие 2 цифры + **
    part3 = "****"  # Четыре звёздочки
    part4 = cleaned[-4:]  # Последние 4 цифры

    return f"{part1} {part2} {part3} {part4}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счёта по правилу **XXXX.

    Args:
        account_number (str): Номер счёта в виде строки (20 цифр)

    Returns:
        str: Замаскированный номер счёта в формате "**XXXX" (последние 4 цифры)

    Raises:
        ValueError: Если номер счёта не содержит ровно 20 цифр

    Example:
        >>> get_mask_account("40702810500000000001")
        '**0001'
    """
    # Удаляем пробелы и проверяем длину
    cleaned = account_number.replace(" ", "")

    if len(cleaned) != 20 or not cleaned.isdigit():
        raise ValueError("Account number must contain exactly 20 digits")

    # Оставляем только последние 4 цифры, остальное маскируем
    visible_end = cleaned[-4:]
    return f"**{visible_end}"
