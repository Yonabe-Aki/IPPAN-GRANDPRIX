from PIL import Image, ImageDraw, ImageFont
from mysite import settings
def create_img(theme,id):
    if settings.mode=="テスト" or settings.mode=="本番":
        font = ImageFont.truetype("/app/.font/ヒラギノ角ゴシック W9.ttc", 60)
    if settings.mode=="ローカルテスト" or settings.mode=="ローカルテスト２":
        font = ImageFont.truetype("/Users/imanishiyuujin/onigiri/.font/ヒラギノ角ゴシック W9.ttc", 60)

    LINES=theme.splitlines()
    LINES_COUNT=len(LINES)

    img = Image.open("media/frame.jpg")
    draw = ImageDraw.Draw(img)
    W,H=img.size
    num=1

    for line_text in LINES:
        w,h=draw.textsize(line_text,font=font)
        h+=5
        x=(W-w)/2
        y=(H-h*LINES_COUNT)/2+h*(num-1)
        coordinate=(x,y)
        draw.text(coordinate , line_text, fill=(0, 0, 0), font=font)
        num+=1
    
    img.save("media/img_"+str(id)+".jpg")




