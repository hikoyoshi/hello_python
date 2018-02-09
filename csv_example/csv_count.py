#-*-coding:utf-8 -*-
import csv
import time,datetime

#開啟demo
f = open('demo.csv', 'r',newline='',encoding='utf-8')
#開啟新檔案demo2
f1 = open('demo2.csv','w',newline='',encoding='utf-8')
w = csv.writer(f1)
#新增第一行，name與avg 
w.writerow(['Name','avg'])
#取出要每行要計算的值
for row in csv.DictReader(f):
    t1 =int(row['chinese']) 
    t2 =int(row['english'])
    t3 =int(row['math'])
    avg = (t1+t2+t3)/3
    #逐行寫入名字與平均成績
    w.writerow([row['Name'],round(avg,1)])
f.close()
f1.close()


