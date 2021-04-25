from requests_html import  HTMLSession

def get_similar_urls(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)

    similar_products = r.html.find('li.swatchAvailable')

    for product in similar_products:
        url = 'https://www.amazon.in/255-Bluetooth-Wireless-Earphone-Immersive' + product.attrs['data-dp-url']
        yield url

