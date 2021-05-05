import requests
import pandas as pd
from itertools import chain
from bs4 import BeautifulSoup


def game_info_getter(url):
    response = requests.get(url)
    data = response.json()

    products = BeautifulSoup(data['results_html'], 'html.parser')

    games = products.find_all('a', {'class': 'search_result_row ds_collapse_flag'})

    for game in games:
        title = game.find('span', {'class': 'title'}).text.strip()
        date_released = game.find('div', {'class': 'col search_released responsive_secondrow'}).text.strip()
        *_, original_price, discount_price = game.find('div', {'class': 'search_price'}).text.strip().split('₹')
        original_price, discount_price = original_price.strip().replace(',', ''), discount_price.strip().replace(',', '')
        original_price = int(original_price) if original_price else ''
        discount_price = int(discount_price) if discount_price else ''

        game_data = dict(
            title = title,
            date_released = date_released,
            original_price = original_price,
            discount_price = discount_price
        )

        yield game_data

games = []
for start in range(0, 1000, 50):
    print(start)
    url = f'https://store.steampowered.com/search/results/?query&start={start}&count=50&dynamic_data=&sort_by=_ASC&ignore_preferences=1&snr=1_7_7_7000_7&filter=topsellers&infinite=1'
    game_info = game_info_getter(url)
    games.append(game_info)

all_games = chain.from_iterable(games)
df = pd.DataFrame(all_games)

df.to_csv('games.csv', index=False)



