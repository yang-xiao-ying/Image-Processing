from PIL import Image


def dynamic():
    image_list = []
    # 图片命名的时候，采用 数字.png ,方便str(i + 1)取
    for i in range(6):
        path = 'C:\\Users\\Administrator\\Desktop\\trend\\{}.png'.format(i + 1)
        img = Image.open(path)
        image_list.append(img)

    list_path = 'C:\\Users\\Administrator\\Desktop\\trend\\dynamic.gif'
    # duration 指的是动图每两张之间的时间间隔，其他的设置我是照抄的
    img.save(list_path, save_all=True, append_images=image_list, duration=1000)


def main():
    dynamic()


if __name__ == '__main__':
    main()
