import numpy as np
import matplotlib.pyplot as plt

# 生成 x 轴数据
x = np.linspace(-np.pi, np.pi, 100)

# 计算正切函数的值
y = np.tan(x)

# 绘制图像
fig, ax = plt.subplots()
ax.plot(x, y)

# 添加垂直虚线
for k in range(-3, 4):
    xk = np.pi/2 + k*np.pi
    line = np.linspace(ax.get_ylim()[0], ax.get_ylim()[1], 100)[:, None]
    ax.plot(xk*np.ones((100,1)), line, linestyle='--', color='gray')

# 显示图像
plt.show()