#!-*- coding:utf-8 -*-
filename = input("請輸入檔名：\n")
msg = input("請輸入內容：\n")

f = open(filename,"w")
f.write(msg)
f.close()

f = open(filename,"r")
print ("讀取檔案為："+f.name)
print ("內容為：")
print f.read()
f.close()