import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


w1 = 3
w2 = 4


def f_der(t, y):
    return np.array([y[2], y[3], -w1 ** 2 * y[0], -w2 ** 2 * y[1]])



def Euler(f, t0, y0, h, N):
    t_arr = np.linspace(t0, t0 + h * N, N + 1)
    y_arr = np.zeros((N + 1, 4))
    y_arr[0] = y0
    for i in range(N):
        y_arr[i + 1] = y_arr[i] + h * f(t_arr[i], y_arr[i])
    return t_arr, y_arr



h = 0.05
N = 200
t0 = 0
y0 = np.array([1, 0, 0, w2])
fig, ax = plt.subplots(ncols=2, nrows=1)


_, y_euler = Euler(f_der, t0, y0, h, N)
ax[0].plot(y_euler[:, 0], y_euler[:, 1], label="Euler")

sol = solve_ivp(f_der, [t0, t0 + h * N], y0, t_eval=np.linspace(t0, t0 + h * N, N + 1))
ax[1].plot(sol.y[0, :], sol.y[1, :], label="RK45")

ax[0].legend()
ax[1].legend()
plt.savefig("lissajous.png")
plt.show()
