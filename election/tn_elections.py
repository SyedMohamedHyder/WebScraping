import requests
import pandas as pd
from itertools import chain
from bs4 import BeautifulSoup

def election_results_html(constituency_num):
    url = f'https://results.eci.gov.in/Result2021/ConstituencywiseS22{constituency_num}.htm?ac={constituency_num}'
    response =requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    constituency = soup.find('td', {'colspan': 9, 'align': 'center'}).text.strip()
    print(constituency)
    return soup

def constituency_data_gen(soup):

    constituency = soup.find('td', {'colspan': 9, 'align': 'center'}).text.strip()
    candidates_data = soup.find_all('tr', {'style': 'font-size:12px;'})
    for candidate_data in candidates_data:
        candidate = candidate_data.find('td', {'align': 'left', 'style': 'width:18%;font-weight:bold;'}).text.strip()
        party = candidate_data.find('td', {'align': 'left', 'style': 'width:0%;font-weight:bold;'}).text.strip()
        votes = int(candidate_data.find_all('td', {'align': 'right', 'style': 'width:13%;font-weight:bold;'})[1].text.strip())

        vote_info = dict(candidate=candidate, party=party, votes=votes, constituency=constituency)
        yield vote_info

all_constituencies = list()
for constituency_num in range(1, 235):
    soup = election_results_html(constituency_num)
    constituency_data = constituency_data_gen(soup)
    all_constituencies.append(constituency_data)

all_candidates = chain.from_iterable(all_constituencies)
df = pd.DataFrame(all_candidates)

df.to_csv('election_results.csv', index=False)

