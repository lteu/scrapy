# -*- coding: utf-8 -*-

import scrapy
import logging
import time
import json
import os
import sys
from corriere.spiders.common_foo import *

class ExampleSpider(scrapy.Spider):
    name = 'ilmessaggero'
    allowed_domains = ['ilmessaggero.it']
    start_urls = [
    	'https://www.ilmessaggero.it'
    	]
    count_collected = 0
    count_parsed = 0


    def closed(self, reason):
        print('done!')

    def parse(self, response):

        # raw_paragraphs = response.xpath('//span[@itemprop="articleBody"]').getall()
        raw_paragraphs = response.css('p').getall()

        paragraphs = filter_paragraphs(raw_paragraphs)
        currentUrl = response.request.url
        
        if len(paragraphs) != 0:
            yield {
                'link':currentUrl,'texts':paragraphs
            }
        

        next_pages = response.css('a::attr(href)').getall()
        for next_page in next_pages:
            if isValidUrl(next_page):
                yield response.follow(next_page, callback=self.parse)