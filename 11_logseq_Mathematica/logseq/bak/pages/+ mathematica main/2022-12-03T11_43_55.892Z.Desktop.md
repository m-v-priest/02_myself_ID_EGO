-
- ### 相关
	- ### 学习进度
		- https://www.bilibili.com/video/BV1Ua4y1v7AU/?spm_id_from=333.788&vd_source=52c6cb2c1143f8e222795afbab2ab1b5
		- 5.22
		-
		- 阮一峰
		- https://www.ruanyifeng.com/blog/algorithm/
		-
		- https://www.bilibili.com/video/BV17U4y1s7EV?p=3&vd_source=52c6cb2c1143f8e222795afbab2ab1b5
		- 1.17.46
		-
		- [https://www.bilibili.com/video/BV1QV411k7Wc/?spm_id_from=333.999.0.0&vd_source=52c6cb2c1143f8e222795afbab2ab1b5](https://www.bilibili.com/video/BV1QV411k7Wc/?p=2&spm_id_from=pageDriver&vd_source=52c6cb2c1143f8e222795afbab2ab1b5)
		- 12.52
	- ### 帮助文档
	  collapsed:: true
		- 官网中文帮助文档 https://reference.wolfram.com/language/
		  background-color:: blue
	- ### 软件本身的功能
		- 字体
		  collapsed:: true
			- 改变字体颜色
				- ![image.png](../assets/image_1667914107212_0.png)
	- ### 常规技巧
		- 删除行 : 选中右边，键盘上按delete
		  collapsed:: true
			- ![image.png](../assets/image_1667959723943_0.png)
		- 让某一行暂不输出结果,就在该行代码后面, 加个分号;
		- 输出成传统数学教科书的模式 (但不推荐这样): $PrePrint = TraditionalForm
		  background-color:: blue
		  collapsed:: true
			- ![image.png](../assets/image_1667967405697_0.png)
		- 添加注释语句: alt+ /
		  background-color:: blue
		- 显示所有计算过程
		  collapsed:: true
			- ![image.png](../assets/image_1667912769937_0.png)
		- 不显示全部的输出结果: Short[列表]
		  background-color:: blue
		  collapsed:: true
			- ![image.png](../assets/image_1668303774218_0.png)
		- 引用行数
		  collapsed:: true
			- 注意: 某一行的编号, 再你每次打开该笔记时,可能会自行变动
			- 引用某一行的代码: 用 "%行数", 来引用该行代码
			  background-color:: blue
			  collapsed:: true
				- ![image.png](../assets/image_1667956970591_0.png)
				-
			- 直接引用上一行的代码: 用 %
			  background-color:: blue
			  collapsed:: true
				- ![image.png](../assets/image_1667957155691_0.png)
				- ![image.png](../assets/image_1667957270830_0.png)
	- ### Mathematica 编程语言的规则
	  collapsed:: true
		- 1. 函数名, 其首字母要大写
		  2. 变量名, 和普通编程语言不同,  Mathematica中的变量名, 不能含下划线.
		  3. 在一般编程语言里, 函数参数, 是用小括号()括起来的, 但在mma里, 小括号作为数学中的常规用法来用, 函数参数就改成了用中括号[]来括了.
		  4. 同样, 一般编程语言里, 列表, 使用中括号[]括起来的, 在mma里, 列表就改成了用大括号{}来括了. 即,  列表, 或定义域, 值域等范围, 用大括号 {} 括起来
		  7. 要让软件自动计算时, 按 shift+enter
-
-
- ---
- ### 变量
  collapsed:: true
	- 清除所有变量中的值:  Clear["Global`*"]
	  collapsed:: true
		- mathematica 中为变量的赋值时永久性的。因此前面定义的变量, 往往在计算后无法释放掉，容易导致后边计算受到影响，因此就需要清除不再使用的变量.
		- Remove[]函数的作用就是消除变量，使用此函数后变量的定义将被删除。
		- 与之类似的是mathematica中的Clear[]函数，但是Clear["`*"]函数只能消除变量的赋值，变量（的定义）还是存在的。
		- ![image.png](../assets/image_1667959116534_0.png)
	- 清除某个变量中的值:  变量=.
	  collapsed:: true
		- ![image.png](../assets/image_1668054641809_0.png)
	- 给变量赋值
	  collapsed:: true
		- ![image.png](../assets/image_1667957525308_0.png)
	-
- [[逻辑语句]]
- [[编程函数]]
- [[列表]]
-
- ### 计算
  background-color:: red
	- 化简: Simplify 和 FullSimplify 函数
	  collapsed:: true
		- ![image.png](../assets/image_1668301564099_0.png)
		- ![image.png](../assets/image_1668301627879_0.png)
	- 解方程:  Solve函数
	  collapsed:: true
		- Solve[expr,vars]
		  attempts to solve the system expr of equations or inequalities for the variables vars. 尝试求解变量为vars的方程组或不等式的方程组expr。
		- Solve[expr,vars,dom]
		  solves over the domain dom. Common choices of dom are Reals, Integers, and Complexes. 在域dom上求解。dom的常用选项有实数、整数和复数。
		-
		- ![image.png](../assets/image_1667960179359_0.png)
		- 例:
			- ![image.png](../assets/image_1668055528606_0.png)
		- 又例:
			- ![image.png](../assets/image_1668051070531_0.png)
	- 展开多项式 :  Expand 函数
	  collapsed:: true
		- ![image.png](../assets/image_1668302183208_0.png)
		- ![image.png](../assets/image_1668302265302_0.png)
		- ![image.png](../assets/image_1667958341676_0.png)
		- ![image.png](../assets/image_1668302420904_0.png)
		- ![image.png](../assets/image_1668302547389_0.png)
		- nu·mer·ator *n.*
		  /ˈnjuːməreɪtə(r) 
		  ( mathematics 数) the number above the line in a **fraction** , for example 3 in the **fraction** 3⁄4 （分数中的）分子
		  -> numer-,数字，-ator,名词后缀。用于指分子，比较denominator.
		-
		- ![image.png](../assets/image_1668302589168_0.png)
		- de-, 向下，强调。-nom, 命名，词源同name. 即命名，同名，用于数学术语分母。参照numerator.
		-
		-
	- 因式分解 : //Factor
	  collapsed:: true
		- ![image.png](../assets/image_1668054515357_0.png)
		- ![image.png](../assets/image_1668301851883_0.png)
		-
		-
	- 合并同类项 Collect[eq, x或y或{x,y}]
	  collapsed:: true
		- ![image.png](../assets/image_1668301919405_0.png)
		- ![image.png](../assets/image_1668302018402_0.png)
		- ![image.png](../assets/image_1668302094719_0.png)
		-
	- 通分: 把几个异分母分数（式）化成与原来分数（式）相等的同分母的分数（式）的过程，叫做通分
	  collapsed:: true
		- ![image.png](../assets/image_1668303203475_0.png)
		- ![image.png](../assets/image_1668303226675_0.png)
		-
	- ![image.png](../assets/image_1668303282283_0.png)
	  collapsed:: true
		- ![image.png](../assets/image_1668303451596_0.png)
	- ![image.png](../assets/image_1668303296833_0.png)
		- ![image.png](../assets/image_1668303419705_0.png)
	- ![image.png](../assets/image_1668304210203_0.png)
	-
- ---
- ### 三角函数
  collapsed:: true
	- ![image.png](../assets/image_1668303863021_0.png)
	  collapsed:: true
		- ![image.png](../assets/image_1668303939383_0.png)
		- ![image.png](../assets/image_1668304156683_0.png)
		-
		-
	-
-
-
- ### 微积分
	-
	-
	- 求极限 : Limit 函数
	  collapsed:: true
		- ![image.png](../assets/image_1668057514084_0.png)
	- 对数: Log 函数
	  collapsed:: true
		- ![image.png](../assets/image_1668064457372_0.png)
		- ![image.png](../assets/image_1668584160666_0.png)
	- 对数: ln函数的写法
	  background-color:: red
	  collapsed:: true
		- ```
		  Log[E,幂]=指数
		  ```
		- ![image.png](../assets/image_1669544106432_0.png)
		- ![image.png](../assets/image_1669544179575_0.png)
	- 泰勒展开
	  collapsed:: true
		- ![image.png](../assets/image_1668056370590_0.png)
		- ![image.png](../assets/image_1668056339457_0.png)
	-
	- 求导数: D函数
	  background-color:: blue
	  collapsed:: true
		- ![image.png](../assets/image_1668055969985_0.png)
		- ![image.png](../assets/image_1668584369180_0.png)
		- ![image.png](../assets/image_1668584978943_0.png)
		- ![image.png](../assets/image_1668584999237_0.png)
		-
	- 不定积分:  Integrate 函数
	  collapsed:: true
		- 如 Integrate [1/(1 - x^3), x]
		- ![image.png](../assets/image_1668084934898_0.png)
		- ![image.png](../assets/image_1668085242983_0.png)
	- 定积分: NIntegrate 函数
	  collapsed:: true
		- ![image.png](../assets/image_1668069558450_0.png)
		- ![image.png](../assets/image_1668069647250_0.png){:height 222, :width 409}
	-
	- ### 对数据进行函数拟合
		- 线性拟合 : Fit[列表, {1, x}, x]
		  collapsed:: true
			- ![image.png](../assets/image_1667969752092_0.png)
- ---
- ### 线性代数
	- [[矩阵]]
- ---
-
- ### 概率与统计
	- 阶乘:
	  collapsed:: true
		- 阶乘 Factorial 函数
		  collapsed:: true
			- ![image.png](../assets/image_1668067602869_0.png)
			- ![image.png](../assets/image_1668067629471_0.png)
		- 从某一个数开始, 乘以它后面的几个数: Pochhammer 函数
		  collapsed:: true
			- ![image.png](../assets/image_1668067334614_0.png)
			- ![image.png](../assets/image_1668067395316_0.png)
			- ![image.png](../assets/image_1668067425300_0.png)
		-
	- 排列组合
	  collapsed:: true
		- 组合 : Binomial 函数 (二项式系数)
		  collapsed:: true
			- ![image.png](../assets/image_1668066753862_0.png)
			- ![image.png](../assets/image_1668066762848_0.png)
			-
		- 排列 :
		  collapsed:: true
			- ![image.png](../assets/image_1668067933756_0.png)
			- 所以, 排列数, 就用Binomial获得组合数，再用个阶乘, 就能获得排列数。
			  比如, P_6^4 = Binomial[6,4] * 4!
			- ![image.png](../assets/image_1668068272711_0.png)
			- ![image.png](../assets/image_1668068285770_0.png)
			-
	-
	- 平均值: Mean[列表]
	  collapsed:: true
		- ![image.png](../assets/image_1668149524707_0.png)
	- 中位数: Median[列表]
	  collapsed:: true
		- ![image.png](../assets/image_1668149184251_0.png)
	- 方差 : Variance[列表]
	  background-color:: blue
	  collapsed:: true
		- ![image.png](../assets/image_1668149608090_0.png)
	- 标准差: StandardDeviation[列表]
	  background-color:: blue
	  collapsed:: true
		- ![image.png](../assets/image_1668149766229_0.png)
	- k阶中心距:  CentralMoment[列表, 第k阶]
	  collapsed:: true
		- ![image.png](../assets/image_1668149924756_0.png)
	-
	- 协方差: Covariance[列表1, 列表2]
	  background-color:: blue
	  collapsed:: true
		- 解释:
		  collapsed:: true
			- 协方差是统计学中使用的一种数值，**用于描述两个变量间"的线性关系"。**
			- **两个变量的"协方差"越大，它们在一系列数据点范围内的取值, 所呈现出的趋势, 就越相近（换句话说，两个变量的曲线距离彼此较近, 走势相同, 如两只蝴蝶双飞双舞）。**
			- **协方差值等于1意味着完全正相关。** 协方差值永远介于1和-1之间。
			- **如果协方差值正好等于1，则两个变量完全正相关。**也就是说，一个变量会随着另一个变量的增加而增加（减少而减少）。这种关系是完全线性的——无论变量取值多大或多小，两个变量之间的关系都一样。
			- **协方差值等于-1, 意味着完全负相关。**
			- **协方差为0意味着不相关。**
		- ![image.png](../assets/image_1668151188013_0.png)
		- ![image.png](../assets/image_1668151246753_0.png)
	- 相关系数:Correlation[列表1, 列表2]
	  background-color:: pink
	  collapsed:: true
		- ![image.png](../assets/image_1668153087445_0.png)
	-
	- PDF 概率函数
	  collapsed:: true
		- ![image.png](../assets/image_1668169480052_0.png)
	- CDF 累积分布函数
	  collapsed:: true
		- 语法:
			- ![image.png](../assets/image_1668169569724_0.png)
		- 例
			- ![image.png](../assets/image_1668170457332_0.png)
			- ![image.png](../assets/image_1668170492903_0.png)
			- ![image.png](../assets/image_1668170563504_0.png)
		-
		-
	-
	-
	- ### 离散数据的分布
	- 二项分布
	  collapsed:: true
		- 解释:
		  collapsed:: true
			- 若每次试验中: 只有两种可能的结果, 
			  这两种结果发生与否, 互相对立. 
			  并且相互独立，与其它各次试验结果无关. 
			  事件发生与否的概率在每一次独立试验中都保持不变，
			  则这一系列试验总称为n重伯努利实验，当试验次数为1时，二项分布服从0-1分布。
			-
			- **n次试验中, 正好得到k次成功的概率**, 由概率质量函数 f(x)给出:
			- ![de72eee084dc44d8fa3cb44d7eb406bb.svg](../assets/de72eee084dc44d8fa3cb44d7eb406bb_1668164894035_0.svg)
			- **即: 我们希望有k次成功(p), 和n−k次失败(1 −p)。**
			- 你可以发现: 实际上，**当n = 1时，二项分布就是伯努利分布**
			-
		- 语法: BinomialDistribution[n,p] 
		  represents a binomial distribution **with n trials and success probability p.**
		-
		- 例 1
			- ![image.png](../assets/image_1668167326859_0.png)
			- ![image.png](../assets/image_1668167358108_0.png)
			- ![image.png](../assets/image_1668167392003_0.png)
		-
	- 超几何分布
	  collapsed:: true
		- 定义:
			- 超几何分布是统计学上一种离散概率分布。它描述了从有限N个物件（其中包含M个指定种类的物件）中抽出n个物件，成功抽出该指定种类的物件的次数（不放回）。称为超几何分布，是因为其形式与“超几何函数”的级数展式的系数有关。
			- N个民女中, 含有M个美女, 皇帝选美, 抽n个人(不放回), 成功抽出美女的次数, 就称为超几何分布. Hypergeometric Distribution
			- 超几何分布中的参数是N(总数),n(抽n次),M()，超几何分布记作X~H(N,n,M)。
		- 语法
			- ![image.png](../assets/image_1668241193409_0.png){:height 176, :width 475}
			-
		- 例:
		  collapsed:: true
			- ![image.png](../assets/image_1668243347922_0.png)
			- ![image.png](../assets/image_1668243483790_0.png){:height 246, :width 475}
			- ![image.png](../assets/image_1668244077364_0.png)
			-
	- 泊松分布
	  collapsed:: true
		- ![image.png](../assets/image_1668248079022_0.png)
		- 例: 50年一遇的大雨.  你就以50年为时间段 (即平均会发生一次这种大雨), 在这50年中, 你遇到0次, 1次, 2次, ... 这种大雨的真实概率, 是多少?
		- ![image.png](../assets/image_1668248667485_0.png)
		- ![image.png](../assets/image_1668248701094_0.png)
		-
		-
	-
	- ### 连续数据的分布
	- 标准正态分布: Probability[x <= 某个值, x \[Distributed] NormalDistribution[]]
	  collapsed:: true
		- ![image.png](../assets/image_1668145879750_0.png)
		- ![image.png](../assets/image_1668145916145_0.png)
		-
	- 均匀分布, 或矩形分布
	  collapsed:: true
		- 定义 :
		  collapsed:: true
			- Uniform Distribution 均匀分布 在相同长度间隔的分布概率, 是等可能的。 均匀分布由两个参数a和b定义，它们是数轴上的最小值和最大值，通常缩写为U（a，b）。
			- 均匀分布的概率函数为：
			  ![image.png](../assets/image_1668250727141_0.png)
		- 语法:
		  collapsed:: true
			- ![image.png](../assets/image_1668251390277_0.png)
			  id:: 636f7ef5-3c78-4262-ba69-f08730e981e4
		- 例:
			- ![image.png](../assets/image_1668252452832_0.png){:height 416, :width 475}
			-
		-
	- 指数分布
	  collapsed:: true
		- 定义:
			-
		- 语法:
			- ![image.png](../assets/image_1668253146405_0.png)
			- 参数λ : 是每单位时间内, 发生某事件的次数。
		- 例:
			- ![image.png](../assets/image_1668256640010_0.png)
			- ![image.png](../assets/image_1668255461880_0.png)
			- ![image.png](../assets/image_1668256370774_0.png)
	-
-
-
- ---
- ### 点图, 数据图
	- 画出某个数列公式的前n位具体数值 : Table[]函数
	  background-color:: red
	  collapsed:: true
		- ![image.png](../assets/image_1669512904879_0.png)
	- 绘制点图:  ListPlot 函数
	  collapsed:: true
		- ListPlot绘制的是什么?
		  依次绘制列表中各元素的值.各点的x值, 给出该元素在列表中的排序位置;y值给出该元素的值.
		- ![image.png](../assets/image_1668132045480_0.png)
		- ![image.png](../assets/image_1667964279508_0.png)
	- 数据图(即将点连线起来): ListLinePlot 函数
	  background-color:: pink
		- 例:
		  collapsed:: true
			- ![image.png](../assets/image_1668137484857_0.png)
		- 将多个列表, 同时显示在一个数轴图上
		  background-color:: pink
		  collapsed:: true
			- ![image.png](../assets/image_1668149436140_0.png)
	- 条形图 : BarChart 函数
	  collapsed:: true
		- ![image.png](../assets/image_1668137579378_0.png)
	- 饼图 : PieChart 函数
	  collapsed:: true
		- ![image.png](../assets/image_1668137654908_0.png)
	- 纯数轴上的数字(去重)图: NumberLinePlot 函数
	  background-color:: blue
	  collapsed:: true
		- ![image.png](../assets/image_1668137714774_0.png)
	- 导入你自己的数据, 来绘制点图: Import 函数
	  collapsed:: true
		- ![image.png](../assets/image_1667964464887_0.png)
	-
	-
- ### 函数图
	- plot函数 : 画函数图, 包括多元函数的3d图, 用 Plot 函数
	  collapsed:: true
		- ![image.png](../assets/image_1667913150420_0.png)
		-
	- graph 函数
	  collapsed:: true
		- graph 函数 : 画出函数图 : 函数公式前面加 =graph 函数, 然后按 shift+回车
			- 输入等号后, 再使用 graph函数, 软件会将代码转成标准的 Mathematica语言.  并计算发送到网络上的服务器上, 再帮我们返回结果.
			- ![image.png](../assets/image_1667960765127_0.png)
			- ![image.png](../assets/image_1667910997450_0.png)
	- 给曲线, 加上它是属于哪一个函数的说明, 即添加上函数名
	  background-color:: red
	  collapsed:: true
		- ```
		  Plot[{Sin[x], Cos[x]}, {x, 0, 2 Pi}, PlotLabels -> "Expressions"]
		  ```
		- ![image.png](../assets/image_1669463729741_0.png)
	-
	- ### 将多个函数曲线, 画在一张图上 :
	  background-color:: blue
	  collapsed:: true
		- 方法1: Plot函数中用 and
			- ![image.png](../assets/image_1667961557838_0.png)
			- ![image.png](../assets/image_1667961166111_0.png)
		- 方法2: 用 Show 函数
			- ![image.png](../assets/image_1667962069230_0.png)
			- ![image.png](../assets/image_1668131488762_0.png)
			- ![image.png](../assets/image_1668130982577_0.png)
			- 但是上图, 而我们看到, 两个曲线合在一起的图, 是错误的, 蓝色部分没有完全显示出来. 原因可能是, 蓝色的坐标轴的原点, 不是从(0,0)开始的
			- ![image.png](../assets/image_1668131437596_0.png)
			-
	-
	- 调整画图的坐标范围, 输出 PlotRange -> {-1, 2}
	  background-color:: blue
	  collapsed:: true
		- 就表示, 显示范围为 y轴的{-1,2} 的区间段上
		- ![image.png](../assets/image_1667910861273_0.png)
	- 在一张图里面, 能进行多个函数图像切换:
	  collapsed:: true
		- ![image.png](../assets/image_1667963466961_0.png)
-
	- ### 互动模型: Manipulate函数
	  collapsed:: true
		- ![image.png](../assets/image_1667962939733_0.png)
		- ![image.png](../assets/image_1667963096519_0.png)
-
	- ### 画图: 改样式
		- x,y坐标轴以1:1的比例来画图
		  background-color:: red
		  collapsed:: true
			- ```
			  AspectRatio -> Automatic
			  ```
			- ![image.png](../assets/image_1669465516486_0.png)
		- x,y坐标轴, 改为 pi 单位
		  background-color:: red
			- ```
			  Ticks -> {Automatic, Range[-Pi/2, Pi/2]}
			  ```
			- ![image.png](../assets/image_1669465936590_0.png)
		- 给曲线下方的面积, 填充颜色:  Filling->Axis
		  collapsed:: true
		  background-color:: red
			- ![image.png](../assets/image_1667962344337_0.png)
		- 在两条曲线之间, 填色
		  background-color:: red
		  collapsed:: true
			- ```
			  Plot[{Sin[x] + x/2, Sin[x] + x}, {x, 0, 10}, Filling -> {1 -> {2}}]
			  ```
			- ![image.png](../assets/image_1669463826888_0.png)
		- 其他填色, 见官方说明
		- 鼠标指在哪个曲线上, 就显示出函数名:   Tooltip[]
		  background-color:: blue
		  collapsed:: true
			- ![image.png](../assets/image_1667961778460_0.png)
-
-
- ---
- ### 各种符号的输入
	- 输入分数 : 用 CTRL+ /键, 来输入分数
	  collapsed:: true
		- ![image.png](../assets/image_1667913574670_0.png)
	- 输入指数上标:  按 ctrl+6
	  collapsed:: true
		- ![image.png](../assets/image_1667913729799_0.png)
	- 输入根号: ctrl+2
	  collapsed:: true
		- ![image.png](../assets/image_1667957854215_0.png)
	- 常数E
	  collapsed:: true
		- ![image.png](../assets/image_1668054317872_0.png)
		-
	- 圆周率, 是 Pi
	  collapsed:: true
		- ![image.png](../assets/image_1668054382502_0.png)
-
### 随机数
	- 随机实数: RandomReal 函数
	  collapsed:: true
		- ![image.png](../assets/image_1668064793754_0.png)
	- 随机整数: RandomInteger 函数
	  collapsed:: true
		- ![image.png](../assets/image_1668065281215_0.png)
	- 在列表里, 随机选出一个元素
	  background-color:: blue
	  collapsed:: true
		- ![image.png](../assets/image_1668065802559_0.png)
-
### 质数
	- 将一个数, 分解成质数: FactorInteger 函数
	  collapsed:: true
		- FactorInteger[n] : gives a list of the prime factors of the integer n, together with their exponents.
		- ![image.png](../assets/image_1667973427888_0.png)
		- ![image.png](../assets/image_1667973484859_0.png)
-
### 算式
	- 乘法 :  Times 函数
	  collapsed:: true
		- Outer函数的作用, 是将第一个list中的每个元素, 依次去乘第二个list中的每个元素.
		- ![image.png](../assets/image_1667993067049_0.png){:height 147, :width 427}
	- 求和: Sum 函数
	  collapsed:: true
		- ![image.png](../assets/image_1667997633575_0.png)
		- ![image.png](../assets/image_1667997804841_0.png)
	- 连乘: Product
	  collapsed:: true
		- ![image.png](../assets/image_1668583599951_0.png)
		- ![image.png](../assets/image_1668583629619_0.png)
		-
-
### 数值的精度
	- 数值的精确解: 直接按 shift+回车, 可以获得分数形式的解
	- 数值的近似解: N[224/24248, 10] ← 第二位参数10,表示精确到小数点后10位.
	  collapsed:: true
		- ![image.png](../assets/image_1667956808687_0.png)
		- ![image.png](../assets/image_1668301001644_0.png)
		-
		-
	- 把小数, 化成分式: Rationalize 函数
	  background-color:: blue
	  collapsed:: true
		- ![image.png](../assets/image_1668063829172_0.png)
		- ![image.png](../assets/image_1668063925999_0.png)
-
### 数字处理
	- 把一个数字, 按个十百千位等, 拆成单个数字, 放在一个列表中 : IntegerDigits 函数
	  collapsed:: true
		- ![image.png](../assets/image_1667982992252_0.png)
		- ![image.png](../assets/image_1667983084683_0.png)
	- 将一个列表中的数字元素, 拼成一个数字 : FromDigits [某列表]
	  collapsed:: true
		- ![image.png](../assets/image_1668141950225_0.png)
		  id:: 636dd363-bdcd-45f9-99eb-3fa83abbaaa8
-
-
-