
import numpy as np
import scipy as sp
from scipy.interpolate import barycentric_interpolate
import matplotlib.pyplot as plt

def function(x):
    return np.exp(3 * x) * np.sin(200 * x ** 2) / (1 + 20 * x ** 2)


observed_x, _ = sp.special.roots_chebyt(20)
observed_y = function(observed_x)
x = np.linspace(np.min(observed_x), np.max(observed_x), 1000)
true_y = function(x)
y = barycentric_interpolate(observed_x, observed_y, x)
plt.plot(observed_x, observed_y, "o", label="observation")
plt.plot(x, y, label="barycentric interpolation")
plt.plot(x, true_y, label="function")
plt.title(r'Интерполяция полинома $f=\frac{e^{3x}\sin{200x^2}}{1+20x^2}$ для 20 точек')
plt.legend()
plt.savefig('6_interpolation.png', dpi=300)
plt.show()
