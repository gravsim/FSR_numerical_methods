import numpy as np
from matplotlib import pyplot as plt


def Euler(f, y0, a, b, h):
    N = int((b-a)/h)
    y_arr = np.zeros((N + 1, 2))
    t_arr = np.arange(a, b, h)
    y_arr[0] = y0
    for i in range(N):
        y_arr[i + 1] = y_arr[i] + h * f(t_arr[i], y_arr[i])
    return t_arr, y_arr.T

alpha, w = 0, 2
a, b = 0, 20*np.pi
h = 2*alpha/(w**2)
h1 = 1/10
h2 = 1/50


def dydt(t, y):
    return np.array([y[1], -2*alpha*y[1] - w**2*y[0]])


theta = np.pi/3
v0 = 0
init = np.array([theta, v0])

t1, s1 = Euler(dydt, init, a, b, h1)
t2, s2 = Euler(dydt, init, a, b, h2)

theta1 = s1[0]
theta2 = s2[0]

plt.figure()
plt.plot(t1, theta1)

plt.figure()
plt.plot(t2, theta2)

plt.show()
