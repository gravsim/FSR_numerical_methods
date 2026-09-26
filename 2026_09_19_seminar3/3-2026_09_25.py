
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline


xx = np.array([-1, 0, 1, 0, 1])
yy = np.array([0, 1, 0.5, 0, -1])
tt = np.array([0, 0, 0, 0, 0], dtype=np.float32)

tt[1:] = np.cumsum(np.sqrt((xx[1:] - xx[:-1]) ** 2 + (yy[1:] - yy[:-1]) ** 2))
print(tt)
bins = np.linspace(tt[0], tt[-1], 1000)
cs_x = CubicSpline(tt, xx)
cs_y = CubicSpline(tt, yy)

fig, ax = plt.subplots(figsize=(6.5, 4))
ax.plot(xx, yy, 'o', label='Data')

ax.plot(cs_x(bins), cs_y(bins), label='Cubic spline')
plt.legend()
plt.savefig('3_cubic_spline.png', dpi=300)
plt.show()
