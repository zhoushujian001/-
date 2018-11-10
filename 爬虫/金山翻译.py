from urllib import request, parse
import json

def fanyi(word):
    # 封装请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }

    url = 'http://fy.iciba.com/ajax.php?a=fy'
    data = {
        'w': word
    }

    # 处理表单数据
    data_str = parse.urlencode(data)

    # 封装请求对象

    req = request.Request(url=url, headers=headers, data=bytes(data_str, encoding='utf-8'))
    # 发起网络请求
    content = request.urlopen(req).read().decode('utf-8')

    # json 格式字符串转换成python对象（列表，字典）
    obj = json.loads(content)
    return obj

if __name__=='__main__':
    while True:
        word = input('请输入单词')
        words = fanyi(word)
        for i in words['content']['word_mean']:
            print(i)
