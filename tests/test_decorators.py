import pytest
import os
from src.decorators import log


class TestLogDecorator:

    @pytest.fixture
    def temp_log_file(self, tmp_path):
        """Фикстура для временного файла логов."""
        file_path = tmp_path / "test_log.txt"
        yield file_path
        # Очистка после теста
        if file_path.exists():
            file_path.unlink()

    def test_log_to_console(self, capsys):
        """Тест логирования в консоль."""
        @log()
        def sample_function(x, y):
            return x + y

        result = sample_function(5, 3)
        captured = capsys.readouterr()

        assert "Вызов функции sample_function(5, 3)" in captured.out
        assert "успешно выполнена" in captured.out
        assert "Результат: 8" in captured.out
        assert result == 8

    def test_log_to_file(self, temp_log_file):
        """Тест логирования в файл."""
        @log(filename=str(temp_log_file))
        def another_function():
            return "OK"

        another_function()

        with open(temp_log_file, 'r', encoding='utf-8') as f:
            content = f.read()

        assert "Вызов функции another_function()" in content
        assert "успешно выполнена" in content
        assert "Результат: 'OK'" in content

    def test_exception_logging(self, capsys):
        """Тест логирования исключений в консоль."""
        @log()
        def faulty_function():
            raise ValueError("Тестовая ошибка")

        with pytest.raises(ValueError):
            faulty_function()

        captured = capsys.readouterr()
        assert "Ошибка в функции faulty_function" in captured.out
        assert "ValueError: Тестовая ошибка" in captured.out

    def test_exception_logging_to_file(self, temp_log_file):
        """Тест логирования исключений в файл."""
        @log(filename=str(temp_log_file))
        def error_function():
            raise TypeError("Ошибка типа")

        with pytest.raises(TypeError):
            error_function()

        with open(temp_log_file, 'r', encoding='utf-8') as f:
            content = f.read()

        assert "Ошибка в функции error_function" in content
        assert "TypeError: Ошибка типа" in content

    def test_function_with_kwargs(self, capsys):
        """Тест функции с именованными аргументами."""
        @log()
        def greet(name, greeting="Привет"):
            return f"{greeting}, {name}!"

        result = greet("Анна", greeting="Здравствуйте")
        captured = capsys.readouterr()

        assert "Вызов функции greet('Анна', greeting='Здравствуйте')" in captured.out
        assert "Результат: 'Здравствуйте, Анна!'" in captured.out
        assert result == "Здравствуйте, Анна!"

    def test_empty_arguments(self, capsys):
        """Тест функции без аргументов."""
        @log()
        def no_args():
            return 42

        result = no_args()
        captured = capsys.readouterr()

        assert "Вызов функции no_args()" in captured.out
        assert "Результат: 42" in captured.out
        assert result == 42
