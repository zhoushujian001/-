import requests
from lxml import etree

url = 'http://maoyan.com/board'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
req = requests.get(url=url, headers=headers).content.decode('utf-8')

tree = etree.HTML(req)

addr = tree.xpath('//dd')
for add in addr:
    # 排名
    index = add.xpath('./i/text()')[0]
    # 地址
    address = add.xpath('./a/img/@data-src')[0]
    # 影名
    name = add.xpath('./div/div/div/p/a/text()')[0]
    # 主演
    star = add.xpath('./div/div/div/p/text()')[0].strip()
    # 上映时间
    time = add.xpath('./div/div/div/p/text()')[1]
    # 评分
    score = add.xpath('./div/div/div/p/i/text()')[0]\
          + add.xpath('./div/div/div/p/i/text()')[1]
    info = index + ':' + name + '\n'\
         + address + '\n'\
         + star + '\n'\
         + time + '\n'\
         + '评分：' + score + '\n'
    print(info)
