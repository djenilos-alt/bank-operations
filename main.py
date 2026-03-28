from src.masks import get_mask_account
from src.masks import get_mask_card_number

if __name__ == "__main__":
    # Примеры использования функций
    try:
        # Пример маскировки карты
        card_mask = get_mask_card_number("1234567890123456")
        print(f"Masked card: {card_mask}")

        # Пример маскировки счёта
        account_mask = get_mask_account("40702810500000000001")
        print(f"Masked account: {account_mask}")
    except ValueError as e:
        print(f"Error: {e}")
