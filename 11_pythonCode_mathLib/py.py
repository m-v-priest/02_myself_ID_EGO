import my_module  # 导入你自己编辑的模块, 里面有你写的函数

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D # 要画3d图, 先导入此模块


my_module.fn_图画显示令支持中文()
# my_module.fn_设定坐标轴数值范围(-2, 20, -2, 2)
# my_module.fn_改成四象限坐标系()

fig = plt.figure() # 创建一个绘图对象,即构建一个画布, 赋值给 fig变量
ax = Axes3D(fig) # 将画布变为3维的

plt.gca().set_box_aspect((1, 1, 1)) # 设置x,y,z轴等比例显示

ax.quiver([0,5,2],[0,3,4],[0,7,8],[5,7,-8],[3,9,6],[7,-3,-3])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 设置轴范围的时候用set_xlim3d，而非set_xlim。
ax.set_xlim3d(-10, 15)
ax.set_ylim3d(-10, 15)
ax.set_zlim3d(-10, 15)

ax.grid()
# plt.plot(x, y)
plt.show()
