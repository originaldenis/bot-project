import requests
import json
from botdir.api.translate_api import to_translate


def search_cocktail(name):
    """
    Функция для поиска коктейля по названию.

    :param name: Передается название коктейля.
    :return: Список составляющих искомого коктейля.
    (Алкогольный или нет, Название, Инструкция по приготовлению, Состав)
    """
    by_name = requests.get(
        f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={name}"
    )
    result_by_name = json.loads(by_name.text)
    if result_by_name["drinks"] is None:
        return None
    else:
        ingredient_list = list()
        common_list = list()
        cocktail_dict = dict()
        for i_drink in result_by_name["drinks"]:
            cocktail_dict["Название коктейля"] = i_drink["strDrink"]
            cocktail_dict["Алкогольный или нет"] = i_drink["strAlcoholic"][1:-7]
            cocktail_dict["Инструкция по приготовлению"] = i_drink["strInstructions"]
            for i_key, i_value in i_drink.items():
                if "strIngredient" in i_key and i_value is not None:
                    ingredient_list.append(i_value)
                for i_elem in range(len(ingredient_list)):
                    if f"strMeasure{i_elem}" in i_key and i_value is not None:
                        ingredient_list[i_elem - 1] = (
                            f"{ingredient_list[i_elem - 1]} (amount:{i_value})"
                        )
            cocktail_dict["Ингредиенты"] = ingredient_list.copy()
            common_list.append(cocktail_dict.copy())
            ingredient_list.clear()
    return common_list


# cocktail = {f'Название коктейля: {to_translate(name)}({name}), '
#                         f' Алкогольный или нет: {to_translate(alc_or_not)[1:-7]}'
#                         f' Ингредиенты: {to_translate(ingredient_list)}'
#                         f' Инструкция по приготовлению:{to_translate(instr)}'}
def search_ingredient(ingredient):
    """
    Функция для поиска коктейля по ингредиенту.

    :param ingredient: Передается ингредиент.
    :return: Список коктейлей,где встречается этот ингредиент.
    """
    by_ingredient = requests.get(
        f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={ingredient}"
    )
    if len(by_ingredient.text) > 2:
        result_by_ingredient = json.loads(by_ingredient.text)
        drink_list = list()
        for i_num, i_item in enumerate(result_by_ingredient["drinks"], start=1):
            drink_list.append(f'{i_num}.{i_item["strDrink"]}')
        return drink_list
    else:
        return None


# drink_list.append(f'{i_num}.{i_item["strDrink"]}({to_translate(i_item["strDrink"])})')
