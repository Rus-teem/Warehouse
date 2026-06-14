"""Парсинг дизайн-студий с Яндекс.Карт через Selenium."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://yandex.ru/maps/43/kazan/category/design_studio/184108267/"


def get_studio_data(url):
    """Извлекает название, адрес и рейтинг студий со страницы Яндекс.Карт."""
    driver.get(url)
    time.sleep(3)
    studio_data = []
    studios = driver.find_elements(By.CLASS_NAME, "org_item")
    for studio in studios:
        name = studio.find_element(By.CLASS_NAME, "org_name").text if studio.find_element(By.CLASS_NAME, "org_name") else "Не указано"
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
