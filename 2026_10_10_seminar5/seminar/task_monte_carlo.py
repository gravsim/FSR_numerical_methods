import numpy as np
from scipy.special import roots_legendre
from scipy.special import erf
import matplotlib.pyplot as plt


def f(x, y):
    return x * y**2

a, b = 0, 2
N = 1000000
V = 1  # Объём - площадь треугольника

x = np.random.uniform(a, b, N)

# Так не делаем
# y = []
# for i in x:
#     y.append(np.random.uniform(0, i/2))


y = np.random.uniform(a, b, N)
ind = np.where(y < x/2)

x = x[ind]
y = y[ind]

N1 = len(x)

r = f(x, y)
res = np.sum((V/N1) * r)
print(res)
print(abs(res - 4/15))

plt.scatter(x, y)
plt.show()