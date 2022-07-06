from PIL import Image, ImageFilter
import math, cmath

from img_utils import deal


def maximage(img1, img2):
    w = img1.width
    h = img1.height
    maximage = Image.new('RGBA', (w, h))

    for i in range(w):
        for j in range(h):
            position = (i, j)
            r, g, b, a = img1.getpixel(position)
            x, y, z, o = img2.getpixel(position)
            r1 = max(r, x)
            g1 = max(g, y)
            b1 = max(b, z)
            maximage.putpixel(position, (r1, g1, b1))

    return maximage


def minimage(img1, img2):
    w = img1.width
    h = img1.height
    minimage = Image.new('RGBA', (w, h))

    for i in range(w):
        for j in range(h):
            position = (i, j)
            r, g, b, a = img1.getpixel(position)
            x, y, z, o = img2.getpixel(position)
            r2 = min(r, x)
            g2 = min(g, y)
            b2 = min(b, z)

            minimage.putpixel(position, (r2, g2, b2))
    return minimage


def multiply(img1, img2):
    w = img1.width
    h = img1.height
    mutlimage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            r, g, b, a = img1.getpixel(position)
            x, y, z, o = img2.getpixel(position)
            cr = int(r * x / 255)
            cg = int(g * y / 255)
            cb = int(b * z / 255)
            mutlimage.putpixel(position, (cr, cg, cb))
    return mutlimage


def colour_filter(img1, img2):
    w = img1.width
    h = img1.height
    maxc = 255
    lvseimage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            r, g, b, a = img1.getpixel(position)
            x, y, z, o = img2.getpixel(position)
            cr = int(maxc - (maxc - r) * (maxc - x) / maxc)
            cg = int(maxc - (maxc - g) * (maxc - y) / maxc)
            cb = int(maxc - (maxc - b) * (maxc - z) / maxc)
            lvseimage.putpixel(position, (cr, cg, cb))
    return lvseimage


def takle(img1, img2, position):
    r, g, b, a = img1.getpixel(position)
    x, y, z, o = img2.getpixel(position)
    maxc = 255
    # cr = int(r - (maxc - r) * (maxc - x) / x)
    # cg = int(g - (maxc - g) * (maxc - y) / y)
    # cb = int(b - (maxc - b) * (maxc - z) / z)

    if x == 0:
        cr = r
    else:
        cr = int(r - (maxc - r) * (maxc - x) / x)
        if cr <= 0:
            cr = 0

    if y == 0:
        cg = g
    else:
        cg = int(g - (maxc - g) * (maxc - y) / y)
        if cg <= 0:
            cg = 0

    if z == 0:
        cb = b
    else:
        cb = int(b - (maxc - b) * (maxc - z) / z)
        if cb <= 0:
            cb = 0
    return cr, cg, cb


def deepse(img1, img2):
    w = img1.width
    h = img1.height
    deepimage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            ccr, ccg, ccb = takle(img1, img2, position)
            deepimage.putpixel(position, (ccr, ccg, ccb))
    return deepimage


def pross(img1, img2, position):
    r, g, b, a = img1.getpixel(position)
    x, y, z, o = img2.getpixel(position)
    maxc = 255
    # cr = int(r + r * x / (maxc - x))
    # cg = int(g + g * y / (maxc - y))
    # cb = int(b + b * z / (maxc - z))

    if (maxc - x) == 0:
        cr = r
    else:
        cr = int(r + r * x / (maxc - x))

    if (maxc - y) == 0:
        cg = g
    else:
        cg = int(g + g * y / (maxc - y))

    if (maxc - z) == 0:
        cb = b
    else:
        cb = int(b + b * z / (maxc - z))

    return cr, cg, cb


def dodge(img1, img2):
    w = img1.width
    h = img1.height

    dodgeimage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            dr, dg, db = pross(img1, img2, position)
            dodgeimage.putpixel(position, (dr, dg, db))
    return dodgeimage


def puse(img1, img2, position):
    r, g, b, a = img1.getpixel(position)
    x, y, z, o = img2.getpixel(position)
    maxc = 255
    cr = int(r + x - maxc)
    cg = int(g + y - maxc)
    cb = int(b + z - maxc)
    if cr < 0:
        cr = 0
    if cg < 0:
        cg = 0
    if cb < 0:
        cb = 0
    return cr, cg, cb


def xian(img1, img2):
    w = img1.width
    h = img1.height
    xianimage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            dr, dg, db = puse(img1, img2, position)
            xianimage.putpixel(position, (dr, dg, db))
    return xianimage


def boss(img1, img2, position):
    r, g, b, a = img1.getpixel(position)
    x, y, z, o = img2.getpixel(position)
    maxc = 255
    cr = int(r + x)
    cg = int(g + y)
    cb = int(b + z)
    if cr > maxc:
        cr = maxc
    if cg > maxc:
        cg = maxc
    if cb > maxc:
        cb = maxc
    return cr, cg, cb


def xiando(img1, img2):
    w = img1.width
    h = img1.height
    xiandoimage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            dr, dg, db = boss(img1, img2, position)
            xiandoimage.putpixel(position, (dr, dg, db))
    return xiandoimage


def over(img1, img2, position):
    r, g, b, a = img1.getpixel(position)
    x, y, z, o = img2.getpixel(position)
    maxc = 255
    mid = 128
    if r <= mid:
        cr = int(r * x / 128)
    else:
        cr = int(maxc - (maxc - r) * (maxc - x) / mid)

    if g <= mid:
        cg = int(g * y / 128)
    else:
        cg = int(maxc - (maxc - g) * (maxc - y) / mid)

    if b <= mid:
        cb = int(b * z / 128)
    else:
        cb = int(maxc - (maxc - b) * (maxc - z) / mid)
    return cr, cg, cb


def overlay(img1, img2):
    w = img1.width
    h = img1.height
    overimage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            dr, dg, db = over(img1, img2, position)
            overimage.putpixel(position, (dr, dg, db))
    return overimage


def hard(img1, img2, position):
    r, g, b, a = img1.getpixel(position)
    x, y, z, o = img2.getpixel(position)

    maxc = 255
    mid = 128
    if x <= mid:
        cr = int(r * x / 128)
    else:
        cr = int(maxc - (maxc - r) * (maxc - x) / mid)

    if y <= mid:
        cg = int(g * y / 128)
    else:
        cg = int(maxc - (maxc - g) * (maxc - y) / mid)

    if z <= mid:
        cb = int(b * z / 128)
    else:
        cb = int(maxc - (maxc - b) * (maxc - z) / mid)
    return cr, cg, cb


def hardlight(img1, img2):
    w = img1.width
    h = img1.height
    hardimage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            dr, dg, db = hard(img1, img2, position)
            hardimage.putpixel(position, (dr, dg, db))
    return hardimage


def ensoft(r, x):
    maxc = 255
    mid = 128
    if x <= mid:
        c = int(r * x / mid + pow(r / maxc, 2) * (maxc - 2 * x))
    else:
        c = int(r * (maxc - x) / mid + math.sqrt(r / maxc) * (2 * x - 255))
    return c


def soft(img1, img2):
    w = img1.width
    h = img1.height
    softimage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            r, g, b, a = img1.getpixel(position)
            x, y, z, o = img2.getpixel(position)
            cr = ensoft(r, x)
            cg = ensoft(g, y)
            cb = ensoft(b, z)
            softimage.putpixel(position, (cr, cg, cb))
    return softimage


def envivid(r, x):
    maxc = 255
    mid = 128
    if x <= mid:
        if x == 0:
            c = r
        else:
            c = int(r - (maxc - r) * (maxc - 2 * x) / (2 * x))
    else:
        if (maxc - x) == 0:
            c = r
        else:
            c = int(r + r * (2 * x - maxc) / (2 * (maxc - x)))
    return c


def vivid(img1, img2):
    w = img1.width
    h = img1.height
    vividimage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            r, g, b, a = img1.getpixel(position)
            x, y, z, o = img2.getpixel(position)
            cr = envivid(r, x)
            cg = envivid(g, y)
            cb = envivid(b, z)
            vividimage.putpixel(position, (cr, cg, cb))
    return vividimage


def enlinear(r, x):
    maxc = 255
    cr = x + 2 * r - maxc
    if cr < 0:
        cr = 0
    if cr > maxc:
        cr = maxc
    return cr


def linear(img1, img2):
    w = img1.width
    h = img1.height
    linearimage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            r, g, b, a = img1.getpixel(position)
            x, y, z, o = img2.getpixel(position)
            dr = enlinear(r, x)
            dg = enlinear(g, y)
            db = enlinear(b, z)
            linearimage.putpixel(position, (dr, dg, db))
    return linearimage


def enpin(r, x):
    mid = 128
    if x <= mid:
        cr = int(min(r, 2 * x))
    else:
        cr = int(max(r, 2 * x - 255))
    return cr


def pinlight(img1, img2):
    w = img1.width
    h = img1.height
    pinimage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            r, g, b, a = img1.getpixel(position)
            x, y, z, o = img2.getpixel(position)
            dr = enpin(r, x)
            dg = enpin(g, y)
            db = enpin(b, z)
            pinimage.putpixel(position, (dr, dg, db))
    return pinimage


def enhardmix(r, x):
    ccr = r + x
    if ccr > 255:
        cr = 255
    else:
        cr = 0
    return cr


def hardmix(img1, img2):
    w = img1.width
    h = img1.height
    hmiximage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            r, g, b, a = img1.getpixel(position)
            x, y, z, o = img2.getpixel(position)
            dr = enhardmix(r, x)
            dg = enhardmix(g, y)
            db = enhardmix(b, z)
            hmiximage.putpixel(position, (dr, dg, db))
    return hmiximage


def endiffer(x, r):
    cr = abs(x - r)
    return cr


def difference(img1, img2):
    w = img1.width
    h = img1.height
    differimage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            r, g, b, a = img1.getpixel(position)
            x, y, z, o = img2.getpixel(position)
            dr = endiffer(r, x)
            dg = endiffer(g, y)
            db = endiffer(b, z)
            differimage.putpixel(position, (dr, dg, db))
    return differimage


def enexclusion(r, x):
    cr = (x + r) - r * x / 128
    return cr


def exclusion(img1, img2):
    w = img1.width
    h = img1.height
    exclusioimage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            r, g, b, a = img1.getpixel(position)
            x, y, z, o = img2.getpixel(position)
            dr = enexclusion(r, x)
            dg = enexclusion(g, y)
            db = enexclusion(b, z)
            exclusioimage.putpixel(position, (dr, dg, db))
    return exclusioimage


def ensubstract(x, r):
    cr = x - r
    if cr < 0:
        cr = 0
    return cr


def subtract(img1, img2):
    w = img1.width
    h = img1.height
    subtractimage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            r, g, b, a = img1.getpixel(position)
            x, y, z, o = img2.getpixel(position)
            dr = ensubstract(r, x)
            dg = ensubstract(g, y)
            db = ensubstract(b, z)
            subtractimage.putpixel(position, (dr, dg, db))
    return subtractimage


def endivide(r, x):
    cr = x + r
    return cr


def divide(img1, img2):
    w = img1.width
    h = img1.height
    divideimage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            r, g, b, a = img1.getpixel(position)
            x, y, z, o = img2.getpixel(position)
            dr = endivide(r, x)
            dg = endivide(g, y)
            db = endivide(b, z)
            divideimage.putpixel(position, (dr, dg, db))
    return divideimage


def generate_img(func, img_name):
    img1 = deal("manhua.png")
    img2 = deal("ren.png")
    i = func(img1, img2)
    i.save("target-file/Image-overlap-fusion/" + img_name)


def main():
    generate_img(maximage, "max.png")
    generate_img(minimage, "min.png")
    generate_img(multiply, "mutltiply.png")
    generate_img(colour_filter, "colour_filter.png")
    generate_img(deepse, "deep.png")
    generate_img(dodge, "dodge.png")
    generate_img(xian, "xian.png")
    generate_img(xiando, "xiando.png")
    generate_img(overlay, "overlay.png")
    generate_img(hardlight, "hardlight.png")
    generate_img(soft, "soft.png")
    generate_img(vivid, "vivid.png")
    generate_img(linear, "linear.png")
    generate_img(pinlight, "pinlight.png")
    generate_img(hardmix, "hardmix.png")
    generate_img(difference, "difference.png")
    generate_img(exclusion, "exclusion.png")
    generate_img(subtract, "subtract.png")
    generate_img(divide, "divide.png")


if __name__ == '__main__':
    main()
