#!-*- coding:utf-8 -*-
#載入pil模組
from PIL import Image,ImageDraw,ImageFont
#載入圖片

#載入字型及大小
font = ImageFont.truetype('msjhbd.ttc',28)
im = Image.open('kaeru.jpg')
#將im的圖放進img_draw的圖層
img_draw = ImageDraw.Draw(im)
#新增位置、顏色及字型
img_draw.text((550,130),'旅行青蛙',fill=(100,0,150),font=font)
im.show()
im.save("img_text.jpg")