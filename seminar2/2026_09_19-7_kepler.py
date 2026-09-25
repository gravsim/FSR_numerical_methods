
import numpy as np
from numpy import polyval
from scipy.special import roots_chebyt
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

a = 1.2
b = 1

def x(t):
    return a * np.cos(t)

def y(t):
    return b * np.sin(t)

N = 5
bins = np.linspace(0, 2 * np.pi, 1000)

t_linear = np.linspace(0, 2 * np.pi, N)
a1 = 0
b1 = 2 * np.pi

t_cheb =  (a1 + b1) / 2 + (b1 - a1) / 2 * roots_chebyt(N)[0]

x_coef_linear = lagrange(t_linear, x(t_linear)).coef
y_coef_linear = lagrange(t_linear, y(t_linear)).coef
x_coef_cheb = lagrange(t_cheb, x(t_cheb)).coef
y_coef_cheb = lagrange(t_cheb, y(t_cheb)).coef

x_linear = polyval(x_coef_linear, bins)
y_linear = polyval(y_coef_linear, bins)
x_cheb = polyval(x_coef_cheb, bins)
y_cheb = polyval(y_coef_cheb, bins)

fig, ax = plt.subplots(1, 1, figsize=(12, 5))

ax.plot(x(t_linear), y(t_linear), 'o', label="linear points")
ax.plot(x(t_cheb), y(t_cheb), 'o', label="cheb points")

ax.plot(x_linear, y_linear, label="linear", color='red')
ax.plot(x_cheb, y_cheb, label="cheb", color='green')
ax.plot(x(bins), y(bins), '--', color='black', label="f(x)")

ax.set_title(r'Эллипс $a=1.2, b=1$ для 5 точек')
ax.legend()

plt.savefig('7_interpolation.png', dpi=300)
plt.show()
