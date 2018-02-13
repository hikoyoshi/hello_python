#!-*-coding:utf-8 -*-

#九九乘法表

for i in range(1, 10):
    for x in range(1, 10):
        print ("{0}x{1}={2}\t".format(i, x, i*x),end="")
    print ("\n")


# while的九九乘法表
y = 1
z =1
while y<10:
    while z<10:
        print  ("{0}x{1}={2}".format(y,z,y*z),end="")
        print ("\t",end="")
        z=z+1
    print ("\n")
    y = y+1
    z=1
