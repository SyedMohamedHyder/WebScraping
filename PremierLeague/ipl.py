import requests
import pandas as pd
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def get_headers(table):
    headers = table.find('tr')
    for header in headers.find_all('th')[2:-1]:
        yield header.text


def get_ipl_data():
    ipl_url = 'https://www.iplt20.com/points-table/2020'
    ipl_html = get_html(ipl_url)
    table = ipl_html.find('table')
    headers = list(get_headers(table))
    for team in table.find_all('tr')[1:]:
        team_info = dict()
        team_info['team'] = team.find('a').span.text
        team_info['url'] = f"https://www.iplt20.com/{team.find('a')['href']}"
        for header, value in zip(headers, team.find_all('td')[2:]):
            team_info[header] = value.text
        yield team_info

#ipl = list(get_ipl_data())

df = pd.DataFrame(get_ipl_data())
#print(df)

df.to_csv('ipl_2020_pt.csv')
df.to_excel('ipl_2020_pt.xlsx')