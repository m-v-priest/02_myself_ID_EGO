import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes()

# 一次性同时画多个向量的话, 要用列表来表示
ax.quiver([0,5,2],[0,3,4],[5,7,-2],[3,9,6],angles='xy', scale_units='xy', scale=1)

ax.grid()

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_xlim(-10, 15)
ax.set_ylim(-10, 15)

plt.show()
