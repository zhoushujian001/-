import requests
import re
import bs4
from selenium import webdriver
import json
from openpyxl import workbook

wb = workbook.Workbook()
ws = wb.active
ws.append(['商品名', '店名', '产地', '付款人数', '原价', '现价', '助攻', '得分'])
url = 'https://s.m.taobao.com/search?'
data = {
    'event_submit_do_new_search_auction': '1',
    '_input_charset': 'utf-8',
    'topSearch'	: '1',
    'atype'	: 'b',
    'searchfrom': '1',
    'action': 'homeredirect_app_action',
    'from': '1',
    'q'	: '红酒',
    'sst': '1',
    'n'	: '20',
    'buying': 'buyitnow',
    'm'	: 'api4h5',
    'abtest': '13',
    'wlsort': '13',
    'page': '1'
}
req = requests.get(url, params=data, verify=False).text
list = json.loads(req)
a = 0
for i in list['listItem']:
    # 名字
    name = i['title']
    # 店名
    nick_name = i['nick']
    # 产地
    place = i['location']
    # 付款
    hum = i['sold']
    # 原价
    new_money = i['originalPrice']
    # 现价
    old_money = i['priceWap']
    # 网址
    auctionURL = i['url']
    a += 1
    print(a)
    try:
        res = requests.get(url=auctionURL, verify=False).text

    except BaseException:
        auctionURL = 'https:' + auctionURL
        res = requests.get(url=auctionURL, verify=False).text

