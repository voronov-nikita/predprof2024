#
# Файл, содержащий в себе основную логику проекта
# По сути здесь располагается вся backend часть, необходимая для обработки данных
# Обработанные данные возвращаются по обратно зависимому признаку, т.е пришел запрос - получен ответ
#


import requests
import json

URL = "https://olimp.miet.ru/ppo_it_final"
HEADER = {"X-Auth-Token": 'ppo_11_11573'}


session = requests.Session()

def getData(url: str = "/date") -> dict:
    '''
    Функция парсинга данных. 

    Функция принимает в себя url страницы для парсинга и возвращает словарь данных.

    '''
    p = session.get(URL+url, headers=HEADER)
    return json.loads(p.text)


def getAllData():
    res = []
    ls = getData()["message"]
    for elem in ls:
        data = elem.split("-")

        day = data[0]
        month = data[1]
        year = data[2]

        p = session.get(
            URL+f"?day={day}&month={month}&year={year}", headers=HEADER)
        res.append(json.loads(p.text)["message"])
    return res


def postData():
    data = {
        "data": {
        "count": 4,
        "rooms": [
            3,
            5,
            9,
            10
        ]
    },
        "date": "01-05-21"}
    HEADER = {"X-Auth-Token": 'ppo_11_11573'}
    p = session.post(URL, params=data, headers=HEADER)
    print(p.text)


# запуск тестирующих модулей по отдельности
if __name__ == "__main__":
    # print(getAllData())
    postData()
