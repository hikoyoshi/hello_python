#!-*- coding:utf-8 -*-
#載入pil模組
from PIL import Image,ImageDraw,ImageFont
#載入圖片
im = Image.open('kaeru.jpg')
#crop的範圍為 左上x,y與右下x,y的四點座標
nim = im.crop((400,100,700,300))
nim.save("crop.jpg")
nim.show()
