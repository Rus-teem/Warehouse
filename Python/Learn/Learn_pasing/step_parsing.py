# pip install requests beautifulsoup4 - устанавливаем библиотеки

# импорт бииблитеки bs4 
from bs4 import BeautifulSoup 

# импорт библиотеки bs4 
import requests

# указываем в переменной url с которого мы будем забирать данные
url = "https://2gis.ru/kazan/search/%D1%81%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F"

# отправляем фейковый user agent
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

# Устанавливаем время тайм аута в запросе
time_out_req = 5
# Оправляем запрос по урлу с содержимым user agent
response = requests.get(url, headers=headers, timeout=time_out_req)


# Получаем данные непосредственно код ответа
status_code_answer = response.status_code
print(status_code_answer)

# проверка содержимого ответа черех другую переменную
status = response
print(f"Тут содержимое response: {status}",
      f"а тут непосредствено код - {status_code_answer}")

# по сути получаю ответ тела HTML страницы
answerStroke = response.text

# записываю ответ в корень в формате .txt
with open("htmlAnswer2gis.txt", mode="w", encoding="utf-8") as file:
    file.write(answerStroke)

# Проверяем статус ответа
if response.status_code == 200:
    # Создаём объект BeautifulSoup из текста ответа
    soup = BeautifulSoup(response.text, 'html.parser')

    # Дальнейшая работа с soup
    print(soup.title.text)  # Выводим заголовок страницы
else:
    print(f"Ошибка при запросе: {response.status_code}")

print("текст заголовка", soup.title.text)


# items = soup.find_all(class_="_1cd6avd")
# title = items.soup.find('span')
# print(title)

