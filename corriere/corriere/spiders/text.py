# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.corriere.it']
    start_urls = [
    	# 'https://www.corriere.it/opinioni/19_settembre_16/i-falsi-miti-caduti-donald-trump-caf7973e-d8b7-11e9-a64f-042100a6f996.shtml/',
    	'https://www.repubblica.it/salute/medicina-e-ricerca/2019/09/12/news/sexting_1_giovane_su_4_riceve_messaggi_a_sfondo_sessuale-235825008//',
    	# 'https://www.corriere.it/salute/diabete/'

    	]


    def parse(self, response):
        # response.css("")
        response.xpath('//span[@itemprop="articleBody"]/text()').getall()


    def cleanUrls(urls):

