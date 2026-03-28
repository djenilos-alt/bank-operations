from datetime import datetime
from src.masks import get_mask_card_number, get_mask_account



def mask_account_card(input_string: str) -> str:
    """
    Обрабатывает информацию о картах и счетах, возвращая строку с замаскированным номером.

    Args:
        input_string (str): Строка, содержащая тип и номер карты или счёта.
            Примеры: "Visa Platinum 7000792289606361", "Счёт 73654108430135874305"

    Returns:
        str: Строка с замаскированным номером, сохраняя тип инструмента.

    Examples:
        >>> mask_account_card("Visa Platinum 7000792289606361")
        'Visa Platinum 7000 79** **** 6361'
        >>> mask_account_card("Счёт 73654108430135874305")
        'Счёт **4305'
    """
    # Разделяем строку на части: всё до последнего числа — это описание, последнее число — номер
    parts = input_string.strip().split()
    if not parts:
        return input_string

    # Извлекаем номер (последнее слово)
    number = parts[-1]
    description = ' '.join(parts[:-1])

    # Определяем тип: если начинается с «Счёт», то это счёт, иначе — карта
    if description.startswith('Счёт'):
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{description} {masked_number}"



def get_date(date_string: str) -> str:
    """
    Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ.

    Args:
        date_string (str): Дата в формате "2024-03-11T02:26:18.671407"

    Returns:
        str: Дата в формате "ДД.ММ.ГГГГ"

    Example:
        >>> get_date("2024-03-11T02:26:18.671407")
        '11.03.2024'
    """
    try:
        # Парсим дату из строки ISO
        dt = datetime.fromisoformat(date_string)
        # Форматируем в нужный вид
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        # Если формат не подходит, возвращаем исходную строку
        return date_string