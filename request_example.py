#! -*-coding:utf-8 -*-
import requests

res = requests.get("http://www.yahoo.com.tw")
r = res.text

print (r)