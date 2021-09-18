import requests
import urllib
from pprint import pprint

RAKUTEN_URL = "https://app.rakuten.co.jp/services/api/Product/Search/20170426"
APPLICATIONID = ""

def get_api(url, params):
    result = requests.get(url, params=params)
    return result.json()

def main():
    keyword = "鬼滅"
    params = {
        'format': "json",
        'keyword': keyword,
        'applicationId' : APPLICATIONID,
        'page': 1,
        'hits': 10
        }
    
    result = get_api(RAKUTEN_URL, params)

    for i in range(0, len(result['Products'])):
        item_maxprice = result['Products'][i]["Product"]['maxPrice']
        item_minprice = result['Products'][i]["Product"]['minPrice']
        print("-"*30)
        print(f"最大価格: {item_maxprice}")
        print(f"最小価格: {item_minprice}")

main()
