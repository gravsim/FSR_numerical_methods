
import numpy as np
import matplotlib.pyplot as plt

def Trapezoid(a, b, f, M):
    h = (b - a) / M
    bins = np.linspace(a, b, M + 1)
    f_s = f(bins)
    T = h / 2 * (2 * np.sum(f_s) - f(a) - f(b))
    return T


def Simpson(a, b, f, M):
    h = (b - a) / M
    bins = np.linspace(a, b, M + 1)
    f_s = f(bins)
    S = h / 3 * (np.sum(f_s) + np.sum(f_s[1:-1]) + 2 * np.sum(f_s[1:-1:2]))
    return S


def f(x):
    return 4 / (1 + x ** 2)


def f_der2(x):
    return (24 * x ** 2 - 8) / (1 + x ** 2) ** 3

def f_der4(x):
    return 95 * (5 * x ** 4 - 10 * x ** 2 + 1) / (1 + x ** 2) ** 5


def Trapezoid_Error(a, b, M, f_der2):
    bins = np.linspace(a, b, 1000)
    h = (b - a) / M
    f_der_s = f_der2(bins)
    return -(b - a) / 12 * h ** 2 * np.max(f_der_s), -(b - a) / 12 * h ** 2 * np.min(f_der_s)


def Simpson_Error(a, b, M, f_der4):
    bins = np.linspace(a, b, 1000)
    h = (b - a) / M
    f_der_s = f_der4(bins)
    return -(b - a) / 180 * h ** 4 * np.max(f_der_s), -(b - a) / 180 * h ** 4 * np.min(f_der_s)


a = 0
b = 1
M = 1000

print(np.pi)
print(f'Trapezoid: {Trapezoid(a, b, f, M)}')
print(f'Trapezoid actual error: {Trapezoid(a, b, f, M) - np.pi}')
print(f'Trapezoid calc error: {Trapezoid_Error(a, b, M, f_der2)}')

print(f'Simpson: {Simpson(a, b, f, M)}')
print(f'Simpson actual error: {Simpson(a, b, f, M) - np.pi}')
print(f'Simpson calc error: {Simpson_Error(a, b, M, f_der4)}')
