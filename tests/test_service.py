def test_example():
    assert 1 + 1 == 2


def test_import():
    try:
        from quote_generator import models
        assert True
    except ImportError:
        assert False, "Не удалось импортировать модуль models"
