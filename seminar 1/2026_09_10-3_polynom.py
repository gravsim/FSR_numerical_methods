
import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return x ** 7 - 7 * x ** 6 + 21 * x ** 5 - 35 * x ** 4 + 35 * x ** 3 - 21 * x ** 2 + 7 * x - 1


x = np.linspace(0.988, 1.012, 50)
y = function(x)
plt.plot(x, y)
plt.savefig('polynom.png')
plt.show()

