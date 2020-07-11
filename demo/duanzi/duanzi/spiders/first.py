# -*- coding: utf-8 -*-
import scrapy

from duanzi.items import DuanziItem
from scrapy.exceptions import DropItem

class FirstSpider(scrapy.Spider):
    name = 'first'
    # allowed_domains = ['https://duanziwang.com/']
    start_urls = ['https://duanziwang.com/']

    page_num = 1

    def parse(self, response):
        print(self.page_num)
        articles = response.xpath("/html/body/section/div/div/main/article")

        for article in articles:
            text = article.xpath("./div[1]/h1/a/text()").extract_first()
            content = article.xpath("./div[2]//code/text()").extract_first()
            if (text and content):
                text = text.strip()
                content = content.strip()
            else:
                contents = article.xpath("./div[2]//p/text()").extract()
                # print(contents)
                for p_con in contents:
                    content = p_con.strip() + "\n"
                    print(content)

            itemsClass = DuanziItem()
            itemsClass['text'] = text
            itemsClass['content'] = content

            yield itemsClass
            # break

        self.page_num += 1
        if(self.page_num <= 64):
            next_url = response.xpath('/html/body/section/div/div/main/nav/a[last()]/@href').extract_first()
            # print(next)
            yield scrapy.Request(url=next_url, callback=self.parse)
