import re
import download_image
from requests_html import HTMLSession

def download(url):
    session = HTMLSession()
    response = session.get(url)
    response.html.render(sleep=1, scrolldown=5)

    images = response.html.find('img')

    for num, image in enumerate(images):
        name = f'rcb{num}'
        link = image.attrs.get('src')

        if link and 'https' in link:
            print(name, link)
            download_image.download_image(link, name)

    session.close()

url = 'https://www.google.com/search?q=rcb+2021&tbm=isch&chips=q:rcb+2021,online_chips:glenn+maxwell:d-LEbnpWy6I%3D&hl=en&sa=X&ved=2ahUKEwigoLaz3qLwAhUJErcAHb_RCcQQ4lYoAXoECAEQGw&biw=1519&bih=358'
download(url)