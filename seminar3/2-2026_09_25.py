
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from tas

x_observed = np.array([0, 1, 2, 3])
y_observed = np.array([0, 0.5, 2, 1.5])

der_a = 0.2
der_b = -10


fig, ax = plt.subplots(figsize=(6.5, 4))


ax.legend()
plt.title("Интерполяционный сплайн с изменением СУ (правильно)")
plt.savefig('2_cubic_my.png', dpi=300)
plt.show()
