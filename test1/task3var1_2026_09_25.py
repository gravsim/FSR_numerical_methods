
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange


x = np.array([1, 2, 3])
y = np.array([-1, -2, 1])
der_a = -1
der2_b = 2


h = x[1:] - x[:-1]
d = (y[1:] - y[:-1]) / h
b = 6 * (d[1:] - d[:-1])

A_up = np.diag(h[1:-1], k=1)
A_middle = np.diag(2 * (h[1:] + h[:-1]), k=0)
A_down = np.diag(h[1:-1], k=-1)

A = A_up + A_middle + A_down

m = np.linalg.solve(A, b)

m_0 = 3 / h[0] * (d[0] - der_a) - der2_b / 2
m_1 = der2_b
m = np.hstack([[m_0], m, [m_1]])

coef0 = y[:-1]
coef1 = d - h / 6 * (2 * m[:-1] + m[1:])
coef2 = m / 2
coef3 = (m[1:] - m[:-1]) / (6 * h)

fig, ax = plt.subplots(ncols=2, figsize=(12, 5))
ax[0].scatter(x, y, label='true')
ax[1].scatter(x, y, label='true')
for k in range(len(coef0)):
    bins = np.linspace(x[k], x[k + 1], 100) - x[k]
    y = np.polyval([coef3[k], coef2[k], coef1[k], coef0[k]], bins)
    y_shtrih = np.polyval([3 * coef3[k], 2 * coef2[k], coef1[k]], bins)
    ax[0].plot(bins + x[k], y)
    ax[1].plot(bins + x[k], y_shtrih)
ax[0].legend()
ax[1].legend()
plt.savefig('task3var1.png', dpi=300)
plt.show()
