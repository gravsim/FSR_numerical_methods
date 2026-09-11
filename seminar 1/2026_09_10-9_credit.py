
import numpy as np

a = 10
p = 1
r = 0.06


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


def function(n) -> float:
    return (1 + r) ** n * (1 - a * r / p) - 1


point, value, steps = bisection(-100, 100, function)
print(f'Point: {point}, value: {value}, steps: {steps}')
