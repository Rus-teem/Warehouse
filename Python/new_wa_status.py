import time
import logging
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# Константы
QR_SCAN_TIMEOUT = 180  # 3 минуты на сканирование QR-кода
ELEMENT_TIMEOUT = 20   # Общее время ожидания элементов
STATUS_TIMEOUT = 30    # Время ожидания для операций со статусом

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("whatsapp_status.log")
    ]
)

def whatsapp_login(driver):
    try:
        driver.get("https://web.whatsapp.com/")
        logging.info("Открыт WhatsApp Web. Отсканируйте QR-код (у вас есть %d секунд).", QR_SCAN_TIMEOUT)
        
        # Ожидаем появления панели чатов
        WebDriverWait(driver, QR_SCAN_TIMEOUT).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="chat-list"]'))
        )
        logging.info("Авторизация прошла успешно.")
    except TimeoutException:
        logging.error("QR-код не отсканирован вовремя.")
        raise
    except Exception as e:
        logging.error(f"Ошибка при авторизации: {e}")
        raise

def post_status(driver, media_path):
    try:
        # Проверка существования файла
        if not os.path.exists(media_path):
            raise FileNotFoundError(f"Файл не найден: {media_path}")

        # 1. Клик по кнопке статуса
        status_button = WebDriverWait(driver, ELEMENT_TIMEOUT).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[data-icon="status-outline"]'))
        )
        status_button.click()
        logging.info("Открыто меню статусов")

        # 2. Клик по кнопке добавления статуса
        add_button = WebDriverWait(driver, ELEMENT_TIMEOUT).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[data-icon="plus"]'))
        )
        add_button.click()
        logging.info("Открыт редактор статусов")

        # 3. Клик по кнопке добавления медиа
        media_button = WebDriverWait(driver, ELEMENT_TIMEOUT).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[data-icon="media-multiple"]'))
        )
        media_button.click()
        logging.info("Открыт выбор медиафайлов")

        # 4. Загрузка файла
        file_input = WebDriverWait(driver, ELEMENT_TIMEOUT).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="file"]'))
        )
        file_input.send_keys(media_path)
        logging.info(f"Файл {media_path} загружен")

        # 5. Ожидание загрузки и клик по кнопке отправки
        send_button = WebDriverWait(driver, STATUS_TIMEOUT).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Отправить"]'))
        )
        send_button.click()
        logging.info("Статус отправлен")

    except TimeoutException as e:
        logging.error(f"Элемент не найден за отведенное время: {e}")
        raise
    except Exception as e:
        logging.error(f"Ошибка при публикации статуса: {e}")
        raise

def job():
    media_path = r"C:\Users\rustem.husnutdinov\Pictures\Wall\listia_temnyj_rastenie_136935_3840x2400.jpg"

    # Настройка Chrome
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(service=service, options=options)

    try:
        whatsapp_login(driver)
        post_status(driver, media_path)
        time.sleep(5)  # Даем время для завершения отправки
    except Exception as e:
        logging.error(f"Ошибка в основном потоке: {e}")
    finally:
        driver.quit()
        logging.info("Браузер закрыт")

if __name__ == "__main__":
    job()