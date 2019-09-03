from PIL import Image, ImageFilter
import math

log = print


def crop(image, frame):
    x = frame[0]
    y = frame[1]
    w = frame[2]
    h = frame[3]
    img = Image.new('RGBA', (w, h))

    for i in range(w):
        for j in range(h):
            position = (i, j)
            temp = (i + x, j + y)

            r, g, b, a = image.getpixel(temp)
            img.putpixel(position, (r, g, b, a))

    return img


def flip(image):
    w = image.width
    h = image.height
    img = Image.new('RGBA', (w, h))

    for i in range(w):
        for j in range(h):
            p = h - j - 1
            position = (i, j)
            temp = (i, p)

            r, g, b, a = image.getpixel(position)
            img.putpixel(temp, (r, g, b, a))

    return img


def flop(image):
    w = image.width
    h = image.height
    img = Image.new('RGBA', (w, h))

    for i in range(w):
        for j in range(h):
            p = w - i - 1
            position = (i, j)
            temp = (p, j)

            r, g, b, a = image.getpixel(position)
            img.putpixel(temp, (r, g, b, a))

    return img


def rotate(image):
    w = image.width
    h = image.height
    t = 2 * w
    o = 2 * h
    img = Image.new('RGBA', (t, o))

    for i in range(w):
        for j in range(h):
            position = (i, j)
            temp = (t - i - 1, j)
            cont = (w - (w - i), t - j - 2)
            dudu = (o - i - 1, t - j - 2)

            r, g, b, a = image.getpixel(position)
            img.putpixel(position, (r, g, b, a))
            img.putpixel(temp, (r, g, b, a))
            img.putpixel(cont, (r, g, b, a))
            img.putpixel(dudu, (r, g, b, a))

    return img


def duijiao(image):
    w = image.width
    h = image.height
    img = Image.new('RGBA', (w, h))

    for i in range(w):
        for j in range(h):
            position = (i, j)
            temp = (h - j - 2, w - i - 2)

            r, g, b, a = image.getpixel(position)
            img.putpixel(temp, (r, g, b, a))

    return img


def tianse(image, img, i, j, i1, j1):
    temp = (i1, j1)
    position = (i, j)
    r, g, b, a = image.getpixel(temp)
    img.putpixel(position, (r, g, b, a))


def tian(img, i, j):
    minal = (i, j)
    img.putpixel(minal, (0, 0, 0))


def will(image, angle):
    sinag = math.sin(angle)
    cosag = math.cos(angle)
    w = image.width
    h = image.height

    w1 = -(w - 1) / 2 * cosag + (h - 1) / 2 * sinag
    h1 = (w - 1) / 2 * sinag + (h - 1) / 2 * cosag

    w2 = (w - 1) / 2 * cosag + (h - 1) / 2 * sinag
    h2 = -(w - 1) / 2 * sinag + (h - 1) / 2 * cosag

    w3 = (w - 1) / 2 * cosag - (h - 1) / 2 * sinag
    h3 = -(w - 1) / 2 * sinag - (h - 1) / 2 * cosag

    w4 = -(w - 1) / 2 * cosag - (h - 1) / 2 * sinag
    h4 = (w - 1) / 2 * sinag - (h - 1) / 2 * cosag

    W = max(abs(w3 - w1), (abs(w4 - w2)))
    H = max(abs(h3 - h1), abs(h4 -h2))

    W1 = int(W)
    H1 = int(H)

    f1 = -(W - 1) / 2 * cosag - (H - 1) / 2 * sinag + (w - 1) / 2
    f2 = (W - 1) / 2 * sinag - (H - 1) / 2 * cosag + (h - 1) / 2
    img = Image.new('RGBA', (W1, H1))

    for i in range(W1):
        for j in range(H1):
            i1 = int(-j * sinag + i * cosag + f2)
            j1 = int(j * cosag + i * sinag + f1)

            if (i1 >= 0 and i1 < h and j1 >= 0 and j1 < w):
                tianse(image, img, i, j, i1, j1)
            else:
                tian(img, i, j)
    img.filter(ImageFilter.SMOOTH)

    return img


def main():
    img = Image.open('meir.jpg')
    img = img.convert('RGBA')

    i = crop(img, (20, 20, 50, 60))
    i.save('mcro.png')

    i = flip(img)
    i.save('mflip.png')

    i = flop(img)
    i.save('mflop.png')

    i = rotate(img)
    i.save('rotate.png')

    i = duijiao(img)
    i.save('duijiao.png')

    i = will(img, 0.5)
    i.save('will.png')


if __name__ == '__main__':
    main()
