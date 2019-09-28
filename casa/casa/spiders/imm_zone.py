import scrapy
import json



class QuotesSpider(scrapy.Spider):
    name = "imm_zone"
    start_urls = [
        
    ]

    def start_requests(self):
        urls_info = []
        cached_urls = []
        with open('catalogues/imm_town.json') as filejson:
            raw = json.load(filejson)
            count  = 0 
            for item in raw:
                urls_info.append([item['townlink'],item['city'],item['townname']])
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
        # if response is None:
            # print(11)
        caseText = response.css('li.zona a span').get()
        if caseText is not None:
            
            if 'Scegli la zona' in caseText:
                for zonetag in response.css('ul.breadcrumb-list_list li'):
                # css('div#srpBreadcrumb div.dropDown ul li'):
                    href = zonetag.css('a::attr(href)').get()
                    zonename = zonetag.css('a::text').get().strip()
                    if href in cached_urls:
                        continue

                    yield {
                        'cityname':cityname,
                        'townname':townname,
                        'zonename':zonename,
                        'zonelink': href
                    }




