from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Функция для заполнения и отправки формы
def submit_form(url, form_data):
    # Настройка веб-драйвера (Chrome)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Открываем сайт
        driver.get(url)
        time.sleep(2)  # Ждем загрузки страницы

        # Пример заполнения полей формы (нужно адаптировать под конкретный сайт)
        try:
            # Поиск полей формы по имени, ID или другим селекторам
            name_field = driver.find_element(By.NAME, "name")  # Замените на реальный селектор
            name_field.send_keys(form_data["name"])
            
            email_field = driver.find_element(By.NAME, "email")  # Замените на реальный селектор
            email_field.send_keys(form_data["email"])
            
            message_field = driver.find_element(By.NAME, "message")  # Замените на реальный селектор
            message_field.send_keys(form_data["message"])
            
            # Поиск кнопки отправки
            submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")  # Замените на реальный селектор
            submit_button.click()
            
            print(f"Форма успешно отправлена на {url}")
            time.sleep(2)  # Ждем, чтобы увидеть результат
            
        except Exception as e:
            print(f"Ошибка при заполнении формы на {url}: {e}")
            
    finally:
        # Закрываем браузер
        driver.quit()

# Пример использования
if __name__ == "__main__":
    # Данные для формы
    form_data = {
        "name": "Иван Иванов",
        "email": "ivan@example.com",
        "message": "Тестовое сообщение"
    }
    
    # Список сайтов с формами
    websites = [
        "https://example.com/form",  # Замените на реальные URL
        # Добавьте другие сайты
    ]
    
    # Проходим по каждому сайту
    for site in websites:
        print(f"Обрабатываем сайт: {site}")
        submit_form(site, form_data)