from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict
from clients.exercises.exercises_schema import Exercise, GetExercisesQuerySchema, GetExercisesResponseSchema, CreateExercisesRequestSchema, UpdateExercisesRequestSchema
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client



class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self,  query: GetExercisesQuerySchema) ->Response:
        """
        Метод получения списка заданий.
        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises/", params=query)

    def get_exercise_api(self, exercise_id: str) ->Response:
        """
        Метод для пиолучения информации о задании
        :param exercises_id для получения иноформации о задании
        :return ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercises_api(self, request: CreateExercisesRequestSchema) ->Response:
        """
        Метод для создания заданий.
        :param request Словарь с title,courseId, maxScore, minScore,orderIndex, description, estimatedTime
        :return ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercise_api(self, exercises_id : str, request: UpdateExercisesRequestSchema) ->Response:
        """
        Метод для частичного обновления заданий
        :param request Словарь с title, maxScore, minScore,orderIndex, description, estimatedTime
        :param exercises_id для для выборки конкретного задания для обновления
        :return ответ от сервера в виде httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercises_id}", json=request.model_dump(by_alias=True))

    def delete_exercise_api(self, exercises_id: str)->Response:
        """
        Метод для удаления задания
        :param exercises_id ля выборка задания подлежащего удалению
        :return ответ от сервера в виде httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercises_id}")



    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """
           Метод получения упражнения.
           :param query: данные из списка Exercise,
           :return: Ответ от сервера в виде объекта httpx.Response
           """
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise(self, exercise_id: str) -> Exercise:
        """
           Метод получения упражнения.
           :param exercise_id: передаем строку Exercise,
           """
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercises(self, request: CreateExercisesRequestSchema) -> Exercise:
        response = self.create_exercises_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExercisesRequestSchema) -> Exercise:
        response = self.update_exercise_api(exercise_id, request)
        return response.json()

    def delete_exercise(self, exercise_id: str) -> dict:
        response = self.delete_exercise_api(exercise_id)
        return response.json()


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создает экземпляр ExercisesClient с уже готовым HTTP клиентом
    :return: Готовый к использованию ExercisesClient
    """
    return ExercisesClient(client=get_private_http_client(user))