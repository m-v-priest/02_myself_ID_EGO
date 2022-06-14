from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D  # 要画3d图, 先导入此模块

fig = plt.figure()  # 创建一个3d画布
ax = Axes3D(fig, auto_add_to_figure=False)  # 将画布变为3维的
fig.add_axes(ax)  # 这句代码一定要跟上一句一起写!

plt.gca().set_box_aspect((1, 1, 1))  # 设置x,y,z轴等比例显示



def fn_创建3d向量(list_n个向量的起点x坐标, list_n个向量的起点y坐标, list_n个向量的起点z坐标, list_n个向量的终点x坐标, list_n个向量的终点y坐标, list_n个向量的终点z坐标):
    ax.quiver(list_n个向量的起点x坐标, list_n个向量的起点y坐标, list_n个向量的起点z坐标, list_n个向量的终点x坐标, list_n个向量的终点y坐标, list_n个向量的终点z坐标)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # 设置轴范围的时候用set_xlim3d，而非set_xlim。
    # ax.set_xlim3d(-10, 15)
    # ax.set_ylim3d(-10, 15)
    # ax.set_zlim3d(-10, 15)

    # ax.grid()
