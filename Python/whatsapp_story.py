import os
import argparse
import requests
import tempfile
import sys

# Используемые библиотеки:
# - argparse: для чтения аргументов из командной строки
# - requests: загрузка изображения из URL
# - tempfile: временное сохранение файла
# - sys: для выхода при ошибке
# - selenium и модули из неё: для автоматизации браузера
# - webdriver_manager: автоматическая установка ChromeDriver
# - time: ожидания между действиями
# - traceback: логирование ошибок

parser = argparse.ArgumentParser(description="Publish WhatsApp story via WhatsApp Web")
parser.add_argument("image", nargs="?", help="Path to the image to publish")
parser.add_argument("--user-data-dir", default="./User_Data", help="Chrome user data directory")
parser.add_argument("--image-url", required=False, help="URL of the image to download and publish")
parser.add_argument("--use-wassenger", action="store_true", help="Use Wassenger API to publish status instead of Selenium")
parser.add_argument("--wa-token", help="Wassenger API token")
parser.add_argument("--wa-device-id", help="Wassenger device ID")
parser.add_argument("--headless", action="store_true", help="Run Chrome in headless mode (без UI)")
args = parser.parse_args()

# Determine source of the image: URL or positional argument
if args.image_url:
    try:
        response = requests.get(args.image_url)
        response.raise_for_status()
        suffix = os.path.splitext(args.image_url)[1] or ".jpg"
        tmpfile = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
        tmpfile.write(response.content)
        tmpfile.close()
        IMAGE_PATH = tmpfile.name
        print(f"✅ Изображение скачано во временный файл: {IMAGE_PATH}")
    except Exception as e:
        print(f"❌ Ошибка при скачивании изображения: {e}")
        sys.exit(1)
elif args.image:
    IMAGE_PATH = args.image
else:
    # Используем изображение по умолчанию
    IMAGE_PATH = "/Users/rustem/Pictures/Обои/photo-1542273917363-3b1817f69a2d.jpeg"
    print(f"ℹ️ Используется изображение по умолчанию: {IMAGE_PATH}")

USER_DATA_DIR = args.user_data_dir

import traceback
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Логирует текущее сообщение и DOM страницы в файл automation_combined_log.txt
def log_browser_action(driver, message):
    from datetime import datetime
    print(message)
    with open("automation_combined_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"[{datetime.now().isoformat()}] {message}\n")
        log_file.write(driver.execute_script("return document.documentElement.outerHTML") + "\n\n")

def publish_story():
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={USER_DATA_DIR}")
    if args.headless:
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    try:
        log_browser_action(driver, "🚀 Открываем WhatsApp Web...")
        driver.get("https://web.whatsapp.com/")
        log_browser_action(driver, "🔐 Отсканируй QR-код в открывшемся окне браузера...")
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))

        wait = WebDriverWait(driver, 60)
        log_browser_action(driver, "🧪 Начинаем попытку автоматизации...")

        status_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-icon='status-refreshed']")))
        status_button = status_icon.find_element(By.XPATH, './ancestor::button')
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", status_button)
        try:
            status_button.click()
        except Exception:
            log_browser_action(driver, "⚠️ Обычный клик не сработал, используем JS")
            driver.execute_script("arguments[0].click();", status_button)
        log_browser_action(driver, "👉 Нажали на кнопку статуса")
        time.sleep(2)

        add_status_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Add Status' or contains(@title, 'статус')]")))
        add_status_button.click()
        log_browser_action(driver, "👉 Кликаем по кнопке 'добавить статус'")
        time.sleep(1)

        media_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@role='button']//span[contains(text(), 'Фото') or contains(text(), 'Photo')]")))
        media_button.click()
        log_browser_action(driver, "👉 Кликаем по пункту 'Фото'")
        time.sleep(1)

        file_path = os.path.abspath(IMAGE_PATH)
        if not os.path.isfile(file_path):
            log_browser_action(driver, f"⚠️ Файл не найден по пути: {file_path}")
            return

        file_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))
        driver.execute_script("arguments[0].style.display = 'block';", file_input)
        file_input.send_keys(file_path)
        time.sleep(1)

        fresh_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        driver.execute_script("""
            arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
            arguments[0].dispatchEvent(new Event('blur', { bubbles: true }));
            arguments[0].dispatchEvent(new Event('drop', { bubbles: true }));
        """, fresh_input)
        log_browser_action(driver, "📤 Файл передан через send_keys без вызова Finder")

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label*='Просмотр']"))
            )
            log_browser_action(driver, "👀 Preview DOM загружен")
        except:
            log_browser_action(driver, "⚠️ Preview DOM не найден — продолжаем")
        time.sleep(2)

        log_browser_action(driver, "⏳ Ждём, когда кнопка отправки станет активной...")
        try:
            preview_confirm_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and (@aria-label='Готово' or @aria-label='Done')]"))
            )
            preview_confirm_button.click()
            log_browser_action(driver, "👉 Клик по кнопке 'Готово'")
            time.sleep(1)
        except:
            log_browser_action(driver, "ℹ️ Кнопка 'Готово' не найдена — возможно, не требуется")

        send_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and @aria-label='Отправить']")))
        send_button.click()
        log_browser_action(driver, "✅ Сториз опубликован!")
    except Exception as e:
        log_browser_action(driver, f"⚠️ Ошибка: {e}")
        traceback.print_exc()
        log_browser_action(driver, "🛑 Финальный DOM после ошибки (логируется в automation_combined_log.txt)")
    finally:
        time.sleep(3)
        driver.quit()
        print("👋 Сессия завершена. Браузер закрыт.")

if __name__ == "__main__":
    publish_story()