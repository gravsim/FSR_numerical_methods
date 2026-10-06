
import numpy as np


def S(a, b, f, M):
    h = (b - a) / M
    x = np.linspace(a, b, M + 1)
    y = f(x)
    sum1 = np.sum(y)
    sum2 = np.sum(y[1:-1])
    sum3 = 2 * np.sum(y[1:-1:2])
    return h / 3 * (sum1 + sum2 + sum3)


def T(a, b, f, M):
    h = (b - a) / M
    x = np.linspace(a, b, M + 1)
    y = f(x)
    return h / 2 * (2 * np.sum(y) - f(a) - f(b))


def f(x):
    return 4 / (1 + np.power(x, 2))



a, b = 0, 1
M = 60

print(T(a, b, f, M))
print(S(a, b, f, M))
print(S(a, b, f, M-1))
print(np.pi)



