from clients.exercises.exercises_schema import ExerciseSchema, CreateExerciseResponseSchema, CreateExerciseRequestSchema
from tools.assertions.base import assert_equal


def assert_create_exercise_response(actual: CreateExerciseRequestSchema, expected: CreateExerciseResponseSchema):
    """
    Проверяет, что фактические данные задания соответствуют ожидаемым.

    :param actual: Фактические данные по заданию.
    :param expected: Ожидаемые данные по заданию.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(expected.exercise.title, actual.title, "title")
    assert_equal(expected.exercise.course_id, actual.course_id, "course_id")
    assert_equal(expected.exercise.max_score, actual.max_score, "max_score")
    assert_equal(expected.exercise.min_score, actual.min_score, "min_score")
    assert_equal(expected.exercise.order_index, actual.order_index, "order_index")
    assert_equal(expected.exercise.description, actual.description, "description")
    assert_equal(expected.exercise.estimated_time, actual.estimated_time, "estimated_time")
