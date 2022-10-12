'''
	@author ： yanan-zhang
	@software : PyCharm
	@file : Gradient Descent.py
	@time : 2022/10/12 10:17
'''

import matplotlib.pyplot as plt
import numpy as np

# 十组Pokemon数据Xcp,Ycp
x_data = [388., 333., 328., 207., 226., 25., 179., 60., 208., 606.]
y_data = [640., 633., 619., 393., 428., 27., 193., 66., 226., 1591.]

# ydata = b + w * xdata

x = np.arange(-200,-100,1)
y = np.arange(-5,5,0.1)
Z = np.zeros((len(x), len(y)))
X, Y = np.meshgrid(x,y)
for i in range(len(x)):
    for j in range(len(y)):
        b = x[i]
        w = y[j]
        Z[j][i] = 0
        for n in range(len(x_data)):
            Z[j][i] += (y_data[n] - b - w * x_data[n]) ** 2
        Z[j][i] /= len(x_data)


# 设置初始w0, b0, learning rate, iteration
b = -120
w = -4
lr = 1
iteration = 100000

b_history = [b]
w_history = [w]

lr_b = 0.0
lr_w = 0.0

for i in range(iteration):

    b_grad = 0.0
    w_grad = 0.0

    for j in range(len(x_data)):
        w_grad += 2.0 * x_data[j] * (b + w * x_data[j] - y_data[j])
        b_grad += 2.0 * (b + w * x_data[j] - y_data[j])

    lr_w = lr_w + w_grad ** 2
    lr_b = lr_b + b_grad ** 2
    b = b - b_grad * lr/np.sqrt(lr_b)
    w = w - w_grad * lr/np.sqrt(lr_w)

    b_history.append(b)
    w_history.append(w)

plt.contourf(x,y,Z, 50, alpha=0.5, cmap=plt.get_cmap('jet'))
plt.plot([-188.4], [2.67], 'x', ms=12, markeredgewidth=3, color='orange')
plt.plot(b_history, w_history, 'o-', ms=3, lw=1.5, color='black')
plt.xlim(-200, -100)
plt.ylim(-5, 5)
plt.xlabel(r'$b$', fontsize=16)
plt.ylabel(r'$w$', fontsize=16)
plt.show()
