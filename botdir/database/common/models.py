from peewee import *

db = SqliteDatabase("Search_history_base.db")


class BaseModel(Model):
    """
    Дочерний класс базовой модели для создания таблицы, от которого будет наследоваться основная таблица.

    Родитель: Model
    """

    id = PrimaryKeyField(unique=True, null=False)

    class Meta:
        database = db


class History(BaseModel):
    """
    Дочерний класс, описывающий модель таблицы в базе данных.

    Родитель: BaseModel
    """

    User = TextField(null=True)
    Search_param = TextField(null=True)
    Cocktail = TextField(null=True)
    Ingredient = TextField(null=True)
