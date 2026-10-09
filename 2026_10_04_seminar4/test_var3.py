
import numpy as np
import matplotlib.pyplot as plt


def Trapezoid(a, b, f, n):
    M = 2 ** n
    h = (b - a) / M
    bins = np.linspace(a, b, M + 1)
    y = f(bins)
    T = h / 2 * (2 * np.sum(y) - y[0] - y[-1])
    return T


def Romberg(a, b, f, eps):
    R = [[Trapezoid(a, b, f, 0)],
         [Trapezoid(a, b, f, 1)]]
    R[1].append(R[1][0] + (R[1][0] - R[0][0]) / (4 ** 1 + 1))
    i = 2
    while np.abs(R[-1][-1] - R[-1][-2]) > eps:
        R.append([])
        R[i].append(Trapezoid(a, b, f, i))
        for j in range(1, i + 1):
            R[i].append(R[i][j - 1] + (R[i][j - 1] - R[i - 1][j - 1]) / (4 ** j - 1))
        i += 1
    return R[-1][-1]


def f(x):
    return np.tan(x)

a = 0.2
b = 1.2
N = 10
answer = np.log(np.cos(0.2) / np.cos(1.2))
eps = 1e-3

print(f'answer: {answer}')
print(f'Romberg: {Romberg(a, b, f, eps)}')
print(f'Romberg error: {Romberg(a, b, f, eps) - answer}')

