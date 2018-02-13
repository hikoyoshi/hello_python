from PIL import Image,ImageDraw,ImageFont
import sys,os
# 新增文字浮水印函數
# Add_text(舊檔案, 要新增的文字、新檔名)
#
def Add_text(filename,newtext,newname):
    #先判定是不是圖片
    Is_img(filename)
    #先載入字型並設定字型大小為28
    font = ImageFont.truetype('msjhbd.ttc',28)
    #開啟檔案
    im = Image.open(filename)
    #取得圖片大小
    x,y = im.size
    #將im 放入ImageDraw的圖層
    img_draw = ImageDraw.Draw(im)
    #將文字放到右下角
    img_draw.text((x-(x/3),y-(y/7)),newtext,fill=(220,220,220),font=font)
    #將新檔名加上.jpg
    nw = newname+".jpg"
    #存檔
    im.save('{0}'.format(nw))
    im.show(nw)


# 判斷是不是圖片的函數
def Is_img(filename):
    #宣告要判斷的副檔名類型
    img_format = ['.jpg','.png','.jpeg']
    #用os的函數os.path.isdir來判斷是檔案還是資料夾
    if  os.path.isdir(filename):
            print ("不是檔案!!!!")
            sys.exit() 
    #用os.path.splitext來分離檔名與副檔名
    name,extension =os.path.splitext(filename)
    #如果副檔名不是jpg、png、jpeg就離開
    if extension not in img_format:
        print("這不是圖片檔........")
        sys.exit()