import requests
import urllib
from pprint import pprint
import pandas as pd
import csv

RAKUTEN_URL = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628"
APPLICATIONID = ""

def get_api(url, params):
    result = requests.get(url, params=params)
    return result.json()

def main():
    genreld = "558929"
    params = {
        'format': "json",
        'genreld': genreld,
        'applicationId' : APPLICATIONID,
        'page': 1,
        'age': 10
        }
    
    result = get_api(RAKUTEN_URL, params)

    with open("result.csv", mode = "w", newline="", encoding="utf-8") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['商品名','価格','ランキング'])

    for i, t in enumerate(range(0, len(result['Items']))):
        item_name = result['Items'][t]["Item"]['itemName']
        item_price = result['Items'][t]["Item"]['itemPrice']

        with open("result.csv", mode = "a", newline="", encoding="utf-8") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([item_name,item_price,i])

        print("-"*30,i+1,"-"*30)
        print(item_name)
        print(item_price)
    
main()
