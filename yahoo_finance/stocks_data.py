import stocks
import requests
import pandas as pd
from bs4 import BeautifulSoup

def stock_data(stock):
    url = f'https://in.finance.yahoo.com/quote/{stock}'

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find('div', {'class': 'Mt(15px)'}).h1.text.strip()

    stock_value, change, *_ = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')

    stock_value, change = stock_value.text.strip(), change.text.strip()

    print(title, stock_value, change)
    return dict(name=title, value=stock_value, change=change)

my_stocks = stocks.give_some_stocks()

stock_info = (stock_data(stock) for stock in my_stocks)

df = pd.DataFrame(stock_info)
df.to_csv('stocks.csv')
