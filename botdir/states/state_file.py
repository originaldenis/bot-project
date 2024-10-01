from telebot.handler_backends import State, StatesGroup


class UserInfoState(StatesGroup):
    """
    Дочерний класс, описывающий состояния пользователя в общении с ботом.

    Родитель: StatesGroup

    """

    name = State()
    history = State()
    help = State()
    choose = State()
    ingredient = State()
    cocktail = State()
    if_continue = State()
