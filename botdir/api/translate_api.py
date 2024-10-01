import json
import requests


def to_translate(text: str) -> str:
    """
    Функция для перевода текста с английского на русский язык.

    :param text: Передается текст на английском для перевода.
    :return: Текст на русском.
    """
    url = "https://deep-translate1.p.rapidapi.com/language/translate/v2"

    payload = {"q": f"{text}", "source": "en", "target": "ru"}
    headers = {
        "x-rapidapi-key": "e5057e5c09msh583abef55da6715p1b81c7jsn09051801c86b",
        "x-rapidapi-host": "deep-translate1.p.rapidapi.com",
        "Content-Type": "application/json",
    }

    response = requests.post(url, json=payload, headers=headers)
    response2 = json.loads(response.text)

    return json.dumps(
        response2["data"]["translations"]["translatedText"], ensure_ascii=False
    )


def translate_to_en(text: str) -> str:
    """
    Функция для перевода текста с русского языка на английский.

    :param text: Передается текст на русском для перевода.
    :return: Текст на английском.
    """
    url = "https://deep-translate1.p.rapidapi.com/language/translate/v2"

    payload = {"q": f"{text}", "source": "ru", "target": "en"}
    headers = {
        "x-rapidapi-key": "e5057e5c09msh583abef55da6715p1b81c7jsn09051801c86b",
        "x-rapidapi-host": "deep-translate1.p.rapidapi.com",
        "Content-Type": "application/json",
    }

    response = requests.post(url, json=payload, headers=headers)
    response2 = json.loads(response.text)
    resp = str(json.dumps(response2["data"]["translations"]["translatedText"])).strip(
        '"'
    )
    return resp
