from PIL import Image, ImageDraw, ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    fillcolor = "#ffffff"
    width, height = img.size
    draw.text((width/2, height/2), u"此图片仅用于腾讯云备案", font=myfont, fill=fillcolor)
    img.save('result.jpg','jpeg')

    return 0
if __name__ == '__main__':
    image = Image.open('lena.jpg')
    add_num(image)
    image.show()
