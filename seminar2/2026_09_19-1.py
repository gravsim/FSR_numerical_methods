
import numpy as np
import scipy as sp
from scipy.interpolate import barycentric_interpolate, lagrange
from numpy import polyfit
import matplotlib.pyplot as plt

def u(x):
    return np.exp(2 * x)

x_observed = np.array([0, 1, 3])
y_observed = np.array([1, 0.9, 0.5])

x = np.linspace(0, 3, 100)
poly = lagrange(x_observed, y_observed)
print(poly)
# sp.interpolate.lagrange()
observed_x, _ = sp.special.roots_chebyt(20)
observed_y = u(observed_x)
x = np.linspace(np.min(observed_x), np.max(observed_x), 1000)
true_y = u(x)
y = barycentric_interpolate(observed_x, observed_y, x)
plt.plot(observed_x, observed_y, "o", label="observation")
plt.plot(x, y, label="barycentric interpolation")
plt.plot(x, true_y, label="function")
plt.title(r'Интерполяция полинома $f=\sin{6x}+sign{x+e^{2x}}$ для 20 точек')
plt.legend()
plt.savefig('5_interpolation.png', dpi=300)
plt.show()
