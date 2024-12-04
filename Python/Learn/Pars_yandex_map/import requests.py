import requests
from bs4 import BeautifulSoup
import time

# Устанавливаем заголовки для имитации запроса от браузера
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# URL страницы с данными (предположим, что это страница Яндекс.Карт или другой открытый сайт)
url = 'https://yandex.ru/maps/43/kazan/category/design_studio/184108267/'

# Функция для получения и парсинга страницы
def get_studio_data(url):
    # Отправляем GET запрос на страницу
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        # Преобразуем содержимое страницы в объект BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Ищем все блоки, которые содержат нужные нам данные
        studios = soup.find_all('div', class_='org_item')  # Пример, зависит от структуры сайта
        
        studio_data = []
        
        for studio in studios:
            # Извлекаем название студии
            name = studio.find('span', class_='org_name').text.strip() if studio.find('span', class_='org_name') else 'Не указано'
            # Извлекаем адрес
            address = studio.find('div', class_='org_address').text.strip() if studio.find('div', class_='org_address') else 'Не указан'
            # Извлекаем рейтинг
            rating = studio.find('div', class_='org_rating').text.strip() if studio.find('div', class_='org_rating') else 'Не указан'
            
            # Добавляем данные в список
            studio_data.append({
                'Name': name,
                'Address': address,
                'Rating': rating
            })
        
        return studio_data
    else:
        print(f"Ошибка загрузки страницы: {response.status_code}")
        return []

# Сохранение собранных данных в файл
def save_to_file(data, filename='design_studios.txt'):
    with open(filename, 'w', encoding='utf-8') as f:
        for studio in data:
            f.write(f"Название: {studio['Name']}\n")
            f.write(f"Адрес: {studio['Address']}\n")
            f.write(f"Рейтинг: {studio['Rating']}\n")
            f.write("-" * 40 + '\n')

# Основной код
if __name__ == "__main__":
    studio_data = get_studio_data(url)
    if studio_data:
        save_to_file(studio_data)
        print(f"Данные успешно сохранены в файл!")
    else:
        print("Не удалось собрать данные.")