"""Функция для парсинга данных с Яндекс.Недвижимости (незавершённый скрипт)."""

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


def get_studio_data(url):
    """Извлекает данные о новостройках (незавершённая реализация)."""
    response = requests.get(url, headers=headers)
    print(response)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        studios = soup.find_all("div", class_="SiteSnippetSearch__info")
        studio_data = []
        for studio in studios:
            name = studio.find("h3", class_="SiteSnippetSearch__heading").text.strip() if studio.find("h3", class_="SiteSnippetSearch__heading") else "Не указано"
            # Дальнейшая обработка не завершена
            studio_data.append({"Name": name})
        return studio_data
    else:
        print(f"Ошибка загрузки страницы: {response.status_code}")
        return []
