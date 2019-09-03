from PIL import Image, ImageFilter
import math, cmath


def mutltiply(img1, img2):
    w = img1.width
    h = img1.height
    mutlimage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            r, g, b, a = img1.getpixel(position)
            x, y, z, o = img2.getpixel(position)
            r = r / 255
            g = g / 255
            b = b / 255
            x = x / 255
            y = y / 255
            z = z / 255
            cr = int(r * x * 255)
            cg = int(g * y * 255)
            cb = int(b * z * 255)
            mutlimage.putpixel(position, (cr, cg, cb))
    return mutlimage


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


def lvse(img1, img2):
    w = img1.width
    h = img1.height
    lvseimage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            r, g, b, a = img1.getpixel(position)
            x, y, z, o = img2.getpixel(position)
            r = r / 255
            g = g / 255
            b = b / 255
            x = x / 255
            y = y / 255
            z = z / 255
            cr = int((1 - (1 - r) * (1 - x)) * 255)
            cg = int((1 - (1 - g) * (1 - y)) * 255)
            cb = int((1 - (1 - b) * (1 - z)) * 255)
            print(cr, cg, cb)
            lvseimage.putpixel(position, (cr, cg, cb))
    return lvseimage


def takle(img1, img2, position):
    r, g, b, a = img1.getpixel(position)
    x, y, z, o = img2.getpixel(position)
    r = r / 255
    g = g / 255
    b = b / 255
    x = x / 255
    y = y / 255
    z = z / 255
    if x == 0:
        cr = 1
    else:
        cr = 1 - (1 - r) / x
        if cr <= 0:
            cr = 0

    if y == 0:
        cg = 1
    else:
        cg = 1 - (1 - g) / y
        if cg <= 0:
            cg = 0

    if z == 0:
        cb = 1
    else:
        cb = 1 - (1 - b) / z
        if cb <= 0:
            cb = 0
    ccr = int(cr * 255)
    ccg = int(cg * 255)
    ccb = int(cb * 255)
    return ccr, ccg, ccb


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
    r = r / 255
    g = g / 255
    b = b / 255
    x = x / 255
    y = y / 255
    z = z / 255
    if (1 - r) == 0:
        cr = 0
    else:
        cr = x / (1 - r)

    if (1 - g) == 0:
        cg = 0
    else:
        cg = y / (1 - g)

    if (1 - b) == 0:
        cb = 0
    else:
        cb = z / (1 - b)

    ccr = int(cr * 255)
    ccg = int(cg * 255)
    ccb = int(cb * 255)
    return ccr, ccg, ccb


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
    r = r / 255
    g = g / 255
    b = b / 255
    x = x / 255
    y = y / 255
    z = z / 255
    cr = r + x - 1
    cg = g + y - 1
    cb = b + z - 1
    if cr < 0:
        cr = 0
    if cg < 0:
        cg = 0
    if cb < 0:
        cb = 0

    ccr = int(cr * 255)
    ccg = int(cg * 255)
    ccb = int(cb * 255)
    return ccr, ccg, ccb


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
    r = r / 255
    g = g / 255
    b = b / 255
    x = x / 255
    y = y / 255
    z = z / 255
    cr = r + x
    cg = g + y
    cb = b + z
    if cr > 1:
        cr = 1
    if cg > 1:
        cg = 1
    if cb > 1:
        cb = 1

    ccr = int(cr * 255)
    ccg = int(cg * 255)
    ccb = int(cb * 255)
    return ccr, ccg, ccb


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
    r = r / 255
    g = g / 255
    b = b / 255
    x = x / 255
    y = y / 255
    z = z / 255

    if x <= 0.5:
        cr = 2 * r * x
    else:
        cr = 1 - 2 * (1 - r) * (1 - x)

    if y <= 0.5:
        cg = 2 * g * y
    else:
        cg = 1 - (1 - g) * (1 - y)

    if z <= 0.5:
        cb = 2 * b * z
    else:
        cb = 1 - (1 - b) * (1 - z)

    ccr = int(cr * 255)
    ccg = int(cg * 255)
    ccb = int(cb * 255)
    return ccr, ccg, ccb


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
    r = r / 255
    g = g / 255
    b = b / 255
    x = x / 255
    y = y / 255
    z = z / 255

    if r <= 0.5:
        cr = 2 * r * x
    else:
        cr = 1 - 2 * (1 - r) * (1 - x)

    if g <= 0.5:
        cg = 2 * g * y
    else:
        cg = 1 - (1 - g) * (1 - y)

    if b <= 0.5:
        cb = 2 * b * z
    else:
        cb = 1 - (1 - b) * (1 - z)

    ccr = int(cr * 255)
    ccg = int(cg * 255)
    ccb = int(cb * 255)
    return ccr, ccg, ccb


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


def ensoft(img1, img2, position):
    r, g, b, a = img1.getpixel(position)
    x, y, z, o = img2.getpixel(position)
    r = r / 255
    g = g / 255
    b = b / 255
    x = x / 255
    y = y / 255
    z = z / 255

    if r <= 0.5:
        cr = 2 * r * x + x * x * (1 - 2 * r)
    else:
        cr = 2 * x * (1 - r) + math.sqrt(x) * (2 * r - 1)

    if g <= 0.5:
        cg = 2 * g * y + y * y * (1 - 2 * g)
    else:
        cg = 2 * y * (1 - g) + math.sqrt(y) * (2 * g - 1)

    if b <= 0.5:
        cb = 2 * b * z + z * z * (1 - 2 * b)
    else:
        cb = 2 * z * (1 - b) + math.sqrt(z) * (2 * b - 1)

    ccr = int(cr * 255)
    ccg = int(cg * 255)
    ccb = int(cb * 255)
    return ccr, ccg, ccb


def soft(img1, img2):
    w = img1.width
    h = img1.height
    softimage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            dr, dg, db = ensoft(img1, img2, position)
            softimage.putpixel(position, (dr, dg, db))
    return softimage


def envivid(img1, img2, position):
    r, g, b, a = img1.getpixel(position)
    x, y, z, o = img2.getpixel(position)
    r = r / 255
    g = g / 255
    b = b / 255
    x = x / 255
    y = y / 255
    z = z / 255

    if r <= 0.5:
        if r == 0:
            cr = 1
        else:
            cr = 1 + (x - 1) / (2 * r)
            if cr < 0:
                cr = 0
            if cr > 1:
                cr = 1
                # print('cr', cr)
    else:
        if (1 - r) == 0:
            cr = 0
        else:
            cr = x / (2 * (1 - r))
            if cr < 0:
                cr = 0
            if cr > 1:
                cr = 1
                # print('cr', cr)

    if g <= 0.5:
        if g == 0:
            cg = 1
        else:
            cg = 1 + (y - 1) / (2 * g)
            if cg < 0:
                cg = 0
            if cg > 1:
                cg = 1
                # print('cg', cg)
    else:
        if (1 - g) == 0:
            cg = 0
        else:
            cg = y / (2 * (1 - g))
            if cg < 0:
                cg = 0
            if cg > 1:
                cg = 1
                # print('cg', cg)

    if b <= 0.5:
        if b == 0:
            cb = 1
        else:
            cb = 1 + (z - 1) / (2 * b)
            if cb < 0:
                cb = 0
            if cb > 1:
                cb = 1
                # print('cb', cb)

    else:
        if (1 - b) == 0:
            cb = 0
        else:
            cb = z / (2 * (1 - b))
            if cb < 0:
                cb = 0
            if cb > 1:
                cb = 1
                # print('cb', cb)

    ccr = int(cr * 255)
    ccg = int(cg * 255)
    ccb = int(cb * 255)
    return ccr, ccg, ccb


def vivid(img1, img2):
    w = img1.width
    h = img1.height
    vividimage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            dr, dg, db = envivid(img1, img2, position)
            vividimage.putpixel(position, (dr, dg, db))
    return vividimage


def enlinear(img1, img2, position):
    r, g, b, a = img1.getpixel(position)
    x, y, z, o = img2.getpixel(position)
    r = r / 255
    g = g / 255
    b = b / 255
    x = x / 255
    y = y / 255
    z = z / 255
    cr = x + 2 * r - 1
    cg = y + 2 * g - 1
    cb = z + 2 * b - 1

    if cr < 0:
        cr = 0
    if cr > 1:
        cr = 1

    if cg < 0:
        cg = 0
    if cg > 1:
        cg = 1

    if cb < 0:
        cb = 0
    if cb > 1:
        cb = 1

    ccr = int(cr * 255)
    ccg = int(cg * 255)
    ccb = int(cb * 255)
    return ccr, ccg, ccb


def linear(img1, img2):
    w = img1.width
    h = img1.height
    linearimage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            dr, dg, db = enlinear(img1, img2, position)
            linearimage.putpixel(position, (dr, dg, db))
    return linearimage


def enpin(img1, img2, position):
    r, g, b, a = img1.getpixel(position)
    x, y, z, o = img2.getpixel(position)
    r = r / 255
    g = g / 255
    b = b / 255
    x = x / 255
    y = y / 255
    z = z / 255
    cr = x + 2 * r - 1
    cg = y + 2 * g - 1
    cb = z + 2 * b - 1

    if r > 0.5:
        cr = max(2 * (r - 0.5), x)
    else:
        cr = min(2 * r, x)

    if g < 0.5:
        cg = max(2 * (g - 0.5), y)
    else:
        cg = min(2 * g, y)

    if b < 0.5:
        cb = max(2 * (b - 0.5), z)
    else:
        cb = min(2 * b, z)

    ccr = int(cr * 255)
    ccg = int(cg * 255)
    ccb = int(cb * 255)
    return ccr, ccg, ccb


def pinlight(img1, img2):
    w = img1.width
    h = img1.height
    pinimage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            dr, dg, db = enpin(img1, img2, position)
            pinimage.putpixel(position, (dr, dg, db))
    return pinimage


def enhardmix(img1, img2, position):
    r, g, b, a = img1.getpixel(position)
    x, y, z, o = img2.getpixel(position)
    r = r / 255
    g = g / 255
    b = b / 255
    x = x / 255
    y = y / 255
    z = z / 255
    ccr = r + x
    ccg = g + y
    ccb = b + z
    if ccr > 1:
        cr = 1
    else:
        cr = 0
    if ccg > 1:
        cg = 1
    else:
        cg = 0

    if ccb > 1:
        cb = 1
    else:
        cb = 0

    hr = int(cr * 255)
    hg = int(cg * 255)
    hb = int(cb * 255)
    return hr, hg, hb


def hardmix(img1, img2):
    w = img1.width
    h = img1.height
    hmiximage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            dr, dg, db = enhardmix(img1, img2, position)
            hmiximage.putpixel(position, (dr, dg, db))
    return hmiximage


def endiffer(img1, img2, position):
    r, g, b, a = img1.getpixel(position)
    x, y, z, o = img2.getpixel(position)
    r = r / 255
    g = g / 255
    b = b / 255
    x = x / 255
    y = y / 255
    z = z / 255
    cr = abs(x - r)
    cg = abs(y - g)
    cb = abs(z - b)

    hr = int(cr * 255)
    hg = int(cg * 255)
    hb = int(cb * 255)
    return hr, hg, hb


def difference(img1, img2):
    w = img1.width
    h = img1.height
    differimage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            dr, dg, db = endiffer(img1, img2, position)
            differimage.putpixel(position, (dr, dg, db))
    return differimage


def enexclusion(img1, img2, position):
    r, g, b, a = img1.getpixel(position)
    x, y, z, o = img2.getpixel(position)
    r = r / 255
    g = g / 255
    b = b / 255
    x = x / 255
    y = y / 255
    z = z / 255
    cr = (x + r) - 2 * r * x
    cg = (y + g) - 2 * g * y
    cb = (z + b) - 2 * b * z

    hr = int(cr * 255)
    hg = int(cg * 255)
    hb = int(cb * 255)
    return hr, hg, hb


def exclusion(img1, img2):
    w = img1.width
    h = img1.height
    exclusioimage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            dr, dg, db = enexclusion(img1, img2, position)
            exclusioimage.putpixel(position, (dr, dg, db))
    return exclusioimage


def ensubstract(img1, img2, position):
    r, g, b, a = img1.getpixel(position)
    x, y, z, o = img2.getpixel(position)
    r = r / 255
    g = g / 255
    b = b / 255
    x = x / 255
    y = y / 255
    z = z / 255
    cr = x - r
    cg = y - g
    cb = z - b

    if cr < 0:
        cr = 0
    if cg < 0:
        cg = 0
    if cb < 0:
        cb = 0
    hr = int(cr * 255)
    hg = int(cg * 255)
    hb = int(cb * 255)
    return hr, hg, hb


def subtract(img1, img2):
    w = img1.width
    h = img1.height
    subtractimage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            dr, dg, db = ensubstract(img1, img2, position)
            subtractimage.putpixel(position, (dr, dg, db))
    return subtractimage


def endivide(img1, img2, position):
    r, g, b, a = img1.getpixel(position)
    x, y, z, o = img2.getpixel(position)
    r = r / 255
    g = g / 255
    b = b / 255
    x = x / 255
    y = y / 255
    z = z / 255
    if r == 0:
        cr = 0
    else:
        cr = x / r
    if g == 0:
        cg = 0
    else:
        cg = y / g
    if b == 0:
        cb = 0
    else:
        cb = z / b

    hr = int(cr * 255)
    hg = int(cg * 255)
    hb = int(cb * 255)
    return hr, hg, hb


def divide(img1, img2):
    w = img1.width
    h = img1.height
    divideimage = Image.new('RGBA', (w, h))
    for i in range(w):
        for j in range(h):
            position = (i, j)
            dr, dg, db = endivide(img1, img2, position)
            divideimage.putpixel(position, (dr, dg, db))
    return divideimage


def main():
    img1 = Image.open("manhua.png")
    img1 = img1.convert('RGBA')

    img2 = Image.open("ren.png")
    img2 = img2.convert('RGBA')

    i = maximage(img1, img2)
    i.save('max.png')

    i = minimage(img1, img2)
    i.save('min.png')

    i = mutltiply(img1, img2)
    i.save('multimage.png')

    i = lvse(img1, img2)
    i.save('lvseimage.png')

    i = deepse(img1, img2)
    i.save('deep.png')

    i = dodge(img1, img2)
    i.save('dodge.png')

    i = xian(img1, img2)
    i.save('xian.png')

    i = xiando(img1, img2)
    i.save('xido.png')

    i = overlay(img1, img2)
    i.save('overlay.png')

    i = hardlight(img1, img2)
    i.save('hard.png')

    i = soft(img1, img2)
    i.save('soft.png')

    i = vivid(img1, img2)
    i.save('vivid.png')

    i = linear(img1, img2)
    i.save('linear.png')

    i = pinlight(img1, img2)
    i.save('pin.png')

    i = hardmix(img1, img2)
    i.save('hardmix.png')

    i = difference(img1, img2)
    i.save('differ.png')

    i = exclusion(img1, img2)
    i.save('exclusion.png')

    i = subtract(img1, img2)
    i.save('subtract.png')

    divideimg = divide(img1, img2)
    divideimg.save('divide.png')


if __name__ == '__main__':
    main()
