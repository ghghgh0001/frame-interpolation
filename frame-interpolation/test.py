# coding: utf-8
from PIL import Image
import matplotlib.pyplot as plt
import os
import os.path
import numpy as np

img = Image.open(r'C:\Users\hp\PycharmProjects\pythonProject\dataset\radar_1_30\00001.png')
print(img.format, img.size, img.mode)
# plt.figure("1")
# plt.imshow(img)
# plt.show()
box1 = (500, 400, 900, 800)  # 设置左、上、右、下的像素
image1 = img.crop(box1)  # 图像裁剪
plt.figure("2")
plt.axis('off')
plt.imshow(image1)
plt.show()