#!-*- coding:utf8 -*-
import sys
def readfile(filename):
    f = open(filename,"r",encoding='utf-8')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print (line)
    f.close()

 
#開始對sys.argv下定義

if len(sys.argv) < 2: #len小於2也就是不帶參數啦
    print ('no argument')
    sys.exit()
if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:] # 取出sys.argv[1]的數值但是忽略掉'--'這兩個字元
    if option == 'version':
        print ('Version 1.2.3')
    elif option == 'help':
        print ('help documention')
    else:
        print ('only --version --help can be used')
        sys.exit()
else:
    for filename in sys.argv[1:]: #檔案名稱於參數位置時讀取檔案
        print(filename)
        readfile(filename)


