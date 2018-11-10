# -*- coding: utf-8 -*-
import scrapy
import re
import json
import jsonpath# pip install jsonpath
from TaoBao.items import TaobaoItem
from urllib import request
import datetime


class Spider01Spider(scrapy.Spider):
    name = 'spider01'
    allowed_domains = ['taobao.com']
    start_urls = []

    #分析接口
    #第1页：'https://s.taobao.com/search?q=%E8%BF%9E%E8%A1%A3%E8%A3%99&bcoffset=6&ntoffset=6&p4ppushleft=1%2C48&s=0'
    #第2页：'https://s.taobao.com/search?q=%E8%BF%9E%E8%A1%A3%E8%A3%99&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44'
    #第3页：'https://s.taobao.com/search?q=%E8%BF%9E%E8%A1%A3%E8%A3%99&bcoffset=3&ntoffset=0&p4ppushleft=1%2C48&s=88'
    base_url = 'https://s.m.taobao.com/search?q=%E8%BF%9E%E8%A1%A3%E8%A3%99&s='

    # base_url='https://s.m.taobao.com/h5?event_submit_do_new_search_auction=1&_input_charset=utf-8&topSearch=1&atype=b&searchfrom=1&action=home%3Aredirect_app_action&from=1&sst=1&n=20&buying=buyitnow&q=%E7%99%BD%E9%85%92'
    for page in range(1,11,1):
        url = base_url+str((page-1)*44)
        start_urls.append(url)
        print(url)

    def parse(self, response):
        #保存
        with open('taobao.json','w',encoding='utf-8') as fp:
            fp.write(response.text)

        #由于数据存放在一个字符串当中，所以我们需要使用正则进行数据字符串的截取
        # pattern = re.compile(r'g_page_config = (.*?);\n')
        # res = pattern.search(response.text)

        #健壮性处理
        if 1:
            # data_str = res.group(1)
            data_dict = json.loads(response.text)

            #jsonpath的使用
            #$:根节点
            #.:子节点----相当于xpath中的‘/’
            #..:跨节点----                //
            #*:所有元素节点
            products = jsonpath.jsonpath(data_dict,'$..itemsArray.*')
            for p in products:

                # title = p['title']#标题
                # nick = p['nick']#店铺名称
                # pic_url = p['pic_url']#图片地址
                # price = p['view_price']#价格
                # loc = p['item_loc']#所在地
                detail_url = p['auctionURL']#详情页地址



                detail_url = request.urljoin(response.url,detail_url)
                with open('data_url_new.txt','a',encoding='utf-8') as fp:
                    fp.write(detail_url+'\n')

                #将数据存储到数据模型
                item = TaobaoItem()
                # item['title'] = title
                # item['nick'] = nick
                # item['price'] = price
                # item['loc'] = loc
                # item['pic_url'] = pic_url
                # item['detail_url']=detail_url
                item['crawl_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                #发起详细页的请求
                # dont_filter:True，允许重复请求
                yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'data':item,'phantomjs':True},dont_filter=True)


    #解析详情页
    def parse_detail(self, response):
        with open('detail.html','w',encoding='utf-8') as fp:
            fp.write(response.text)

        item = response.request.meta['data']

        # 交易成功数和评论数
        if 'tm-count' in response.text:#天猫
            span_list = response.xpath('//span[@class="tm-count"]/text()').extract()
            item['sell_counter'] = self.getDataFromList(span_list,0)
            item['rate_counter'] = self.getDataFromList(span_list,1)
        else:#淘宝
            item['sell_counter']=response.xpath('//strong[@id="J_SellCounter"]/text()').extract()[0].strip()
            item['rate_counter']=response.xpath('//strong[@id="J_RateCounter"]/text()').extract()[0].strip()
        yield item

    #代码的健壮性处理
    def getDataFromList(self,l,index):
        if len(l)>index:
            return l[index].strip()
        else:
            return 0













