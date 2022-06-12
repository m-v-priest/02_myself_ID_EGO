import my_module  # 导入你自己编辑的模块, 里面有你写的函数

import numpy as np
from matplotlib import pyplot as plt

my_module.fn_图画显示令支持中文()
my_module.fn_设定坐标轴数值范围(-2, 20, -2, 2)
my_module.fn_改成四象限坐标系()

# 本例, 我们先构造一条sin曲线
x = np.arange(0, 101)
y = np.sin(x)

# 在sin曲线上, 标出一个点来
point1_x = 7
point1_y = np.sin(point1_x)
plt.scatter(point1_x, point1_y, s=100, c='r')  # 画出这个点. plt.scatter()函数用于生成一个scatter散点图。
# 其中, s参数, 指定点的显示大小 size, 默认20.
# c参数, 表示点的色彩 color, 默认为蓝色’b’.

# 下面来画从上面这个点, 到x轴的垂直虚线.

my_module.fn_做标注(point1_x,point1_y,注释文本的坐标值偏移量x=1,注释文本的坐标值偏移量y=1.5)

plt.plot(x, y)
plt.show()
