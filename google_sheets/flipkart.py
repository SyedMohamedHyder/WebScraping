import requests
from datetime import datetime
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_price(url):
    html = get_html(url)
    price_text = html.find('div', {'class' : '_30jeq3 _16Jk6d'}).text
    price = int(''.join(char for char in price_text if char.isnumeric()))
    return price

def get_price_log(*urls):
    for url in urls:
        yield (url[0], get_price(url[1]), str(datetime.now()))