from PIL import Image


def dynamic():
    image_list = []
    for i in range(11):
        img_path = 'originalImg/dynamic/{}.png'.format(i)
        img = Image.open(img_path)
        image_list.append(img)

    path = "target-file/dynamic.gif"
    img.save(path, save_all=True, append_images=image_list, duration=1000)


def main():
    dynamic()


if __name__ == '__main__':
    main()
