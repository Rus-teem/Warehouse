import requests
from bs4 import BeautifulSoup
import time

# Устанавливаем заголовки для имитации запроса от браузера
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# URL страницы с данными (предположим, что это страница Яндекс.Карт или другой открытый сайт)
url = "https://2gis.ru/kazan/search/%D0%94%D0%B8%D0%B7%D0%B0%D0%B9%D0%BD%20%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%8C%D0%B5%D1%80%D0%BE%D0%B2/rubricId/331/page/3"

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
            "div", class_="_1kf6gff")  # Пример, зависит от структуры сайта

        studio_data = []

        for studio in studios:
            # Извлекаем название студии
            name = (
                studio.find("span", class_="_1cd6avd").text.strip()
                if studio.find("span", class_="_1cd6avd")
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
            f.write(f"Адрес: {studio['Address']}\n")
            f.write(f"Рейтинг: {studio['Rating']}\n")
            f.write(f"Количество рейтинга: {studio['count_rating']}\n")
            f.write("-" * 40 + '\n')

# Основной код
if __name__ == "__main__":
    studio_data = get_studio_data(url)
    if studio_data:
        save_to_file(studio_data)
        print(f"Данные успешно сохранены в файл!")
    else:
        print("Не удалось собрать данные.")
