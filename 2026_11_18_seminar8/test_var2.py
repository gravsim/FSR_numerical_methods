import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve



def f_der(t, y):
    return np.array([y[1], np.sin(2 * t) - 2 * y[1] - 9 * y[0]])


def Euler_impl(f, t0, y0, h, N):
    t_arr = np.linspace(t0, t0 + h * N, N + 1)
    y_arr = np.zeros((N + 1, 2))
    y_arr[0] = y0
    for i in range(N):
        def func(y):
            return y - y_arr[i] - h * f(t_arr[i + 1], y)
        y_arr[i + 1] = fsolve(func, y_arr[i], xtol=1e-5)
    return t_arr, y_arr

y0 = np.array([2, 1])
t0 = 0
h = 0.01
N = 100

t_arr, y_arr = Euler_impl(f_der, t0, y0, h, N)
plt.plot(t_arr, y_arr[:, 0])
plt.show()
