import re
import pandas as pd
from itertools import chain
from requests_html import HTMLSession


def product_data_gen(page):

    print(f'Getting page number: {page}')
    url = f'https://www.canoeandkayakstore.co.uk/collections/activity-recreational-beginner?page={page}'

    session = HTMLSession()
    response = session.get(url)

    products = response.html.find('div.grid__item.product-grid-item')

    pattern = r'[\d.]+'

    for product in products:
        title = product.find('a.h4.product-grid-item__info__title', first=True).text.strip()
        stock = product.find('span.product-grid-item__info__availability--value', first=True).text.strip()
        price = product.find('span.product-grid-item-price', first=True).text.strip().split('£')
        price = price[2] if len(price)>3 else price[1]
        price = float(re.search(pattern, price)[0])

        product_data = dict(
            title=title,
            stock=stock,
            price=price,
        )

        yield product_data

if __name__ == '__main__':
    products = list()
    for page in range(1, 10):
        products.append(product_data_gen(page))
    all_products = chain.from_iterable(products)
    df = pd.DataFrame(all_products)
    df.to_csv('products.csv', index=False)


