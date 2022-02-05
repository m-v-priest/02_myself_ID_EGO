-
- ==代数余子式:  即 在这个元素的"余子式"前面, 适当的加上正负号.==
	- > -cofactor :
	  /ˈkoˌfæktər/ N a number associated with an element in a square matrix, equal to the determinant of the matrix formed by removing the row and column in which the element appears from the given determinant 余子式
-
- ^^正负号的规则是: (-1)^{ i+j} <- 即用该元素所在的"行数"和"列数"之和, 作为(-1)的指数, 整体得到的正负号.^^
	- 如:
	  #+BEGIN_EXPORT latex
	  \boxed{
	  代数余子式 A_{23} = (-1)^{(2+3)} × 余子式 M_{23}
	  }
	  #+END_EXPORT
	- #+BEGIN_QUOTE
	  如上例中, 我们已经知道
	  #+BEGIN_EXPORT latex
	  M_{32} = \begin{vmatrix}
	  1 & 0 \\
	  3 & 4 \\
	  \end{vmatrix}
	  #+END_EXPORT
	  
	  则, 该"代数余子式" =
	  #+BEGIN_EXPORT latex
	  A_{32} = (-1)^{(3+2)} × M_{32} = - 
	  \begin{vmatrix}
	  1 & 0 \\
	  3 & 4 \\
	  \end{vmatrix}
	  #+END_EXPORT 
	  #+END_QUOTE