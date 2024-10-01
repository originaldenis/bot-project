from telebot.types import BotCommand
from botdir.config.configuration import Default_commands


def set_commands(bot):
    bot.set_my_commands([BotCommand(*i) for i in Default_commands])
