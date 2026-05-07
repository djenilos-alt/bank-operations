import pytest
from unittest.mock import patch, Mock
import requests  # <-- эта строка решает проблему
from src.currency_converter import convert_currency


class TestCurrencyConverter:
    """Тесты для функции конвертации валюты."""

    def test_convert_currency_success_with_conversion_rate(self):
        """Тест успешной конвертации с готовым курсом в транзакции."""
        transaction = {
            "operationAmount": {
                "amount": 100,
                "currency": {
                    "code": "USD"
                }
            },
            "conversionRate": {
                "rate": 92.5
            }
        }

        result = convert_currency(transaction)

        assert result['status'] == 'success'
        assert result['original_amount'] == 100
        assert result['original_currency'] == 'USD'
        assert result['target_currency'] == 'RUB'
        assert result['exchange_rate'] == 92.5
        assert result['target_amount'] == 9250.0

    @patch('requests.get')
    def test_convert_currency_success_with_api(self, mock_get):
        """Тест успешной конвертации через API (без готового курса)."""
        # Настройка mock для ответа API
        mock_response = Mock()
        mock_response.json.return_value = {
            'rates': {'RUB': 92.5}
        }
        mock_get.return_value = mock_response

        transaction = {
            "operationAmount": {
                "amount": 50,
                "currency": {
                    "code": "EUR"
                }
            }
        }

        result = convert_currency(transaction)

        assert result['status'] == 'success'
        assert result['original_amount'] == 50
        assert result['original_currency'] == 'EUR'
        assert result['target_currency'] == 'RUB'
        assert result['exchange_rate'] == 92.5
        assert result['target_amount'] == 4625.0

    def test_missing_operation_amount_key(self):
        """Тест отсутствия ключа 'operationAmount'."""
        transaction = {
            "amount": 100,
            "currency": "USD"
        }

        result = convert_currency(transaction)

        assert result is None

    def test_missing_amount_in_operation_amount(self):
        """Тест отсутствия ключа 'amount' в 'operationAmount'."""
        transaction = {
            "operationAmount": {
                "currency": {
                    "code": "USD"
                }
            }
        }

        result = convert_currency(transaction)

        assert result is None

    def test_missing_currency_in_operation_amount(self):
        """Тест отсутствия ключа 'currency' в 'operationAmount'."""
        transaction = {
            "operationAmount": {
                "amount": 100
            }
        }

        result = convert_currency(transaction)

        assert result is None

    def test_missing_code_in_currency(self):
        """Тест отсутствия ключа 'code' в 'currency'."""
        transaction = {
            "operationAmount": {
                "amount": 100,
                "currency": {}
            }
        }

        result = convert_currency(transaction)

        assert result is None

    def test_invalid_amount_type(self):
        """Тест некорректного типа данных для 'amount'."""
        transaction = {
            "operationAmount": {
                "amount": "not_a_number",
                "currency": {
                    "code": "USD"
                }
            }
        }

        result = convert_currency(transaction)

        assert result is None

    @patch('requests.get')
    def test_api_request_failure(self, mock_get):
        """Тест ошибки при обращении к API."""
        mock_get.side_effect = requests.exceptions.RequestException("Network error")

        transaction = {
            "operationAmount": {
                "amount": 100,
                "currency": {
                    "code": "USD"
                }
            }
        }

        result = convert_currency(transaction)

        assert result is None

    @patch('requests.get')
    def test_api_response_missing_rates(self, mock_get):
        """Тест ответа API без поля 'rates'."""
        mock_response = Mock()
        mock_response.json.return_value = {'error': 'No rates available'}
        mock_get.return_value = mock_response

        transaction = {
            "operationAmount": {
                "amount": 100,
                "currency": {
                    "code": "USD"
                }
            }
        }

        result = convert_currency(transaction)

        assert result is None

    @patch('requests.get')
    def test_currency_not_found_in_api_response(self, mock_get):
        """Тест отсутствия целевой валюты в ответе API."""
        mock_response = Mock()
        mock_response.json.return_value = {
            'rates': {'EUR': 0.85}  # RUB отсутствует
        }
        mock_get.return_value = mock_response

        transaction = {
            "operationAmount": {
                "amount": 100,
                "currency": {
                    "code": "USD"
                }
            }
        }

        result = convert_currency(transaction)

        assert result is None

    def test_empty_transaction(self):
        """Тест пустой транзакции."""
        transaction = {}

        result = convert_currency(transaction)

        assert result is None

    def test_none_transaction(self):
        """Тест передачи None вместо транзакции."""
        result = convert_currency(None)

        assert result is None