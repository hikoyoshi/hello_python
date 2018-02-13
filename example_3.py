#!-*- coding:utf-8 -*-

print "算算看你有沒有過重"
w = input("請輸入體重：\n")
h = input("請輸入身高(cm)：\n")

bmi = w /((h/100.0)**2)
print "你的bmi是",bmi
if bmi<18.5:
    print ("過輕")
elif bmi>=18.5 and bmi <24:
    print ("正常體重")
elif bmi>24 and bmi <27:
    print ("有點過重")
else:
    print ("小胖該減肥了......")