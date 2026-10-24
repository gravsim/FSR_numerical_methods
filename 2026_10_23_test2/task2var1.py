
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.legendre import leggauss

def core(t, s):
    return np.cos(s) + 12 / np.pi ** 3 * t * s


def heterogeneity(t):
    return np.pi ** 2 * np.sin(t)


def analytical(t):
    return -4 + 6 * t / np.pi + np.pi ** 2 * np.sin(t)


def get_x(t, w):
    A = []
    for i in range(len(t)):
        tmp = []
        for j in range(len(t)):
            tmp.append(w[j] * core(t[i], t[j]))
        A.append(tmp)
    A = np.array(A) - np.eye(len(t))
    B = -heterogeneity(t)
    return np.linalg.solve(A, B)


a = np.pi / 2
b = 3 * np.pi / 2
M = 3
t, w = leggauss(M + 1)
t = (a + b) / 2 + (b - a) / 2 * t
w = (b - a) / 2 * w
x = get_x(t, w)

plt.plot(t, x, label='numerical')
plt.plot(t, analytical(t), '--', label='analytical', color='black')
plt.legend()
plt.show()
