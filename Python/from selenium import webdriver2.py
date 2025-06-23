from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def submit_form_you_design(url, form_data):
    # Настройка веб-драйвера (Chrome)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Фоновый режим
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    except Exception as e:
        print(f"Ошибка при инициализации ChromeDriver: {e}")
        print("Попробуйте скачать ChromeDriver вручную и указать путь.")
        return

    try:
        # Открываем сайт
        driver.get(url)
        print(f"Открываем сайт: {url}")
        time.sleep(2)  # Даем странице начать загрузку

        # Прокрутка к форме
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        # Ожидание загрузки формы
        wait = WebDriverWait(driver, 20)  # Увеличиваем время ожидания до 20 секунд

        # Проверка на iframe
        try:
            iframes = driver.find_elements(By.TAG_NAME, "iframe")
            if iframes:
                print(f"Обнаружено {len(iframes)} iframe, переключаемся на первый")
                driver.switch_to.frame(iframes[0])
        except Exception as e:
            print(f"Ошибка при проверке iframe: {e}")

        # Проверка на модальное окно
        try:
            modal_trigger = driver.find_elements(By.XPATH, "//button[contains(text(), 'Заказать') or contains(text(), 'Оставить заявку')]")
            if modal_trigger:
                modal_trigger[0].click()
                print("Кликнули на кнопку для открытия формы")
                time.sleep(1)
        except Exception as e:
            print(f"Ошибка при открытии модального окна: {e}")

        # Заполнение поля имени
        try:
            name_field = wait.until(EC.visibility_of_element_located((By.NAME, "name")))
            name_field.click()  # Клик для активации
            name_field.clear()
            name_field.send_keys(form_data["name"])
            print("Поле имени заполнено")
        except Exception as e:
            print(f"Ошибка при заполнении поля имени: {e}")
            print("HTML формы для отладки:")
            form = driver.find_elements(By.TAG_NAME, "form")
            if form:
                print(form[0].get_attribute("outerHTML")[:2000])  # Вывод HTML формы
            else:
                print("Форма не найдена")
            return

        # Заполнение поля телефона
        try:
            phone_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='tel']")))
            driver.execute_script("arguments[0].scrollIntoView(true);", phone_field)  # Прокрутка к элементу
            phone_field.click()  # Клик для активации
            phone_field.clear()
            phone_field.send_keys(form_data["phone"])
            print("Поле телефона заполнено")
        except Exception as e:
            print(f"Ошибка при заполнении поля телефона: {e}")
            # Пробуем альтернативный селектор
            try:
                phone_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@name, 'phone') or contains(@id, 'phone')]")))
                driver.execute_script("arguments[0].scrollIntoView(true);", phone_field)
                phone_field.click()
                phone_field.clear()
                phone_field.send_keys(form_data["phone"])
                print("Поле телефона заполнено через XPATH")
            except Exception as e:
                print(f"Ошибка при поиске поля телефона по XPATH: {e}")
                print("HTML формы для отладки:")
                form = driver.find_elements(By.TAG_NAME, "form")
                if form:
                    print(form[0].get_attribute("outerHTML")[:2000])
                else:
                    print("Форма не найдена")
                return

        # Нажатие кнопки отправки
        try:
            submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Оставить заявку') or contains(text(), 'Отправить')]")))
            driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
            submit_button.click()
            print("Форма успешно отправлена")
            time.sleep(2)  # Ждем ответа
        except Exception as e:
            print(f"Ошибка при отправке формы: {e}")
            return

    finally:
        # Закрываем браузер
        driver.quit()

if __name__ == "__main__":
    # Данные для формы
    form_data = {
        "name": "Иван Иванов",
        "phone": "+79991234567"
    }

    # URL сайта
    url = "https://you-design-studio.ru/"

    # Отправка формы
    submit_form_you_design(url, form_data)