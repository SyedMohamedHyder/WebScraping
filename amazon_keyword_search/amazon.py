import pandas as pd
from itertools import chain
from bs4 import BeautifulSoup
from requests_html import HTMLSession

def get_products(url):

    session = HTMLSession()
    response = session.get(url)
    response.html.render(sleep=1)
    soup = BeautifulSoup(response.html.html, 'html.parser')
    session.close()
    return soup

def get_product_info(soup):

    products = soup.find_all('div', {'data-component-type': 's-search-result'})

    for product in products:

        title_box = product.find('a', {'class': 'a-link-normal a-text-normal'})
        price_details = product.find_all('span', {'class': 'a-offscreen'})

        title = title_box.text.strip()
        link = 'https://www.amazon.in' + title_box['href']

        if len(price_details) >= 2:
            current_price = price_details[0].text.strip().replace(',', '').replace('₹', '')
            original_price = price_details[1].text.strip().replace(',', '').replace('₹', '')

            current_price = float(current_price) if current_price.isnumeric() else ''
            original_price = float(original_price) if original_price.isnumeric() else ''

        else:
            current_price = ''
            original_price = ''

        discount_percentage = ((original_price - current_price) / original_price) * 100 if (current_price and original_price) else 0

        try:
            ratings = float(product.find('span', {'class': 'a-icon-alt'}).text.strip().replace(' out of 5 stars', ''))
            num_reviews = int(product.find('span', {'class': 'a-size-base'}).text.strip().replace(',', ''))
        except:
            ratings, num_reviews = 0, 0

        product_detail = {
            'title': title,
            'link': link,
            'current_price': current_price,
            'original_price': original_price,
            'discount_percentage': discount_percentage,
            'ratings': ratings,
            'reviews': num_reviews
        }
        yield product_detail

def get_next_page(soup):
    next_page = soup.find('ul', {'class': 'a-pagination'}).find('li', {'class': 'a-last'}).a
    return 'https://www.amazon.in' + next_page['href'] if next_page else None

if __name__ == '__main__':

    keyword = input('Enter the keyword to search for : ')
    url_keyword = keyword.replace(' ', '+')
    url = f'https://www.amazon.in/s?k={url_keyword}'

    product_gens = list()

    while url:
        print(url)
        soup = get_products(url)
        product_gen = get_product_info(soup)
        product_gens.append(product_gen)
        url = get_next_page(soup)

    products = chain.from_iterable(product_gens)
    df = pd.DataFrame(products)
    df.to_csv(f"{keyword.replace(' ', '_')}_amazondeals.csv", index=False)


