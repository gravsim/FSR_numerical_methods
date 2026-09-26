
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x = np.array([0, 1, 2, 3])
y = np.array([0, 0.5, 2, 1.5])

der_a = 0.2
der_b = -10

def cubic_spline(ax, x, y, der_a, der_b):
    bins = np.linspace(x[0], x[-1], 1000)
    cs = CubicSpline(x, y)

    fig, ax = plt.subplots(figsize=(6.5, 4))
    ax.plot(x, y, 'o', label='Data')
    ax.plot(bins, cs(bins), label='Cubic spline')
