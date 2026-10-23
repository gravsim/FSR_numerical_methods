
import numpy as np
import matplotlib.pyplot as plt

def P(x):
    return 924 * x ** 6 - 2772 * x ** 5 + 3150 * x ** 4 - 1680 * x ** 3 + 420 * x ** 2 - 42 * x + 1


def bisection(a, b):
    c = (a + b) / 2
    if P(a) * P(b) > 0:
        return bisection(0, 0.5)
    while np.abs(b - a) > 1e-14:
        c = (a + b) / 2
        if P(a) * P(c) < 0:
            b = c
        else:
            a = c
    return c

x = np.linspace(0, 1, 100)
solutions = np.round(np.array([bisection(a, a + 0.05) for a in np.arange(0, 1, 0.01)]), 11)
solutions = np.unique(solutions)
print(solutions)
plt.grid(which='major')
plt.grid(which='minor')
plt.plot(x, P(x))
plt.scatter(solutions, P(solutions))
plt.savefig('task1var3.png', dpi=300)
plt.show()
