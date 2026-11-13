import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def dy_dt(t, y):
    return np.array([y[0], 3 * y[0] - y[1]])

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
N = 10
starts = np.array([[1, 1], [-1, 1], [1, -1], [-1, -1]])
for i, y0 in enumerate(starts):
    t0 = 0
    t_arr, y_arr = RK2(dy_dt, y0, t0, h, N)
    plt.plot(y_arr[:, 0], y_arr[:, 1])
plt.gca().set_aspect("equal")
plt.grid()
plt.show()