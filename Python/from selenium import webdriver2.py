"""Заполнение и отправка формы на you-design-studio.ru через Selenium."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


def submit_form_you_design(url, form_data):
    """Заполняет форму на сайте you-design-studio.ru: имя, телефон и отправляет."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    except Exception as e:
        print(f"Ошибка при инициализации ChromeDriver: {e}")
        return

    try:
        driver.get(url)
        print(f"Открываем сайт: {url}")
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        wait = WebDriverWait(driver, 20)

        try:
            iframes = driver.find_elements(By.TAG_NAME, "iframe")
            if iframes:
                print(f"Обнаружено {len(iframes)} iframe, переключаемся на первый")
                driver.switch_to.frame(iframes[0])
        except Exception as e:
            print(f"Ошибка при проверке iframe: {e}")

        try:
            modal_trigger = driver.find_elements(
                By.XPATH, "//button[contains(text(), 'Заказать') or contains(text(), 'Оставить заявку')]"
            )
            if modal_trigger:
                modal_trigger[0].click()
                print("Кликнули на кнопку для открытия формы")
                time.sleep(1)
        except Exception as e:
            print(f"Ошибка при открытии модального окна: {e}")

        try:
            name_field = wait.until(EC.visibility_of_element_located((By.NAME, "name")))
            name_field.click()
            name_field.clear()
            name_field.send_keys(form_data["name"])
            print("Поле имени заполнено")
        except Exception as e:
            print(f"Ошибка при заполнении поля имени: {e}")
            return

        try:
            phone_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='tel']")))
            driver.execute_script("arguments[0].scrollIntoView(true);", phone_field)
            phone_field.click()
            phone_field.clear()
            phone_field.send_keys(form_data["phone"])
            print("Поле телефона заполнено")
        except Exception as e:
            print(f"Ошибка при заполнении поля телефона: {e}")
            try:
                phone_field = wait.until(
                    EC.visibility_of_element_located((By.XPATH, "//input[contains(@name, 'phone') or contains(@id, 'phone')]"))
                )
                driver.execute_script("arguments[0].scrollIntoView(true);", phone_field)
                phone_field.click()
                phone_field.clear()
                phone_field.send_keys(form_data["phone"])
                print("Поле телефона заполнено через XPATH")
            except Exception as e2:
                print(f"Ошибка при поиске поля телефона по XPATH: {e2}")
                return

        try:
            submit_button = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(text(), 'Оставить заявку') or contains(text(), 'Отправить')]")
                )
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
            submit_button.click()
            print("Форма успешно отправлена")
            time.sleep(2)
        except Exception as e:
            print(f"Ошибка при отправке формы: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    form_data = {"name": "Иван Иванов", "phone": "+79991234567"}
    url = "https://you-design-studio.ru/"
    submit_form_you_design(url, form_data)
