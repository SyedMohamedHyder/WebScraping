import re
import csv
from datetime import datetime
from requests_html import HTMLSession

price_pattern = r'[\d.]+'

session = HTMLSession()

def westend():
    url = 'https://www.westenddj.co.uk/shure-sm7b'
    response = session.get(url)
    price = response.html.find('span.regular-price', first=True).text.strip()
    return price

def dawsons():
    url = 'https://www.dawsons.co.uk/93267/shure-sm7b-vocal-microphone'
    response = session.get(url)
    price = response.html.find('span.details_price_now.details_price_now_red', first=True).text.strip()
    return price

def gear4music():
    url = 'https://www.gear4music.com/PA-DJ-and-Lighting/Shure-SM7B-Dynamic-Studio-Microphone/G6X'
    response = session.get(url)
    price = response.html.find('span.c-val', first=True).text.strip()
    return price

def andertons():
    url = 'https://www.andertons.co.uk/shure-sm7b-dynamic-vocal-mic-sm7b'
    response = session.get(url)
    price = response.html.find('span.product-price', first=True).text.strip()
    return price

if __name__ == '__main__':

    shops_fn = westend, dawsons, gear4music, andertons
    prices = (*map(lambda fn: float(re.search(price_pattern, fn())[0]), shops_fn), datetime.now().date())
    with open('shops.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(prices)
