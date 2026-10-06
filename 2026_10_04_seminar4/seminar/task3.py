
import numpy as np


def Trapezoid(a, b, f, M):
    h = (b - a) / M
    x = np.linspace(a, b, M + 1)
    y = f(x)
    return h / 2 * (2 * np.sum(y) - f(a) - f(b))


def Simpson(a, b, f, M):
    h = (b - a) / M
    x = np.linspace(a, b, M + 1)
    y = f(x)
    sum1 = np.sum(y)
    sum2 = np.sum(y[1:-1])
    sum3 = 2 * np.sum(y[1:-1:2])
    return h / 3 * (sum1 + sum2 + sum3)


def f(x):
    return 1 / (x + 4)

a, b = 0, 2
M_t = 16 # Илюха считал
M_s = 4 # Вася считала

print(Trapezoid(a, b, f, M_t) - np.log(3/2))
print(Simpson(a, b, f, M_s) - np.log(3/2))


