# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.corriere.it']
    start_urls = ['http://www.corriere.it/']

    def parse(self, response):
        # response.css("")
        pass


    def cleanUrls(urls):
    	pass

