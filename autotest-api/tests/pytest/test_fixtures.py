import pytest

@pytest.fixture(autouse=True)
def send_analytics_data():
    print('[AUTOUSE] Отправляем данные в сервис аналитики')

@pytest.fixture(scope="session")
def settings():
    print("[SESSION] Инициализируем настройки автотеста")

@pytest.fixture(scope="class")
def user():
    print('[CLASS]  создаем данные пользователя один раз на тестовый класс')

@pytest.fixture(scope='function')
def users_client(settings):
    print('[FUNCTION] СОЗДАЕМ api КЛИЕНТ НА КАЖДЫЙ АВТОТЕСТ')


class TestUserFlow:
    def test_user_login(self,settings,user, users_client ):
        ...

    def test_user_can_create_course(self,settings,user, users_client):
        ...


class TestAccountFlow:
    def test_user_account(self,user,settings, users_client):
        ...

@pytest.fixture()
def user_data() -> dict:
    print("Создаем пользователя до теста (setup)") #до теста
    yield {"username":"test_user", "email":"test@example.com"} #выполняется сам тест
    print("Удалчем пользователя после теста(teardown)") # после теста
def test_user_email(user_data: dict):
    print(user_data)
    assert user_data['email'] == 'test@example.com'


def test_user_username(user_data: dict):
    print(user_data)
    assert user_data['username'] == 'test_user'