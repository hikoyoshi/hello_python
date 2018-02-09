#-*-coding:utf-8 -*-
import csv

def BMI(h,w):
    bmi = w /((h/100.0)**2)
    return str(round(bmi,1))


#開啟demo
f = open('example_11.csv', 'r',newline='',encoding='utf-8')
#開啟新檔案demo2
f1 = open('bmi.csv','w',newline='',encoding='utf-8')
w = csv.writer(f1)
#新增第一行，name與avg 
w.writerow(['Name','bmi'])
#取出要每行要計算的值
for row in csv.DictReader(f):
    height =int(row['height']) 
    weight =int(row['weight'])

    bmi = BMI(height,weight)

    w.writerow([row['Name'],bmi])
f.close()
f1.close()