import chompjs
import pandas as pd
from requests_html import HTMLSession

url = 'https://www.rei.com/c/backpacks?page=2'
session = HTMLSession()
response = session.get(url)

results_css = '#initial-props'
results = response.html.find(results_css, first=True).text

data = chompjs.parse_js_object(results)

bags = data['ProductSearch']['products']['searchResults']['results']

df = pd.json_normalize(bags)
df.to_csv('bags.csv')


