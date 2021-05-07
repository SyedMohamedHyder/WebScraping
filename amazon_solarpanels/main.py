import json
import asin_scrapper
import product_review

keyword = 'solar panel'

asins = asin_scrapper.asin_gen(keyword)

reviews = list(filter(None, (product_review.product_review(asin) for asin in asins)))

all_product_data = dict(
    product_type=keyword,
    products=reviews
)


with open(f'{keyword}_amazon.json', 'w') as file:
    json.dump(all_product_data, file)

