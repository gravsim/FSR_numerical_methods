
import numpy as np
import matplotlib.pyplot as plt


def get_y2(y1, y0, k):
    return 5 * y1 - 4 * y0 + 2 * np.cos(3 * k) - 5 ** k

y_s = [0, 0]

N = 30
for k in range(2, N):
    print(k)
    y_s.append(get_y2(y_s[-1], y_s[-2], k))

plt.scatter(np.arange(2, N + 2), y_s)
plt.show()
