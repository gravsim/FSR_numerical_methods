
import numpy as np


def bisection(a, b, f):
    steps = 0
    middle = (a + b) / 2
    if f(a) * f(b) > 0:
        return 0
    while np.abs(f(middle)) > 1e-16:
        steps += 1
        middle = (a + b) / 2.0
        if f(a) * f(middle) <= 0:
            b = middle
        else:
            a = middle
    return middle, f(middle), steps


def function(x) -> float:
    return x ** 2 - 2 * x - 3


point, value, steps = bisection(-2, 1, function)
print(f'Point: {point}, value: {value}, steps: {steps}')
