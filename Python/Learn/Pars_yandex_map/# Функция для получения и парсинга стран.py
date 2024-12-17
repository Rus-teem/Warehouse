# Функция для получения и парсинга страницы
def get_studio_data(url):
    # Отправляем GET запрос на страницу
    response = requests.get(url, headers=headers)
    print(response)

    if response.status_code == 200:
        # тут надо добавить строчку перед преобразованиеем в оьъект
        # response.encoding = response.apparent_encoding -- если рес рузке, то атрибут обычно выручает
        # Преобразуем содержимое страницы в объект BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Ищем все блоки, которые содержат нужные нам данные
        #!если есть поиск, то надо обрабатывать!
        studios = soup.find_all(
            "div", class_="SiteSnippetSearch__info"
        )  # Пример, зависит от структуры сайта

        studio_data = []

        for studio in studios:
            # Извлекаем название студии
            name = (
                studio.find("h3", class_="SiteSnippetSearch__heading").text.strip()
                if studio.find("h3", class_="SiteSnippetSearch__heading")
                else "Не указано"
            )
