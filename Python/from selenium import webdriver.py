"""Универсальный скрипт для заполнения и отправки веб-форм через Selenium."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def submit_form(url, form_data):
    """Заполняет форму на указанном URL и отправляет её."""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get(url)
        time.sleep(2)

        try:
            name_field = driver.find_element(By.NAME, "name")
            name_field.send_keys(form_data["name"])

            email_field = driver.find_element(By.NAME, "email")
            email_field.send_keys(form_data["email"])

            message_field = driver.find_element(By.NAME, "message")
            message_field.send_keys(form_data["message"])

            submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            submit_button.click()

            print(f"Форма успешно отправлена на {url}")
            time.sleep(2)

        except Exception as e:
            print(f"Ошибка при заполнении формы на {url}: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    form_data = {
        "name": "Иван Иванов",
        "email": "ivan@example.com",
        "message": "Тестовое сообщение"
    }
    websites = ["https://example.com/form"]
    for site in websites:
        print(f"Обрабатываем сайт: {site}")
        submit_form(site, form_data)
