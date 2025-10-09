from clients.exercises.exercises_schema import ExerciseSchema, CreateExerciseResponseSchema, CreateExerciseRequestSchema, GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema
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


def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


def asser_get_exercise_response(actual: GetExerciseResponseSchema, expected: CreateExerciseResponseSchema):
    """Проверяет что тело ответ совпадает с ожидаемым телом ответа"""
    assert_exercise(actual.exercise, expected.exercise)


def assert_update_exercise_response(request: UpdateExerciseRequestSchema,response: UpdateExerciseResponseSchema):
    """Проверяет на соответствие того, что тело ответа соответствует запросу на обновление задания """
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")