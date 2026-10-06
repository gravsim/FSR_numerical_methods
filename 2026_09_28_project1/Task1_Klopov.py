import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import barycentric_interpolate

import pandas as pd
df = pd.read_csv('Kamaz_upper.csv', sep=';', header=None)
df = df.replace(',', '.', regex=True).astype(np.float64).values
x = df[:, 0]
y = df[:, 1]
der_b = -10

df = pd.read_csv('Kamaz_param.csv', sep=';', header=None)
df = df.replace(',', '.', regex=True).astype(np.float64).values
x_param = df[:, 0]
y_param = df[:, 1]


def get_coeffs(x, y):
 h = x[1:] - x[:-1]
 d = (y[1:] - y[:-1]) / h
 b = 6 * (d[1:] - d[:-1])

 A_up = np.diag(h[1:-1], k=1)
 A_middle = np.diag(2 * (h[1:] + h[:-1]), k=0)
 A_down = np.diag(h[1:-1], k=-1)

 A = A_up + A_middle + A_down

 A[-1, -1] -= h[-1] / 2
 b[-1] -= 3 * (der_b - d[-1])

 m = np.linalg.solve(A, b)

 m_0 = 0
 m_N = 3 / h[-1] * (der_b - d[-1]) - m[-1] / 2

 m = np.hstack([m_0, m, m_N])

 s0 = y[:-1]
 s1 = d - h / 6 * (2 * m[:-1] + m[1:])
 s2 = m[:-1] / 2
 s3 = (m[1:] - m[:-1]) / (6 * h)
 return s0, s1, s2, s3


def cubic_spline(x, y, bins):
 s0, s1, s2, s3 = get_coeffs(x, y)
 spline = np.array([])
 for k in range(len(s0)):
  local_bins = bins[(bins >= x[k]) & (bins <= x[k + 1])] - x[k]
  f = np.polyval([s3[k], s2[k], s1[k], s0[k]], local_bins)
  spline = np.append(spline, f)
 return spline


def plot_derivative(ax, x, s1, s2, s3):
 for k in range(len(s3)):
  bins = np.linspace(x[k], x[k + 1], 100) - x[k]
  y = np.polyval([3 * s3[k], 2 * s2[k], s1[k]], bins)
  ax[0].plot(x[k] + bins, y, color='red')

 ax[0].set_xlabel('x')
 ax[0].set_ylabel('y', rotation=0)
 ax[0].set_title("S'(x)")
 ax[0].minorticks_on()
 ax[0].grid(True, which='major', linestyle='-')
 ax[0].grid(True, which='minor', linestyle='--', alpha=0.5)


def plot_derivative2(ax, x, s2, s3):
 for k in range(len(s3)):
  bins = np.linspace(x[k], x[k + 1], 100) - x[k]
  y = np.polyval([6 * s3[k], 2 * s2[k]], bins)
  ax[1].plot(x[k] + bins, y, color='green')

 ax[1].set_xlabel('x')
 ax[1].set_ylabel('y', rotation=0)
 ax[1].set_title("S''(x)")
 ax[1].minorticks_on()
 ax[1].grid(True, which='major', linestyle='-')
 ax[1].grid(True, which='minor', linestyle='--', alpha=0.5)


def plot_der12():
 fig, ax = plt.subplots(ncols=2, figsize=(9.5, 4))
 s0, s1, s2, s3 = get_coeffs(x, y)
 plot_derivative(ax, x, s1, s2, s3)
 plot_derivative2(ax, x, s2, s3)

plot_der12()
plt.savefig('figure2.png', dpi=300)
plt.show()