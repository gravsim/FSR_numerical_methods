
import numpy as np
import matplotlib.pyplot as plt

from seminar3.task2_cubic_spline import cubic_spline
from seminar3.task2_closing import closing
from seminar3.task2_natural import natural


x = np.array([0, 1, 2, 3])
y = np.array([0, 0.5, 2, 1.5])

der_a = 0.2
der_b = -10


fig, ax = plt.subplots(figsize=(6.5, 4))
ax.plot(x, y, 'o', label='Data')
cubic_spline(ax, x, y)
closing(ax, x, y, der_a, der_b)
natural(ax, x, y)
ax.legend()
plt.title("Интерполяционный сплайн с изменением СУ (правильно)")
plt.savefig('2_cubic_my.png', dpi=300)
plt.show()
