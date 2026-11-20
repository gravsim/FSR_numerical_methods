import numpy as np
import matplotlib.pyplot as plt


def f_der(t, y):
    return y * np.cos(3 * t)


def method(f, t0, y0, a, b, N):
    h = (b - a) / N
    t = np.linspace(t0, t0 + h * N, N + 1)
    y = [y0, y0 + h * f(t0, y0)]
    for i in range(1, N):
        y.append(y[-1] + h * (3 / 2 * f(t[i], y[-1]) - 1 / 2 * f(t[i - 1], y[-2])))
    return t, y

t0 = 0
y0 = 1
a = 0
b = 5
N = 100
t, y = method(f_der, t0, y0, a, b, N)

plt.plot(t, y, label="Numerical")
plt.plot(t, np.exp(np.sin(3 * t) / 3), label="Analytical")
plt.legend()
plt.show()