
import numpy as np
import matplotlib.pyplot as plt

n = 1000

x = np.linspace(-5, 20, 30)
y = np.linspace(-7, 7, 30)
xx, yy = np.meshgrid(x, y)
alpha = np.arctan(xx - yy ** 2)
N = 1000
k_x = np.cos(alpha)
k_y = np.sin(alpha)

plt.title("Поле касательных к решениям y'=x-y^2")
plt.quiver(xx, yy, k_x, k_y)
plt.savefig('diff_eq.png', dpi=300)
plt.show()
