import requests
import urllib
from pprint import pprint
from 商品名と価格の一覧を取得 import * 

RAKUTEN_URL = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
APPLICATIONID = ""

def get_api(url, params):
    result = requests.get(url, params=params)
    return result.json()

def test_main():
    keyword = "鬼滅"
    params = {
        'format': "json",
        'keyword': keyword,
        'applicationId' : APPLICATIONID,
        'page': 1,
        'sort': "-updateTimestamp",
        'hits': 10
        }
    
    result = get_api(RAKUTEN_URL, params)

    for i in range(0, len(result['Items'])):
        item_name = result['Items'][i]["Item"]['itemName']
        item_price = result['Items'][i]["Item"]['itemPrice']
        print(item_name)
        print(item_price)
    
    #正常系
    assert len(result) >= 1
    assert result['Items'][0]["Item"]['itemName']

    #異常系
    assert len(result) == 1
    assert result['Items'][0]["Item"]['itemName']

main()
