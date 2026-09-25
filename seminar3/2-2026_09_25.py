
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x_observed = np.array([0, 1, 2, 3])
y_observed = np.array([0, 0.5, 2, 1.5])

der_a = 0.2
der_b = -10

h = x_observed[1:] - x_observed[:-1]
d = (y_observed[1:] - y_observed[:-1]) / h
b = 6 * (d[1:] - d[:-1])

A_up = np.diag(h[1:-1], k=1)
A_middle = np.diag(2 * (h[1:] + h[:-1]), k=0)
A_down = np.diag(h[1:-1], k=-1)


A = A_up + A_middle + A_down

A[0][0] -= 0.5 * h[0]
A[-1][-1] -= 0.5 * h[-1]

b[0] -= 3 * (d[0] - der_a)
b[-1] -= 3 * (der_b - d[-1])

m = np.linalg.solve(A, b)

m_0 = 3 / h[0] * (d[0] - der_a) - m[0] / 2
m_N = 3 / h[-1] * (der_b - d[-1]) - m[-1] / 2

m = np.hstack([m_0, m, m_N])

coef0 = y_observed[:-1]
coef1 = d - h / 6 * (2 * m[:-1] + m[1:])
coef2 = m[:-1] / 2
coef3 = (m[1:] - m[:-1]) / (6 * h)

bins = np.linspace(x_observed[0], x_observed[-1], 1000)
cs = CubicSpline(x_observed, y_observed)

fig, ax = plt.subplots(figsize=(6.5, 4))
ax.plot(x_observed, y_observed, 'o', label='Data')
ax.plot(bins, cs(bins), label='Cubic spline')

for k in range(len(coef0)):
    bins = np.linspace(x_observed[k], x_observed[k + 1], 100) - x_observed[k]

    y = np.polyval([coef3[k], coef2[k], coef1[k], coef0[k]], bins)
    ax.plot(x_observed[k] + bins, y, color='red')


h = x_observed[1:] - x_observed[:-1]
d = (y_observed[1:] - y_observed[:-1]) / h
b = 6 * (d[1:] - d[:-1])

A = A_up + A_middle + A_down
m = np.linalg.solve(A, b)

m_0 = 0
m_N = 0

m = np.hstack([m_0, m, m_N])

coef0 = y_observed[:-1]
coef1 = d - h / 6 * (2 * m[:-1] + m[1:])
coef2 = m[:-1] / 2
coef3 = (m[1:] - m[:-1]) / (6 * h)

for k in range(len(coef0)):
    bins = np.linspace(x_observed[k], x_observed[k + 1], 100) - x_observed[k]

    y = np.polyval([coef3[k], coef2[k], coef1[k], coef0[k]], bins)
    ax.plot(x_observed[k] + bins, y, color='blue')

ax.legend()
plt.title("Интерполяционный сплайн с изменением СУ (правильно)")
plt.savefig('2_cubic_my.png', dpi=300)
plt.show()
