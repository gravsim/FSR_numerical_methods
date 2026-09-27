
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def function(x):
    return 1 / (1 + 25 * x ** 2)

x_observed = np.linspace(-7, 7, 11)
y_observed = function(x_observed)
bins = np.linspace(-7, 7, 1000)
cs = CubicSpline(x_observed, y_observed)

fig, ax = plt.subplots(figsize=(6.5, 4))
ax.plot(x_observed, y_observed, 'o', label='Data')
ax.plot(bins, function(bins), label='True')
ax.plot(bins, cs(bins), label='Cubic spline')
plt.legend()
plt.savefig('1_cubic_spline.png', dpi=300)
plt.show()
