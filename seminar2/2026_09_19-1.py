
import numpy as np
import scipy as sp
from scipy.interpolate import barycentric_interpolate, lagrange
from numpy import polyfit, polyval
import matplotlib.pyplot as plt

def u(x, g0, g1, g2):
    return g0 * np.exp(g1 * x + g2 * x ** 2)

x_observed = np.array([0, 1, 3])
u_observed = np.array([1, 0.9, 0.5])
ln_u = np.log(u_observed)


x = np.linspace(0, 3, 100)
poly = lagrange(x_observed, ln_u)
coef_s = poly.coef
gamma0 = np.exp(coef_s[2])
gamma1 = coef_s[1]
gamma2 = coef_s[0]
print(gamma0, gamma1, gamma2)
y = np.exp(polyval(poly.coef, x))
real_y = u(x, gamma0, gamma1, gamma2)

plt.plot(x_observed, u_observed, "o", label="observation")
plt.plot(x, y, label="polyval interpolation")
plt.plot(x, real_y, '--', label="u(x)")

plt.title(r'Интерполяция полинома $f=\gamma_0e^{\gamma_1x+\gamma_2x^2}$ для 3 точек')
plt.legend()
plt.savefig('1_interpolation.png', dpi=300)
plt.show()
