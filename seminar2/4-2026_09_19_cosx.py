
import numpy as np
from numpy import polyval, polyfit
from scipy.special import roots_chebyt
import matplotlib.pyplot as plt
N = 5
def f(x):
    return np.cos(x)
bins = np.linspace(0, 1.2, 1000)

x_linear = np.linspace(0, 1.2, N)


a = 0
b = 1.2

x_cheb =  (a + b) / 2 + (b - a ) / 2 * roots_chebyt(N)[0]

degree = 3
coef_linear = polyfit(x_linear, f(x_linear), degree)
coef_cheb = polyfit(x_cheb, f(x_cheb), degree)

y_linear = polyval(coef_linear, bins)
y_cheb = polyval(coef_cheb, bins)

cheb_error = np.max(np.abs(y_cheb - f(bins)))
linear_error = np.max(np.abs(y_linear - f(bins)))

print(f'cheb_error: {cheb_error}\nlinear_error: {linear_error}')
plt.plot(x_linear, f(x_linear), 'o', label="linear points")
plt.plot(x_cheb, f(x_cheb), 'o', label="cheb points")


plt.plot(bins, y_linear, label="linear")
plt.plot(bins, y_cheb, label="cheb")
plt.plot(bins, f(bins), '--', color='black', label="f(x)")


plt.title(r'Интерполяция полинома $f(x)=cos(x)$ для 4 точек')
plt.legend()
plt.savefig('4_interpolation.png', dpi=300)
plt.show()
