import csv
import amazon_urls
from datetime import datetime
from requests_html import HTMLSession

def get_data(url):
    with HTMLSession() as session:
        response = session.get(url)
        response.html.render(sleep=3)
        title = response.html.find('span.a-size-large.product-title-word-break', first=True).text.strip()
        price = response.html.find('span.a-size-medium.a-color-price.priceBlockBuyingPriceString', first=True)
        return (title, (price or '') and price.text.strip(), datetime.now())

url = 'https://www.amazon.in/255-Bluetooth-Wireless-Earphone-Immersive/dp/B07C2VJXP4/ref=sr_1_1_sspa?crid=3WP0PVYVQ9H2&dchild=1&keywords=bluetooth+earphones+%E0%A4%82&qid=1619358442&sprefix=bluetoot%2Caps%2C319&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyVjlQUzJZSjY2NTNPJmVuY3J5cHRlZElkPUEwMjk4OTA1WURVU0FaUzNBVThLJmVuY3J5cHRlZEFkSWQ9QTAwNTkxNzkzUUc2SVo2WFJVU0tJJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
urls = amazon_urls.get_similar_urls(url)

with open('amazon_prices.csv', 'a', newline='', encoding='utf8') as file:
    writer = csv.writer(file)
    for url in urls:
        writer.writerow(get_data(url))
        print(url)


