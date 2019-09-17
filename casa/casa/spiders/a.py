import scrapy
import sys


class QuotesSpider(scrapy.Spider):
    name = "location"
    # start_urls = [
    #     'https://www.casa.it'
    # ]

    def start_requests(self):
        urls = [
            'https://www.casa.it'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for regione in response.css("div.regionsList dl"):
            for city in regione.css("dd"):
                if 'vendita' not in city.css('a::attr(href)').get():  
                    continue

                regionename = regione.css('dt::text').get()
                cityname = city.css('a span::text').get()
                urladdr = city.css('a::attr(href)').get()

                href = city.css('a::attr(href)').get()
                href = response.urljoin(href)


                request = scrapy.Request(href,
                         callback=self.parseTown,
                         cb_kwargs=dict(regionename=regionename,city=cityname,urladdr=urladdr))
                yield request

                # yield {
                #     'regione': regione.css('dt::text').get(),
                #     'city': city.css('a span::text').get(),
                #     'url-addr':city.css('a::attr(href)').get()
                # }



    def parseTown(self, response, regionename, city, urladdr):
        for town in response.css('div.townsList li'):
            townname = town.css('a::text').get()
            if not townname:
                continue

            townlink = town.css('a::attr(href)').get()
            yield {
                        'regione': regionename,
                        'city': city,
                        'townname':townname,
                        'townlink':townlink
            }
   
