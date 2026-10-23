
import numpy as np
from numpy.polynomial.legendre import leggauss


def f(x):
    return -12 * x ** 10 - 5 * x ** 4 - 7

analytical = 2 * (-12 / 11 * 2 ** 11 - 2 ** 5 - 7 * 2)
N = 6
roots, weights = leggauss(N)
roots *= 2
weights *= 2
integral = np.sum(f(roots) * weights)
print(f"Analytical {analytical}")
print(f"Integral {integral}")
