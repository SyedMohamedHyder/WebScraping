from requests_html import HTMLSession

def product_review(asin):
    print(asin)
    url = f'https://www.amazon.in/dp/{asin}/'
    session = HTMLSession()
    response = session.get(url)

    response.html.render(sleep=1)

    title = response.html.find('#title', first=True)

    if not title:
        print('Wasted')
        return
    else:
        title = title.text.strip()

    num_ratings = response.html.find('#acrCustomerReviewText', first=True)
    num_ratings = num_ratings and int(num_ratings.text.strip(' ratings').replace(',',''))

    ratings = response.html.find('#a-icon-alt', first=True)
    ratings = ratings and float(ratings.text.strip(' out of 5 stars'))

    top_reviews = response.html.find('div[data-hook=review]')

    reviews = []
    for review in top_reviews:

        user = review.find('span.a-profile-name', first=True).text.strip()
        review_title = review.find('a[data-hook=review-title]', first=True).text.strip()
        review_data = review.find('div[data-hook=review-collapsed]', first=True).text.strip()

        reviews.append(
            dict(
                user=user,
                review_title=review_title,
                review=review_data
            )
        )
    return dict(
        asin=asin,
        title=title,
        num_ratings=num_ratings,
        ratings=ratings,
        top_reviews=reviews
    )


if __name__ == '__main__':
    print(product_review('B08F3C7MVY'))