import time
from faker import Faker


class Fake:
    """
    Класс для генерации случайных тестовых данных с ипользованием библиотеки Faker
    """

    def __init__(self, faker: Faker):
        """
        :param faker: Экземпляр класса Faker, который будет использоваться для генерации данных
        """
        self.faker = faker

    def text(self) -> str:
        """
        Генерирует случайный текст
        :return: Случайный текст
        """
        return self.faker.text()

    def uuid4(self) -> str:
        """
        Генерирует случайный UUID4
        :return: Случайный UUID%
        """
        return self.faker.uuid4()

    def email(self, domain: str | None = None) -> str:
        """
        Генерирует случайный email.

        :param domain: Домен электронной почты (например, "example.com").
        Если не указан, будет использован случайный домен.
        :return: Случайный email.
        """
        return self.faker.email(domain=domain)

    def sentence(self) -> str:
        """
        Генерирует предложение
        :return: Случайное предложение
        """
        return self.faker.sentence()

    def password(self) -> str:
        """
        Генерирует случайный пароль
        :return: Случайный пароль
        """
        return self.faker.password()

    def last_name(self) -> str:
        """
        Генерирует last_name
        :return: случайный last_name
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """
          Генерирует first_name
          :return: случайный first_name
          """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
          Генерирует first_name
          :return: случайный first_name
          """
        return self.faker.first_name()

    def integer(self, start: int = 1, end: int = 100) -> int:
        """
        Генерирует случайное число от 1 до 100
        :return: От 1 до 100
        """
        return self.faker.random_int(start, end)

    def estimated_time(self) -> str:
        """
        Генерирует время прохождение курса на основе функции integer
        :return: Время прохождения курса
        """
        return f"{self.integer(1, 10)} weeks"

    def max_score(self) -> int:
        """
        Генерирует максимальный бал от 50 до 100
        :return: От 50 до 100
        """
        return self.integer(start=50, end=100)

    def min_score(self) -> int:
        """
        Генерирует минимальный бал от 1 до 30
        :return: от 1 до 30
        """
        return self.integer(start=1, end=30)


fake = Fake(faker=Faker("ru_RU"))
