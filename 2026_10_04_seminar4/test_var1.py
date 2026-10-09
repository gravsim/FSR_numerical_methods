
import numpy as np
import matplotlib.pyplot as plt


h = 6.62e-34
c = 3e8
k = 1.38e-23
T = 5800
R = 6.96e8
S = 4 * np.pi * R ** 2

def Trapezoid(a, b, f, M):
    h = (b - a) / M
    bins = np.linspace(a, b, M + 1)
    f_s = I(bins)
    T = h / 2 * (2 * np.sum(f_s) - f(a) - f(b))
    return T


def x(lambd):
    return h * c / (lambd * k * T)


def I(x):
    return x ** 3 / (np.exp(x) - 1)



a = x(800e-9)
b = x(300e-9)
M = 100

answer = S * 2 * np.pi * k ** 4 * T ** 4 / (h ** 3 * c ** 2) * Trapezoid(a, b, I, M)


print(f'Trapezoid: {answer}')


