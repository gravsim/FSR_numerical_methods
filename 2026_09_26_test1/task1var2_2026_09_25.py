
import numpy as np
import matplotlib.pyplot as plt

def g(x, c):
    return c * x * (1 - x)

def solve(c):
    x = 0.5
    while np.abs(g(x, c) - x) / np.abs(g(x, c)) > 1e-6:
        x = g(x, c)
    return x

c_s = np.arange(0, 3, 0.01)
x_s = [solve(c_i) for c_i in c_s]
plt.plot(c_s, x_s)
plt.savefig('task1var2.png', dpi=300)
plt.show()
