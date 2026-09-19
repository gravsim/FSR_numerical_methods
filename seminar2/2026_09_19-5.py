
import numpy as np
from IPython.core.pylabtools import figsize
from numpy import polyval, polyfit
from scipy.special import roots_chebyt
from numpy import polyfit
import matplotlib.pyplot as plt

def f(x):
    return np.sin(6 * x) + np.sign(np.sin(x + np.exp(2 * x)))

N = 10
bins = np.linspace(-1, 1, 1000)

x_linear = np.linspace(-1, 1, N)
x_cheb = roots_chebyt(N)[0]

coef_linear = polyfit(x_linear, f(x_linear), N - 1)
coef_cheb = polyfit(x_cheb, f(x_cheb), N - 1)

y_linear = polyval(coef_linear, bins)
y_cheb = polyval(coef_cheb, bins)

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

ax[0].plot(x_linear, f(x_linear), 'o', label="linear points")
ax[0].plot(x_cheb, f(x_cheb), 'o', label="cheb points")

ax[0].plot(bins, y_linear, label="linear", color='red')
ax[0].plot(bins, y_cheb, label="cheb", color='green')
ax[0].plot(bins, f(bins), '--', color='black', label="f(x)")

ax[0].set_title(r'$f(x)=\sin(6x)+sign(\sin(x+e^{2x}))$ для 10 точек', loc='left')
ax[0].legend()


linear_error = np.abs(y_linear - f(bins))
cheb_error = np.abs(y_cheb - f(bins))

ax[1].plot(bins, linear_error, label="linear", color='red')
ax[1].plot(bins, cheb_error, label="cheb", color='green')
ax[1].legend()
ax[1].set_title(r'Ошибки', loc='left')

plt.savefig('5_interpolation.png', dpi=300)
plt.show()
