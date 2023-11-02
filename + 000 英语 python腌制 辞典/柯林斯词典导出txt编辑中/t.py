


txt读取的文件名 = '脱水后的柯林斯内容txt文件.txt'
txt写入的文件名 = '写入.txt'

listLines = []

with open(txt读取的文件名, 'r', encoding='utf-8') as f:
    listLines = f.readlines() # readlines() 能读取整个文件的所有行，并返回一个字符串列表。


with open(txt写入的文件名, 'w', encoding='utf-8') as file:
    for i in listLines:
        newI = i.strip()
        file.write(newI)



