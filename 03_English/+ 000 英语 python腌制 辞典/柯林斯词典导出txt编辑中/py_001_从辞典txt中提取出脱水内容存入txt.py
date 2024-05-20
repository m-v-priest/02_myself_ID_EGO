
import re

# txt读取的文件名 = '新文件 26.txt - setp2.txt'
txt读取的文件名 = '柯林斯净化中 step2.txt'

re正则_词头 = r'う(.+?)え'
re正则_音标 = r'か(.+?)き'
re正则_词性 = r'く(.+?)け'
re正则_释义 = r'す(.+?)せ'
re正则_例句 = r'さ(.+?)し'

txt词头 = ""
txt音标 = ""
txt词性 = ""
txt释义 = ""
txt例句 = ""

list_从原始字典中提取出的脱水内容 = []



count = 0

#第一步: 读取词典txt文件, 将里面的词头,词性等内容脱水出来(即取html标签), 然后存入一个list中.
with open(txt读取的文件名, 'r', encoding='utf-8') as f:
    lines = f.readlines() # readlines() 能读取整个文件的所有行，并返回一个字符串列表。
    for line in lines:
        #print(line.strip())
        try :
            txt词头 = re.search(re正则_词头, line).group(1) # 注意: 用组来匹配时, 索引必须用1, 而不是0. 因为group(0)会把你正则要查找的所有内容都显示出来, 而非只组中的内容.
            list_从原始字典中提取出的脱水内容.append("▸ " + txt词头)
            # print("\r\n --- \r\n")
            # print(txt词头)
            count +=1
            print(count)
        except :
            pass

        #####################

        try :
            txt音标 = re.search(re正则_音标, line).group(1)
            list_从原始字典中提取出的脱水内容.append(txt音标)
            # print(txt音标)
        except :
            pass

        #####################

        try :
            txt词性 = re.search(re正则_词性, line).group(1)
            #print(txt词性)
        except :
            pass

        #####################

        try :
            txt释义 = re.search(re正则_释义, line).group(1)
            list_从原始字典中提取出的脱水内容.append("{0} {1}".format(txt词性, txt释义))
            # print("{0} {1}".format(txt词性, txt释义))
        except :
            pass

        #####################


        try :
            txt例句 = re.search(re正则_例句, line).group(1)
            list_从原始字典中提取出的脱水内容.append("⇒ " +txt例句)
            # print(txt例句)
        except :
            pass

        #####################



#第二步: 将存放在list中的字典脱水内容, 写入一个新文件中
with open('脱水后的柯林斯内容txt文件.txt', 'w',encoding='utf-8') as file:
    for i in list_从原始字典中提取出的脱水内容:
        file.write(i)
        file.write("\r\n")


