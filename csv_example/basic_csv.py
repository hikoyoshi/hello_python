#-*-coding:utf-8 -*-
import csv

#基本的讀取
f = open("demo.csv",'r',encoding='utf-8')
for row in csv.reader(f):
    print (row)
f.close()

#字典式讀取
f = open('demo.csv','r',encoding='utf-8')
for row in csv.DictReader(f):
    print (row)
f.close()

#讀取特定資料
f = open('demo.csv', 'r',encoding='utf-8')
for row in csv.DictReader(f):
    if row['Name'] == "小白":
        print (row)
f.close()