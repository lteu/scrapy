import scrapy
import json



class QuotesSpider(scrapy.Spider):
    name = "imm_district"
    start_urls = [
        
    ]

    def start_requests(self):
        urls_info = []
        cached_urls = []
        with open('catalogues/imm_zone.json') as filejson:
            raw = json.load(filejson)
            count  = 0 
            for item in raw:
                urls_info.append([item['zonelink'],item['cityname'],item['townname'],item['zonename']])
                cached_urls.append(item['zonelink'])
                count += 1
                # if count > 78:
                #     break
        
        cached_urls = set(cached_urls)
        for url in urls_info:
            cityname = url[1]
            townname = url[2]
            zonename = url[3]
            yield scrapy.Request(url=url[0], 
                callback=self.parseAdsPage,
                cb_kwargs=dict(cityname=cityname,townname=townname,zonename=zonename,cached_urls=cached_urls))


    

    def parseAdsPage(self, response,cityname,townname,zonename,cached_urls):
        # print(cached_urls)
        # if response is None:
            # print(11)
        caseText = response.css('li.quartiere a span').get()
        if caseText is not None:
            
            if 'Scegli il quartiere' in caseText:
                for districttag in response.css('li.quartiere ul.breadcrumb-list_list li'):
                    if districttag is None:
                        continue
                # css('div#srpBreadcrumb div.dropDown ul li'):
                    href = districttag.css('a::attr(href)').get()
                    district = districttag.css('a::text').get().strip()
                    if href in cached_urls:
                        continue

                    yield {
                        'cityname':cityname,
                        'townname':townname,
                        'zonename':zonename,
                        'district':district,
                        'districtlink': href
                    }




