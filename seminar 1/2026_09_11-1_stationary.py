
import numpy as np


def stationary(x0, f):
    steps = 0
    x = x0
    while np.abs(f(x) - x) > 1e-16:
        steps += 1
        x = f(x)
    return x, steps


def function1(x) -> float:
    return np.sqrt(2 * x + 3)

def function2(x) -> float:
    return 3 / (x - 2)

def function3(x) -> float:
    return (x ** 2 - 3) / 2


point, steps = stationary(4, function1)
print(f'Point: {point}, steps: {steps} \n')

point, steps = stationary(4, function2)
print(f'Point: {point}, steps: {steps} \n')

point, steps = stationary(4, function3)
print(f'Point: {point}, steps: {steps} \n')
