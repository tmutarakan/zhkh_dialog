from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class APIOpenCity:
    """API Открытый Нижнекамск"""
    authentication_url: str
    apigate_url: str
    login: str
    password: str


@dataclass
class Redis:
    password: str
    host: str
    port: int
    db: int


@dataclass
class Postgres:
    host: str
    port: int
    db: str
    user: str
    password: str


@dataclass
class Config:
    tg_bot: TgBot
    api_opencity: APIOpenCity
    redis: Redis
    postgres: Postgres


def load_config(path: str | None) -> Config:
    # Создаем экземпляр класса Env
    env: Env = Env()

    # Добавляем в переменные окружения данные, прочитанные из файла .env
    env.read_env(path)

    # Создаем экземпляр класса Config и наполняем его данными из переменных
    # окружения
    return Config(
        tg_bot=TgBot(
            token=env("BOT_TOKEN"),
        ),
        api_opencity=APIOpenCity(
            authentication_url=env("APIOPENCITY_AUTHENTICATION_URL"),
            apigate_url=env("APIOPENCITY_APIGATE_URL"),
            login=env("APIOPENCITY_LOGIN"),
            password=env("APIOPENCITY_PASSWORD")
        ),
        redis=Redis(
            password=env("REDIS_PASSWORD"),
            host=env("REDIS_HOST"),
            port=env.int("REDIS_PORT"),
            db=env.int("REDIS_DB")
        ),
        postgres=Postgres(
            host=env("POSTGRES_HOST"),
            port=env.int("POSTGRES_PORT"),
            db=env("POSTGRES_DB"),
            user=env("POSTGRES_USER"),
            password=env("POSTGRES_PASSWORD"),
        )
    )
