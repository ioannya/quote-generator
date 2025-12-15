import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

def test_example():
    """Простой тест для проверки работы CI."""
    assert 1 + 1 == 2

def test_import():
    """Проверяем, что можем импортировать модули."""
    try:
        from quote_generator import models
        assert True
    except ImportError:
        assert False, "Не удалось импортировать модуль models"
