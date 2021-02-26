import requests
from bs4 import BeautifulSoup

def get_page_html(page_number):
    url = f'http://books.toscrape.com/catalogue/page-{page_number}.html'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_book_data(book):
    book_data = {
        'book_url' : f"http://books.toscrape.com/catalogue/{book.find('a')['href']}",
        'image_url' : f"http://books.toscrape.com/catalogue/{book.find('img')['src']}",
        'star_rating' : book.find('p')['class'][1],
        'title' : book.find('h3').a['title'],
        'price' : float(book.find('p', {'class' : 'price_color'}).text.strip('Â£')),
        'stock_availability' : book.find('p', {'class' : 'instock availability'}).text.strip()
    }
    return book_data

def get_books_in_page(page_number):
    page = get_page_html(page_number)
    books = page.find_all('article', {'class' : 'product_pod'})
    return [get_book_data(book) for book in books]


def get_total_pages(html):
    header = html.find('form', {'class' : 'form-horizontal'}).find_all('strong')
    num_of_books = int(header[0].text)
    books_in_a_page = int(header[2].text)
    pages = num_of_books // books_in_a_page
    return pages

def all_book_data():
    total_pages = get_total_pages(get_page_html(1))
    all_books = list()
    for page_num in range(1, total_pages+1):
        print(f'Processing {page_num}')
        all_books.extend(get_books_in_page(page_num))
    return all_books
