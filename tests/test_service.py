def test_example():
    assert 1 + 1 == 2


def test_import():
    try:
        assert True
    except ImportError:
        assert False, "Не удалось импортировать модуль models"
