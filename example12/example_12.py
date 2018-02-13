#!-*- coding:utf8 -*-
from img_module import *

if len(sys.argv) < 2: #len小於2也就是不帶參數啦
    print ('-help or h 查詢可用參數')
    sys.exit()
# 取出sys.argv[1]的數值但是忽略掉'-'這個字元
if sys.argv[1].startswith('-'):
    #取出第一個參數，用切片的方式將'-'拿掉
    option = sys.argv[1][1:] 
    if option == 'version':
        print ('Version 0.0.1 示範板')
    elif option == 'help' or option =='h':
        print ('\t-version 版本宣告')
        print ('\t-t 新增文字浮水印')
        print ('\t使用範例:')
        print ('\tpython example_12.py -t filename newtext newfilename')
        print ('\tfilename => 要新增文字的圖檔')
        print ('\tnewtext => 要新增的文字')
        print ('\tnewfilename => 存檔的檔名，不需要加.jpg')
    elif option == "t":
        #print (len(sys.argv))
        if len(sys.argv) < 5: 
            print ("參數錯誤，請再確認輸入的參數，或輸入 -h 取得使用說明")
            sys.exit()
        #檔案名
        filename = sys.argv[2] #檔案名稱於參數位置時讀取檔案
        #要新增的文字
        text = sys.argv[3]
        #另存新檔的檔名
        newname = sys.argv[4]
        
        #print(filename,text,newname)
        #將檔名、要新增的文字及新檔名等三個函數放到新增文字浮水印函數
        Add_text(filename,text,newname)
    else:
        print ('\n\t參數錯誤\n')
        print ('\t可使用參數如下:\n\t-version 版本宣告\n\t--help 使用說明\n\t -t 在圖片右下角加上想要的文字')
        sys.exit()
else:
    print("\n\t命令格式錯誤，請輸入-h 或 --help取得說明")
