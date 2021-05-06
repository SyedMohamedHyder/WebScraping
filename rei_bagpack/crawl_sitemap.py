import requests
from bs4 import BeautifulSoup

sitemap_url = 'https://www.rei.com/sitemap.xml'

def get_all_links(url):
    response = requests.get(url)
    xml = response.text
    xml_website = BeautifulSoup(xml, 'lxml')

    links = map(lambda link: link.text, xml_website.find_all('loc'))

    for link in links:
        if link.endswith('.xml'):
            print(link)
            yield from get_all_links(link)
        else:
            yield link

links = get_all_links(sitemap_url)

with open('rei_all_links.txt', 'w') as file:
    for link in links:
        file.write(link)
        file.write('\n')


