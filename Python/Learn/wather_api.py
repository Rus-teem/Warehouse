"""Запрос погоды через OpenWeatherMap API и вывод в консоль."""

import requests


class requestApi:
    """Класс для хранения параметров запроса к API погоды."""

    def __init__(self, city, cityId, appId, units, lang):
        self.city = city
        self.cityId = cityId
        self.appId = appId
        self.units = units
        self.lang = lang


requestApiBody = requestApi(
    "Казань",
    551487,
    "79d1ca96933b0328e1c7e3e7a26cb347",
    "metric",
    "ru"
)

url = (
    "https://api.openweathermap.org/data/2.5/weather?q="
    + requestApiBody.city
    + "&units=" + requestApiBody.units
    + "&lang=" + requestApiBody.lang
    + "&appid=" + requestApiBody.appId
)

weather_data = requests.get(url).json()
data_requests = dict(weather_data)

temperature = round(weather_data["main"]["temp"])
temperature_feels = round(weather_data["main"]["feels_like"])
weatherSky3 = data_requests["weather"][0]["description"]


def changeWords():
    """Возвращает комментарий в зависимости от температуры."""
    if temperature >= 30:
        return "и это капец как жарко"
    elif temperature >= 25:
        return "и это еще терпимо"
    return ""


def comment():
    """Возвращает комментарий об ощущении температуры."""
    if temperature >= 25 and (temperature_feels - temperature) >= 3:
        return ", а по ощущениям еще жарче"
    return ""


print("Сейчас в городе", requestApiBody.city, str(temperature), "°C", changeWords())
print("Ощущается как", str(temperature_feels), "°C", comment())
print("Состояние неба:", str(weatherSky3))
