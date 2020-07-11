# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DuanziPipeline:

    def __init__(self):
        self.num = 1
        self.fp = None

    def open_spider(self, spider):
        print('---------start---------')
        self.fp = open('./duanzi.txt', 'w', encoding='utf-8')

    def close_spider(self, spider):
        print('---------end---------')
        self.fp.close()

    def process_item(self, item, spider):
        self.fp.write(str(self.num) + "--")
        self.fp.write(item['text'] + "\n")
        self.fp.write(item['content'] + "\n")
        self.num = self.num + 1
        return item
