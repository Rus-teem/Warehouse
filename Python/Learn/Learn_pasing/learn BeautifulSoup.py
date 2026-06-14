"""Обучение работе с BeautifulSoup: извлечение данных из HTML."""

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

soup = BeautifulSoup(html, 'lxml')

all_product_name = soup.find_all('h2', class_='product-name')
all_product_price = soup.find_all('span', class_='product-price')
all_product_link = soup.find_all('a', class_='product-link')

name_product = [name.text.strip() for name in all_product_name]
product_price = [price.text.strip() for price in all_product_price]
product_links = [link.get('href').strip() for link in all_product_link]

print("название", name_product, "цена", product_price, "ссылка", product_links)

for name, price, link in zip(name_product, product_price, product_links):
    print(f"название товара - {name}, цена товара - {price}, ссылка товара - {link}")
