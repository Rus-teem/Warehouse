import requests
from bs4 import BeautifulSoup
import time
import codecs

# Устанавливаем заголовки для имитации запроса от браузера
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# URL страницы с данными (предположим, что это страница Яндекс.Карт или другой открытый сайт)
url = "https://realty.yandex.ru/tatarstan/kupit/novostrojka/?deliveryDate=4_2027&buildingClass=COMFORT_PLUS&buildingClass=BUSINESS&buildingClass=ELITE&sort=COMMISSIONING_DATE"

# Функция для получения и парсинга страницы
def get_studio_data(url):
    # Отправляем GET запрос на страницу
    response = requests.get(url, headers=headers)
    print (response)
    if response.status_code == 200:
        # Преобразуем содержимое страницы в объект BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Ищем все блоки, которые содержат нужные нам данные
        studios = soup.find_all(
            "div", class_="SiteSnippetSearch__info"
        )  # Пример, зависит от структуры сайта

        studio_data = []

        for studio in studios:
            # Извлекаем название студии
            name = (
                studio.find("h3", class_="SiteSnippetSearch__heading").text.strip()
                if studio.find("h3", class_="SiteSnippetSearch__heading")
                else "Не указано"
            )
            utf8Lol = name.encode("utf-8")
            print(utf8Lol)
            # Извлекаем тип фирмы
            type_firm = (
                studio.find("span", class_="_oqoid").text.strip()
                if studio.find("span", class_="_oqoid")
                else "Не указано"
            )
            # Извлекаем адрес
            address = (
                studio.find("span", class_="_1w9o2igt").text.strip()
                if studio.find("span", class_="_1w9o2igt")
                else "Не указан"
            )
            # Извлекаем рейтинг
            # rating = studio.find('div', class_='org_rating').text.strip() if studio.find('div', class_='org_rating') else 'Не указан'
            rating = (
                studio.find("div", class_="_y10azs").text.strip()
                if studio.find("div", class_="_y10azs")
                else "Не указан"
            )
            count_rating = (
                studio.find("div", class_="_jspzdm").text.strip()
                if studio.find("div", class_="_jspzdm")
                else "Не указан"
            )
            # Добавляем данные в список
            studio_data.append(
                {
                    "Name": name,
                    "Address": address,
                    "Rating": rating,
                    "count_rating": count_rating,
                    "type_firm": type_firm,
                }
            )

        return studio_data
    else:
        print(f"Ошибка загрузки страницы: {response.status_code}")
        return []

# Сохранение собранных данных в файл
def save_to_file(data, filename='design_studios.txt'):
    with open(filename, 'w', encoding='utf-8') as f:
        for studio in data:
            f.write(f"Название: {studio['Name']}\n")
            f.write(f"Тип компании: {studio['type_firm']}\n")
            f.write(f"Адрес: {studio['Address']}\n")
            f.write(f"Рейтинг: {studio['Rating']}\n")
            f.write(f"Количество рейтинга: {studio['count_rating']}\n")
            # f.write("-" * 40 + '\n')

# Основной код
if __name__ == "__main__":
    studio_data = get_studio_data(url)
    if studio_data:
        save_to_file(studio_data)
        print(f"Данные успешно сохранены в файл!")
    else:
        print("Не удалось собрать данные.")
