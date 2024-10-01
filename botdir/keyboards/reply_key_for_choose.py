from telebot.types import ReplyKeyboardMarkup, KeyboardButton


class Keyboards:
    """
    Класс, описывающий используемые клавиатуры бота.

    """

    @staticmethod
    def users_choice_keyboard() -> ReplyKeyboardMarkup:
        """
        Метод, дающий пользователю клавиатуру для выбора параметров поиска.

        :return: Объект клавиатуры.
        """
        keyb = ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = KeyboardButton(text="Названию")
        button_2 = KeyboardButton(text="Ингредиенту")
        keyb.add(button_1, button_2)
        return keyb

    @staticmethod
    def exit_search() -> ReplyKeyboardMarkup:
        """
        Метод, дающий пользователю клавиатуру для выбора параметров поиска.

        :return: Объект клавиатуры.
        """
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = KeyboardButton(text="Завершить поиск")
        button_2 = KeyboardButton(text="Поищу другое")
        button_3 = KeyboardButton(text="История поиска")
        keyboard.add(button_1, button_2, button_3)
        return keyboard
