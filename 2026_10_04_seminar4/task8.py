import matplotlib.pyplot as plt
import numpy as np


def S(a, b, f, M):
    h = (b - a) / M
    x = np.linspace(a, b, M + 1)
    y = f(x)
    sum1 = np.sum(y)
    sum2 = np.sum(y[1:-1])
    sum3 = 2 * np.sum(y[1:-1:2])
    return h / 3 * (sum1 + sum2 + sum3)


a, b = 0.01, 2
arr = [a, b]
tol = 10**(-4)

def adapt(a, b, f, tol):
    M = 2
    S_01 = S(a, b, f, M)
    S_02 = S(a, b, f, 2 * M)

    if (abs(S_01 - S_02)/15 <= tol/M):
        return S_01
    else:
        c = (a + b)/2
        arr.append(c)
        S_11 = adapt(a, c, f, tol/2)
        S_21 = adapt(c, b, f, tol/2)
        return S_11 + S_21

def f(x):
    return np.sin(1/x)

print(adapt(a, b, f, tol))
arr = np.array(arr)
x = np.linspace(a, b, 500)
plt.plot(x, f(x), "k--")
plt.scatter(arr, f(arr))
plt.show()
