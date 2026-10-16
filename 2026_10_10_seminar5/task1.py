import numpy as np
from scipy.special import roots_legendre, erf


def Simpson(a, b, f, M):
    h = (b - a) / M
    bins = np.linspace(a, b, M + 1)
    y = f(bins)
    return h / 3 * (np.sum(y) + np.sum(y[1:-1]) + 2 * np.sum(y[1:-1:2]))


def error_function(x):
    return 1 / (np.sqrt(np.pi) * np.exp(x ** 2))

a = -1
b = 1
M = 1000

print(f"Erf: {erf(1)}")
print(f"Simpson: {Simpson(a, b, error_function, M)}")
for N in [2, 3, 5]:
    roots, weights = roots_legendre(N)
    # print(weights)
    legendre = np.sum(error_function(roots) * weights)
    print(f"N: {N}, Legendre: {legendre}")
