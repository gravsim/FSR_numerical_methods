
import numpy as np
from numpy import polyval, polyfit
from scipy.special import roots_chebyt
import matplotlib.pyplot as plt
N = 5
def f(x):
    return np.sin(x)
bins = np.linspace(0, np.pi, 1000)


x_half_pi = (roots_chebyt(N)[0] + 1) * np.pi / 4
x_pi = (roots_chebyt(N)[0] + 1) * np.pi / 2

coef_half_pi = polyfit(x_half_pi, f(x_half_pi), N - 1)
coef_pi = polyfit(x_pi, f(x_pi), N - 1)

y_half_pi = polyval(coef_half_pi, bins)
y_pi = polyval(coef_pi, bins)

plt.plot(x_half_pi, f(x_half_pi), 'o', label="half pi points")
plt.plot(x_pi, f(x_pi), 'o', label="pi points")


plt.plot(bins, y_pi, label="pi")
plt.plot(bins, y_half_pi, label="half_pi")
plt.plot(bins, f(bins), '--', color='black', label="f(x)")


plt.title(r'Интерполяция полинома $f(x)=sin(x)$ для 5 точек')
plt.legend()
plt.savefig('3_interpolation.png', dpi=300)
plt.show()
