
import numpy as np


def Archimedes(x, f, f_der):
    steps = 0
    while np.abs(f(x)) > 1e-16:
        x = x - f(x) / f_der(x)
        steps += 1
    return x, f(x), steps


def function(x) -> float:
    R = 0.1
    return 3 * R * x ** 2 - x ** 3 - 7 / 5 * R ** 3


def derivative(x) -> float:
    R = 0.1
    return 6 * x * R - 3 * x ** 2


point, value, steps = Archimedes(1, function, derivative)
print(f'Point: {point}, value: {value}, steps: {steps}')
