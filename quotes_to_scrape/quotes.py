import chompjs
import pandas as pd
from requests_html import HTMLSession

session = HTMLSession()

url = 'https://quotes.toscrape.com/js/'
response = session.get(url)
response.html.render(sleep=1)

script_css = 'script:contains("var data")'
script_text = response.html.find(script_css, first=True).text

quotes = chompjs.parse_js_object(script_text)

df = pd.json_normalize(quotes)
df.to_csv('quotes.csv')



