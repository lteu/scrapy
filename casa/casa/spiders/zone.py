import scrapy
import json



class QuotesSpider(scrapy.Spider):
    name = "zone"
    start_urls = [
        
    ]

    def start_requests(self):
        urls_info = []
        cached_urls = []
        with open('towns.json') as filejson:
            raw = json.load(filejson)
            count  = 0 
            for item in raw:
                urls_info.append(['https://www.casa.it'+item['townlink'],item['city'],item['townname']])
                cached_urls.append(item['townlink'])
                count += 1
                # if count > 78:
                #     break
        
        cached_urls = set(cached_urls)
        for url in urls_info:
            cityname = url[1]
            townname = url[2]
            yield scrapy.Request(url=url[0], 
                callback=self.parseAdsPage,
                cb_kwargs=dict(cityname=cityname,townname=townname,cached_urls=cached_urls))


    

    def parseAdsPage(self, response,cityname,townname,cached_urls):
        # print(cached_urls)

        caseText = response.css('div#srpBreadcrumb li.ddContainer button::text').get()
        if 'Scegli la zona' in caseText:
            for zonetag in response.css('div#srpBreadcrumb div.dropDown ul li'):
                href = zonetag.css('a::attr(href)').get()
                zonename = zonetag.css('a span.locName::text').get()
                if href in cached_urls:
                    continue

                yield {
                    'cityname':cityname,
                    'townname':townname,
                    'zonename':zonename,
                    'zonelink': href
                }




