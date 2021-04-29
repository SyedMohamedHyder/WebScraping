import requests
from bs4 import BeautifulSoup

def give_some_stocks():
    url = 'https://in.finance.yahoo.com/most-active'

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    rows = soup.find_all('tr', {'class': 'simpTblRow'})

    for row in rows:
        stock = row.td.a.text.strip()
        yield stock