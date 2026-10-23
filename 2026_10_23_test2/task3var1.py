
import numpy as np
from scipy.integrate import dblquad


def f(x, y):
    return y * np.exp(2 * x)



for N in [1000, 3000, 4000, 100000]:
    x = np.random.uniform(0, 1, N)
    y = np.random.uniform(0, 1, N)

    indices = np.where((x ** 2 + (y - 1) ** 2) <= 1)
    answer = dblquad(lambda y, x: f(x, y), 0, 1, lambda x: 1 - np.sqrt(1 - x ** 2), lambda x: 1)
    x = x[indices]
    y = y[indices]
    print(f"N = {N} 1/sqrt(N) = {1 / np.sqrt(N)} answer: {answer}")
    integral = np.pi / 4 / len(x) * np.sum(f(x, y))

    print(f"integral: {integral}")
    print(f"integral error: {integral - answer[0]}")
# plt.scatter(x, y)
# plt.show()
