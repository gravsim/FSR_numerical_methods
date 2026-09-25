
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from numpy import polyval

def f(x):
    return np.sin(3 * x / 2 + 1)
a = 0
b = np.pi
N = 9
x_linear = np.linspace(a, b, N)
k = np.arange(0, N, 1)
x_cheb = (a + b) / 2 + (b - a) / 2 * np.cos(np.pi * (2 * k - 1) / (2 * N))

bins = np.linspace(a, b, 100)

coefs_linear = lagrange(x_linear, f(x_linear)).coef
coefs_cheb = lagrange(x_cheb, f(x_cheb)).coef

y_linear = polyval(coefs_linear, bins)
y_cheb = polyval(coefs_cheb, bins)

plt.plot(bins, f(bins), label='true')
plt.plot(x_linear, y_linear, label='linear')
plt.plot(x_cheb, y_cheb, label='cheb')
plt.scatter(x_linear, f(x_linear))
plt.scatter(x_cheb, f(x_cheb))
plt.savefig('task2var1.png', dpi=300)
plt.show()
