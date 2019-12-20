from PIL import Image, ImageDraw, ImageFont
from mysite import settings
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import io
from io import BytesIO

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
    
    # img.save("media/img_"+str(id)+".jpg")

    def upload_image_to_s3(img, bucket_name, key_name):
    
        conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
        bucket = conn.get_bucket(bucket_name)
        k = Key(bucket, key_name)
        image_buffer = io.BytesIO()
        img.save(image_buffer, 'JPEG')
        image_buffer.seek(0)  
        k.set_contents_from_string(image_buffer.read(),headers={'Content-Type': 'image/jpeg'})
    
    upload_image_to_s3(img,settings.AWS_STORAGE_BUCKET_NAME,"media/img_"+str(id)+".jpg")




