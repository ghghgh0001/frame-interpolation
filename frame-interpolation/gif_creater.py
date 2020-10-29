import os
import imageio


def create_gif(image_list, gif_name):
    frames = []
    for image_name in image_list:
        if image_name.endswith('.png'):
            print(image_name)
            frames.append(imageio.imread(image_name))
    # Save them as frames into a gif
    imageio.mimsave(gif_name, frames, 'GIF', duration=0.4)

    return


def main():
    path = r'C:\Users\hp\PycharmProjects\pythonProject\dataset\radar_1_30_2/'  # 存放PNG图片文件夹位置
    files = os.listdir(path)
    # files.sort()
    # files.sort(key=lambda x: int(x[:-4]))

    image_list = [path + img for img in files]
    gif_name = 'curve_gif_30_crop_0.4s.gif'  # 生成gif的名称
    create_gif(image_list, gif_name)


if __name__ == "__main__":
    main()