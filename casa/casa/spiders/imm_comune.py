import scrapy
import sys
from w3lib.html import remove_tags

class QuotesSpider(scrapy.Spider):
    name = "imm_location"
    # start_urls = [
    #     'https://www.casa.it'
    # ]

    def start_requests(self):
        urls = [
            'https://www.immobiliare.it'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for city in response.css("li.nd-listMeta__item--meta"):
            if 'vendita-case' not in city.css('a::attr(href)').get():  
                continue
            cityname = city.css('a::text').get().replace('\n','').strip()
            urladdr = city.css('a::attr(href)').get()

            href = urladdr
            href = response.urljoin(href)

            request = scrapy.Request(href,
                     callback=self.parseTown,
                     cb_kwargs=dict(city=cityname,urladdr=urladdr))
            yield request

       


    def parseTown(self, response, city, urladdr):
        for town in response.css('li.nd-listMeta__item--meta'):
            # townname = town.css('a::text').get().replace('\n','').strip()
            townname = remove_tags(town.css('a').get()).replace('\n','').strip()
            if not townname:
                continue

            townlink = town.css('a::attr(href)').get()
            yield {
                        'city': city,
                        'townname':townname,
                        'townlink':townlink
            }
   
