from clients.exercises.exercises_schema import ExerciseSchema, CreateExerciseResponseSchema, \
    CreateExerciseRequestSchema, GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema, \
    GetExercisesResponseSchema
from tools.assertions.base import assert_equal, assert_lenght
from clients.erros_schema import InternalErrorResponseSchema
from tools.assertions.errors import assert_internal_error_response
import allure
from clients.event_hooks import get_logger


logger = get_logger("Exercises Assertions")

@allure.step("Check create exercise response")
def assert_create_exercise_response(actual: CreateExerciseRequestSchema, expected: CreateExerciseResponseSchema):
    """
    Проверяет, что фактические данные задания соответствуют ожидаемым.

    :param actual: Фактические данные по заданию.
    :param expected: Ожидаемые данные по заданию.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check get exercise response")

    assert_equal(expected.exercise.title, actual.title, "title")
    assert_equal(expected.exercise.course_id, actual.course_id, "course_id")
    assert_equal(expected.exercise.max_score, actual.max_score, "max_score")
    assert_equal(expected.exercise.min_score, actual.min_score, "min_score")
    assert_equal(expected.exercise.order_index, actual.order_index, "order_index")
    assert_equal(expected.exercise.description, actual.description, "description")
    assert_equal(expected.exercise.estimated_time, actual.estimated_time, "estimated_time")

@allure.step("Check exercise")
def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    logger.info("Check exercise")

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")

@allure.step("Check get exercise response")
def asser_get_exercise_response(actual: GetExerciseResponseSchema, expected: CreateExerciseResponseSchema):
    """Проверяет что тело ответ совпадает с ожидаемым телом ответа"""
    logger.info("Check Get exercise response")

    assert_exercise(actual.exercise, expected.exercise)

@allure.step("Check update exercise response")
def assert_update_exercise_response(request: UpdateExerciseRequestSchema, response: UpdateExerciseResponseSchema):
    """Проверяет на соответствие того, что тело ответа соответствует запросу на обновление задания """
    logger.info("Check update exercise response")

    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")

@allure.step("Check exercise not found response")
def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если задание не найдено.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "Exercise not found"
    """
    logger.info("Check exercise not found response")

    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_internal_error_response(actual, expected)

@allure.step("Check get exercises response")
def assert_get_exercises_response(
        get_exercises_response: GetExercisesResponseSchema,
        create_exercises_responses: list[CreateExerciseResponseSchema]):
    """
    Проверяет, что ответ на получение списка заданий соответствует ответам на их создание.

    :param get_exercises_response: Ответ API при запросе списка заданий.
    :param create_exercises_responses: Список API ответов при создании заданий.
    :raises AssertionError: Если данные заданий не совпадают.
    """
    logger.info("Check get exercises response")

    assert_lenght(get_exercises_response.exercises, create_exercises_responses, "courses")

    for index, create_exercises_responses in enumerate(create_exercises_responses):
        assert_exercise(get_exercises_response.exercises[index], create_exercises_responses.exercise)
