from typing import Any, Sized
import allure


@allure.step("Check that response status code equals to {expected}")
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


@allure.step("Check that {name} equals to {expected}")
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


@allure.step("Check that {name} is true")
def assert_is_true(actual: Any, name: str):
    """
    Проверяет, что фактическое значение является истинным.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :raises AssertionError: Если фактическое значение ложно.
    """
    assert actual, (
        f'Incorrect value: "{name}". '
        f'Expected true value but got: {actual}'
    )


def assert_lenght(actual: Sized, expected: Sized, name: str):
    """
    Проверяет, что длины двух объектов совпадают.

    :param name: Название проверяемого объекта.
    :param actual: Фактический объект.
    :param expected: Ожидаемый объект.
    :raises AssertionError: Если длины не совпадают.
    """
    with allure.step(f"Check that length of {name} equals to {len(expected)}"):
        assert len(actual) == len(expected), (
            f'Incorrect object length: "{name}". '
            f'Expected length: {len(expected)}. '
            f'Actual length: {len(actual)}'
        )
