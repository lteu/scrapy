import json
import csv

# filename = 'catalogues/casa-zones.json'
# filename = 'catalogues/casa-towns.json'
# filename = 'catalogues/imm_district.json'
# filename = 'catalogues/imm_district.json'
# filename = 'catalogues/imm_zone.json'


def json2csv(filename):
	with open(filename) as filejson:
		raw = json.load(filejson)

	keys = raw[0].keys()

	outfile = filename.split('.json')[0]+'.csv'
	with open(outfile, 'w') as outfile:
		out = "output"
		outfile.write(';'.join(keys)+"\n")
		for x in raw:
			arr = [x[y] for y in keys]
			outfile.write(';'.join(arr)+"\n")


arr = ['catalogues/imm_district.json',
'catalogues/imm_town.json',
'catalogues/imm_zone.json']


for item in arr:
	json2csv(item)
# print(raw[0])