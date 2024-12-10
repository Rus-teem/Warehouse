# pip install requests beautifulsoup4 - устанавливаем библиотеки 


import requests

# указываем в переменной url с которого мы будем забирать данные 
url = "https://2gis.ru/kazan/search/%D1%81%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F"

# отправляем фейковый user agent
headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

# Оправляем запрос по урлу с содержимым user agent
response = requests.get(url, headers=headers)

# проверка содержимого ответа черех другую переменную
status = response
print(f"Тут содержимое response: {status}")

print(response.status_code)

# response = requests.get("https://jsonplaceholder.typicode.com/posts", params={"userId": 1})
# print(response.status_code)  # Статус-код ответа (например, 200)
# # print(response.json())       # Преобразование JSON-ответа в Python-объект

# Проверяем статус-код ответа
# if response.status_code == 200:
#     print("Страница успешно загружена!")
# else:
#     print(f"Ошибка загрузки: {response.status_code}")



