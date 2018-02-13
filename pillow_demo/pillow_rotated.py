#!-*- coding:utf-8 -*-
#載入pil模組
from PIL import Image,ImageDraw,ImageFont
#載入圖片
im = Image.open('kaeru.jpg')
#旋轉45度，可旋轉任意角度但rotate的旋轉不是整張旋轉所以會帶有黑邊
nim = im.rotate(45)
nim.save("rotated.jpg")
# transpose 為整張旋轉不會有黑邊，可上下左右翻轉，旋轉角度以90、180、270
nimt =im.transpose(Image.FLIP_LEFT_RIGHT)
nimt.save("transpose.jpg") 
nim.show()
nimt.show()