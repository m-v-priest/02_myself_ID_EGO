import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D  # 要画3d图, 先导入此模块
from matplotlib.animation import FuncAnimation  # FuncAnimation 通过周期性地调用函数func来制作动画

fig = plt.figure()  # 创建一个3d画布

ax = Axes3D(fig, auto_add_to_figure=False)  # 将画布变为3维的
fig.add_axes(ax)  # 这句代码一定要跟上一句一起写!

plt.gca().set_box_aspect((1, 1, 1))  # 设置x,y,z轴等比例显示


# 函数区-------------------------

def fn_创建3d向量(list_allVec, list_xyzLim3d=None):
    list_allVec_起点x坐标 = []
    list_allVec_起点y坐标 = []
    list_allVec_起点z坐标 = []

    list_allVec_终点x坐标 = []
    list_allVec_终点y坐标 = []
    list_allVec_终点z坐标 = []

    for vec in list_allVec:
        list_allVec_起点x坐标.append(0)
        list_allVec_起点y坐标.append(0)
        list_allVec_起点z坐标.append(0)
        list_allVec_终点x坐标.append(vec[0])
        list_allVec_终点y坐标.append(vec[1])
        list_allVec_终点z坐标.append(vec[2])

    ax.quiver(list_allVec_起点x坐标, list_allVec_起点y坐标, list_allVec_起点z坐标, list_allVec_终点x坐标, list_allVec_终点y坐标,
              list_allVec_终点z坐标)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # 设置轴范围的时候用set_xlim3d，而非set_xlim。
    if list_xyzLim3d == None:
        ax.set_xlim3d(-100, 100)
        ax.set_ylim3d(-100, 100)
        ax.set_zlim3d(-100, 100)
    else:
        ax.set_xlim3d(list_xyzLim3d[0], list_xyzLim3d[1])
        ax.set_ylim3d(list_xyzLim3d[2], list_xyzLim3d[3])
        ax.set_zlim3d(list_xyzLim3d[4], list_xyzLim3d[5])

    # ax.grid()


# --------


# def fn_update(frame):
#     # 设置图像的观察角度 (即眼睛看到的3维空间的透视角度)
#     ax.view_init(elev=20, azim=frame)  # elevation 仰角, azimuth 方位角
#
# # 开始动画
# anim = FuncAnimation(fig, func=fn_update, frames=360, interval=100)
# '''
# fig: 为你对哪个画布上的图画,执行动画, 指定画布名称
# func : 指定你要不断更新哪个函数, 以让它来实现动画效果. 我们会让它指向你自定义的fn_update(frame)函数.
# frames :一次动画循环, 包含的帧数. 该 帧数值, 会传递给你自定义的fn_update(frame)函数.
# interval : 每一帧的运行时间，以ms计
# '''
#
# anim.save('move1.gif', writer='ffmpeg', fps=10)
#


# 代码区-------------------------

x_vec = np.array([4, 2, 6])  # 原像x
matirxA = np.array([[4, 5, 2], [7, 9, -3], [5, -8, 2]])  # 新基矩阵A
b_vex = np.dot(matirxA, x_vec)  # Ax =b , 用点积相乘, 来得到原像x, 在经过新基A变换后 的新像b
# print(b_vex) # [38 28 16]


fn_创建3d向量([x_vec, b_vex], [-10, 15, -10, 15, -10, 15])

# 当前的坐标系子区域为 ax, 你可以在 ax区域上画图
# ax.plot([2, 3, 5], [5, 2, 1])


plt.show()
