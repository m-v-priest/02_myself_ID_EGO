
'''
在执行此py文件前, 先把你的dict脱水txt文件, 所有内容先去掉所有换行符, 先变成一个大行,
然后再把每个词头(用と定位)前面, 添加换行符\r\n,
再把一个单词的词头外的其它部分(第一行用な定位)前, 添加换行\r\n,
现在, 就能变成 一个单词, 是词头一行(能作为key), 其它部分是另一行(能作为value),
这样就能好处理到dict中了
'''


import pickle
import os

txt读取的文件名 = '002_处理成dict字典前的文件.txt'

list_key = []
list_value = []
dict柯林斯 = {}


with open(txt读取的文件名, 'r', encoding='utf-8') as f:
    lines = f.readlines() # readlines() 能读取整个文件的所有行，并返回一个字符串列表。
    for line in lines :
        if line.startswith("▸"):
            key = line.strip()
            list_key.append(key)

        if line.startswith("な"):
            value = line.strip()
            list_value.append(value)

#用两个list, 来分别作为key和value, 构造出一个dict
dict柯林斯 = dict(zip(list_key, list_value))


# 下面开始把上面的  dict柯林斯  腌制到硬盘上
txtPath = os.getcwd() + '/003_pickle腌制成的柯林斯.txt'
objFile = open(txtPath, 'wb')  # 注意,必须以wb,二进制模式写入pickle操作

pickle.dump(dict柯林斯, objFile)  # 将 dict数据,腌制到objFile文件中
objFile.close()  # 注意,dump后必须先关闭文件句柄.这句一定要写!






