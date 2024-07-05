# подключаем библиотеку для работы с запросами
import requests
import json

# указываем город
city = "Казань"
cityId = 551487
appId = "79d1ca96933b0328e1c7e3e7a26cb347"
# формируем запрос
url = (
    "https://api.openweathermap.org/data/2.5/weather?q="
    + city
    + "&units=metric&lang=ru&appid="
    + appId
)
# отправляем запрос на сервер и сразу получаем результат
weather_data = requests.get(url).json()
data_requests = dict(weather_data)
# print(data_requests)
# получаем данные о температуре и о том, как она ощущается
temperature = round(weather_data["main"]["temp"])
temperature_feels = round(weather_data["main"]["feels_like"])
weatherSky = data_requests["weather"]
weatherSky2 = weatherSky[0]["description"]
# выводим значения на экран
print("Сейчас в городе", city, str(temperature), "°C")
print("Ощущается как", str(temperature_feels), "°C")
print("Состояние неба:", str(weatherSky2))
# print(weather_data)
