import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def y_der(t, y):
    length = (y[0] ** 2 + y[1] ** 2) ** (3 / 2)
    return np.array([y[2], y[3], -4 * np.pi ** 2 * y[0] / length, -4 * np.pi ** 2 * y[1] / length])


def Euler(f, t0, y0, h, N):
    t_arr = np.linspace(t0, t0 + h * N, N + 1)
    y_arr = np.zeros((N + 1, 4))
    y_arr[0] = y0
    for i in range(N):
        y_arr[i + 1] = y_arr[i] + h * f(t_arr[i], y_arr[i])
    return t_arr, y_arr



def RK2(f, t0, y0, h, N):
    t_arr = np.linspace(t0, t0 + h * N, N + 1)
    y_arr = np.zeros((N + 1, 4))
    y_arr[0] = y0
    for i in range(N):
        k1 = h * f(t_arr[i], y_arr[i])
        k2 = h * f(t_arr[i] + h / 2, y_arr[i] + k1 / 2)
        y_arr[i + 1] = y_arr[i] + k2
    return t_arr, y_arr


h = 0.005
N = 200
t0 = 0
y0 = np.array([1, 0, 0, 2 * np.pi])
fig, ax = plt.subplots(ncols=2, nrows=1)


t_euler, y_euler = Euler(y_der, t0, y0, h, N)
ax[0].plot(y_euler[:, 0], y_euler[:, 1], label="Euler")

t_rk2, y_rk2 = RK2(y_der, t0, y0, h, N)
ax[0].plot(y_rk2[:, 0], y_rk2[:, 1], label="RK2")


ax[1].plot(t_rk2, (y_rk2[:, 2] ** 2 + y_rk2[:, 3] ** 2) / 2 - 4 * np.pi ** 2 / np.sqrt((y_rk2[:, 0] ** 2 + y_rk2[:, 1] ** 2)), label="Энергия")
ax[0].legend()
ax[1].legend()
plt.show()
