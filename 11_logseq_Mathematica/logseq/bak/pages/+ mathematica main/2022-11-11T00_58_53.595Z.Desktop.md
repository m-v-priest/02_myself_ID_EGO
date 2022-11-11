-
- https://www.bilibili.com/video/BV17U4y1s7EV?p=3&vd_source=52c6cb2c1143f8e222795afbab2ab1b5
- 1.17.46
-
- [https://www.bilibili.com/video/BV1QV411k7Wc/?spm_id_from=333.999.0.0&vd_source=52c6cb2c1143f8e222795afbab2ab1b5](https://www.bilibili.com/video/BV1QV411k7Wc/?p=2&spm_id_from=pageDriver&vd_source=52c6cb2c1143f8e222795afbab2ab1b5)
- 12.52
- ---
- 帮助文档
  collapsed:: true
	- ![image.png](../assets/image_1667913312156_0.png)
- 官网中文帮助文档 https://reference.wolfram.com/language/
  background-color:: blue
- 要让某一行在 shift+enter 时算输出, 就在改行代码后面, 加个分号;
- 添加注释语句: alt+/
- 输出成传统数学教科书的模式: $PrePrint = TraditionalForm
  background-color:: blue
  collapsed:: true
	- ![image.png](../assets/image_1667967405697_0.png)
- 删除行 : 选中右边，键盘上按delete
  collapsed:: true
	- ![image.png](../assets/image_1667959723943_0.png)
- ---
- Mathematica 编程语言的规则:
	- 1. 函数名, 其首字母要大写
	  2. 变量名, 和普通编程语言不同,  Mathematica中的变量名, 不能含下划线.
	  3. 你要计算的公式, 要用中括号[] 括起来
	  4. 列表, 或定义域, 值域等范围, 用大括号 {} 括起来
	  5. 要让软件自动计算时, 按 shift+enter
		-
- ---
- 变量
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
- ---
- 引用行数
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
-
- ---
- 逻辑关系
	- 或 :  ||
	  collapsed:: true
		- ![image.png](../assets/image_1668054828088_0.png)
	- 并且: &&
	  collapsed:: true
		- ![image.png](../assets/image_1668054940313_0.png)
-
- ---
- 随机数
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
- ---
- 列表 ← 用{}括起来, 而不是一般编程语言中的中括号[]
	- 创建一个某数值范围内的列表: Range[num]
	  collapsed:: true
		- 注意: 它和一般的编程语言不同, 第一个数是从1开始的, 而不是从0开始.
		- ![image.png](../assets/image_1667970271015_0.png)
		- ![image.png](../assets/image_1667970410704_0.png)
	- 生成一个列表:  Table 函数
	  collapsed:: true
		- ![image.png](../assets/image_1667971604849_0.png){:height 223, :width 340}
		- ![image.png](../assets/image_1667972219355_0.png)
		- ![image.png](../assets/image_1667972317662_0.png)
	- 一个列表中, 包含多个子列表, 将这多个子列表合并成一个大列表:  //Flatten
	  collapsed:: true
		- ![image.png](../assets/image_1667970786382_0.png)
	- 删除列表里的重复元素: // DeleteDuplicates
	  collapsed:: true
		- ![image.png](../assets/image_1667970969083_0.png)
	- 对列表中的元素, 求和 : // Total
	  collapsed:: true
		- ![image.png](../assets/image_1667971070093_0.png)
	- 筛选出列表中符合某条件的元素: Select函数
	  collapsed:: true
		- ![image.png](../assets/image_1667972619159_0.png)
	- 用函数来筛选列表中的元素, 即, 若列表中的元素满足给定函数的返回值, 则就筛选出来.
	  background-color:: blue
	  collapsed:: true
		- ![image.png](../assets/image_1667973214723_0.png)
	- 反向排列 列表中的元素: Reverse函数
	  collapsed:: true
		- ![image.png](../assets/image_1667992394121_0.png)
		-
-
- 子集: Subsets 函数
  background-color:: blue
  collapsed:: true
	- ![image.png](../assets/image_1668068604975_0.png)
	- 注意: 上面这里的 Subsets[list4, {2}] 代码, 因为 list4中是有5个元素的, 取出含有2个元素的子集, 就相当于是 "组合数的 5取2", 即共10种组合.
	  ![image.png](../assets/image_1668068775090_0.png)
	-
-
- ---
- 函数
	- 创建函数  f[参数名_] := 函数体
	  background-color:: blue
	  collapsed:: true
		- 注意: 在自定义函数时, 参数变量名, 必须后面加个下划线_
		- ![image.png](../assets/image_1667958216731_0.png)
		- ![image.png](../assets/image_1667958445139_0.png)
	- 将两个列表中的元素, 依次作为某函数的两个参数, 传入该函数中 : Outer 函数
	  collapsed:: true
		- ![image.png](../assets/image_1667993977084_0.png)
	- @ :  ←  这个其实就是给函数传参的另一种写法
	  background-color:: blue
	  collapsed:: true
		-
		- ![image.png](../assets/image_1667994342683_0.png)
		- ![image.png](../assets/image_1667994464626_0.png)
	- //表示在将 // 后面的函数, 作用在前面的自变量身上. 可以在后面连续写多个函数, 相当于管道运算, 如:
	  background-color:: blue
	  collapsed:: true
		- ![image.png](../assets/image_1667971212814_0.png)
		- ![image.png](../assets/image_1667971349929_0.png)
	- 给函数传入一个多维参数, 即把一个列表作为打包参数, 传给函数, 并将列表中的元素解包, 赋值给函数中的多个参数上:  @@
	  background-color:: blue
	  collapsed:: true
		- ![image.png](../assets/image_1667995067061_0.png)
	-
- ---
- 输入分数 : 用 CTRL+ /键, 来输入分数
  background-color:: blue
  collapsed:: true
	- ![image.png](../assets/image_1667913574670_0.png)
- 输入指数上标:  按 ctrl+6
  background-color:: blue
  collapsed:: true
	- ![image.png](../assets/image_1667913729799_0.png)
- 输入根号: ctrl+2
  background-color:: blue
  collapsed:: true
	- ![image.png](../assets/image_1667957854215_0.png)
- 求极限 : Limit 函数
  collapsed:: true
	- ![image.png](../assets/image_1668057514084_0.png)
-
- 对数: Log 函数
  collapsed:: true
	- ![image.png](../assets/image_1668064457372_0.png)
- ---
- 矩阵
	- 创建矩阵: 将list转成矩阵 (方法件下面的 Det函数的例子)
	- 获得"行列式"的值: Det 函数
	  collapsed:: true
		- ![image.png](../assets/image_1668060711192_0.png)
	- 创建矩阵: 可以用 Table来创建
	  collapsed:: true
		- ![image.png](../assets/image_1668058961612_0.png)
		- ![image.png](../assets/image_1668059026254_0.png)
	- 获取"特征向量"(Eigenvectors函数) 和 "特征值"(Eigenvalues函数):
	  collapsed:: true
		- ![image.png](../assets/image_1668060957510_0.png)
		- ![image.png](../assets/image_1668061072323_0.png)
	- 矩阵的转置: Transpose函数
	  collapsed:: true
		- ![image.png](../assets/image_1668061443643_0.png)
	- 逆矩阵 : Inverse 函数
	  collapsed:: true
		- ![image.png](../assets/image_1668061594862_0.png)
	- 点积: Dot 函数
	  collapsed:: true
		- ![image.png](../assets/image_1668061764839_0.png)
	-
- ---
- 排列组合
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
- 阶乘:
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
- 求导数: D函数
  background-color:: blue
	- ![image.png](../assets/image_1668055969985_0.png)
-
- 泰勒展开
  collapsed:: true
	- ![image.png](../assets/image_1668056370590_0.png)
	- ![image.png](../assets/image_1668056339457_0.png)
- ---
-
- 求积分
  background-color:: purple
	- 不定积分:  Integrate 函数
	  collapsed:: true
		- 如 Integrate [1/(1 - x^3), x]
	-
	- 定积分: NIntegrate 函数
	  collapsed:: true
		- ![image.png](../assets/image_1668069558450_0.png)
		- ![image.png](../assets/image_1668069647250_0.png){:height 222, :width 409}
- ---
- 显示所有计算过程
  collapsed:: true
	- ![image.png](../assets/image_1667912769937_0.png)
- ---
- 解方程
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
	-
- ---
- 画函数图
	- plot函数
		- 画函数图, 包括多元函数的3d图, 用 Plot 函数
		  collapsed:: true
			- ![image.png](../assets/image_1667913150420_0.png)
			- ![image.png](../assets/image_1667961166111_0.png)
		- 调整画图的坐标范围, 输出 PlotRange -> {-1, 2}
		  background-color:: blue
		  collapsed:: true
			- 就表示, 显示范围为 y轴的{-1,2} 的区间段上
			- ![image.png](../assets/image_1667910861273_0.png)
		- 鼠标指在哪个曲线上, 就显示出函数名:   Tooltip[]
		  background-color:: blue
		  collapsed:: true
			- ![image.png](../assets/image_1667961778460_0.png)
	-
	- graph 函数
		- 画出函数图 : 函数公式前面加 =graph 函数, 然后按 shift+回车
		  collapsed:: true
			- 输入等号后, 再使用 graph函数, 软件会将代码转成标准的 Mathematica语言.  并计算发送到网络上的服务器上, 再帮我们返回结果.
			- ![image.png](../assets/image_1667960765127_0.png)
			- ![image.png](../assets/image_1667910997450_0.png)
	-
	- 将多个函数曲线, 画在一张图上
	  background-color:: blue
		- 方法1: 用 and
		  collapsed:: true
			- ![image.png](../assets/image_1667961557838_0.png)
		- 方法2:
		  collapsed:: true
			- ![image.png](../assets/image_1667962069230_0.png)
	-
	- 给曲线下方的面积, 填充颜色:  Filling->Axis
	  collapsed:: true
		- ![image.png](../assets/image_1667962344337_0.png)
- 互动模型: Manipulate函数
  collapsed:: true
	- ![image.png](../assets/image_1667962939733_0.png)
	- ![image.png](../assets/image_1667963096519_0.png)
- 在一张图里面, 能进行多个函数图像切换:
  collapsed:: true
	- ![image.png](../assets/image_1667963466961_0.png)
-
- 绘制数据图
	- 绘制点图:  ListPlot 函数
	  collapsed:: true
		- ![image.png](../assets/image_1667964279508_0.png)
	- 导入你自己的数据, 来绘制点图: Import 函数
	  collapsed:: true
		- ![image.png](../assets/image_1667964464887_0.png)
-
- ---
- 对数据进行函数拟合
	- 线性拟合 : Fit[列表, {1, x}, x]
	  collapsed:: true
		- ![image.png](../assets/image_1667969752092_0.png)
- ---
- 多项式
	- 展开多项式 :  Expand 函数
	  collapsed:: true
		- ![image.png](../assets/image_1667958341676_0.png)
	- 因式分解 : //Factor
	  collapsed:: true
		- ![image.png](../assets/image_1668054515357_0.png)
		-
-
- 将一个数, 分解成质数: FactorInteger 函数
  collapsed:: true
	- FactorInteger[n] : gives a list of the prime factors of the integer n, together with their exponents.
	- ![image.png](../assets/image_1667973427888_0.png)
	- ![image.png](../assets/image_1667973484859_0.png)
-
- ---
- 数值的精度
	- 数值的精确解: 直接按 shift+回车, 可以获得分数形式的解
	- 数值的近似解: N[224/24248, 10] ← 第二位参数10,表示精确到小数点后10位
	  collapsed:: true
		- ![image.png](../assets/image_1667956808687_0.png)
		-
		-
	- 把小数, 化成分式: Rationalize 函数
	  background-color:: blue
	  collapsed:: true
		- ![image.png](../assets/image_1668063829172_0.png)
		- ![image.png](../assets/image_1668063925999_0.png)
-
- ---
- 把一个数字, 按个十百千位等, 拆成单个数字, 放在一个列表中 : IntegerDigits 函数
  collapsed:: true
	- ![image.png](../assets/image_1667982992252_0.png)
	- ![image.png](../assets/image_1667983084683_0.png)
-
- 切割列表: Partition 函数
  collapsed:: true
	- ![image.png](../assets/image_1668050098731_0.png)
	- ![image.png](../assets/image_1668049946598_0.png)
- ---
- 乘法 :  Times 函数
  collapsed:: true
	- Outer函数的作用, 是将第一个list中的每个元素, 依次去乘第二个list中的每个元素.
	- ![image.png](../assets/image_1667993067049_0.png){:height 147, :width 427}
- 求和: Sum 函数
  collapsed:: true
	- ![image.png](../assets/image_1667997633575_0.png)
	- ![image.png](../assets/image_1667997804841_0.png)
- ---
- 常数E
  collapsed:: true
	- ![image.png](../assets/image_1668054317872_0.png)
	-
- 圆周率, 是 Pi
  collapsed:: true
	- ![image.png](../assets/image_1668054382502_0.png)
-
- 字体
  collapsed:: true
	- 改变字体颜色
		- ![image.png](../assets/image_1667914107212_0.png)
-