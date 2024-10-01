from typing import List, Dict, TypeVar
from botdir.database.common.models import BaseModel
from peewee import ModelSelect
from botdir.database.common.models import db

T = TypeVar("T")


def _create_note(base: db, model: T, *data: List[Dict]) -> None:
    """
    Функция для создания записей в таблице базы данных.

    :param base: Используемая база данных.
    :param model: Используемая таблица.
    :param data: Требуемые данные для внесения.
    """
    with base.atomic():
        model.insert_many(*data).execute()


def _read_history(base: db, model: T, user_name: str = None) -> ModelSelect:
    """
    Функция для прочтения записей из таблицы базы данных.

    :param base: Используемая база данных.
    :param model: Используемая таблица.
    :param user_name: Имя пользователя, чьи записи необходимо посмотреть.
    :return: Список строк таблицы.
    """
    with base.atomic():
        hist = (
            model.select()
            .where(model.User == user_name)
            .order_by(model.id.desc())
            .dicts()
        )
        hist = hist.limit(5)
        return hist


def _delete_rows(base: db, model: T, *columns: BaseModel) -> None:
    """
    Функция для удаления строк из таблицы базы данных.

    :param base: Используемая база данных.
    :param model: Используемая таблица.
    :param columns: Значение в столбце id для удаления этой строки
    """
    with base.atomic():
        model.delete().where(*columns).execute()


class CRUDInterface:
    """
    Класс, описывающий интерфейс создания, удаления и чтения записей из таблицы базы данных.

    """

    @staticmethod
    def write(base, model, data) -> None:
        """
        Метод для создания записей в таблице базы данных.

        :param base: Используемая база данных.
        :param model: Используемая таблица.
        :param data: Требуемые данные для внесения.
        """
        return _create_note(base, model, data)

    @staticmethod
    def read(base, model, user_name) -> ModelSelect:
        """
        Метод для прочтения записей из таблицы базы данных.

        :param base: Используемая база данных.
        :param model: Используемая таблица.
        :param user_name: Имя пользователя, чьи записи необходимо посмотреть.
        :return: Список строк таблицы.
        """
        return _read_history(base, model, user_name)

    @staticmethod
    def delete(base, model, data) -> None:
        """
        Метод для удаления строк из таблицы базы данных.

        :param base: Используемая база данных.
        :param model: Используемая таблица.
        :param data: Значение в столбце id для удаления этой строки
        """
        return _delete_rows(base, model, data)


if __name__ == "main":
    _create_note(base=db, model=T)
    _delete_rows(base=db, model=T)
    _read_history(base=db, model=T)
    CRUDInterface()
