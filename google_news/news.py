import pandas as pd
from requests_html import HTMLSession

url = 'https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en'

session = HTMLSession()
response = session.get(url)

response.html.render(sleep=1, scrolldown=5)

articles = response.html.find('article')

newslist = []

#loop through each article to find the title and link. try and except as repeated articles from other sources have different h tags.
for article in articles:
        news_data = article.find('h3', first=True)
        if news_data:
            title = news_data.text
            link = news_data.absolute_links.pop()
            newsarticle = {
                'title': title,
                'link': link
            }
            newslist.append(newsarticle)

#Save to csv
df = pd.DataFrame(newslist)
df.to_csv('google_news_india.csv', index=False)