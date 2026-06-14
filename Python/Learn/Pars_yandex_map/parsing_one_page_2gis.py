"""Парсинг новостроек с Яндекс.Недвижимости через BeautifulSoup."""

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
url = "https://realty.yandex.ru/tatarstan/kupit/novostrojka/?deliveryDate=4_2027&buildingClass=COMFORT_PLUS&buildingClass=BUSINESS&buildingClass=ELITE&sort=COMMISSIONING_DATE"


def get_studio_data(url):
    """Извлекает данные о новостройках со страницы Яндекс.Недвижимости."""
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        studios = soup.find_all("div", class_="SiteSnippetSearch__info")
        studio_data = []
        for studio in studios:
            name = studio.find("h3", class_="SiteSnippetSearch__heading").text.strip() if studio.find("h3", class_="SiteSnippetSearch__heading") else "Не указано"
            type_firm = studio.find("span", class_="_oqoid").text.strip() if studio.find("span", class_="_oqoid") else "Не указано"
            address = studio.find("span", class_="_1w9o2igt").text.strip() if studio.find("span", class_="_1w9o2igt") else "Не указан"
            rating = studio.find("div", class_="_y10azs").text.strip() if studio.find("div", class_="_y10azs") else "Не указан"
            count_rating = studio.find("div", class_="_jspzdm").text.strip() if studio.find("div", class_="_jspzdm") else "Не указан"
            studio_data.append({"Name": name, "Address": address, "Rating": rating, "count_rating": count_rating, "type_firm": type_firm})
        return studio_data
    else:
        print(f"Ошибка загрузки страницы: {response.status_code}")
        return []


def save_to_file(data, filename='design_studios.txt'):
    """Сохраняет данные о новостройках в текстовый файл."""
    with open(filename, 'w', encoding='utf-8') as f:
        for studio in data:
            f.write(f"Название: {studio['Name']}\nТип компании: {studio['type_firm']}\nАдрес: {studio['Address']}\nРейтинг: {studio['Rating']}\nКоличество рейтинга: {studio['count_rating']}\n")


if __name__ == "__main__":
    studio_data = get_studio_data(url)
    if studio_data:
        save_to_file(studio_data)
        print("Данные успешно сохранены в файл!")
    else:
        print("Не удалось собрать данные.")
