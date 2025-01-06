# импортируем библиотку requests для запросов
import requests 

# импортируем модуль и берем класс BeautifulSoup
from bs4 import BeautifulSoup

# импорт библотеки для работы с html
import lxml

# импорт питеки для работы со времене, а также с задержками 
import time

# импорт библотеки для создания юзер агента
from fake_useragent import UserAgent

# импорт рандомайзера
import random

# Импорт библиотеки pandas
import pandas as pd

# Создание папок
from pathlib import Path


# ====================================================
# NOTE Создаем папку для результатов парсинга
# ====================================================


# Указываем путь для создания папки
path = Path("C:/Projects/Warehouse/Parsing_results")

# Создаем папку
path.mkdir(parents=True, exist_ok=True)

print(f"Папка создана по пути: {path}")


# ====================================================
# NOTE Создаем список для урлов
# ====================================================


# количество страниц
num_of_page = 16
# по умолчанию в 2 гис в гет запросах нужно начинать со второй страницы
start_num_of_page = 2


# создал url с которых будем производить парсинг 
url1 = 'https://2gis.ru/kazan/search/%D0%A1%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B8'
# пример формирования url2 = 'https://2gis.ru/kazan/search/%D0%A1%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B8/page/2'
url3 = 'https://2gis.ru/kazan/search/%D0%A1%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B8/page/'


# Создаем списки для урлов
url_list = []
# создаю лист с количеством страниц
range_list = list(range(start_num_of_page, num_of_page))

# Добавил первый url 
url_list.append(url1)

# добавил последующие урлы
for number in range_list:
    # произвожу Конкатенацию через "f" строки 
    url_concat = f"{url3}{number}"
    # добавляю в список 
    url_list.append(url_concat)



# ====================================================
# NOTE Создаем юзер агента
# ====================================================


# Создаем юзер агента
ua = UserAgent()

# сделал UA - chrome
ua_chrome = str(ua.chrome) 
# сделал ключ
key_ua_chrome = "User-Agent"
# сделал словарик 
user_agent_for_request = {}
# засунул ключ и значние в словарик 
user_agent_for_request[key_ua_chrome] = ua_chrome

# ====================================================
# NOTE Продолжаем готовить запрос
# ====================================================

# добавил в заголовок запроса юзер агента
headers = user_agent_for_request

# получаем рандомное количество секунд между запросами 
timeout_sek = random.randint(4, 10)

# ====================================================
# NOTE Создаем списки
# ====================================================

# список названий компаний
company_name_list = []
# список типов компаний
company_type_list = []
# лист с рекламой
ad_list = []
# лист с баллами
score_list = []
# количество оценок
number_of_ratings_list = []

# ====================================================
# NOTE Создаем dataFrame с помощью библиотеки pandas
# ====================================================

data = {
    'Название компании': company_name_list,
    'Тип компании': company_type_list,
    'Наличие рекламы': ad_list,
    'Балл компании': score_list,
    'Количество оценок': number_of_ratings_list
}

# ====================================================
# NOTE Создаем запрос
# ====================================================

# засунул в цикл чтобы автоматически перебирал урлы
for url_substitution in url_list:

    # делаем запрос
    response = requests.get(url_substitution, headers = headers, timeout=timeout_sek)
    # решил вывести чтобы смотреть как отпрабатывает запрос 
    print(f"{url_substitution} {response.status_code}")

    # начинаем парсинг и вместо html.parser используем библиотеку - lxml
    soup = BeautifulSoup(response.text, 'lxml')

    # ====================================================
    # IMPORTANT начинаем поиск элементов
    # ====================================================

    # ищем название компании по классу
    name_company = soup.find_all('span', class_='_1cd6avd')

    # удаляем пустоты отправляем данные в список
    for element in name_company:
        clean_text = element.text.replace('\xa0', '')
        company_name_list.append(clean_text)

    # ищем тип компании по классу
    type_company = soup.find_all('span', class_='_oqoid')

    for element in type_company:
        clean_text = element.text.replace('\xa0', '')
        company_type_list.append(clean_text)

    # Общие данные в котейнере где содердатся все элементы (решил сделать черз общий контейнер)
    general_object = soup.find_all('div', class_='_1kf6gff')

    # определяем по наличию класса есть ли там реклама
    for container in general_object:
        # Ищем элемент с классом "_owmyyi" внутри текущего контейнера
        inner_element = container.find('span', class_='_owmyyi')
        
        if inner_element:
            ad_list.append("Yes")
        else:
            ad_list.append("No")

    # ищем оценку - балл 
    for container in general_object:
        # Ищем элемент с классом "_y10azs" внутри текущего контейнера
        inner_element = container.find('div', class_='_y10azs').text
        score = inner_element
        
        if score:
            score_list.append(score)
        else:
            score_list.append("No")

    # ищем сколько компания получила оценок
    for container in general_object:
        # Ищем элемент с классом "_jspzdm" внутри текущего контейнера
        inner_element = str(container.find('div', class_='_jspzdm').text)
        # проходимся циклом чтобы убрать слова которые не нужны
        if ' оценок' in inner_element or ' оценки' in inner_element or ' оценка' in inner_element:
            clean_text = inner_element.replace(' оценок', '').replace(' оценки', '').replace(' оценка', '')
        
        if score:
            number_of_ratings_list.append(clean_text)
        else:
            number_of_ratings_list.append("No")
    # время между срабатываними цикла "for"
    time.sleep(2)

# ====================================================
# NOTE создаю dataframe по словарю data
# ====================================================

df = pd.DataFrame(data)
# сохраняю в csv файл, убираю индексы, а также устанавливаю кодировку
df.to_csv('C:/Projects/Warehouse/Parsing_results/Результаты_парсинга.csv', index=False, encoding='windows-1251')


# ====================================================
# FIXME просто вывожу чтобы посмотреть 
# ====================================================

# print("Отдельный элемент", range_list )
print("тут выводим лист ", company_name_list, company_type_list, ad_list, score_list, number_of_ratings_list)
print(df)