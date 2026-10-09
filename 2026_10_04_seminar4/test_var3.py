
import numpy as np
import matplotlib.pyplot as plt



def Trapezoid(a, b, f, M):
    h = (b - a) / M
    bins = np.linspace(a, b, M + 1)
    y = f(bins)
    T = h / 2 * (np.sum(2 * y) - y[0] - y[-1])
    return T


def Simpson(a, b, f, M):
    h = (b - a) / M
    bins = np.linspace(a, b, M + 1)
    y = f(bins)
    T = h / 3 * (np.sum(y) + np.sum(y[1:-1]) + 2 * np.sum(y[1:-1:2]))
    return T


def f(x):
    return np.sin(x) ** 2

a = 0
b = np.pi / 3
M = 6
answer = np.pi / 6 - np.sqrt(3) / 8

print(np.power((b - a) ** 5 * 8 * 1e4 / 180, 1 / 4))

print(f'answer: {answer}')
print(f'Trapezoid: {Trapezoid(a, b, f, M)}')
print(f'Trapezoid error: {Trapezoid(a, b, f, M) - answer}')

print(f'Simpson: {Simpson(a, b, f, M)}')
print(f'Simpson error: {Simpson(a, b, f, M) - answer}')


