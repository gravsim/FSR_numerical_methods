
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline


def closing(ax, x, y):
    h = x[1:] - x[:-1]
    d = (y[1:] - y[:-1]) / h
    b = 6 * (d[1:] - d[:-1])

    A_up = np.diag(h[1:-1], k=1)
    A_middle = np.diag(2 * (h[1:] + h[:-1]), k=0)
    A_down = np.diag(h[1:-1], k=-1)

    A = A_up + A_middle + A_down
    m = np.linalg.solve(A, b)

    m_0 = 0
    m_N = 0

    m = np.hstack([m_0, m, m_N])

    coef0 = y[:-1]
    coef1 = d - h / 6 * (2 * m[:-1] + m[1:])
    coef2 = m[:-1] / 2
    coef3 = (m[1:] - m[:-1]) / (6 * h)

    for k in range(len(coef0)):
        bins = np.linspace(x[k], x[k + 1], 100) - x[k]

        y = np.polyval([coef3[k], coef2[k], coef1[k], coef0[k]], bins)
        ax.plot(x[k] + bins, y, color='blue')

