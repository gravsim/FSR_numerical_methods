
import numpy as np


def chord(x1, x2, f):
    steps = 0
    b = (x1 * f(x2) - x2 * f(x1)) / (x1 - x2)
    k = (f(x1) - b) / x1
    middle = - b / k
    if f(x1) * f(x2) > 0:
        return 0
    while np.abs(f(middle)) > 1e-16:
        steps += 1
        middle = (x1 + x2) / 2.0
        if f(x1) * f(middle) <= 0:
            x2 = middle
        else:
            x1 = middle
    return middle, f(middle), steps


def function(x) -> float:
    return x ** 2 - 2 * x - 3

point, value, steps = chord(-2, 1, function)
print(f'Point: {point}, value: {value}, steps: {steps}')
