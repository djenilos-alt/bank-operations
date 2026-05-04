 ## Тестирование

Проект имеет покрытие тестами более 85 %.

### Структура тестов

* `tests/test_masks.py` — тесты для модуля маскировки данных (карты и счета);
* `tests/test_widget.py` — тесты для виджета отображения операций;
* `tests/test_processing.py` — тесты для обработки транзакций;
* `tests/conftest.py` — фикстуры для тестовых данных.

### Покрытие кода

### Шаги по установке

1. Клонируйте репозиторий:
```bash
git clone https://github.com/your-username/bank-operations-widget.git
cd bank-operations-widget

### Основные функции
1. Маскировка данных

* mask_account_card(input_string) — маскирует номера карт и счетов.

* get_date(date_string) — преобразует дату из ISO‑формата в ДД.ММ.ГГГГ.

2. Обработка данных

* filter_by_state(transactions, state='EXECUTED') — фильтрует транзакции по статусу.

* sort_by_date(transactions, reverse=True) — сортирует транзакции по дате.

### Примеры работы
1. Пример маскировки

* from src.widget import mask_account_card

  result = mask_account_card("Visa Platinum 7000792289606361")
  print(result)  # Visa Platinum 7000 79** **** 6361
  
2. Пример фильтрации

* from src.processing import filter_by_state

  transactions = [
      {'id': '441945886', 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041'},
      {'id': '41428829', 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}
  ]
  filtered = filter_by_state(transactions)
# Вернёт только транзакции со статусом 'EXECUTED'

3. Пример сортировки

   from src.processing import sort_by_date

   sorted_transactions = sort_by_date(transactions)
# Отсортирует транзакции от новых к старым

## Модуль decorators

Модуль содержит декораторы для логирования выполнения функций.

### Декоратор `log`

Декоратор для автоматического логирования вызовов функций, их результатов и ошибок.

**Параметры:**
* `filename` (опционально) — имя файла для записи логов. Если не указано, логи выводятся в консоль.

**Логирует:**
* начало выполнения функции (имя и аргументы);
* успешное завершение (время выполнения и результат);
* ошибки (тип ошибки, сообщение, входные параметры).

**Пример использования:**

```python
from src.decorators import log

# Логирование в консоль
@log()
def add(a, b):
    return a + b

# Логирование в файл
@log(filename="app.log")
def divide(x, y):
    return x / y

# Использование
result1 = add(5, 3)  # Вывод в консоль
result2 = divide(10, 2)  # Запись в файл app.log
* Модуль `masks`: 90 %

