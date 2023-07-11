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


for i in range(2):
   urlOne = 'https://shopee.vn/search?keyword=s%C3%B4%20c%C3%B4%20la&page='+str(i)
   driver.get(urlOne)
   time.sleep(2)
   for request in driver.requests:
      if 'https://shopee.vn/api/v4/search/search_items?by=relevancy' in request.url:
         if 'limit=60&newest='+str(i*60) in request.url:     
            response = request.response
            print(request.url)
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


