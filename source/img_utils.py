import math

from PIL import Image, ImageFilter

def deal(img_name):
    path = "originalImg/"+img_name
    print(path)
    img = Image.open(path)

    img = img.convert('RGBA')
    return img



print(pow(2, 2))
print(math.sqrt(10))