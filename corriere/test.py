# import scrapy
import json
import logging
import time


# with open('outt.json') as filejson:
#     raw = json.load(filejson)

# aStr = [item['texts'] for item in raw if item['link'] == 'https://www.quotidiano.net/cronaca/pay-tv-illegale-1.4790142']
# aStr = aStr[0]
# # aStr = aStr[0]
# aStr = [item.lower() for item in aStr]

# if '"i' in aStr[-1]:
#     print('1')
# else:
#     print('2')
# print(aStr[-1])




for i in range(10):
	
    print(f'\r{i} foo bar', end=' ', flush=True)
    time.sleep(0.5)

print('\ndone!')