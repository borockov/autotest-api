from typing import Any
def assert_status_code(actual: int, expected: int):
    """
    Проверяет, что фактический статус-код ответа соответствует ожидаемому

    :param actual: Фактический статус-код ответа.
    :param expected: Ожидаемый статус код.
    raise AssertionError: Если статус-коды не совпадают.
    """
    assert actual == expected, (
        'Неккоректный статус код'
        f'Ожидаемый статус {expected}'
        f'Полученный статус {actual}'
    )


def assert_equal(actual: Any, expected: Any, name: str):
    """
    Проверяет, что фактическое значение равно ожидаемому.
    :param name: Название проверяемого поля.
    :param actual: Фактическое значение.
    :param expected: Ожидаемое значение.
    :raise AssertionError: Если фактическое значение не равно ожидаемому
    """
    assert actual == expected, (
        f'Неккорректное значение:"{name}".'
        f'Ожидаемое значение:{expected}.'
        f'Акутальное значение:{actual}.'
    )