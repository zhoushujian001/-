import requests
import random

url = 'http://www.renren.com/PLogin.do'

proxy_list = [
    {
        'https': '101.81.10.171:39522',
        'http': '114.217.3.70:808',
    },
    {
        'https': '119.1.97.193:60916',
        'http': '61.138.33.20:808'
    }
]

proxies = random.choice(proxy_list)

data = {
    'email': '18323291912',
    'password': 'as123456'
}

session = requests.session()
# 发起第一次请求
req1 = session.post(url, data, proxies)
with open('renren1.html', 'w', encoding='utf-8')as f:
    f.write(req1.text)
# 第二次请求
req2 = session.get(url='http://www.renren.com/896754064', proxies=proxies)
# req = requests.post(url, data, proxies)

with open('renren2.html', 'w', encoding='utf-8')as f:
    f.write(req2.text)
