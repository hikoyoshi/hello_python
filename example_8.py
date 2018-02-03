#!-*- coding:utf-8 -*-
import sys

#攝式轉華式
def c2f(c):
    f = c*(9.0/5.0)+32
    return f 

#華式轉攝式
def f2c(f):
    c = 5.0/9.0*(f-32)
    return c

c_or_f = raw_input("0、離開 1、轉換為華式 2、轉換為攝式\n")
if c_or_f == "0":
    print "ByeBye~~"
    sys.exit()
elif c_or_f != "1" and c_or_f !="2":
    print "沒這個選項啦~~"
    sys.exit()
    
temp = input("請輸入溫度:\n")

if c_or_f == "0":
    print "ByeBye~~"
    sys.exit()
elif c_or_f =="1":
    f = c2f(temp)
    print f
    print "華式溫度為{}".format(f)
elif c_or_f =="2":
    c = f2c(temp)
    print "攝式溫度為{}".format(c)