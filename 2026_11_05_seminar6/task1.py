import numpy as np
import matplotlib.pyplot as plt

def f_der(x, y):
    return (2 * x + y) / (3 * x + 4 * y)


def Euler(f, y0, t0, N, h):
    t_s = np.linspace(t0, t0 + h * (N + 1), N + 1)
    y_s = np.zeros(N + 1)
    y_s[0] = y0
    for i in range(N):
        y_s[i + 1] = y_s[i] + h * f(t_s[i], y_s[i])
    return t_s, y_s


def RK2(f, y0, t0, N, h):
    t_s = np.linspace(t0, t0 + h * (N + 1), N + 1)
    y_s = np.zeros(N + 1)
    y_s[0] = y0
    for i in range(N):
        k1 = h * f(t_s[i], y_s[i])
        k2 = h * f(t_s[i] + h / 2, y_s[i] + k1 / 2)
        y_s[i + 1] = y_s[i] + k2
    return t_s, y_s


N = 10
h = 0.1


t0 = 1
y0 = -0.2
t_s1, y_s1 = Euler(f_der, y0, t0, N, h)
t_s2, y_s2 = RK2(f_der, y0, t0, N, h)
plt.plot(t_s1, y_s1, label="Euler")
plt.plot(t_s2, y_s2, label="RK2")
plt.show()
