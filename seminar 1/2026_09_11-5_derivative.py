
import numpy as np
import matplotlib.pyplot as plt

n = 1000


def factorial(n):
    answer = 1
    for i in range(2, n + 1):
        answer *= i
    return answer

def factorial_divide(x, n):
    for i in range(2, n + 1):
        x /= i
    return x

def exp(x):
    result = 1
    for i in range(1, n):
        result += factorial_divide(x ** i, i)
    return result


def derivative(x, h):
    return (exp(x + h) - exp(x)) / h


for i in range(20):
    print(i, derivative(1, 10 ** -i), derivative(1, 10 ** -i) - np.exp(1))
