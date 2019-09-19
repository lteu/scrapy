import scrapy
import json
import logging

# from scrapy.xlib.pydispatch import dispatcher
# from scrapy import signals
# # from scrapy.stats import stats
from datetime import datetime



class QuotesSpider(scrapy.Spider):
    name = "price"

    global a
    a = 0


    # def __init__(self, mainurl=None, *args, **kwargs):
    #     super(MySpider, self).__init__(*args, **kwargs)
    #     self.start_urls = [mainurl]
    #     # ...


    def start_requests(self):
        urls = [
            # 'https://www.casa.it/vendita/residenziale/bologna/murri/'
            'https://www.casa.it/vendita/residenziale/bologna/bolognina/'
        ]

        counter = 1
        for url in urls:
            cityname = 'bologna'
            townname = 'bologna'
            zone = 'bolognina'
            yield scrapy.Request(url=url, 
                callback=self.parsePriceAds,
                cb_kwargs=dict(cityname=cityname,townname=townname,zone=zone,counter=counter,url=url))


    
    def spider_closed(self, spider):
        spider.logger.info('Spider closed ^_____________________^ : %s', spider.name)


    def closed(self, reason):
        global a
        print('cal='+str(a))
        # logging.warning('Spider closed ^_____________!________^'+str(a))

    def parsePriceAds(self, response,cityname,townname,zone,counter,url):
        global a
  
        if counter !=1 and 'pagina' not in response.css('div.heading h1::text').get():
            work_time = datetime.now() - startedon
            logging.warning('This is an info message')
            logging.warning('Spider closed ^_____________________^ !!!')
        else:
            for casa in response.css('article.srp-card'):
                title = casa.css('p.casaAdTitle a::text').get()
                link = casa.css('p.casaAdTitle a::attr(href)').get()

                info = casa.css('div.infos')
                price = info.css('div.features p::text')[1].get() if len(info.css('div.features p::text')) > 1 else ''
                mq = info.css('div.features li::text')[0].get()
                lc = info.css('div.features li::text')[2].get() if len(info.css('div.features li::text')) > 2 else ''
                text = info.css('p.decription::text').get()

                a += 1
                # zonename = zonetag.css('a span.locName::text').get()
                # if href in cached_urls:
                #     continue

                yield {
                    'title':title,
                    'price':price,
                    'mq':mq,
                    'lc':lc,
                    'link':link

                }

            counter += 1
            next_url = url+'?page='+str(counter)
            yield scrapy.Request(url=next_url, 
                callback=self.parsePriceAds,
                cb_kwargs=dict(cityname=cityname,townname=townname,zone=zone,counter=counter,url=url))




