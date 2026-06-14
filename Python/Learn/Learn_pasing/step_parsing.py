"""Базовый парсинг страницы 2GIS с сохранением HTML в файл."""

from bs4 import BeautifulSoup
import requests

url = "https://2gis.ru/kazan/search/%D1%81%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F"

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

time_out_req = 5
response = requests.get(url, headers=headers, timeout=time_out_req)

status_code_answer = response.status_code
print("Status code:", status_code_answer)

# Сохранение HTML-ответа в файл
with open("htmlAnswer2gis.txt", mode="w", encoding="utf-8") as file:
    file.write(response.text)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    print("Title:", soup.title.text)
else:
    print(f"Ошибка при запросе: {response.status_code}")
