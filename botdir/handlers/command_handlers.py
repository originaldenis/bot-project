from telebot.types import Message
from botdir.keyboards.reply_key_for_choose import Keyboards
from botdir.loader.loader_file import bot
from botdir.states.state_file import UserInfoState
from botdir.database.utils.core import CRUDInterface
from botdir.database.common.models import db, History
from telebot.types import ReplyKeyboardRemove


@bot.message_handler(commands=["start"])
def send_welcome(message: Message) -> None:
    """
    Функция для команды "start" бота.

    :param message: Сообщение пользователя.
    """
    bot.set_state(message.from_user.id, UserInfoState.name, message.chat.id)
    bot.reply_to(
        message,
        "Привет! Я знаю все про коктейли и помогу тебе найти нужный. Как тебя зовут?",
    )


@bot.message_handler(commands=["help"])
def help_command(message: Message) -> None:
    """
    Функция-хендлер для команды "help" бота.

    :param message: Сообщение пользователя.
    """
    bot.reply_to(
        message,
        "Привет! Это бот,знающий почти все про коктейли,их составы и способы приготовления."
        "\nЧтобы выполнить поиск по названию коктейля,выбери/введи команду '/search_by_name'."
        "\nЧтобы выполнить поиск по ингредиенту коктейля, выбери/введи команду '/search_by_ing'."
        "\nНу а чтобы познакомиться и запустить бота, выбери/введи команду '/start'",
    )
    bot.set_state(message.from_user.id, UserInfoState.help, message.chat.id)


@bot.message_handler(commands=["history"])
@bot.message_handler(state=UserInfoState.history)
def history_look(message: Message) -> None:
    """
    Функция-хендлер для команды "history" бота.

    :param message: Сообщение пользователя.
    """
    bot.reply_to(
        message,
        "Сейчас покажу последние 5 запросов",
        reply_markup=ReplyKeyboardRemove(),
    )
    result = CRUDInterface.read(db, History, message.from_user.username)
    for i_elem in result:
        if i_elem["Ingredient"] is not None:
            bot.send_message(
                message.from_user.id,
                f"Пользователь: {i_elem['User']} искал "
                f"{i_elem['Search_param']} : {i_elem['Ingredient']} ",
            )
        if i_elem["Cocktail"] is not None:
            bot.send_message(
                message.from_user.id,
                f"Пользователь: {i_elem['User']} искал "
                f"{i_elem['Search_param']} : {i_elem['Cocktail']} ",
            )
    bot.set_state(message.from_user.id, UserInfoState.if_continue, message.chat.id)
    bot.send_message(
        message.chat.id,
        f"Поищем другой вариант?",
        reply_markup=Keyboards.exit_search(),
    )


@bot.message_handler(
    func=lambda message: message.text == "Названию", state=UserInfoState.choose
)
@bot.message_handler(commands=["search_by_name"])
def choose_the_cocktail(message: Message) -> None:
    """
    Функция-хендлер для команды "search_by_name" бота.

    :param message: Сообщение пользователя.
    """
    bot.send_message(
        message.from_user.id,
        "Пожалуйста, введи название коктейля. ",
        reply_markup=ReplyKeyboardRemove(),
    )
    bot.set_state(message.from_user.id, UserInfoState.cocktail, message.chat.id)


@bot.message_handler(
    func=lambda message: message.text == "Ингредиенту", state=UserInfoState.choose
)
@bot.message_handler(commands=["search_by_ing"])
def choose_the_ingredient(message: Message) -> None:
    """
    Функция-хендлер для команды "search_by_ing" бота.

    :param message: Сообщение пользователя.
    """
    bot.send_message(
        message.from_user.id,
        "Пожалуйста, введи ингредиент. ",
        reply_markup=ReplyKeyboardRemove(),
    )
    bot.set_state(message.from_user.id, UserInfoState.ingredient, message.chat.id)
