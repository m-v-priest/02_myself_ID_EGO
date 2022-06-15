from fractions import Fraction # 要让numpy输出分数形式, 要载入该模块. Fraction类具有一个内置方法limit_denominator(), 能将小数, 转换为分数显示
import numpy as np
import matplotlib.pyplot as plt

# 设置矩阵元素输出用分数表示
np.set_printoptions(formatter={'all':lambda x: str(Fraction(x).limit_denominator())})
'''
set_printoptions() ——控制输出方式
formatter ——通用格式化输出
Fraction(x).limit_denominator(y) ——返回一个分母不大于y且最接近x的分数
'''

a = np.array([[3,2,4],[2,0,2],[4,2,3]])
e_value, e_vec = np.linalg.eig(a) # 该方法获取矩阵的特征值, 和特征向量
print(e_value)
print(e_vec)

