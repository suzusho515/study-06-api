import requests
import urllib
from pprint import pprint
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials 

RAKUTEN_URL = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
APPLICATIONID = ""
JSON_FILE = ''
SPREADSHEET_KEY = ''
SHEETNAME = ""

#2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

#認証情報設定
#ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_FILE, scope)

#OAuth2の資格情報を使用してGoogle APIにログインします。
gc = gspread.authorize(credentials)

#共有設定したスプレッドシートのシート1を開く
worksheet = gc.open_by_key(SPREADSHEET_KEY).worksheet(SHEETNAME)

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
        'sort': "-updateTimestamp",
        'hits': 20
        }
    
    result = get_api(RAKUTEN_URL, params)
    
    item_list = []
    global item_lists
    item_lists = [] 
    #header追加
    item_lists.append(["商品名", "価格"])
    for i in range(0, len(result['Items'])):
        item_name = result['Items'][i]["Item"]['itemName']
        item_price = result['Items'][i]["Item"]['itemPrice']
        item_list = [item_name,item_price]
        item_lists.append(item_list)

main()

#2次元リスト書込み
item_length = len(item_lists)
worksheet.update(f'A1:B{item_length}', item_lists)




