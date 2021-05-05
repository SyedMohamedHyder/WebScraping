from requests_html import HTMLSession


def get_asins(keyword):
    url = f'https://www.amazon.in/s?k={keyword}'
    session = HTMLSession()
    response = session.get(url)
    response.html.render(sleep=1)
    asins = map(lambda product: product.attrs['data-asin'], response.html.find('div[data-asin]'))
    asins = filter(None, asins)
    yield from asins


