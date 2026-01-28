import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure() # 创建空白画布
# ax = fig.add_axes([0,0,1,1])
ax = plt.gca() # 获得当前的ax, 画图会花在这个ax区域中



#函数区------------------------------


def fn_图画显示令支持中文():
    import matplotlib
    matplotlib.rc("font", family='Microsoft YaHei')  # 注意, 要想在画图中成功显示中文, 必须加上这句代码


def fn_设定坐标轴数值范围(x_min=0, x_max=100, y_min=0,y_max=100):
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)


def fn_改成四象限坐标系(x_origin=0,y_origin=0, name_x_axis='x轴', name_y_axis='y轴'): # 输入新的原点所在位置, 即新原点, 放在x轴上的哪个数值处, 放在y轴的哪个数值处.
    # 获取当前的"轴对象" Get Current Axes (gca), 下面对轴的所有自定义修改, 都是对 gca对象的修改.

    # ax = plt.gca() 如果你要导入此模块的py文件, 没有写这条代码, 就先打开这条代码!

    #原图有上下左右四个边线, 为了转成四象限图, 我们只要保留两个边线就行了, 让left边线变成y轴, 让bottom边线变成x轴. 然后隐藏掉另两根边线 right 和 top.
    ax.spines["right"].set_color('none')
    ax.spines["top"].set_color('none')

    # 下面, 先设定四象限坐标的新原点, 在x和y轴上数值上的哪一边
    ax.spines["left"].set_position(('data', x_origin))  # 原left边线, 现在就变成y轴, 把它竖立在x轴的 x_origin 数值处. 第一个参数'data'表示按数值挪动.
    ax.spines["bottom"].set_position(('data', y_origin))  # 原bottom边线, 现在就变成x轴, 把它竖立在y轴的 y_origin 数值处.

    plt.xlabel(name_x_axis, loc='right') # loc参数, 用来指定坐标轴说明文字的摆放位置
    plt.ylabel(name_y_axis, loc='top')


def fn_做标注(目标元素的x坐标, 目标元素的y坐标,注释文本的颜色='black',注释文本的坐标值偏移量x =0,注释文本的坐标值偏移量y=0 , 箭头线的边框颜色='black', 注释的边框内部填色 ='white', 注释的边框线颜色='black'):
    plt.plot([目标元素的x坐标, 目标元素的x坐标], [目标元素的y坐标, 0], 'k--')
    plt.annotate(text=r'本点的x坐标轴:{}, 本点的y坐标轴:{}'.format(目标元素的x坐标, 目标元素的y坐标), xy=(目标元素的x坐标, 目标元素的y坐标), color=注释文本的颜色,
                 arrowprops=dict(arrowstyle='->', edgecolor=箭头线的边框颜色, connectionstyle='arc3, rad=.2'), xytext=(注释文本的坐标值偏移量x, 注释文本的坐标值偏移量y),
                 bbox=dict(facecolor=注释的边框内部填色, edgecolor=注释的边框线颜色))

    '''
    用 plt.plot()函数来画, 它可以绘制点和线.
    
    用plt.annotate()函数,来进行"文字标注". 其参数有:
    text参数: 为你做的注释的文本内容
    color参数: 指定你的注释文字, 用哪种颜色.
    xy参数 : 指定你要为哪个位置上的元素(比如哪个特殊的数据点), 进行注释. 其实此处, xy参数只要指出这个元素的坐标点即可.
    xytext参数 :  用来指定你做的"注释文本"的坐标点, 即摆放的坐标位置在何处. 注意, 你要输入的是偏移值. 即相对于"xy参数中坐标"的偏移值.
    
    arrowprops参数: 是箭头参数,参数类型为字典dict.  其参数有:
    --> facecolor：箭头颜色. 注意, 如果箭头太细的话, "箭头颜色"会被下面的"箭头边框线的颜色"所压制.
    --> edgecolor：(简写ec)箭头的边框线条颜色, 默认为黑色.
    --> connectionstyle: 用来指定箭头线的弧度
    
    bbox参数: 给标题增加外框. 其中的参数有: 
    -->  facecolor：(简写fc)背景颜色, 默认为蓝色.
    --> edgecolor：(简写ec)边框线条颜色, 默认为黑色.
    '''


def fn_创建2d向量(list_n个向量的起点x坐标,list_n个向量的起点y坐标, list_n个向量的终点x坐标, list_n个向量的终点y坐标):
    # 一次性同时画多个向量的话, 要用列表来表示
    ax.quiver(list_n个向量的起点x坐标,list_n个向量的起点y坐标, list_n个向量的终点x坐标, list_n个向量的终点y坐标,angles='xy', scale_units='xy', scale=1)

    # ax.set_xlabel('X')
    # ax.set_ylabel('Y')
    # ax.set_xlim(-10, 15)
    # ax.set_ylim(-10, 15)



#代码区------------------------------

fn_设定坐标轴数值范围(-10,20,-10,20)
fn_创建2d向量([0,5,2],[0,3,4],[5,7,-2],[3,9,6])




ax.grid()
plt.show()


