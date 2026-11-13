import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def dy_dt(t, y):
    return np.array([y[1], np.sin(2 * t) - 2 * y[1] - 9 * y[0]])

def Euler(f, y0, t0, h, N):
    t_arr = np.linspace(t0, t0 + h * N, N + 1)
    y_arr = np.zeros((N + 1, 2))
    y_arr[0] = y0
    for i in range(N):
        y_arr[i + 1] = y_arr[i] + h * f(t_arr[i], y_arr[i])
    return t_arr, y_arr


def RK2(f, y0, t0, h, N):
    t_arr = np.linspace(t0, t0 + h * N, N + 1)
    y_arr = np.zeros((N + 1, 2))
    y_arr[0] = y0
    for i in range(N):
        k1 = h * f(t_arr[i], y_arr[i])
        k2 = h * f(t_arr[i] + h / 2, y_arr[i] + k1 / 2)
        y_arr[i + 1] = y_arr[i] + k2
    return t_arr, y_arr


h = 0.1
y0 = np.array([2, 1])
t0 = 0
N = 10

fig, ax = plt.subplots(ncols=2, nrows=1)


t_arr1, y_arr1 = Euler(dy_dt, y0, t0, h, N)
ax[0].plot(y_arr1[:, 0], y_arr1[:, 1], label="Фазовый портрет Euler")

t_arr2, y_arr2 = RK2(dy_dt, y0, t0, h, N)
ax[0].plot(y_arr2[:, 0], y_arr2[:, 1], label="Фазовый портрет RK2")

ax[1].plot(t_arr2, y_arr2[:, 1] ** 2 / 2 + 9 * y_arr2[:, 0] ** 2 / 2, label="Энергия")
ax[0].legend()
ax[1].legend()
plt.show()
