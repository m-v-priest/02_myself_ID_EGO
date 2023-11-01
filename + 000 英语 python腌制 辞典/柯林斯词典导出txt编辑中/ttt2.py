
import re

txt读取的文件名 = '新文件 26.txt.adoc'

re正则_词头 = 'う(.+?)え'
re正则_词性 = 'く(.+?)け'


#读取文件
with open(txt读取的文件名, 'r', encoding='utf-8') as f:
    lines = f.readlines() # readlines() 能读取整个文件的所有行，并返回一个字符串列表。
    for line in lines:
        #print(line.strip())
        try :
            txt词头 = re.search(re正则_词头, line).group(1)
            print(txt词头)
        except :
            pass

        #####################

        try :
            txt词性 = re.search(re正则_词性, line).group(1)
            print(txt词性)
        except :
            pass

        #####################




        # if re.search( re正则_词头,line).group() :
        #     txt词头 = re.search( re正则_词头, line).group(1)
        #     print(txt词头)
        # else:
        #     print("没查找到词头")


