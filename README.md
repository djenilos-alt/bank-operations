# Виджет банковских операций клиента

Виджет для обработки и отображения банковских операций с функциями маскировки данных и фильтрации транзакций.

## Установка и настройка

### Предварительные требования

* Python 3.10+
* Poetry (менеджер зависимостей)

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
