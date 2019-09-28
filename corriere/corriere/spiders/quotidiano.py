# -*- coding: utf-8 -*-
# parser for quotitiano.net
import scrapy
import logging
import time
import json


from corriere.spiders.common_foo import *

class ExampleSpider(scrapy.Spider):
    name = 'quotidiano'
    allowed_domains = ['quotidiano.net']
    start_urls = [
    	'https://www.quotidiano.net',
        # 'http://pinkitalia.it',
        # 'http://www.cavallomagazine.it',
        # 'https://www.hwupgrade.it'
    	]
    count_collected = 0
    count_parsed = 0

    checked = [] 
    with open('qdurls.json') as filejson:
        checked = json.load(filejson)


    def closed(self, reason):
        print('done!')

    def parse(self, response):


        # response.xpath('//span[@itemprop="articleBody"]/text()').getall()
        raw_paragraphs = response.css('p').getall()
        paragraphs = filter_paragraphs(raw_paragraphs)
        currentUrl = response.request.url

        self.count_parsed = self.count_parsed + 1
        

        if len(paragraphs) != 0 and currentUrl not in self.checked:
            self.count_collected = self.count_collected + 1
            yield {
                'link':currentUrl,'texts':paragraphs
            }
        
        print(f'\r{self.count_collected} collected', end=' ', flush=True)

        next_pages = response.css('a::attr(href)').getall()
        for next_page in next_pages:
            if isValidUrl(next_page):
                yield response.follow(next_page, callback=self.parse)
            
                

        
            

    
