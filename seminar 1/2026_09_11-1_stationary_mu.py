
import numpy as np
import matplotlib.pyplot as plt

def stationary(x0, f, mu):
    steps = 0
    x = x0
    while np.abs(f(x, mu) - x) > 1e-16:
        steps += 1
        x = f(x, mu)
    return x


def function(x, mu1) -> float:
    return mu1 * x * (1 - x)


mu = np.linspace(3, 4, 10)

y = [stationary(0.4, function, mu_i) for mu_i in mu]
plt.scatter(mu, y)
plt.show()


