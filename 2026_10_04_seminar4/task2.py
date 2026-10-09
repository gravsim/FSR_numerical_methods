
import numpy as np
import matplotlib.pyplot as plt


def Trapezoid(a, b, f, n):
    M = 2 ** (n - 1)
    h = (b - a) / M
    bins = np.linspace(a, b, M + 1)
    f_s = f(bins)
    T = h / 2 * (2 * np.sum(f_s) - f(a) - f(b))
    return T


def Romberg(a, b, f, N):
    R = np.zeros((N, N))
    R[:, 0] = np.array([Trapezoid(a, b, f, n) for n in range(1, N + 1)])
    for i in range(N):
        for j in range(1, i + 1):
            R[i, j] = R[i, j - 1] + 1 / (4 ** j - 1) * (R[i, j - 1] - R[i - 1, j - 1])
    # print(R)
    return R[-1, -1]


def f(x):
    return 4 / (1 + x ** 2)


a = 0
b = 1
M = 3
N = 20

print(np.pi)
print(f'Trapezoid: {Trapezoid(a, b, f, M)}')
print(f'Trapezoid error: {Trapezoid(a, b, f, M) - np.pi}')
print(f'Romberg: {[Romberg(a, b, f, N) - np.pi for N in range(1, 30)]}')
print(f'Romberg error: {Romberg(a, b, f, N) - np.pi}')

