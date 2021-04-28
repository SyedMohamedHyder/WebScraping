import requests
import pandas as pd
from itertools import chain
from bs4 import BeautifulSoup
from datetime import datetime


def stack_data(topic, page_number, tab='active'):
    url = f'https://stackoverflow.com/questions/tagged/{topic}?tab={tab}&page={page_number}&pagesize=50'

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    questions = soup.find_all('div', {'class': 'mln24'})

    for question in questions:
        title_data = question.find('a', {'class': 'question-hyperlink'})

        question_info = dict(
            link = 'https://stackoverflow.com' + title_data['href'],
            title = title_data.text.strip(),
            votes = int(question.find('span', {'class': 'vote-count-post'}).strong.text),
            answers = int(question.find('div', {'class': 'status'}).strong.text),
            date = datetime.fromisoformat(question.find('span', {'class': 'relativetime'})['title'].replace(' ', 'T').strip('Z')),
            user = question.find('div', {'class': 'user-details'}).a.text.strip())

        yield question_info

topics = 'python', 'java', 'html'

stacks = []

for topic in topics:
    for page_number in range(1, 4):
        print(f'--------Getting {topic}: {page_number}-----------')
        info = stack_data(topic, page_number)
        stacks.append(info)
stacks = chain.from_iterable(stacks)

df = pd.DataFrame(stacks)
df.to_csv('stack_info.csv', index=False)
