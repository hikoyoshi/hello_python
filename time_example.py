#!-*- coding:utf-8 -*-
import time,datetime

print(time.time())  # 返回當前時間的時間戳(1970紀元後經過的浮點秒數)
print(time.altzone) # 返回與UTC時間的時間差，以秒計算
print(time.localtime()) # 返回本地時間的struct time物件格式
print(time.gmtime(time.time())) # 返回UTC時間的struct時間物件格式
print(time.asctime()) # 返回時間格式'Fri Feb  9 15:55:27 2018'
print(time.asctime(time.localtime())) # 返回時間格式'Fri Feb  9 15:55:27 2018'
print(time.ctime()) # 返回時間格式'Fri Feb  9 15:55:27 2018',同上
 
print ("---------------------")
 #日期字串 轉成 時間戳
print(time.strptime('2018-02-08','%Y-%m-%d')) # 將日期字串轉成struct時間物件格式
print(time.mktime(time.strptime('2018-02-08','%Y-%m-%d'))) # 將struct時間物件轉成時間戳
 
# 將時間戳 轉成 字串
print(time.gmtime()) # 將UTC時間戳轉換成struct_time格式
print(time.strftime('%Y-%m-%d %H:%M:%S')) # 返回以可讀字串表示的當地時間


print ("---------------------")

print(datetime.datetime.now()) # 返回'2018-02-09 16:04:43.109066'
print(datetime.date.fromtimestamp(time.time())) # 時間戳直接轉成日期格式'2018-02-09'
 
# 時間加減
print(datetime.datetime.now() + datetime.timedelta(3)) # 當前時間+3天
print(datetime.datetime.now() - datetime.timedelta(3)) # 當前時間-3天
print(datetime.datetime.now() + datetime.timedelta(hours=3)) # 當前時間+3小時
print(datetime.datetime.now() + datetime.timedelta(minutes=30)) # 當前時間+30分鐘