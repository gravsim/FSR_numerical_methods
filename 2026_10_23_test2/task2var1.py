
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.legendre import leggauss

def core(t, s):
    return np.cos(s) + 12 / np.pi ** 3 * t * s


def heterogeneity(t):
    return np.pi ** 2 * np.sin(t)


def analytical(t):
    return -4 + 6 * t / np.pi + np.pi ** 2 * np.sin(t)


def get_x(a, b, t, M):
    A = []
    h = (b - a) / M
    for i in range(len(t)):
        tmp = []
        for j in range(len(t)):
            w = 1 if j == 0 or j == M else 2
            tmp.append(w * core(t[i], t[j]))
        A.append(tmp)
    A = h / 2 * np.array(A) - np.eye(len(t))
    b = -heterogeneity(t)
    return np.linalg.solve(A, b)


a = np.pi / 2
b = 3 * np.pi / 2
M = 100
t = np.linspace(a, b, M + 1)
x = get_x(a, b, t, M)

plt.plot(t, x, label='numerical')
plt.plot(t, analytical(t), label='analytical')
plt.legend()
plt.show()
