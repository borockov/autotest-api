from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий по ID курса.
     """
    courseId: str

class CreateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на создания упражнений в курсе
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление упражнений в курсе
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self,  query: GetExercisesQueryDict) ->Response:
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

    def create_exercises_api(self, request: CreateExercisesRequestDict) ->Response:
        """
        Метод для создания заданий.
        :param request Словарь с title,courseId, maxScore, minScore,orderIndex, description, estimatedTime
        :return ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercises_id : str, request: UpdateExercisesRequestDict) ->Response:
        """
        Метод для частичного обновления заданий
        :param request Словарь с title, maxScore, minScore,orderIndex, description, estimatedTime
        :param exercises_id для для выборки конкретного задания для обновления
        :return ответ от сервера в виде httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercises_id}", json=request)

    def delete_exercise_api(self, exercises_id: str)->Response:
        """
        Метод для удаления задания
        :param exercises_id ля выборка задания подлежащего удалению
        :return ответ от сервера в виде httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercises_id}")
