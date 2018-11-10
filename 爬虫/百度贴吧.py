from urllib import request,parse

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
name = input('请输入贴吧名:')
url = 'http://tieba.baidu.com/f?'
num = int(input('请输入页数:'))
for i in range(0, num):
    j = i*50
    data = {
        'ie': 'utf-8',
        'fr': 'search',
        'kw': name,
        'pn': j
    }
    # parse功能：
    # 1.将汉字进行解码
    # 2.将多个参数用&连接起来
    # 3.键与值用=连接
    url = 'http://tieba.baidu.com/f?' + parse.urlencode(data)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }
    req = request.Request(url=url, headers=headers)
    response = request.urlopen(req)
    content = response.read().decode('utf-8')
    with open('%s第%d页.html' % (name, i+1), 'w', encoding='utf-8') as fp:
        fp.write(content)
