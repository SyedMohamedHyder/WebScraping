import pandas as pd
from requests_html import HTMLSession

famous_quotes = []
def extract_quote(page_number):
    url = f'https://quotes.toscrape.com/js/page/{page_number}/'

    with HTMLSession() as session:
        response = session.get(url)
        response.html.render(sleep=1)

        quotes = response.html.find('div.quote')
        for box in quotes:
            famous_quotes.append(
                dict(
                    quote=box.find('span.text', first=True).text.strip(),
                    author=box.find('small.author', first=True).text.strip()
                )
            )
for page_number in range(1, 11):
    print(f'Getting page number : {page_number}')
    extract_quote(page_number)

df = pd.DataFrame(famous_quotes)
df.to_csv('quotes.csv', index=False)
