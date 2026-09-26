
import numpy as np

h = 6.62607015e-34
c = 299792458
k = 1.380649e-23


def b(x):
    return h * c / (k * x)


def f(x):
    return 5 * np.exp(-x) + x - 5


def der(x):
    return -5 * np.exp(-x) + 1

def Newton(x0):
    x = x0 - f(x0) / der(x0)
    while np.abs(f(x) / f(x0)) > 10e-6:
        x = x - f(x) / der(x)
    return x

print(b(Newton(100)))
