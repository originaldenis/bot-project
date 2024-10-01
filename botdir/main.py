from botdir.loader.loader_file import bot
from botdir import handlers
from telebot.custom_filters import StateFilter
from utils.set_commands_file import set_commands

if __name__ == "__main__":
    bot.add_custom_filter(StateFilter(bot))
    set_commands(bot)
    bot.infinity_polling()
