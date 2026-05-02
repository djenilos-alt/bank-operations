from datetime import datetime

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(input_string: str) -> str:
    """Определяет тип и маскирует карту или счёт."""
    if not input_string or len(input_string.strip()) == 0:
        return input_string

    parts = input_string.split()
    if len(parts) < 2:
        return input_string  # недостаточно данных


    # Определяем тип: счёт или карта
    last_part = parts[-1]
    is_account = any(word.lower() in input_string.lower() for word in ['счёт', 'счет', 'account'])


    if is_account:
        # Обрабатываем счёт (20 цифр)
        if len(last_part) == 20 and last_part.isdigit():
            masked = get_mask_account(last_part)
            prefix = ' '.join(parts[:-1])
            return f"{prefix} {masked}"
        else:
            return input_string
    else:
        # Обрабатываем карту (16 цифр)
        if len(last_part) == 16 and last_part.isdigit():
            masked = get_mask_card_number(last_part)
            return ' '.join(parts[:-1]) + ' ' + masked
        else:
            return input_string
