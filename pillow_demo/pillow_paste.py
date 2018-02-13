#!-*- coding:utf-8 -*-
#載入pil模組
from PIL import Image,ImageDraw,ImageFont
#載入被貼圖片
im = Image.open('kaeru.jpg')
#載入要貼的圖片
pim = Image.open('crop.jpg')
#將pim貼在im上，於左上角(0,0)位置
im.paste(pim,(100,100))
im.save("paste.jpg")
im.show()
