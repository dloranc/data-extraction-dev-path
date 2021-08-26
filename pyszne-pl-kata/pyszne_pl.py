import requests
import json

r = requests.get(
    'https://cw-api.takeaway.com/api/v25/restaurant?slug=zielona-krowa',
    headers={
        'accept': 'application/json, text/plain, */*',
        'x-country-code': 'pl'
    }
)

content = json.loads(r.content)

products = content['menu']['products']
product_keys = products.keys()

for key in product_keys:
    product = products[key]
    print(product['name'], end=' - ')
    for variant in product['variants']:
        price = str(variant['prices']['delivery'])
        a = price[:-2]
        b = price[-2:]
        print(f'{a},{b}', end=' zł ')
    print()
