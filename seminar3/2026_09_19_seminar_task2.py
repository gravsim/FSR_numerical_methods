import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from scipy.interpolate import CubicSpline

#========= 1 задача ============


s_a = 0.2
s_b = -1

x_observed = np.array([0, 1, 2, 3])
y_observed = np.array([0, 0.5, 2, 1.5])

h = x_observed[1:] - x_observed[:-1]
d = (y_observed[1:] - y_observed[:-1]) / h
b = (d[1:] - d[:-1]) * 6

A_up = h[1:-1]
A_down = h[1:-1]
A_main = 2 * (h[1:] + h[:-1])

a1 = np.diag(A_up, 1)
a2 = np.diag(A_down, -1)
a3 = np.diag(A_main, 0)

A = a1 + a2 + a3

M = np.linalg.solve(A, b)

M0 = 3 / h[0] * (d[0] - s_a) - M[0] / 2
M_n = 3 / h[-1] * (s_b - d[-1]) - M[-1] / 2

M = np.hstack([M0, M, M_n])
# print(M)



A3 = (M[1:] - M[:-1]) / (6 * h)
A2 = M[:-1]/2
A1 = d - h * (2 * M[:-1] + M[1:]) / 6
A0 = y_observed[:-1]


for i in range(len(A3)):
    bins = np.linspace(x_observed[i], x_observed[i + 1], 100) - x_observed[i]
    y = np.polyval([A3[i], A2[i], A1[i], A0[i]], bins)
    plt.scatter(x_observed, y_observed)
    plt.plot(bins + x_observed[i], y)
plt.show()