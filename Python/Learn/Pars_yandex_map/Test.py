"""Парсинг дизайн-студий с 2GIS через Selenium."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://2gis.ru/kazan/search/%D0%94%D0%B7%D0%B0%D0%B9%D0%BD%20%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%8C%D0%B5%D1%80%D0%BE%D0%B2/rubricId/331"


def get_studio_data(url):
    """Извлекает название, адрес и рейтинг студий с 2GIS."""
    driver.get(url)
    time.sleep(5)
    studio_data = []
    studios = driver.find_elements(By.CLASS_NAME, "org_item")
    for studio in studios:
        name = studio.find_element(By.CLASS_NAME, "_1cd6avd ").text if studio.find_element(By.CLASS_NAME, "_1cd6avd ") else "Не указано"
        address = studio.find_element(By.CLASS_NAME, "org_address").text if studio.find_element(By.CLASS_NAME, "org_address") else "Не указан"
        rating = studio.find_element(By.CLASS_NAME, "org_rating").text if studio.find_element(By.CLASS_NAME, "org_rating") else "Не указан"
        studio_data.append({"Name": name, "Address": address, "Rating": rating})
    return studio_data


def save_to_file(data, filename='design_studios_selenium.txt'):
    """Сохраняет данные о студиях в текстовый файл."""
    with open(filename, 'w', encoding='utf-8') as f:
        for studio in data:
            f.write(f"Название: {studio['Name']}\nАдрес: {studio['Address']}\nРейтинг: {studio['Rating']}\n" + "-"*40 + "\n")


if __name__ == "__main__":
    studio_data = get_studio_data(url)
    if studio_data:
        save_to_file(studio_data)
        print("Данные успешно сохранены в файл!")
    else:
        print("Не удалось собрать данные.")
    driver.quit()
