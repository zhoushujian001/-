# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoItem(scrapy.Item):
    # define the fields for your item here like:
    # title = scrapy.Field()
    # nick = scrapy.Field()
    # price = scrapy.Field()
    # loc = scrapy.Field()
    # pic_url = scrapy.Field()
    detail_url = scrapy.Field()


    sell_counter = scrapy.Field()#30天交易成功的数量
    rate_counter = scrapy.Field()#评论数

    crawl_time = scrapy.Field() #爬取时间

