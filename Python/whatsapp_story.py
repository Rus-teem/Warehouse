

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

IMAGE_PATH = "story.jpg"  # Замени, если имя файла другое

def publish_story():
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=./User_Data")  # сохраняем сессию входа
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("https://web.whatsapp.com/")
    print("🔐 Отсканируй QR-код в открывшемся окне браузера...")

    time.sleep(20)  # время на авторизацию

    try:
        # Клик по иконке статуса
        status_icon = driver.find_element(By.XPATH, '//span[contains(@data-icon, "status-v3")]')
        status_icon.click()
        time.sleep(2)

        # Клик по кнопке "добавить статус"
        add_status = driver.find_element(By.XPATH, '//div[@title="Click to add status update"]')
        add_status.click()
        time.sleep(2)

        # Загрузка файла
        upload_input = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        upload_input.send_keys(os.path.abspath(IMAGE_PATH))
        time.sleep(5)

        # Отправка статуса
        send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
        send_button.click()

        print("✅ Сториз опубликован!")

    except Exception as e:
        print(f"⚠️ Ошибка: {e}")

    time.sleep(3)
    driver.quit()

if __name__ == "__main__":
    publish_story()