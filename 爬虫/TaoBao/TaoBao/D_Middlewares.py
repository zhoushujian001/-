
from selenium import webdriver
import time

from scrapy.http.response.html import HtmlResponse

class MyDownloaderMiddleware(object):

    def __init__(self):
        self.browser = webdriver.PhantomJS(r'E:\python0502班爬虫视频讲义\爬虫安装包\phantomjs-2.1.1-windows\bin\phantomjs.exe')

    def process_request(self, request, spider):

        if request.meta.get('phantomjs',False):
            self.browser.get(request.url)
            time.sleep(1)
            content = self.browser.page_source

            #封装成一个response对象
            response = HtmlResponse(url=request.url,encoding='utf-8',body=content,request=request)
            return response


    # def process_response(self, request, response, spider):
    #
    #     return response

