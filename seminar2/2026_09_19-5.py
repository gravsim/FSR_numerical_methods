
import numpy as np
import scipy as sp
from scipy.interpolate import barycentric_interpolate, lagrange
from numpy import polyfit
import matplotlib.pyplot as plt

def function(x):
    return np.sin(6 * x) + np.sign(np.sin(x + np.exp(2 * x)))


# sp.interpolate.lagrange()
observed_x, _ = sp.special.roots_chebyt(20)
observed_y = function(observed_x)
x = np.linspace(np.min(observed_x), np.max(observed_x), 1000)
true_y = function(x)
y = barycentric_interpolate(observed_x, observed_y, x)
plt.plot(observed_x, observed_y, "o", label="observation")
plt.plot(x, y, label="barycentric interpolation")
plt.plot(x, true_y, label="function")
plt.title(r'Интерполяция полинома $f=\sin{6x}+sign{x+e^{2x}}$ для 20 точек')
plt.legend()
plt.savefig('5_interpolation.png', dpi=300)
plt.show()
