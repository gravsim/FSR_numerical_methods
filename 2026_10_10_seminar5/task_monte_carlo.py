import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return x * y ** 2


N = 10000
x = np.random.uniform(0, 2, N)
y = np.random.uniform(0, 1, N)

mask = y < x / 2
y = y[mask]
x = x[mask]

analytical = 4 / 15
volume = 1
monte_carlo = volume / len(x) * np.sum(f(x, y))

print(f'Analytical: {analytical}')
print(f'Monte Carlo: {monte_carlo}')
print(f'Monte Carlo error: {monte_carlo - analytical}')

plt.scatter(x, y)
plt.show()