
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.legendre import leggauss

def core(t, s):
    return np.sin(s) + s * np.cos(t)


def right(t):
    return 1 - 2 * t / np.pi


def analytical(t):
    return 1 - 2 * t / np.pi - np.pi ** 2 / 18 * np.cos(t)


def get_x(a, b, t, M):
    h = (b - a) / M
    A = []
    for i in range(len(t)):
        tmp = []
        for j in range(len(t)):
            w = 1
            if 0 < j < M:
                w = 2
                if j % 1 == 0:
                    w = 4
            tmp.append(w * core(t[i], t[j]))
        A.append(tmp)

    A = np.array(A)
    A = h / 3 * A - np.eye(len(t))
    B = -right(t)
    return np.linalg.solve(A, B)


a = 0
b = np.pi
M = 4
t = np.linspace(a, b, M + 1)
plt.plot(t, analytical(t), label='analytical')
plt.plot(t, get_x(a, b, t, M), label='numerical')
plt.legend()
plt.show()
