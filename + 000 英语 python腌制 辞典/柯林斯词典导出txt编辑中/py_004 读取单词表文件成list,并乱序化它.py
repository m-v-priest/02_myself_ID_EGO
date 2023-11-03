
import random

# txt读取的文件名 = '脱水后的柯林斯内容txt文件.txt'
# txt写入的文件名 = '写入.txt'
#
# listLines = []
#
# with open(txt读取的文件名, 'r', encoding='utf-8') as f:
#     listLines = f.readlines() # readlines() 能读取整个文件的所有行，并返回一个字符串列表。
#
#
# with open(txt写入的文件名, 'w', encoding='utf-8') as file:
#     for i in listLines:
#         newI = i.strip()
#         file.write(newI)


txt读取的文件名 = '词汇表_新东方托福.txt'


with open(txt读取的文件名, 'r', encoding='utf-8') as f:
    listLines = f.readlines()
    random.shuffle(listLines) # 将list中的元素排列顺序, 先乱序化. 就是把单词表中的单词不要顺序排列, 乱序排列
    for i in listLines:
        i = i.strip() # 取出每行头尾的空白字符
        print(i)
