
# 将硬盘上的 柯林斯腌制文件, 读取到python中

import pickle
import os

txtPath = os.getcwd() + '/003_pickle腌制成的柯林斯.txt'
objFile = open(txtPath, 'rb')
# 因为pickle时是用的二进制模式,所以读取时也要rb二进制模式来读取


dict柯林斯 = pickle.load(objFile)  # 从文件对象中,读取腌制的数据
# print(dict柯林斯["▸ go と"])

