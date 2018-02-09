#!-*- coding:utf-8 -*-
import random

game1 = {"1":"剪刀","2":"石頭","3":"布"}

print ("來猜拳吧!!!")
player="1"
while player !="0":
    player = input("0:退出遊戲 1：剪刀 2：石頭 3：布\n")
    if player =="0":
        print ("ByeBye~~")
        break
        
    cpu = str(random.randint(1,3))
    print ("玩家出..{}，cpu出...{}".format(game1[player],game1[cpu]))

    if player=="1" and cpu == "3" or player =="2" and cpu =="1" or player =="3" and cpu == "2":
        print ("玩家贏了")
    elif player==cpu:
        print ("平手")
    else:
        print ("電腦贏了")

