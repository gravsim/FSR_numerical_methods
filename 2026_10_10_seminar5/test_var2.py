import numpy as np
from scipy.special import roots_laguerre


lam = 67
N = 2

def f_mean(x):
    return x

def f_dispersion(x, mean):
    return (x / lam - mean) ** 2


def laguerre(x):
    return 1 / 6 * (-x ** 3 + 9 * x ** 2 - 18 * x + 6)

roots = np.array([2 - np.sqrt(2), 2 + np.sqrt(2)])
weights = roots / ((N + 1) ** 2 * laguerre(roots) ** 2)

scipy_roots, scipy_weights = roots_laguerre(N)

mean = 1 / lam * np.sum(f_mean(roots) * weights)
dispersion = np.sum(f_dispersion(roots, mean) * weights)

scipy_mean = 1 / lam * np.sum(f_mean(roots) * weights)
scipy_dispersion = np.sum(f_dispersion(roots, mean) * weights)


print(f"analytical mean: {1 / lam}")
print(f"analytical dispersion: {1 / (lam ** 2)}")

print(f"scipy_mean: {scipy_mean}")
print(f"scipy_dispersion: {scipy_dispersion}")

print(f"mean: {mean}")
print(f"dispersion: {dispersion}")