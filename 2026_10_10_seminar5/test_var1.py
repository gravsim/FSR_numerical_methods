import numpy as np
from scipy.special import roots_hermite
from math import factorial

k = 1.38e-23
T = 100
m = 16 * 1.66e-27

N = 4

def f(x):
    return np.abs(x)

def hermite(x):
    return 8 * x ** 3 - 12 * x

my_roots = np.roots([1, 0, -6, 0, 3])
my_weights = 2 ** (N - 1) * factorial(N) * np.sqrt(np.pi) / (N ** 2 * hermite(my_roots) ** 2)

analytical = np.sqrt(2 * k * T / (np.pi * m))
roots, weights = roots_hermite(N)

coeff = np.sqrt(2 * k * T / (m * np.pi))

integral = coeff * np.sum(f(my_roots) * my_weights)
scipy_integral = coeff * np.sum(f(roots) * weights)
print(f"analytical: {analytical}")
print(f"integral: {integral}")
print(f"integral error: {integral - analytical}")
print(f"scipy_integral: {scipy_integral}")
print(f"scipy_integral error: {scipy_integral - analytical}")