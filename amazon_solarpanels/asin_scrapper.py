from requests_html import HTMLSession

def asin_gen(keyword):

    keyword = keyword.replace(' ', '+')
    url = f'https://www.amazon.in/s?k={keyword}'
    session = HTMLSession()
    response = session.get(url)

    response.html.render(sleep=1)
    products = response.html.find('div[data-asin]')

    yield from filter(None, map(lambda product: product.attrs['data-asin'], products))


if __name__=='__main__':
    print(list(asin_gen('solar panel')))
