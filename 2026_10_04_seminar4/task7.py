
import numpy as np


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
        return adaptive(c, b, f, eps / 2) + adaptive(a, c, f, eps / 2)


def f(x):
    return np.exp(2 * x) * np.sin(3 * x)


def F(x):
    return 4 / 13 * (1 / 2 * np.sin(3 * x) - 3 / 4 * np.cos(3 * x)) * np.exp(2 * x)

a = 0
b = 2
eps = 1e-4
answer = F(2) - F(0)
print(f"answer: {answer}")
print(f"adaptive: {adaptive(a, b, f, eps)}")
print(f"adaptive error: {adaptive(a, b, f, eps) - answer}")