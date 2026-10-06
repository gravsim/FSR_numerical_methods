import matplotlib.pyplot as plt
import numpy as np


def Simpson(a, b, f, M):
    h = (b - a) / M
    x = np.linspace(a, b, M + 1)
    y = f(x)
    sum1 = np.sum(y)
    sum2 = np.sum(y[1:-1])
    sum3 = 2 * np.sum(y[1:-1:2])
    return h / 3 * (sum1 + sum2 + sum3)

a = 0.1
b = 2

arr = [a, b]
tol = 1e-4


def adaptive(a, b, f, tol):
    M = 2
    S_01 = Simpson(a, b, f, M)
    S_02 = Simpson(a, b, f, 2 * M)

    if np.abs(S_01 - S_02) / 15 <= tol / M:
        return S_02
    else:
        c = (a + b) / 2
        arr.append(c)
        S_11 = adaptive(a, c, f, tol / 2)
        S_21 = adaptive(c, b, f, tol / 2)
        return S_11 + S_21


def f(x):
    return np.sin(1/x)


print(adaptive(a, b, f, tol))
arr = np.array(arr)
x = np.linspace(a, b, 500)
plt.plot(x, f(x), "k--")
plt.scatter(arr, f(arr))
plt.show()
