

'''
字符串的zfill()方法, 可以用来给字符串前面补0
如:
n = "123"
s = n.zfill(5)
assert s == "00123"
'''

str1 = "image:../../03_readBook/img_readBook/img_miRNA/miRNA_"
str2 =".jpg[]"

for i in range(60):
    str3 = str1 + str(i).zfill(2) + str2
    print(str3)
    print('\r\n')

