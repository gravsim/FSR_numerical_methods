
import numpy as np
import scipy as sp
from scipy.interpolate import barycentric_interpolate
import matplotlib.pyplot as plt

def f(x):
    return np.exp(3 * x) * np.sin(200 * x ** 2) / (1 + 20 * x ** 2)

N = 10
bins = np.linspace(-1, 1, 1000)

points_range = np.arange(51, 201, 10)
errors = np.array([])
for k in points_range:
    x = sp.special.roots_chebyt(k)[0]
    y = barycentric_interpolate(x, f(x), bins)
    error = np.max(np.abs(y - f(bins)))
    errors = np.append(errors, error)

x = sp.special.roots_chebyt(N)[0]
y = barycentric_interpolate(x, f(x), bins)
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

ax[0].plot(x, f(x), 'o', label="points")
ax[0].plot(bins, y, label="cheb")
ax[0].plot(bins, f(bins), label="f(x)")

ax[0].set_title(r'$f(x)=\sin(6x)+sign(\sin(x+e^{2x}))$ для 10 точек', loc='left')
ax[0].legend()


ax[1].plot(points_range, errors, label="error", color='red')
ax[1].legend()
ax[1].set_title(r'Ошибки при разном числе точек', loc='left')
ax[1].set_xlabel('Число точек')
ax[1].set_ylabel('Ошибка')
plt.savefig('6_interpolation.png', dpi=300)
plt.show()
