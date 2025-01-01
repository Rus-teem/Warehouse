from bs4 import BeautifulSoup

import lxml

html = """
<html>
  <body>
    <div class="product">
      <h2 class="product-name">Телефон</h2>
      <span class="product-price">30,000 руб</span>
      <a href="/product/phone" class="product-link">Подробнее</a>
    </div>
    <div class="product">
      <h2 class="product-name">Ноутбук</h2>
      <span class="product-price">80,000 руб</span>
      <a href="/product/laptop" class="product-link">Подробнее</a>
    </div>
    <div class="product">
      <h2 class="product-name">Часы</h2>
      <span class="product-price">10,000 руб</span>
      <a href="/product/watch" class="product-link">Подробнее</a>
    </div>
  </body>
</html>

"""

# Создаём объект BeautifulSoup
soup = BeautifulSoup(html, 'lxml')

# Выводим красиво отформатированный HTML
# print(soup.prettify())

first_product = (soup.find('h2', class_='product-name')).text
first_product_price = (soup.find('span', class_='product-price')).text
first_product_link = soup.find('a', ).get('href')
# first_product_link_text = first_product_link.get('href')

# print("Продукт:", first_product, 'Цена:', first_product_price, "Ссылка:", first_product_link_text)
print(first_product_link)

all_product_name = soup.find_all('h2', class_='product-name')
all_product_price = soup.find_all('span', class_='product-price')
all_product_link = soup.find_all('a')


name_product = []
product_price = []
product_links = []

for links in all_product_link:
    product_links_href = links.get('href')
    product_links.append(product_links_href)

for price in all_product_price:
    product_name_list = price.text
    product_price.append(product_name_list)
    # print(product_price)

for name in all_product_name:
    product_name_list= name.text
    name_product.append(product_name_list)
    # print(name_product)

print("название", name_product, "цена", product_price, "ссылка", product_links)


for name, price, link in zip (name_product, product_price, product_links):
    print(f"название товара - {name}, цена товара- {price}, ссылка товара - {link}")



# for soups in soup:
#     soups1 = (soup.find_all('h2', class_='product-name')).text
#     soups2 = (soup.find_all('span', class_='product-price')).text
#     first_product_link = soup.find('a')
#     soups3 = first_product_link.get('href')
#     print (soups1, soups2, soups3)