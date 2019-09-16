# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ("http://www.runoob.com/w3cnote/scrapy-detail.html",)

    def parse(self, response):
        print('response',response) #打印出响应
        filename = "teacher.html"
        open(filename, 'w').write(response.body)
