import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def whatsapp_login(driver):
    try:
        driver.get("https://web.whatsapp.com/")
        logging.info("Открыт WhatsApp Web. Отсканируйте QR-код (у вас есть 90 секунд).")
        
        # Просто даём время на ручную авторизацию
        time.sleep(90)

        # Проверим, появился ли интерфейс WhatsApp после авторизации
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Статус"]'))
        )
        logging.info("Авторизация прошла успешно.")
    except TimeoutException:
        logging.error("QR-код не отсканирован вовремя или страница не загрузилась.")
        raise

def post_status(driver, media_path):
    try:
        status_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Статус"]'))
        )
        status_button.click()

        add_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Добавить статус"]'))
        )
        add_button.click()

        input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="file"]'))
        )
        input_element.send_keys(media_path)
        logging.info("Медиафайл загружен.")

        send_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Отправить"]'))
        )
        send_button.click()
        logging.info("Статус успешно опубликован.")
    except NoSuchElementException as e:
        logging.error(f"Элемент не найден: {e}")
    except TimeoutException as e:
        logging.error(f"Таймаут при ожидании элемента: {e}")
    except Exception as e:
        logging.error(f"Ошибка при публикации статуса: {e}")

def job():
    media_path = r"C:\Users\rustem.husnutdinov\Pictures\Wall\listia_temnyj_rastenie_136935_3840x2400.jpg"

    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=service, options=options)

    try:
        whatsapp_login(driver)
        post_status(driver, media_path)
    except Exception as e:
        logging.error(f"Ошибка выполнения задачи: {e}")
    finally:
        driver.quit()
        logging.info("Браузер закрыт.")

# Запуск
job()
