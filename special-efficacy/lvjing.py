from PIL import Image, ImageFilter

import random
import math

log = print


def grayscale(image, w, h):
    # 由于 python 用缩进表示代码结构
    # 所以发明了一个 pass 语句
    # 这个语句没有其他作用，只是一个占位符
    # 如果没有 pass 直接留空函数就会有语法错误
    # Gray =（R + G + B） / 3
    # log('img', image.width)
    for i in range(1, w):
        for j in range(1, h):
            position = (i, j)
            r, g, b, a = image.getpixel(position)
            # rgb = (r * 0.3 + g * 0.59 + b * 0.11)
            rgb = (r * 30 + g * 59 + b * 11) / 100
            # rgb = (r * 76 + g * 151 + b * 28) >> 8
            # rgb = g
            rgb = int(rgb)
            image.putpixel(position, (rgb, rgb, rgb, a))
    return image


def randindex():
    index = int(random.random() * 8)
    return index


def maoboli(image, w, h):
    mm = 8
    w = w - mm
    h = h - mm
    for i in range(1, w):
        for j in range(1, h):
            index = randindex()
            position = (i, j)
            temp = (i + index, j - index)
            r, g, b, a = image.getpixel(temp)
            image.putpixel(position, (r, g, b, a))
    return image


def chang(image, i, j):
    if (i % 10 == 0) and (j % 10 == 0):
        for m in range(10):
            for n in range(10):
                temp = (i, j)
                position = (i + m, j + n)
                r, g, b, a = image.getpixel(temp)
                image.putpixel(position, (r, g, b, a))


def masaike(image, w, h):
    mm = 8
    w = w - mm
    h = h - mm
    for i in range(1, w):
        for j in range(1, h):
            chang(image, i, j)
    return image


def manhua(image, w, h):
    for i in range(1, w):
        for j in range(1, h):
            position = (i, j)
            r, g, b, a = image.getpixel(position)
            x = int(abs(g - b + g + r) * r / 256)
            y = int(abs(b - g + b + r) * r / 256)
            z = int(abs(b - g + b + r) * g / 256)
            image.putpixel(position, (x, y, z, a))
    return image


def fanxiang(image, w, h):
    for i in range(1, w):
        for j in range(1, h):
            position = (i, j)
            r, g, b, a = image.getpixel(position)
            r = 255 - r
            g = 255 - g
            b = 255 - b
            image.putpixel(position, (r, g, b, a))
    return image


def heibai(image, w, h):
    for i in range(1, w):
        for j in range(1, h):
            position = (i, j)
            r, g, b, a = image.getpixel(position)
            avg = (r + g + b) / 3
            if avg >= 130:
                rgb = 255
            else:
                rgb = 0
            image.putpixel(position, (rgb, rgb, rgb, a))
    return image


def huaijiu(image, w, h):
    for i in range(1, w):
        for j in range(1, h):
            position = (i, j)
            r, g, b, a = image.getpixel(position)
            x = int(r * 0.393 + g * 0.769 + b * 0.189)
            y = int(r * 0.349 + g * 0.686 + b * 0.168)
            z = int(r * 0.272 + g * 0.534 + b * 0.131)
            image.putpixel(position, (x, y, z, a))
    return image


# def tackle(image, i, j):
#     to = (i, j)
#     temp = (i + 1, j)
#     r, g, b, a = image.getpixel(to)
#     x, y, z, a = image.getpixel(temp)
#     r = r - x + 128
#     g = g - y + 128
#     b = b - z + 128
#     rgb = int(r * 0.3 + g * 0.59 + b * 0.11)


def fudiao(image, w, h):
    temp = (1, 1)
    for i in range(1, w - 5):
        for j in range(1, h - 5):
            position = (i, j)
            temp = (i + 2, j + 2)
            r, g, b, a = image.getpixel(position)
            # log('r,g,b', r, g, b)
            x, y, z, a = image.getpixel(temp)
            r = r - x + 128
            g = g - x + 128
            b = g - z + 128
            # log(r, g, b)
            rgb = int(r * 0.3 + g * 0.59 + b * 0.11)
            image.putpixel(position, (rgb, rgb, rgb, a))
    return image


def quse(img):
    w = img.width
    h = img.height
    image = Image.new('RGBA', (w, h))

    for i in range(w):
        for j in range(1, h):
            position = (i, j)
            r, g, b, a = img.getpixel(position)
            rgb = (r * 30 + g * 59 + b * 11) / 100
            rgb = int(rgb)
            image.putpixel(position, (rgb, rgb, rgb, a))
    return image


def fanqu(img):
    w = img.width
    h = img.height
    # image此刻为灰度图
    image = quse(img)
    for i in range(1, w):
        for j in range(1, h):
            position = (i, j)
            r, g, b, a = image.getpixel(position)
            # 对image各通道进行反色操作，
            r = 255 - r
            g = 255 - g
            b = 255 - b

            image.putpixel(position, (r, g, b, a))
    return image


def gaosi(img):
    image = fanqu(img)
    gaoimg = image.filter(ImageFilter.GaussianBlur(radius=2))
    return gaoimg


def sumiao(img):
    w = img.width
    h = img.height
    # image是计算公式中的C
    image = Image.new('RGBA', (w, h))
    #  im是计算公式中的A
    im = quse(img)
    #  gao为计算公式中的B
    gao = gaosi(img)

    for i in range(w):
        for j in range(h):
            position = (i, j)
            r, g, b, a = im.getpixel(position)
            x, y, z, o = gao.getpixel(position)
            # 以下的if else语句是为了实现公式 A +（A×B）/（255-B），
            # 为了说明公式 A +（A×B）/（255-B）暂记作 temp
            # 其中 255-B 如果为0，需要特殊考虑
            if (255 - x) == 0:
                r1 = r
            else:
                r1 = r + (r * x) / (255 - x)

            if (255 - y) == 0:
                g1 = g
            else:
                g1 = g + (g * y) / (255 - y)

            if (255 - z) == 0:
                b1 = b
            else:
                b1 = b + (b * z) / (255 - z)
            # 以下三行为了实现min(temp, 255)
            sr = int(min(r1, 255))
            sg = int(min(g1, 255))
            sb = int(min(b1, 255))

            image.putpixel(position, (sr, sg, sb, a))
    return image


def caimiao(img):
    w = img.width
    h = img.height
    # image是计算公式中的C
    image = Image.new('RGBA', (w, h))
    #  im是计算公式中的A
    im = img
    #  gao为计算公式中的B
    gao = gaosi(img)

    for i in range(w):
        for j in range(h):
            position = (i, j)
            r, g, b, a = im.getpixel(position)
            x, y, z, o = gao.getpixel(position)
            # 以下的if else语句是为了实现公式 A +（A×B）/（255-B），
            # 为了说明公式 A +（A×B）/（255-B）暂记作 temp
            # 其中 255-B 如果为0，需要特殊考虑
            if (255 - x) == 0:
                r1 = r
            else:
                r1 = r + (r * x) / (255 - x)

            if (255 - y) == 0:
                g1 = g
            else:
                g1 = g + (g * y) / (255 - y)

            if (255 - z) == 0:
                b1 = b
            else:
                b1 = b + (b * z) / (255 - z)
            # 以下三行为了实现min(temp, 255)
            sr = int(min(r1, 255))
            sg = int(min(g1, 255))
            sb = int(min(b1, 255))

            image.putpixel(position, (sr, sg, sb, a))
    return image


def tackle(img, w, h, i, j):
    offset = 10
    li = i + offset
    if li > (w - 1):
        li = w - 1
    ri = i - offset
    if ri < 0:
        ri = 0
    uj = j + offset
    if uj > (h - 1):
        uj = j - 1
    dj = j - offset
    if dj < 0:
        dj = 0

    position1 = (li, j)
    position2 = (ri, j)
    position3 = (i, uj)
    position4 = (i, dj)
    r1, g1, b1, a1 = img.getpixel(position1)
    r2, g2, b2, a2 = img.getpixel(position2)
    r3, g3, b3, a3 = img.getpixel(position3)
    r4, g4, b4, a4 = img.getpixel(position4)
    r = int((r1 + r2 + r3 + r4) / 4)
    g = int((g1 + g2 + g3 + g4) / 4)
    b = int((b1 + b2 + b3 + b4) / 4)
    a = int((a1 + a2 + a3 + a4) / 4)
    return r, g, b, a


def ghost(img):
    w = img.width
    h = img.height
    image = Image.new('RGBA', (w, h))

    for i in range(0, w):
        for j in range(0, h):
            position = (i, j)
            r, g, b, a = tackle(img, w, h, i, j)
            image.putpixel(position, (r, g, b, a))
    return image


def deal():
    img = Image.open("meir.jpg")
    # 注意由于不是每个图像都有 a 所以这里强制转换成 RGBA 格式
    img = img.convert('RGBA')
    return img


def main():
    # 打开图像文件
    img = deal()
    # 把座标 position 的像素值改写为 白色（全发光就是白色，0 0 0 0 是黑色）
    # img.putpixel(position, (255, 255, 255, 255))
    w = img.width
    h = img.height
    img = deal()
    i = grayscale(img, w, h)
    i.save('gray.png')
    img = deal()
    i = maoboli(img, w, h)
    i.save('mai.png')
    img = deal()
    i = masaike(img, w, h)
    i.save('masaike.png')
    img = deal()
    i = manhua(img, w, h)
    i.save('manhua.png')
    img = deal()
    i = fanxiang(img, w, h)
    i.save('fan.png')
    img = deal()
    i = heibai(img, w, h)
    i.save('heibai.png')
    img = deal()
    i = huaijiu(img, w, h)
    i.save('huaijiu.png')
    img = deal()
    i = fudiao(img, w, h)
    i.save('fudi.png')
    img = deal()

    i = sumiao(img)
    i.save('sumiao.png')
    img = deal()
    i = caimiao(img)
    i.save('caimiao.png')
    img = deal()
    i = ghost(img)
    i.save('ghost.png')


if __name__ == '__main__':
    main()
