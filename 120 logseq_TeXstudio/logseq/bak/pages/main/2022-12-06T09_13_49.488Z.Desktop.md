-
- 安装 latex
	- 官网 https://www.tug.org/texlive/
	- 下载流程
	  collapsed:: true
		- 教程 https://zhuanlan.zhihu.com/p/56982388
		- ![image.png](../assets/image_1670242099846_0.png)
		- ![image.png](../assets/image_1670242139731_0.png)
		- ![image.png](../assets/image_1670242165581_0.png)
		- ![image.png](../assets/image_1670242188310_0.png)
		-
	- 安装:
	  collapsed:: true
		- 将下载的iso文件, 解压
		- ![image.png](../assets/image_1670242445666_0.png)
		- 安装路径, 一定要是英文的. 安装需要半小时
		-
		-
		-
	- 初次使用
	  collapsed:: true
		- 开始菜单, 打开这个程序
		- ![image.png](../assets/image_1670244130596_0.png)
		- 选择 XeLaTex,  它对中文支持更好
		- ![image.png](../assets/image_1670244204707_0.png)
		- 然后拷贝如如下代码
		- ```
		  
		  \documentclass[UTF8]{ctexart}
		  
		  \begin{document}
		  
		  \section{中文} 中文论文排版测试。
		  
		  \end{document}
		  ```
		- 保存后, 按绿色按钮预览
		- ![image.png](../assets/image_1670244363908_0.png)
- ---
- TeXstudio软件
	- 界面转中文语言
	  collapsed:: true
		- ![image.png](../assets/image_1670241812746_0.png)
		- ![image.png](../assets/image_1670241791430_0.png)
		-
	- 配置各种latex编译器
	  collapsed:: true
		- ![image.png](../assets/image_1670244861312_0.png)
		- ![image.png](../assets/image_1670244901453_0.png)
	- 初次代码测试
	  background-color:: red
	  collapsed:: true
		- ```
		  \documentclass[UTF8]{ctexart}
		  \usepackage{picinpar, graphicx} % 导入这个库后,就能支持插入表格
		  \usepackage{algorithm, algorithmic} % 支持数学公式输入
		  
		  \title{你的标题写在这里}
		  \author{作者名字}
		  \date{\today}
		  
		  \begin{document}
		  	\maketitle  %这行代码, 让你前面的 title, author, date生效
		  	\newpage  %分页
		  	
		  	\section{大标题} %大标题
		  	中文论文排版测试。
		  	\subsection {第二级标题} %会形如: 1.1,  2.1,   3.1 
		  	\subsubsection {第三级标题} %会形如 1.1.1,   2.1.1
		  	
		  	%插入表格
		  	\begin{table}[!t]
		  		\renewcommand{\arraystretch}{1.3}
		  		\caption{An Example of a Table}
		  		\label{table_example}
		  		\centering
		  		\begin{tabular}{|c||c|}
		  			\hline
		  			One & Two\\
		  			\hline
		  			Three & Four\\
		  			\hline
		  		\end{tabular}
		  	\end{table}
		  
		  
		  %插入图片. 图片目录一定要和.tex文件在同一目录下.
		  % 另外注意: [!t]、[width=2.5in] 这个是不能缺的
		  \begin{figure}[!t]
		  	\centering
		  	\includegraphics[width=2.5in]{img/j1.jpg}L
		  	\caption{Simulation results for the network.}
		  	\label{fig_sim}
		  \end{figure}
		  
		  
		  %插入latex公式
		  \begin{equation}
		  	\frac{2} {4}
		  	\int_a^b f(x) dx
		  \end{equation}
		  
		  
		  
		  \end{document}
		  ```
-