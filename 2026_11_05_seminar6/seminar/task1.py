import numpy as np
import matplotlib.pyplot as plt


def dydx(x, y):
    return (2*x + y) / (3*x + 4*y)


def Euler(f, y0, t0, h, n):
    y_arr = np.array([y0])
    t_arr = np.array([t0])
    for i in range(0, n):
        y_arr = np.append(y_arr, y_arr[i] + h*f(t_arr[i], y_arr[i]))
        t_arr = np.append(t_arr, t_arr[i] + h)
    return y_arr, t_arr


def RK(f, y0, t0, h, n):
    y_arr = np.array([y0])
    t_arr = np.array([t0])
    for i in range(0, n):
        k1 = h*f(t_arr[i], y_arr[i])
        k2 = h*f(t_arr[i] + h/2, y_arr[i] + k1/2)
        y_arr = np.append(y_arr, y_arr[i] + k2)
        t_arr = np.append(t_arr, t_arr[i] + h)
    return y_arr, t_arr


t0 = 1
y0 = -0.2
n = 10
h = 0.1

y1, t1 = Euler(dydx, y0, t0, h, n)
y2, t2 = RK(dydx, y0, t0, h, n)

plt.plot(t1, y1, color='red')
plt.plot(t2, y2, color='orange')
plt.show()