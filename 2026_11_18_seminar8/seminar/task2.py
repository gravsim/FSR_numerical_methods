import numpy as np
from matplotlib import pyplot as plt

def f(t, y):
    return y ** 2

y0 = 1
a = 0
b = 0.9
n = 100
h = (b - a) / n

alpha1 = 1
beta1 = 3 / 2
beta2 = -1 / 2

y = [y0, y0 + h]
t = np.linspace(a, b, n)
for i in range(2, n):
    y.append(alpha1 * y[-1] + beta1 * h * f(t[i], y[-1]) + beta2 * h * f(t[i - 1], y[-2]))

plt.plot(t, y, '--', label="Численное")
plt.plot(t, 1 / (1 - t), '-', label="Аналитическое")
plt.legend()
plt.show()
