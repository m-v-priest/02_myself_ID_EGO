
# 将硬盘上的 柯林斯腌制文件, 读取到python中

import pickle
import os
import random


# 第1步: 读取柯林斯腌制文件
txtPath = os.getcwd() + '/003_pickle腌制成的柯林斯.txt'
objFile = open(txtPath, 'rb')
# 因为pickle时是用的二进制模式,所以读取时也要rb二进制模式来读取


dict柯林斯 = pickle.load(objFile)  # 从文件对象中,读取腌制的数据
# print(dict柯林斯["▸ congress と"])


# 第2步: 读取词汇表txt文件, 并查找柯林斯中的相应的内容, 存入一个新的dict_柯林斯版托福 中.
txt读取的文件名 = '词汇表_新东方托福.txt'
txt要写入的文件名 = '柯林斯版_新东方托福.txt'
dict_柯林斯版托福 = {}

with open(txt读取的文件名, 'r', encoding='utf-8') as f:
    listLines = f.readlines()
    random.shuffle(listLines) # 将list中的元素排列顺序, 先乱序化. 就是把单词表中的单词不要顺序排列, 乱序排列
    for i in listLines:
        i单词词头 = i.strip()
        res是否找到 =  dict柯林斯.get("▸ {} と".format(i单词词头),"辞典中没找到") # 先在柯林斯dict中, 查找该词头, 是否存在, 如果存在则返回该value; 如果不存在则返回 "辞典中没找到" 这个字符串提示.
        if res是否找到 != "辞典中没找到" :
            dict_柯林斯版托福[i单词词头]=res是否找到
        else :
            dict_柯林斯版托福[i单词词头]= "辞典中没找到"

        # print(i单词词头)



# print(len(dict_柯林斯版托福))
# print(dict_柯林斯版托福["go"])
#
# for k,v in dict_柯林斯版托福.items(): # 遍历字典, 打印出每一项item的 key和value
#     print ("{} --> {}".format(k,v))
#     print ("----------------")


# 第3步: 再把 dict_柯林斯版托福 中的内容, 存入一个新txt中.
count = 1

with open(txt要写入的文件名, 'w',encoding='utf-8') as file:
    for k,v in dict_柯林斯版托福.items():
        file.write("▸ {}  [{}] \r\n {}".format(k, count,v))
        file.write("\r\n")
        count += 1


