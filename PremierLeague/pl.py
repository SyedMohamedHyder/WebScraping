import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_table_data(table):
    teams = table.find_all('tr')
    for team in teams:
        team_info = dict()
        info = team.find_all('td', {'class' : 'standing-table__cell'})
        #print(info)
        team_info['team'] = info[1]['data-long-name']
        team_info['position'] = int(info[0].text)
        team_info['played'] = int(info[2].text)
        team_info['won'] = int(info[3].text)
        team_info['draw'] = int(info[4].text)
        team_info['lost'] = int(info[5].text)
        team_info['fouls'] = int(info[6].text)
        team_info['assists'] = int(info[7].text)
        team_info['goals'] = int(info[8].text)
        team_info['points'] = int(info[9].text)
        yield team_info
        #break
url = 'https://www.skysports.com/premier-league-table'
table = get_html(url).find('tbody')
data = get_table_data(table)