import pytest
from string_utils import StringUtils

# Создаем экземпляр класса StringUtils
string_utils = StringUtils()


class TestCapitalize:
    @pytest.mark.positive
    @pytest.mark.parametrize("input_str, expected", [
        ("skypro", "Skypro"),
        ("hello world", "Hello world"),
        ("python", "Python"),
        ("a", "A"),
    ])
    def test_capitalize_positive(self, input_str, expected):
        """Позитивные тесты для capitalize"""
        result = string_utils.capitalize(input_str)
        assert result == expected, f"Ошибка капитализации строки '{input_str}'"

    @pytest.mark.negative
    @pytest.mark.parametrize("input_str, expected", [
        ("123abc", "123abc"),
        ("", ""),
        ("   ", "   "),
        ("ABC", "ABC"),
    ])
    def test_capitalize_negative(self, input_str, expected):
        """Негативные тесты для capitalize"""
        result = string_utils.capitalize(input_str)
        assert result == expected, f"""
        Ошибка обработки нестандартных данных в строке '{input_str}'"""


class TestTrim:
    @pytest.mark.positive
    @pytest.mark.parametrize("input_str, expected", [
        ("   skypro", "skypro"),
        ("\tskypro\t", "skypro"),
        ("\nskypro\n", "skypro"),
        ("  hello world  ", "hello world"),
    ])
    def test_trim_positive(self, input_str, expected):
        """Позитивные тесты для trim"""
        result = string_utils.trim(input_str)
        assert result == expected, f"""
        Ошибка при удалении начальных пробельных символов из строки
        '{input_str}'"""

    @pytest.mark.negative
    @pytest.mark.parametrize("input_str, expected", [
        ("", ""),
        ("   ", ""),
        ("\n\n\n", ""),
        (" abc ", "abc"),
    ])
    def test_trim_negative(self, input_str, expected):
        """Негативные тесты для trim"""
        result = string_utils.trim(input_str)
        assert result == expected, f"""
        Ошибка обработки специфичных данных в строке '{input_str}'"""


class TestContains:
    @pytest.mark.positive
    @pytest.mark.parametrize("input_str, symbol, expected", [
        ("SkyPro", "S", True),
        ("SkyPro", "P", True),
        ("abcdef", "bcd", True),
    ])
    def test_contains_positive(self, input_str, symbol, expected):
        """Позитивные тесты для contains"""
        result = string_utils.contains(input_str, symbol)
        assert result == expected, f"""
        Ошибка обнаружения символа {symbol} в строке '{input_str}'"""

    @pytest.mark.negative
    @pytest.mark.parametrize("input_str, symbol, expected", [
        ("SkyPro", "X", False),
        ("SkyPro", "", False),
        ("", "A", False),
        ("123", "abc", False),
    ])
    def test_contains_negative(self, input_str, symbol, expected):
        """Негативные тесты для contains"""
        result = string_utils.contains(input_str, symbol)
        assert result == expected, f"""
        Ошибка при проверке отсутствия символа {symbol}
        в строке '{input_str}'"""


class TestDeleteSymbol:
    @pytest.mark.positive
    @pytest.mark.parametrize("input_str, symbol, expected", [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("abcdef", "bc", "adef"),
    ])
    def test_delete_symbol_positive(self, input_str, symbol, expected):
        """Позитивные тесты для delete_symbol"""
        result = string_utils.delete_symbol(input_str, symbol)
        assert result == expected, f"""Ошибка удаления символа {symbol}
          из строки '{input_str}'"""

    @pytest.mark.negative
    @pytest.mark.parametrize("input_str, symbol, expected", [
        ("SkyPro", "X", "SkyPro"),
        ("SkyPro", "", "SkyPro"),
        ("", "A", ""),
        ("123", "abc", "123"),
    ])
    def test_delete_symbol_negative(self, input_str, symbol, expected):
        """Негативные тесты для delete_symbol"""
        result = string_utils.delete_symbol(input_str, symbol)
        assert result == expected, f"""
        Ошибка при обработке необычных данных: удаление символа
          {symbol} из строки '{input_str}'"""
