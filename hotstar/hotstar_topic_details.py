import csv
from pprint import pprint
from requests_html import HTMLSession

def topics_title_link(filename='hotstar_topics.csv'):
    with open(filename, 'r') as file:
        dialect = csv.Sniffer().sniff(file.read(1000))
        file.seek(0)
        reader = csv.reader(file, dialect=dialect)
        next(reader)
        yield from reader


def shows(topic):
    url = 'https://www.hotstar.com'
    title, link = topic
    print(title)
    with HTMLSession() as session:
        response = session.get(link)
        response.html.render(sleep=1, scrolldown=15)
        movies = response.html.find('div.normal')
        for movie in movies:
            movie_data = {
                    'title': movie.find('span.content-title', first=True) and movie.find('span.content-title', first=True).text,
                    'duration': movie.find('div.dur', first=True) and movie.find('div.dur', first=True).text,
                    'link': url + movie.find('a', first=True).attrs['href'],
                    'genre': movie.find('span.subtitle', first=True) and movie.find('span.subtitle', first=True).text,
                    'description': movie.find('div.description', first=True) and movie.find('div.description', first=True).text
                }
            print(movie_data)
            yield movie_data

def entire_shows(topics):
    for topic in topics:
        yield from shows(topic)

def save_to_file(filename, headers=('title', 'duration', 'link', 'genre', 'description')):
    topics = list(topics_title_link())[10:20]
    show_details = entire_shows(topics)
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(show_details)

if __name__ == '__main__':
    save_to_file('all_hotstar_shows.csv')