from PIL import Image, ImageDraw, ImageFont
def create_img(theme,id):


    img = Image.open("media/frame.jpg")
    W,H=img.size

    draw = ImageDraw.Draw(img)
    w,h=draw.textsize(theme)



    draw.text(((W-w)/2,(H-h)/2), theme, fill=(0, 0, 255))
    img.save("media/img_"+str(id)+".jpg")




