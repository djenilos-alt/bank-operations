import requests
import json
from typing import Dict, Optional

def convert_currency(transaction: Dict) -> Optional[Dict]:
    """
    Конвертирует валюту по данным из транзакции.
    """
    # 1. Проверка на None
    if transaction is None:
        print("Ошибка: транзакция не предоставлена (None)")
        return None

    # 2. Проверка обязательных ключей в структуре transaction
    if 'operationAmount' not in transaction:
        print("Ошибка: отсутствует ключ 'operationAmount' в транзакции")
        return None

    operation_amount = transaction['operationAmount']

    if 'amount' not in operation_amount:
        print("Ошибка: отсутствует ключ 'amount' в 'operationAmount'")
        return None
    if 'currency' not in operation_amount:
        print("Ошибка: отсутствует ключ 'currency' в 'operationAmount'")
        return None

    currency_data = operation_amount['currency']
    if 'code' not in currency_data:
        print("Ошибка: отсутствует ключ 'code' в 'currency'")
        return None

    # 3. Извлечение данных
    try:
        original_amount = float(operation_amount['amount'])
        original_currency = currency_data['code'].upper()
    except (ValueError, TypeError) as e:
        print(f"Ошибка преобразования данных: {e}")
        return None

    target_currency = 'RUB'

    # 4. Проверка, есть ли уже готовый курс в транзакции
    if 'conversionRate' in transaction and 'rate' in transaction['conversionRate']:
        exchange_rate = float(transaction['conversionRate']['rate'])
    else:
        # 5. Запрос к API для получения курса
        try:
            url = f"https://api.exchangerate-api.com/v4/latest/{original_currency}"  # или http://
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            if 'rates' not in data:
                print("Ошибка: в ответе API отсутствует поле 'rates'")
                return None
            if target_currency not in data['rates']:
                print(f"Курс для валюты {target_currency} не найден в ответе API")
                return None

            exchange_rate = data['rates'][target_currency]
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при обращении к API: {e}")
            return None
        except KeyError as e:
            print(f"Ошибка обработки ответа API: отсутствует ключ {e}")
            return None
        except Exception as e:
            print(f"Неожиданная ошибка при обращении к API: {e}")
            return None

    # 6. Расчёт и формирование результата
    converted_amount = round(original_amount * exchange_rate, 2)

    result = {
        "original_amount": original_amount,
        "original_currency": original_currency,
        "target_amount": converted_amount,
        "target_currency": target_currency,
        "exchange_rate": exchange_rate,
        "status": "success"
    }
    return result
