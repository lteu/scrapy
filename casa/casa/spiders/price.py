import scrapy
import json



class QuotesSpider(scrapy.Spider):
    name = "price"
    

    def start_requests(self):
        urls = [
            'https://www.casa.it/vendita/residenziale/bologna/bolognina'
        ]

        counter = 1
        for url in urls:
            cityname = 'bologna'
            townname = 'bologna'
            zone = 'bolognina'
            yield scrapy.Request(url=url, 
                callback=self.parsePriceAds,
                cb_kwargs=dict(cityname=cityname,townname=townname,zone=zone,counter=counter,url=url))


    

    def parsePriceAds(self, response,cityname,townname,zone,counter,url):
        # print(cached_urls)
        if counter !=1 and 'pagina' not in response.css('div.heading h1::text').get():
            print('Done')
        else:
            for casa in response.css('article.srp-card'):
                title = casa.css('p.casaAdTitle a::text').get()
                link = casa.css('p.casaAdTitle a::attr(href)').get()

                info = casa.css('div.infos')
                price = info.css('div.features p::text')[1].get()
                mq = info.css('div.features li::text')[0].get()
                lc = info.css('div.features li::text')[2].get() if len(info.css('div.features li::text')) > 2 else ''
                text = info.css('p.decription::text').get()

                # zonename = zonetag.css('a span.locName::text').get()
                # if href in cached_urls:
                #     continue

                yield {
                    'title':title,
                    'price':price,
                    'mq':mq,
                    'lc':lc,
                    'link':link,
                    'text':text
                }

            counter += 1
            next_url = url+'?page='+str(counter)
            yield scrapy.Request(url=next_url, 
                callback=self.parsePriceAds,
                cb_kwargs=dict(cityname=cityname,townname=townname,zone=zone,counter=counter,url=url))




