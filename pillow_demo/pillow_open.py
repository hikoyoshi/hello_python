#!-*- coding:utf-8 -*-
#載入pil模組
from PIL import Image,ImageDraw,ImageFont
#載入圖片

im = Image.open('kaeru.jpg')
#列出檔案格式、大小與顏色模式
print (im.format,im.size,im.mode)
#開啟圖片
im.show()