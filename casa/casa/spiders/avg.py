import scrapy
import json
import logging

from datetime import datetime



class AvgSpider(scrapy.Spider):
    name = "avg" # spider identifier

    global a,b,c
    a,c = 0,1
    # b=[]


    def start_requests(self):
        page_counter = 1
        mainurl = self.mainurl # passed from arg 
        if mainurl[-1] == '/':
            mainurl = mainurl[:-1]


        yield scrapy.Request(url=mainurl, 
                callback=self.parsePrices,
                cb_kwargs=dict(page_counter=page_counter,url=mainurl))

    
    def spider_closed(self, spider):
        spider.logger.info('Spider closed ^_____________________^ : %s', spider.name)


    def closed(self, reason):
        global a,b,c
        print('cal='+str(a)+"; c="+str(c))
        # print (sum(b)/len(b))

    def parsePrices(self, response,page_counter,url):
        global a,b,c
  
        if page_counter !=1 and 'pagina' not in response.css('div.heading h1::text').get():
            work_time = datetime.now() - startedon
            logging.info('Spider closed ^_____________________^ !!!') # for some reason this is not shown
        else:
            for casa in response.css('article.srp-card'):
                title = casa.css('p.casaAdTitle a::text').get()
                link = casa.css('p.casaAdTitle a::attr(href)').get()

                info = casa.css('div.infos')
                price = info.css('div.features p::text')[1].get() if len(info.css('div.features p::text')) > 1 else ''
                mq = info.css('div.features li::text')[0].get()
                lc = info.css('div.features li::text')[2].get() if len(info.css('div.features li::text')) > 2 else ''
                text = info.css('p.decription::text').get()

                # price post processing
                price = price.replace('.', '')
                price = price.replace(',', '.')

                mq = mq.replace('.', '')
                mq = mq.replace(',', '.')
                

                # filter
                if 'nuda' not in text and 'nudo' not in text and 'asta' not in text and 'Lotto' not in text and 'lotto' not in text:
                    if mq.strip() != '' and price.strip() != '':
                        logging.info(price+' '+mq+' page_counter:'+str(page_counter) + ' c:'+str(c))
                        mq_price = float(price)/float(mq)
                        a = (a*(c-1) + mq_price)/c
                        c += 1                
                    # b.append(mq_price)


                yield {
                    'title':title,
                    'price':price,
                    'mq':mq,
                    'lc':lc,
                    'link':link
                }

            page_counter += 1
            next_url = url+'?page='+str(page_counter)
            yield scrapy.Request(url=next_url, 
                callback=self.parsePrices,
                cb_kwargs=dict(page_counter=page_counter,url=url))




