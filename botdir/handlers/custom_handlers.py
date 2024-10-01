from botdir.loader.loader_file import bot
from botdir.keyboards.reply_key_for_choose import Keyboards
from telebot.types import ReplyKeyboardRemove, MenuButtonCommands, ForceReply
from botdir.states.state_file import UserInfoState
from telebot.types import Message
from botdir.api.for_search_file import search_cocktail, search_ingredient
from botdir.database.common.models import db, History

# from botdir.api.translate_api import translate_to_en
from botdir.database.utils.core import CRUDInterface


@bot.message_handler(state=UserInfoState.name)
def get_name(message: Message) -> None:
    """
    Функция-хендлер сообщений для знакомства и дальнейшего определения параметров поиска коктейля.

    :param message: Сообщение пользователя.
    """
    if message.text.isalpha():
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data["User"] = message.from_user.username
        bot.send_message(
            message.from_user.id, f"Приятно познакомиться,{message.text}! "
        )
        bot.send_message(
            message.from_user.id,
            f"Ищем коктейль по названию или ингредиенту?",
            reply_markup=Keyboards.users_choice_keyboard(),
        )
        bot.set_state(message.from_user.id, UserInfoState.choose, message.chat.id)
    else:
        bot.send_message(message.from_user.id, "Имя может содержать только буквы")


@bot.message_handler(state=UserInfoState.cocktail)
def cocktail_search(message: Message) -> None:
    """
    Функция-хендлер для показа результата поиска коктейля по названию.

    :param message: Сообщение пользователя
    """
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["Cocktail"] = message.text  # translate_to_en(message.text)
        data["Search_param"] = "Cocktail"
        data["Ingredient"] = None
        if "User" not in data.keys():
            data["User"] = message.from_user.username
    result = search_cocktail(data["Cocktail"])
    if not result:
        bot.send_message(
            message.from_user.id,
            "Такого коктейля не существует!Проверьте и повторите ввод!",
        )
    else:
        CRUDInterface.write(db, History, [data])
        for i in result:
            bot.send_message(message.from_user.id, f"Результат поиска: ")
            for i_key, i_value in i.items():
                if i_key != "Ингредиенты":
                    bot.send_message(message.from_user.id, f" \n{i_key} :{i_value}. ")
                else:
                    bot.send_message(message.from_user.id, f" \n{i_key} : ")
                    for i_ing in i_value:
                        bot.send_message(message.from_user.id, f" {i_ing} ")
    bot.set_state(message.from_user.id, UserInfoState.if_continue, message.chat.id)
    bot.send_message(
        message.chat.id, f"Поищем другой вариант?", reply_markup=Keyboards.exit_search()
    )


@bot.message_handler(state=UserInfoState.ingredient)
def cocktail_search(message: Message) -> None:
    """
    Функция-хендлер для показа результата поиска коктейля по ингредиенту.

    :param message: Сообщение пользователя
    """
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["Ingredient"] = message.text  # translate_to_en(message.text)
        data["Search_param"] = "Ingredient"
        data["Cocktail"] = None
        if "User" not in data.keys():
            data["User"] = message.from_user.username
    result = search_ingredient(data["Ingredient"])
    if not result:
        bot.send_message(
            message.from_user.id,
            "Такого коктейля не существует!Проверьте и повторите ввод!",
        )
    else:
        CRUDInterface.write(db, History, [data])
        bot.send_message(message.from_user.id, f"Результат поиска: {result}. ")
        bot.set_state(message.from_user.id, UserInfoState.if_continue, message.chat.id)
        bot.send_message(
            message.chat.id,
            f"Поищем другой вариант?",
            reply_markup=Keyboards.exit_search(),
        )


@bot.message_handler(state=UserInfoState.if_continue)
def continue_search(message: Message) -> None:
    """
    Функция-хендлер для продолжения поиска по параметрам ,просмотра истории, либо завершения диалога.

    :param message: Сообщение пользователя
    """
    if message.text == "Поищу другое":
        bot.set_state(message.from_user.id, UserInfoState.choose, message.chat.id)
        ReplyKeyboardRemove()
        bot.send_message(
            message.from_user.id,
            f"Ищем коктейль по названию или ингредиенту?",
            reply_markup=Keyboards.users_choice_keyboard(),
        )
    elif message.text == "Завершить поиск":
        bot.delete_state(message.from_user.id, message.chat.id)
        bot.send_message(
            message.from_user.id,
            f"Был рад помочь!Наслаждайся коктейлем!Жду тебя снова) ",
            reply_markup=ReplyKeyboardRemove(),
        )
    else:
        bot.set_state(message.from_user.id, UserInfoState.history, message.chat.id)
        bot.send_message(
            message.chat.id,
            "Нажми на /history или выбери в меню",
        )
