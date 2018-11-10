import requests, time,re
from openpyxl import workbook
from threading import Thread

def get(page,ws):
    url = 'https://www.douyu.com/gapi/rkc/directory/0_0/' + str(page)
    req = requests.get(url=url, verify=False).text
    json_list = json.loads(req)
    for i in json_list['data']['rl']:
        studio = i['rn']
        classify = i['c2name']
        anchor = i['nn']
        heat = i['ol']
        ws.append([studio, classify, anchor, heat])

def index():
    wb = workbook.Workbook()
    ws = wb.active
    ws.append(['姓名', '时间', '篮板', '助攻', '得分'])
    threads = [Thread(target=get, args=(page,ws)) for page in range(1,200)]
    threads.start()
    threads.join()
    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    start_time = time.time()
    index()
    end_time = time.time()
    print('时间%.2f' % (end_time - start_time))