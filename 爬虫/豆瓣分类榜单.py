from urllib import request,parse
import json

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

a = int(input('请输入要查询的起始位置:'))+1
b = input('请输入要查询的电影个数:')
c = input('请输入要查询的电影范围（如评分为100%-90%以内，输入100:90）:')

url='https://movie.douban.com/j/chart/top_list?type=19&action='

data = {
    'start': a,
    'limit': b,
    'interval_id':c
}
data = parse.urlencode(data).encode('utf - 8')
req = request.Request(url, data, head)
response = request.urlopen(req).read().decode('utf - 8')
obj= json.loads(response)
for i in obj:
    print(i['title'])

