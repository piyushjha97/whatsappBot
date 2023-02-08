# MARKETSTACK_API_KEY

import os
import requests
import json

API_KEY = '22a4a78db9aed75a0b97449601ef0cf3' #os.environ.get('MARKETSTACK_API_KEY')
BASE_URL = 'http://api.marketstack.com/v1/'

def get_stock_LTP(symbol):
    params = {
        'access_key':API_KEY
    }
    end_points = ''.join([BASE_URL, "tickers/", symbol,"/intraday/latest"])
    api_result = requests.get(end_points,params)
  #  print(api_result)
    json_result = json.loads(api_result.text)

 #   print(json_result)
    return {    
     "last_price": json_result["open"]

    }

result = get_stock_LTP("AAPL")
print(result)

