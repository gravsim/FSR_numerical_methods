
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

a = 0
b = 1
points = [a, b]
epsabs = 1e-5

def f(x):
    return 4 / (1 + x ** 2)


def trapezoid(a, b, f, M):
    h = (b - a) / M
    bins = np.linspace(a, b, M + 1)
    f_s = f(bins)
    T = h / 2 * (2 * np.sum(f_s) - f(a) - f(b))
    return T


def adaptive_quad(a, b, f, tol):
    M = 2
    S_1 = trapezoid(a, b, f, M)
    S_2 = trapezoid(a, b, f, 2 * M)
    if np.abs(S_1 - S_2) < 15 * tol / M:
        return S_2
    else:
        c = (a + b) / 2
        points.append(c)
        return adaptive_quad(a, c, f, tol / 2) + adaptive_quad(c, b, f, tol / 2)



print(f'Trapezoid: {adaptive_quad(a, b, f, epsabs) - np.pi}')
quad = quad(f, a, b, epsabs=epsabs)
print(f'quad: {quad}')
points = np.array(points)
plt.scatter(points, f(points))
bins = np.linspace(a, b, 1000)
plt.plot(bins, f(bins))
plt.show()
