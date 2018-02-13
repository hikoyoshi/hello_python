#!-*- coding:utf-8 -*-
#載入pil模組
from PIL import Image,ImageDraw,ImageFont
#載入圖片
im = Image.open('kaeru.jpg')
#顏色轉換，1為1bit單色、L為8bit灰階、RGB....等可選擇
garyim = im.convert('1')
garyim.save("convert.jpg")
garyim.show()