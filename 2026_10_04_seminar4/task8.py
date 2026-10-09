
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

a = 0.1
b = 2
points = [a, b]


def f(x):
    return np.sin(1 / x)


def Simpson(a, b, f, M):
    h = (b - a) / M
    bins = np.linspace(a, b, M + 1)
    y = f(bins)
    return h / 3 * (np.sum(y) + np.sum(y[1:-1]) + 2 * np.sum(y[1:-1:2]))


def adaptive(a, b, f, eps):
    M = 2
    S_1 = Simpson(a, b, f, M)
    S_2 = Simpson(a, b, f, 2 * M)
    if np.abs(S_1 - S_2) / 15 <= eps / M:
        return S_2
    else:
        c = (a + b) / 2
        points.append(c)
        return adaptive(c, b, f, eps / 2) + adaptive(a, c, f, eps / 2)


result = adaptive(a, b, f, 1e-15)
print(f'Quad: {quad(f, a, b)[0]}')

print(f'Simpson: {Simpson(a, b, f, 10000000)}')
print(f'Simpson error: {Simpson(a, b, f, 10000000) - quad(f, a, b)[0]}')

print(f'Adaptive: {result}')
print(f'Adaptive error: {result - quad(f, a, b)[0]}')
bins = np.linspace(a, b, 1000)
points = np.array(points)
plt.plot(bins, f(bins), label='f(x)')
plt.scatter(points, f(points), label='points')
plt.legend()
plt.show()

