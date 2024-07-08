# подключаем библиотеку для работы с запросами
import requests
# import json

# Для ручного ввода
# city = "Казань"
# cityId = 551487
# appId = "79d1ca96933b0328e1c7e3e7a26cb347"

#  Создали класс requestApi
class requestApi:
    def __init__(self, city, cityId, appId, units, lang):
        # указываем город
        self.city = city
        self.cityId = cityId
        self.appId = appId
        self.units = units
        self.lang = lang

# Создали объект на основе класса
requestApiBody = requestApi(
    "Казань", 
    551487, 
    "79d1ca96933b0328e1c7e3e7a26cb347", 
    "metric", 
    "ru"
)


# формируем запрос
url = (
    "https://api.openweathermap.org/data/2.5/weather?q="
    + requestApiBody.city
    + "&units="
    + requestApiBody.units
    + "&lang="
    + requestApiBody.lang
    + "&appid="
    + requestApiBody.appId
)
# отправляем запрос на сервер и сразу получаем результат
weather_data = requests.get(url).json()
data_requests = dict(weather_data)
# print(data_requests)

# получаем данные о температуре и о том, как она ощущается
temperature = round(weather_data["main"]["temp"])
temperature_feels = round(weather_data["main"]["feels_like"])

# Тут просто тестирую
# weatherSky = data_requests["weather"]
# weatherSky2 = weatherSky[0]["description"]

# Вывод состояния состояния неба
weatherSky3 = data_requests["weather"][0]["description"]

def changeWords():
    if temperature >= 25:
        if temperature >= 30:
            return "и это капец как жарко"
        else:
            return "и это еще терпимо"
    else:
        return ""


def comment():
    if temperature >= 25:
        if (temperature_feels - temperature) >= 3:
            return ", а по ощущениям еще жарче 😉"
        else:
            return ""
    else:
        return ""

# выводим значения на экран
print("Сейчас в городе", requestApiBody.city, str(temperature), "°C", changeWords())
print("Ощущается как", str(temperature_feels), "°C", comment())
print("Состояние неба:", str(weatherSky3))

# Сердечко
print(
    "\n".join(
        " ".join(*zip(*row))
        for row in (
            [
                [
                    (
                        "*"
                        if row == 0
                        and col % 3 != 0
                        or row == 1
                        and col % 3 == 0
                        or row - col == 2
                        or row + col == 8
                        else " "
                    )
                    for col in range(7)
                ]
                for row in range(6)
            ]
        )
    )
)
# print(weather_data)
