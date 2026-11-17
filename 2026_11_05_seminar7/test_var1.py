import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

m = 1
g = 9.81

def RK2(f, t0, y0, N, h):
    t_arr = np.linspace(t0, t0 + h * N, N + 1)
    y_arr = np.zeros((N + 1, 4))
    y_arr[0] = y0
    for i in range(N):
        k1 = h * f(t_arr[i], y_arr[i])
        k2 = h * f(t_arr[i] + h / 2, y_arr[i] + k1 / 2)
        y_arr[i + 1] = y_arr[i] + k2
    return t_arr, y_arr


def f_der(t, y):
    v_x = y[2]
    v_y = y[3]
    a_x = -0.2 * np.sqrt(y[2] ** 2 + y[3] ** 2) * y[2] / m
    a_y = -0.2 * np.sqrt(y[2] ** 2 + y[3] ** 2) * y[3] / m - g
    return np.array([v_x, v_y, a_x, a_y])



def f_der_no_air(t, y):
    v_x = y[2]
    v_y = y[3]
    a_x = 0
    a_y = - g
    return np.array([v_x, v_y, a_x, a_y])

h = 0.01
N = 50
t0 = 0
y0 = np.array([0, 0, 5 * np.sqrt(3) / 2, 5 * 1 / 2])

t_s1, y_s1 = RK2(f_der, t0, y0, N, h)

plt.plot(y_s1[:, 0], y_s1[:, 1], label="With air")
t_s2, y_s2 = RK2(f_der_no_air, t0, y0, N, h)
plt.plot(y_s2[:, 0], y_s2[:, 1], label="No air")
plt.legend()
plt.grid()
plt.show()