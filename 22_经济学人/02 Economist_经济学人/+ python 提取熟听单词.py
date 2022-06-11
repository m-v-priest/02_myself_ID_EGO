import re

urlTxt = r'd:\ttt.txt'  # ttt.txt就是你要读取的文章. 你会对该文章进行正则提取
rePattern = '\(`=(.*?):'

# 用正则来查找, 输入txt行, 返回该行中的所有匹配内容, 返回一个list


def fn_reFindAll(line):
    listRes = re.findall(rePattern, line)
    # 只有在list中含有匹配到的内容时, 才返回. 即, 如果list为空,该list就没用了, 不需要返回它.
    if len(listRes) != 0:
        return listRes

# 将含有所有匹配内容的大列表, 打印成adoc中的表格格式


def fn_printTable(listOk):
    print("|=== \r\n|word |description")
    for i in listOk:
        print('|{}|'.format(i))  # print()会自动输入换行符, 所以不需要你再手动添加换行符了!
    print("|===")


# 读取文件, 并调用你自定义的正则函数来查找
with open(urlTxt, 'r', encoding='utf-8') as fRead:
    listOk = []  # 把每一行中匹配到的内容, 统一放到这个大列表中集中.
    for line in fRead:
        listRes = fn_reFindAll(line)
        if listRes != None:
            for i in listRes:
                if i != ' ' and i != '':  # 去除掉内容是"空"的元素
                    i = i.strip()
                    listOk.append(i)
    # print(listOk)
    fn_printTable(listOk)
