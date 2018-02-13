#!-*- coding:utf8 -*-

M = 1

D = int(raw_input("DAy?"))

s = (M*2+D) % 3

if s == 0:
    print ("普通")
elif s == 1:
    print ("吉")
else:
    print ("大吉")
