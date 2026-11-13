import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def dy_dt(t, y):
    return np.array([3 * y[0], 2 * y[0] + y[1]])


def Euler(f, t0, y0, N, h):
    t_s = np.linspace(t0, t0 + h * N, N + 1)
    y_s = np.zeros((N + 1, 2))
    y_s[0] = y0
    for i in range(N):
        y_s[i + 1] = y_s[i] + h * f(t_s[i], y_s[i])
    return t_s, y_s


def RK2(f, t0, y0, N, h):
    t_s = np.linspace(t0, t0 + h * N, N + 1)
    y_s = np.zeros((N + 1, 2))
    y_s[0] = y0
    for i in range(N):
        k1 = h * f(t_s[i], y_s[i])
        k2 = h * f(t_s[i] + h / 2, y_s[i] + k1 / 2)
        y_s[i + 1] = y_s[i] + k2
    return t_s, y_s

N = 10
h = 0.1

t0 = 1
y0 = np.array([1, -0.5])
t_s1, y_s1 = Euler(dy_dt, t0, y0, N, h)
t_s2, y_s2 = RK2(dy_dt, t0, y0, N, h)

plt.plot(y_s1[:, 0], y_s1[:, 1], label="Euler")
plt.plot(y_s2[:, 0], y_s2[:, 1], label="RK2")

plt.legend()

plt.show()
