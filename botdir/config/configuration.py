from dotenv import load_dotenv, find_dotenv
from pydantic import SecretStr
from pydantic_settings import BaseSettings
import os

if not find_dotenv():
    exit("Переменные окружения не загружены т.к. отсутствует файл .env")
else:
    load_dotenv()


class BotSettings(BaseSettings):
    """
    Класс, описывающий настройки бота(api ключ и токен).
    """

    API_KEY: SecretStr = os.getenv("API_KEY")
    BOT_TOKEN: SecretStr = os.getenv("BOT_TOKEN")


Default_commands = (
    ("start", "Запустить бота"),
    ("help", "Справка о командах "),
    ("search_by_name", "Искать по названию коктейля"),
    ("search_by_ing", "Искать по ингредиенту"),
    ("history", "История запросов"),
)
