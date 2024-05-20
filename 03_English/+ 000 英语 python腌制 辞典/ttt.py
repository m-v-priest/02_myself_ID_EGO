

# 读取腌制

import pickle
import os

txtPath = os.getcwd() + '/+腌制 金山 有道 合体版 柯林斯 dict.txt'
objFile = open(txtPath, 'rb')
# 因为pickle时是用的二进制模式,所以读取时也要rb二进制模式来读取


data = pickle.load(objFile)  # 从文件对象中,读取腌制的数据
print(data["substitute"])  # {1: 'usa', 2: 'china', 3: 'jp'}

for i in data["substitute"]:
    print(i)

