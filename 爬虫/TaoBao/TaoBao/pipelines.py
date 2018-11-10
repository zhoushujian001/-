# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import json

class TaobaoPipeline(object):
    # def __init__(self):
    #     self.client = pymongo.MongoClient('    ')
    #     self.db = self.client['TaobaoDB']

    def process_item(self, item, spider):
        # self.db['baijiu'].insert(dict(item))
        # return item
        json.dump(dict(item),open('data.json','a',encoding='utf-8'),ensure_ascii=False)
