import numpy as np
import matplotlib.pyplot as plt

g = 9.81
L = 1

w = np.sqrt(g / L)

def RK2(f, t0, y0, h, N):
    t_arr = np.linspace(t0, t0 + h * N, N + 1)
    y_arr = np.zeros((N + 1, 2))
    y_arr[0] = y0
    for i in range(N):
        k1 = h * f(t_arr[i], y_arr[i])
        k2 = h * f(t_arr[i] + h / 2, y_arr[i] + k1 / 2)
        y_arr[i + 1] = y_arr[i] + k2
    return t_arr, y_arr


def f_der(t, y):
    return np.array([y[1], -w ** 2 * y[0]])


def f_der_phis(t, y):
    return np.array([y[1], -w ** 2 * np.sin(y[0])])

t0 = 0

h = 0.01
N = 1000

fig, ax = plt.subplots(nrows=1, ncols=4)


y0 = np.pi / 3
t_arr, y_arr = RK2(f_der, t0, y0, h, N)
ax[0].plot(L * np.sin(y_arr[:, 0]), -L * np.cos(y_arr[:, 0]), label="Math")

t_arr2, y_arr2 = RK2(f_der_phis, t0, y0, h, N)
ax[1].plot(L * np.sin(y_arr2[:, 0]), -L * np.cos(y_arr2[:, 0]), label="Phis")

t, y = RK2(f_der, t0, y0, h, N)
ax[2].plot(y[:, 0], y[:, 1], label="Math")

t2, y2 = RK2(f_der_phis, t0, y0, h, N)
ax[3].plot(y2[:, 0], y2[:, 1], label="Phis")

ax[0].set_aspect('equal')
ax[1].set_aspect('equal')
ax[2].set_aspect('equal')
ax[3].set_aspect('equal')
ax[0].legend()
ax[1].legend()
ax[2].legend()
ax[3].legend()
plt.show()
