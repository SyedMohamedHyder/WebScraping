import csv
from datetime import datetime
from requests_html import HTMLSession


def scrape_price(asin):
    url = f'https://www.amazon.in/dp/{asin}/'
    session = HTMLSession()
    response = session.get(url)

    response.html.render(sleep=1)
    title = response.html.find('#productTitle', first=True).text.strip()
    price = float(response.html.find('span.a-size-medium.a-color-price', first=True).text.strip('₹ ').replace(',', ''))
    return title, price

asins = ['B0869855B8', 'B08697WT6D', 'B08697N43N', 'B08XJBPCTR', 'B086985T6R']


with open('price_tracker.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['asin', 'title', 'price', 'date'])
    for asin in asins:
        title, price = scrape_price(asin)
        print(title, price)
        writer.writerow((asin, title, price, datetime.now()))

