import json
import requests

headers = {
    'authority': 'api.sofascore.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '^\\^',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'accept': '*/*',
    'origin': 'https://www.sofascore.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.sofascore.com/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'if-none-match': 'W/^\\^848499f94d^\\^',
}

response = requests.get('https://api.sofascore.com/api/v1/unique-tournament/7/season/29267/standings/total', headers=headers)


with open('sports.json', 'w') as file:
    json.dump(response.json(), file)


