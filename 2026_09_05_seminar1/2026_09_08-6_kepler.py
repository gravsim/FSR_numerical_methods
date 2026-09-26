
import numpy as np
import matplotlib.pyplot as plt

a = 1.52
e = 0.093

def Newton_method(x, M, f, f_der):
    while np.abs(f(x, M)) > 1e-15:
        x = x - f(x, M) / f_der(x)
    return x


def function(E, M) -> float:
    return E - e * np.sin(E) - M


def derivative(E) -> float:
    return 1 - e * np.cos(E)


M_s = np.linspace(0, 2 * np.pi, 10000)

E = [Newton_method(0, M, function, derivative) for M in M_s]
# plt.plot(M_s, y)

x = a * (np.cos(E) - e)
b = a * np.sqrt(1 - e ** 2)
y = b * np.sin(E)

fig = plt.figure()
ax = fig.add_subplot()
ax.set_aspect('equal')
ax.plot(x, y)
plt.savefig('kepler')
plt.show()