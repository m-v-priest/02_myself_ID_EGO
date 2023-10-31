import pickle

old_地址 = r'F:\+++ En-En-Merriam-Websters Advanced Learners English Dictionary\++ 韦氏\单词表\all gre n.txt'  # 生词表
new_地址 = r'F:\+++ En-En-Merriam-Websters Advanced Learners English Dictionary\++ 韦氏\单词表\韦氏版 gre n.txt'


腌制地址_英英韦氏 = r'F:\+++ En-En-Merriam-Websters Advanced Learners English Dictionary\++ 韦氏\+ 腌制_韦氏全.txt'


old_对象 = open(old_地址,'r',encoding='utf-8')
new_对象 = open(new_地址,'w+',encoding='utf-8')

对象_读取腌制韦氏 = open(腌制地址_英英韦氏,'rb')

all_dict韦氏 = pickle.load(对象_读取腌制韦氏)

# -----------------------------------
def 函数_返回释义和例句(k,dict):  # 从腌制大辞典中,抽取出考研等单词表的生词块
    if k in dict:
        # print(k)
        v =  dict[k]
        return v
    else:
        print(k)
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
    # print(词头)
    v = 函数_返回释义和例句(词头,all_dict韦氏)
    函数_打印列表到文件中(v,new_对象)





