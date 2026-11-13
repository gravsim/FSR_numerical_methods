import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def Euler(f, t0, y0, h, N):
    y_arr = np.zeros((N + 1, 2))
    t_arr = np.linspace(t0, t0 + h * N, N + 1)
    y_arr[0] = y0
    for i in range(N):
        # print(y_arr[i])
        y_arr[i + 1] = y_arr[i] + h * f(t_arr[i], y_arr[i])
    return t_arr, y_arr


def RK2(f, t0, y0, h, N):
    y_arr = np.zeros((N + 1, 2))
    t_arr = np.linspace(t0, t0 + h * N, N + 1)
    y_arr[0] = y0
    for i in range(N):
        k1 = h * f(t_arr[i], y_arr[i])
        k2 = h * f(t_arr[i] + h / 2, y_arr[i] + k1 / 2)
        # print(y_arr[i])
        y_arr[i + 1] = y_arr[i] + k2
    return t_arr, y_arr


def dydt(t, y):
    return np.array([3 * y[0], 2 * y[0] + y[1]])


h = 0.1
t0 = 0
y0 = np.array([1, -0.5])
N = 10

t1, y1 = Euler(dydt, t0, y0, h, N)
t2, y2 = RK2(dydt, t0, y0, h, N)

print(y1, y2)

res = solve_ivp(dydt,[t0, t0 + h * N], y0, t_eval=np.linspace(t0, t0 + h * N, N + 1))

plt.plot(res.y[0, :], res.y[1, :], label='RK45')
plt.plot(y1[:, 0], y1[:, 1], label='Euler')
plt.plot(y2[:, 0], y2[:, 1], label='RK')
plt.legend()
plt.show()