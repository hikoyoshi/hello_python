#-*- coding:utf-8 -*-
import temperature as tp

c_or_f = input("0、離開 1、轉換為華式 2、轉換為攝式\n")
if c_or_f == "0":
    print ("ByeBye~~")
    sys.exit()
elif c_or_f != "1" and c_or_f !="2":
    print ("沒這個選項啦~~")
    sys.exit()
    
temp = input("請輸入溫度:\n")

if c_or_f == "0":
    print ("ByeBye~~")
    sys.exit()
elif c_or_f =="1":
    f = tp.c2f(int(temp)
    print f
    print ("華式溫度為{}".format(f))
elif c_or_f =="2":
    c = tp.f2c(int(temp)
    print ("攝式溫度為{}".format(c))