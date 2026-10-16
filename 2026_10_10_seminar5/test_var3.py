import numpy as np
from numpy.polynomial.legendre import leggauss
import matplotlib.pyplot as plt


def non_linear(x, theta0):
    return 1 / (np.sqrt(np.cos(x) - np.cos(theta0)))


def get_period(theta):
    a = 0
    b = theta
    roots, weights = leggauss(N)
    roots = (a + b) / 2 + (b - a) / 2 * roots
    return 2 * np.sqrt(2) * (b - a) / 2 * np.sum(non_linear(roots, theta) * weights)

N = 50
theta0 = np.linspace(0.01, np.pi-0.01, 1000)

periods = [get_period(theta) for theta in theta0]
plt.plot(theta0, periods, label='non_linear')
plt.plot(theta0, np.ones_like(periods) * 2 * np.pi, label='linear')
plt.legend()
plt.title('Линейно и не линейно')
plt.xlabel(r'$\theta_0$')
plt.ylabel(r'$T(\theta_0)$', rotation=0)
plt.savefig('test_var3.png', dpi=300)
plt.show()
