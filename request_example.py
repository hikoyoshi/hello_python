#! -*-coding:utf-8 -*-
import requests

res = requests.get("http://opendata2.epa.gov.tw/AQI.json")
r = res.json()
#取得json的總長度後用for列出
for i in range(len(r)):
    if r[i]['County'] == "宜蘭縣":
        print (r[i]['PM2.5'])