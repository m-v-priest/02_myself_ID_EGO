import pickle

old_地址 = r'F:\剑桥导excel表格 7段分列\导入欧路词典的 单词表\all 精选 v.txt'
new_地址 = r'F:\+ 英英 柯林斯\考研 v.txt'

腌制地址_英英柯林斯 = r'F:\+ 英英 柯林斯\+ 腌制_英英柯林斯.txt'


old_对象 = open(old_地址,'r',encoding='utf-8')
new_对象 = open(new_地址,'w+',encoding='utf-8')

对象_读取腌制柯林斯 = open(腌制地址_英英柯林斯,'rb')

all_dict柯林斯 = pickle.load(对象_读取腌制柯林斯)

# -----------------------------------
def 函数_返回释义和例句(k,dict):
    if k in dict:
        v =  dict[k]
        return v
    else:
        v = ''
        return v

# ------------------------------
def 函数_打印列表到文件中(list,new_file):
    for item in list:
        new_file.write(item)
    new_file.write('_'*30+'\n\n')


# ----------------------------------
for line in old_对象:
    词头 = line.strip()
    v = 函数_返回释义和例句(词头,all_dict柯林斯)
    函数_打印列表到文件中(v,new_对象)





