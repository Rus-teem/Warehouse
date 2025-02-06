from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настройка Selenium

# Создание объекта настроек для браузера Chrome
options = webdriver.ChromeOptions()
# Добавление аргумента для запуска браузера в безголовом режиме (без GUI)
options.add_argument("--headless")

# Инициализация веб-драйвера Chrome с использованием настроек и менеджера драйверов
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)
# URL страницы Яндекс.Карт с дизайн-студиями
url = "https://yandex.ru/maps/43/kazan/category/design_studio/184108267/"


# Функция для сбора данных о студиях
def get_studio_data(url):
    driver.get(url)
    time.sleep(3)  # Ждем, пока страница полностью загрузится

    studio_data = []

    # Ищем элементы с данными о студиях
    studios = driver.find_elements(
        By.CLASS_NAME, "org_item"
    )  # Пример, зависит от структуры

    for studio in studios:
        name = (
            studio.find_element(By.CLASS_NAME, "org_name").text
            if studio.find_element(By.CLASS_NAME, "org_name")
            else "Не указано"
        )
        address = (
            studio.find_element(By.CLASS_NAME, "org_address").text
            if studio.find_element(By.CLASS_NAME, "org_address")
            else "Не указан"
        )
        rating = (
            studio.find_element(By.CLASS_NAME, "org_rating").text
            if studio.find_element(By.CLASS_NAME, "org_rating")
            else "Не указан"
        )

        studio_data.append({"Name": name, "Address": address, "Rating": rating})

    return studio_data


# Функция для сохранения данных в файл
def save_to_file(data, filename="design_studios_selenium.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for studio in data:
            f.write(f"Название: {studio['Name']}\n")
            f.write(f"Адрес: {studio['Address']}\n")
            f.write(f"Рейтинг: {studio['Rating']}\n")
            f.write("-" * 40 + "\n")


# Основной код
if __name__ == "__main__":
    studio_data = get_studio_data(url)
    if studio_data:
        save_to_file(studio_data)
        print(f"Данные успешно сохранены в файл!")
    else:
        print("Не удалось собрать данные.")

    driver.quit()  # Закрытие браузера после выполнения

