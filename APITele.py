# from seleniumwire import webdriver
# import time
# from seleniumwire.utils import decode
# import json
# import re
# from selenium.webdriver.chrome.options import Options
# from selenium import webdriver

# store_data = open('db.json', 'w')
# dataShoppe = []

# chrome_options = Options()
# chrome_options.add_argument("--headless")

# for i in range(9):
#     driver = webdriver.Chrome(options=chrome_options)
#     # Go to the Google home page
#     url = 'https://shopee.vn/B%C3%A1ch-H%C3%B3a-Online-cat.11036525?page='+str(i)
#     driver.get(url)
#     for request in driver.requests:
#         if request.response:
#             if request.url.startswith('https://shopee.vn/api/v4/recommend/recommend?bundle=category_landing_page&cat_level=1&catid=11036525&limit=60&offset='+str(i*60)):
#                 response = request.response
#                 body = decode(response.body,response.headers.get('Content-Encoding','Identity'))
#                 decode_body = body.decode('utf8')
#                 json_data = json.loads(decode_body)
#                 dataAll = json_data['data']['sections'][0]['data']
#                 for itemTwo in dataAll['item']:
#                     itemTwo.pop('label_ids')
#                     itemTwo.pop('tier_variations')
#                     keys_to_removeItemTwo = [key for key, value in itemTwo.items() if value is None]
#                     for key in keys_to_removeItemTwo:
#                         itemTwo.pop(key)
#                     dataShoppe.append(itemTwo)

# objNew = {
#     "items": dataShoppe
# }

# store_data.write(json.dumps(objNew))
































from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from seleniumwire.utils import decode
import json
import re
from selenium.webdriver.chrome.options import Options
import time



dataShoppe = []
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=C:/Users/Admin/AppData/Local/Google/Chrome/User Data/Profile 1")
store_data = open('db.json', 'w')
driver = webdriver.Chrome(options=chrome_options)



for i in range(9):
   urlOne = 'https://shopee.vn/search?keyword=s%C3%B4%20c%C3%B4%20la&page='+str(i)
   driver.get(urlOne)
   for request in driver.requests:
      if 'https://shopee.vn/api/v4/search/search_items?by=relevancy' in request.url:     
         response = request.response
         body = decode(response.body,response.headers.get('Content-Encoding','Identity'))
         decode_body = body.decode('utf8')
         json_data = json.loads(decode_body)
         for x in json_data['items']:
            x['item_basic'].pop('label_ids')
            x['item_basic'].pop('tier_variations')
            keys_to_removeItemTwo = [key for key, value in x['item_basic'].items() if value is None]
            for key in keys_to_removeItemTwo:
               x['item_basic'].pop(key)
            dataShoppe.append(x['item_basic'])
objNew = {
    "items": dataShoppe
}
store_data.write(json.dumps(objNew))
        