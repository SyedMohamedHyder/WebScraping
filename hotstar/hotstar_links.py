import csv
from requests_html import HTMLSession

url = 'https://www.hotstar.com/in'

def all_trays(url='https://www.hotstar.com/in'):
    session = HTMLSession()
    response = session.get(url)
    response.html.render(sleep=1, scrolldown=20)
    trays = response.html.find('a.tray-link')
    return trays

def links_title(trays):
    for tray in trays:
        tray_title = tray.text
        tray_link = url + tray.attrs['href']
        yield tray_title, tray_link

def save_to_csv(filename, header=('title', 'link')):
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        topics = all_trays()
        writer.writerows(links_title(topics))

if __name__=='__main__':
    save_to_csv('hotstar_topics.csv')