
import numpy as np
import matplotlib.pyplot as plt
from mpmath import zeros
from scipy.interpolate import CubicSpline


def extrapolated(ax, x, y):
    h = x[1:] - x[:-1]
    d = (y[1:] - y[:-1]) / h
    b = 6 * (d[1:] - d[:-1])


    A_up = np.diag(h[1:-1], k=1)
    A_middle = np.diag(2 * (h[1:] + h[:-1]), k=0)
    A_down = np.diag(h[1:-1], k=-1)
    print(A_up)
    print(A_middle)
    print(A_down)

    A = A_up + A_middle + A_down
    print(A)
    A[0][0] = 3 * h[0] + 2 * h[1] + h[0] ** 2 / h[1]
    A[0][1] = h[1] - h[0] ** 2 / h[1]
    A[-1][-1] = 2 * h[-2] + 3 * h[-1] + h[-1] ** 2 / h[-2]
    A[-1][-2] = h[-2] - h[-1] ** 2 / h[-2]

    m = np.linalg.solve(A, b)

    m_0 = m[0] - h[0] * (m[1] - m[0]) / h[1]
    m_N = m[-1] - h[-1] * (m[-1] - m[-2]) / h[-2]

    m = np.hstack([m_0, m, m_N])

    coef0 = y[:-1]
    coef1 = d - h / 6 * (2 * m[:-1] + m[1:])
    coef2 = m[:-1] / 2
    coef3 = (m[1:] - m[:-1]) / (6 * h)

    for k in range(len(coef0)):
        bins = np.linspace(x[k], x[k + 1], 100) - x[k]

        y = np.polyval([coef3[k], coef2[k], coef1[k], coef0[k]], bins)
        ax.plot(x[k] + bins, y, color='green')

