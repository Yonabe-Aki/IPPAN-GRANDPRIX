from PIL import Image, ImageDraw, ImageFont
from mysite import settings
def create_img(theme,id):
    if settings.mode=="テスト" or settings.mode=="本番":
        font = ImageFont.truetype("/app/.font/ipaexm.ttf", 27)
    if settings.mode=="ローカルテスト" or settings.mode=="ローカルテスト２":
        font = ImageFont.truetype("/Users/imanishiyuujin/onigiri/.font/ipaexm.ttf", 27)


    img = Image.open("media/frame.jpg")
    W,H=img.size

    draw = ImageDraw.Draw(img)
    w,h=draw.textsize(theme,font=font)

    #フォントの設定(フォントファイルのパスと文字の大きさ)

    draw.text(((W-w)/2,(H-h)/2), theme, fill=(0, 0, 255), font=font)
    img.save("media/img_"+str(id)+".jpg")




