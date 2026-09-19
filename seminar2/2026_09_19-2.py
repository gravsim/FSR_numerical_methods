
import numpy as np
from numpy import polyval, polyfit
from scipy.special import roots_chebyt
import matplotlib.pyplot as plt
N = 14
def f(x):
    return 1 / (1 + 25 * x ** 2)
bins = np.linspace(-1, 1, 1000)

x_linear = np.linspace(-1, 1, N)
x_cheb, _ = roots_chebyt(N)

coef_linear = polyfit(x_linear, f(x_linear), N - 1)
coef_cheb = polyfit(x_cheb, f(x_cheb), N - 1)

y_linear = polyval(coef_linear, bins)
y_cheb = polyval(coef_cheb, bins)

plt.plot(bins, f(bins), label="f(x)")
plt.plot(bins, y_linear, label="linear")
plt.plot(bins, y_cheb, label="cheb")


plt.title(r'Интерполяция полинома $f=\frac{1}{1+25x^2}$ для 14 точек')
plt.legend()
plt.savefig('2_interpolation.png', dpi=300)
plt.show()
