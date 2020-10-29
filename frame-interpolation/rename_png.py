# --** coding="UTF-8" **--

import os
import re
import sys

fileList = os.listdir(r"C:\Users\hp\PycharmProjects\pythonProject\dataset\radar")
print("start...")
# 得到进程当前工作目录
currentpath = os.getcwd()
# 将当前工作目录修改为待修改文件夹的位置
os.chdir(r"C:\Users\hp\PycharmProjects\pythonProject\dataset\radar")
#名称变量
num = 1
# 遍历文件夹中所有文件
for fileName in fileList:
    # 文件重新命名
    s = '%05d' % num
    os.rename(fileName, (str(s) + '.png'))
    # 改变编号，继续下一项
    num = num + 1
print("end...")
# 改回程序运行前的工作目录
os.chdir(currentpath)
# 刷新
sys.stdin.flush()
