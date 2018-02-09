#-*-coding:utf-8 -*-
import csv

#基本寫入
f = open('demo3.csv','w',newline='',encoding='utf-8')
w = csv.writer(f)
w.writerow(['name','age'])
w.writerow(['herry','13'])
w.writerow(['andy','14'])
f.close()

#使用字典寫入
csvfile = open('names.csv', 'w+',newline='',encoding='utf-8')
fieldnames = ['first_name', 'last_name']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

writer.writeheader()
writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
csvfile.close()