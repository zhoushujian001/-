from urllib import request, parse
import ssl
from http import cookiejar

ssl._create_default_https_context = ssl._create_unverified_context

cookie=cookiejar.CookieJar()#cookie对象
cookie_handler=request.HTTPCookieProcessor(cookie)#生成cookie管理器
http_handle=request.HTTPHandler()#http请求管理器
https_handle=request.HTTPHandler()#http请求管理器
opener=request.build_opener(http_handle,https_handle,cookie_handler)#发起请求的管理器

def login():
    login_url='https://security.kaixin001.com/login/login_post.php'

    data={
        'email':'18001176982',
        'password':'ycx5431116'
    }
    data=parse.urlencode(data).encode('utf-8')
    req = request.Request(url=login_url,data=data)
#     自定义opener发起请求
    response=opener.open(req)

def getHomePage():
    home_url='http://www.kaixin001.com/home/?_profileuid=181794564'
    response = opener.open(home_url)
    print(response.read().decode('utf-8'))

if __name__=='__main__':
    login()
    getHomePage()
