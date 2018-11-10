from selenium import webdriver
from lxml import etree

driver = webdriver.PhantomJS(executable_path=r'C:\Users\IBM\Desktop\python\phantomjs-2.1.1-windows\bin\phantomjs.exe')

driver.get('https://book.douban.com/subject_search?search_text=python&cat=1001')

tree = etree.HTML(driver.page_source)
addr = tree.xpath('//div[@class="sc-dnqmqq eXEXeG"]')

for add in addr:
    for i in range(0, 10):
        # 链接
        index = add.xpath('./div/div/a/img/@src')[i]
        # 书名
        name = add.xpath('./div/div/div/div/a/text()')[i]
        # 评分
        num = add.xpath('./div/div/div/div/span[@class="rating_nums"]/text()')[i]
        # 评分人数
        p1 = add.xpath('./div/div/div/div/span[@class="pl"]/text()')[i]
        # 简介
        meta = add.xpath('./div/div/div/div[@class="meta abstract"]/text()')[i]
        info = '链接：' + index + '\n' \
             + '书名：' + name + '\n' \
             + '评分：' + num + '\n' \
             + '评分人数：' + p1 + '\n' \
             + '作者/译者/出版社/出版时间/价格：' + meta + '\n'
        print(info)
