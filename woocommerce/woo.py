import csv
import requests
from bs4 import BeautifulSoup

url = 'https://barefootbuttons.com/product-category/version-1/'
response = requests.get(url)

html = response.text
soup = BeautifulSoup(html, 'html.parser')

products = soup.find_all('div', 'product-small box')

for product in products:
    link = product.find('a')['href']
    title = product.find('p', {'class': 'name product-title woocommerce-loop-product__title'}).text.strip()
    price = float(product.find('span', {'class': 'woocommerce-Price-amount amount'}).text.strip().replace('$', ''))
    with open('woo_products.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([title, link, price])

