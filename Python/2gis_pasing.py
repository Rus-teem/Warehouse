"""Многостраничный парсер стоматологий на 2GIS с сохранением в CSV."""

import requests
from bs4 import BeautifulSoup
import lxml
import time
from fake_useragent import UserAgent
import random
import pandas as pd
from pathlib import Path

path = Path("Parsing_results")
path.mkdir(parents=True, exist_ok=True)

num_of_page = 16
start_num_of_page = 2
url1 = 'https://2gis.ru/kazan/search/%D0%A1%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B8'
url3 = 'https://2gis.ru/kazan/search/%D0%A1%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B8/page/'

url_list = [url1] + [f"{url3}{n}" for n in range(start_num_of_page, num_of_page)]

ua = UserAgent()
user_agent_for_request = {"User-Agent": str(ua.chrome)}

company_name_list = []
company_type_list = []
ad_list = []
score_list = []
number_of_ratings_list = []

for url_substitution in url_list:
    response = requests.get(url_substitution, headers=user_agent_for_request, timeout=random.randint(4, 10))
    print(f"{url_substitution} {response.status_code}")

    soup = BeautifulSoup(response.text, 'lxml')

    name_company = soup.find_all('span', class_='_1cd6avd')
    for element in name_company:
        company_name_list.append(element.text.replace('\xa0', ''))

    type_company = soup.find_all('span', class_='_oqoid')
    for element in type_company:
        company_type_list.append(element.text.replace('\xa0', ''))

    general_object = soup.find_all('div', class_='_1kf6gff')
    for container in general_object:
        inner_element = container.find('span', class_='_owmyyi')
        ad_list.append("Yes" if inner_element else "No")

    for container in general_object:
        inner_element = container.find('div', class_='_y10azs')
        score_list.append(inner_element.text if inner_element else "No")

    for container in general_object:
        inner_element = container.find('div', class_='_jspzdm')
        if inner_element:
            text = inner_element.text
            for word in [' оценок', ' оценки', ' оценка']:
                text = text.replace(word, '')
            number_of_ratings_list.append(text)
        else:
            number_of_ratings_list.append("No")

    time.sleep(2)

data = {
    'Название компании': company_name_list,
    'Тип компании': company_type_list,
    'Наличие рекламы': ad_list,
    'Балл компании': score_list,
    'Количество оценок': number_of_ratings_list
}

df = pd.DataFrame(data)
df.to_csv('Parsing_results/Результаты_парсинга.csv', index=False, encoding='windows-1251')

print(company_name_list, company_type_list, ad_list, score_list, number_of_ratings_list)
print(df)
