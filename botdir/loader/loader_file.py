from botdir.config.configuration import BotSettings
from telebot.storage import StateMemoryStorage
from telebot import TeleBot


bot_config = BotSettings()
storage = StateMemoryStorage()

bot = TeleBot(token=bot_config.BOT_TOKEN.get_secret_value(), state_storage=storage)
