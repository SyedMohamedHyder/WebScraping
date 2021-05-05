import requests
import pandas as pd

headers = {
    'sec-ch-ua': '^\\^',
    'accept': 'application/json',
    'Referer': 'https://www.walmart.com/search/?query=',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}

params = (
    ('el', 'sponsored-container-bottom-1'),
    ('type', 'product'),
    ('min', '2'),
    ('max', '20'),
    ('placementId', '1145x345_B-C-OG_TI_2-20_HL-BOTTOM'),
    ('platform', 'desktop'),
    ('bucketId', ''),
    ('moduleLocation', 'bottom'),
    ('isSpecialBrowse', ''),
    ('zipCode', '94066'),
    ('isZipLocated', 'false'),
    ('pageType', 'browse'),
    ('customerId', '30472B6AD6C8C7E8-60001767C2C3E487'),
    ('vtc', 'V0zmJihM0ix2xpHFfooa_I'),
    ('uid', '0fb84b40-6e07-41ad-b4df-40ae640b5500'),
    ('rviItems', '464666168'),
    ('itemsAddedToCart', '0'),
    ('viewportHeight', '295'),
    ('viewportWidth', '1536'),
    ('userLoggedIn', 'false'),
    ('showBrand', 'false'),
    ('itemsList', '613082578^%^2C911675914^%^2C40196447^%^2C622174886^%^2C897977138^%^2C17094368^%^2C21020403^%^2C556111088^%^2C37117854^%^2C50213225'),
    ('pageId', '1085666_7192911'),
    ('pageNumber', '1'),
    ('keyword', 'Here^%^20for^%^20Every^%^20Beauty'),
    ('taxonomy', '1085666_7192911'),
    ('persistControls', 'true'),
    ('isTwoDayDeliveryTextEnabled', 'true'),
    ('mloc', 'bottom'),
    ('module', 'wpa'),
)

response = requests.get('https://www.walmart.com/search/api/wpa', headers=headers, params=params)

data = response.json()

df = pd.json_normalize(data['result']['products'])

df.to_csv('walmart_products.csv', index=False)
