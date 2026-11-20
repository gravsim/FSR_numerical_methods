import numpy as np
import matplotlib.pyplot as plt


def f_der(t, y):
    return y ** 2


def method(f, y0, t0, a, b, N):
    h = (b - a) / N
    t = np.linspace(t0, t0 + h * N, N + 1)
    y = [y0, y0 + h * f(t0, y0)]
    for i in range(1, N):
        y.append(y[-2] + 2 * h * f(t[i], y[-1]))
    return t, y


t0 = 0
y0 = 1
a = 0
b = 0.9
N = 100
t, y = method(f_der, y0, t0, a, b, N)
C = -1
plt.plot(t, y, label="Numerical")
plt.plot(t, -1 / (t + C), label="Analytical")
plt.legend()
plt.show()