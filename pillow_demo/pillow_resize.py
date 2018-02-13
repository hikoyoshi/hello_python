#!-*- coding:utf-8 -*-
#載入pil模組
from PIL import Image,ImageDraw,ImageFont
#載入圖片
im = Image.open('kaeru.jpg')
#取得圖片大小分別放進x,y
x,y = im.size
#縮小圖片
nim = im.resize((int(x/2),int(y/2)),Image.LANCZOS)
print (nim.size)
#儲存
nim.save("resize.jpg")
nim.show()
