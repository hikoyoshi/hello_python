#!-*- coding:utf-8 -*-

import requests,json

res = requests.get('http://opendata2.epa.gov.tw/AQI.json')
data = res.json()

for i in range(0,len(data)):
	print (data[i]['County'])
	print (data[i]['PM2.5'])