import numpy as np
import matplotlib.pyplot as plt


alpha = 1
w = 1

def f_der(y):
    return np.array([y[1], -2 * alpha * y[1] - w ** 2 * y[0]])


def Euler(f, t0, y0, h, N):
    t = np.linspace(t0, t0 + h * N, N + 1)
    y = np.zeros((N + 1, 2))
    y[0] = y0
    for i in range(N):
        y[i + 1] = y[i] + h * f(y[i])
    return t, y


def method(f, t0, y0, a, b, N):
    h = (b - a) / N
    t = np.linspace(t0, t0 + h * N, N + 1)
    y = [*(Euler(f, t0, y0, h, 3)[1])]
    for i in range(3, N):
        p = y[-1] + h / 24 * (55 * f(y[-1]) - 59 * f(y[-2]) + 37 * f(y[-3]) - 9 * f(y[-4]))
        next = y[-1] + h / 24 * (9 * f(p) + 19 * f(y[-1]) - 5 * f(y[-2]) +f(y[-3]))
        y.append(next)
    return t, y

t0 = 0
y0 = np.array([np.pi / 3, 0])
a = 0
b = 10
N = 100
t, y = method(f_der, t0, y0, a, b, N)
y = np.array(y)
plt.plot(t, y[:, 0], label="Numerical")
plt.legend()
plt.show()
