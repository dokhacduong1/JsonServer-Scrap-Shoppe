from seleniumwire import webdriver
import time
from seleniumwire.utils import decode
import json
import re
from selenium.webdriver.chrome.options import Options

store_data = open('db.json', 'w')
dataShoppe = []

chrome_options = Options()
chrome_options.add_argument("--headless")

for i in range(9):
    driver = webdriver.Chrome(options=chrome_options)
    # Go to the Google home page
    url = 'https://shopee.vn/B%C3%A1ch-H%C3%B3a-Online-cat.11036525?page='+str(i)
    driver.get(url)
    for request in driver.requests:
        if request.response:
            if request.url.startswith('https://shopee.vn/api/v4/recommend/recommend?bundle=category_landing_page&cat_level=1&catid=11036525&limit=60&offset='+str(i*60)):
                response = request.response
                body = decode(response.body,response.headers.get('Content-Encoding','Identity'))
                decode_body = body.decode('utf8')
                json_data = json.loads(decode_body)
                dataAll = json_data['data']['sections'][0]['data']
                for itemTwo in dataAll['item']:
                    itemTwo.pop('label_ids')
                    itemTwo.pop('tier_variations')
                    keys_to_removeItemTwo = [key for key, value in itemTwo.items() if value is None]
                    for key in keys_to_removeItemTwo:
                        itemTwo.pop(key)
                    dataShoppe.append(itemTwo)

objNew = {
    "items": dataShoppe
}

store_data.write(json.dumps(objNew))
