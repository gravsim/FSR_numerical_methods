
import numpy as np


N = 2

lamb = 2
def f(x):
    return 1 / lamb ** 3 * x ** 3


def L3(x):
    return 1 / 6 * (-x ** 3 + 9 * x ** 2 - 18 * x + 6)


def get_weights(x):
    return x / ((N + 1) ** 2 * L3(x) ** 2)


roots = np.array([2 - np.sqrt(2), 2 + np.sqrt(2)])
weights = get_weights(roots)
integral = np.sum(f(roots) * weights)
print(f'Integral: {integral}')
print(f'Analytical: {0.75}')
