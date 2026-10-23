
import numpy as np

from numpy.polynomial.hermite import hermgauss

def f(x):
    return x / np.sqrt(2 * np.pi) + 0.6


def f_dispersion(x, mean):
    return (x / np.sqrt(2 * np.pi) + 0.6 - mean) ** 2

for N in [2, 3, 5]:
    roots, weights = hermgauss(N)
    mean = 1 / np.sqrt(np.pi) * np.sum(f(roots) * weights)
    dispersion = 1 / np.sqrt(np.pi) * np.sum(f_dispersion(roots, mean) * weights)
    print(f"N = {N} Mean: {mean} Dispersion: {dispersion}")
