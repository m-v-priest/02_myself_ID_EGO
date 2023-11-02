


txt读取的文件名 = '柯林斯净化中 step2.txt'

dict柯林斯 = {}

with open(txt读取的文件名, 'r', encoding='utf-8') as f:
    lines = f.readlines() # readlines() 能读取整个文件的所有行，并返回一个字符串列表。
    for line in lines :
        if line.startswith("▸"):
            key = line.strip()
            dict柯林斯[key]
        else:
            list_value = []




