
import numpy as np


def Newton_method(x, f, f_der):
    steps = 0

    while np.abs(f(x)) > 1e-16:
        x = x - f(x) / f_der(x)
        steps += 1
    return x, f(x), steps


def function(x) -> float:
    return x ** 2 - 2 * x - 3


def derivative(x) -> float:
    return 2 * x - 2


point, value, steps = Newton_method(20, function, derivative)
print(f'Point: {point}, value: {value}, steps: {steps}')
