import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve



def f_der(x, y):
    return (-y - 2 * x) / y


def Euler_impl(f, t0, y0, h, N):
    t_arr = np.linspace(t0, t0 + h * N, N + 1)
    y_arr = np.zeros((N + 1))
    y_arr[0] = y0
    for i in range(N):
        def func(y):
            return y - y_arr[i] - h * f(t_arr[i + 1], y)
        y_arr[i + 1] = fsolve(func, y_arr[i], xtol=1e-5)[0]
    return t_arr, y_arr

y0 = -1
t0 = -1
h = 0.01
N = 100

t_arr, y_arr = Euler_impl(f_der, t0, y0, h, N)
plt.plot(t_arr, y_arr)
plt.show()
