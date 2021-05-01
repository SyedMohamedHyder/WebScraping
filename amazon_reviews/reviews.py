import pandas as pd
from requests_html import HTMLSession

def scrape_review(product_id, page_number):
    url = f'https://www.amazon.in/product-reviews/{product_id}?pageNumber={page_number}'
    session = HTMLSession()
    response = session.get(url)
    response.html.render(sleep=1)
    reviews = response.html.find('div.a-section.review.aok-relative')

    for review in reviews:
        review_data = dict(
            username = review.find('span.a-profile-name', first=True).text.strip(),
            review_rating = float(review.find('a.a-link-normal', first=True).attrs['title'].strip(' out of 5 stars')),
            title = review.find('a.a-size-base', first=True).text.strip(),
            review_date = review.find('span.a-size-base.a-color-secondary.review-date', first=True).text.strip(),
            info = review.find('span.a-size-base.review-text.review-text-content', first=True).text.strip(),
        )
        yield review_data

asins = ['B0869855B8', 'B08697WT6D', 'B08697N43N']

def product_review(asins, page_number):
    for asin in asins:
        for page in range(1, page_number+1):
            print(asin, page)
            yield from scrape_review(asin, page)

reviews = product_review(asins, 3)

df = pd.DataFrame(reviews)
df.to_csv('reviews.csv', index=False)





