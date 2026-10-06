import matplotlib.pyplot as plt
import numpy as np



M = 30
a, b = 0, 1
t = np.linspace(a, b, M+1)
h = (b - a)/M

A = []
for i in range(len(t)):
    tmp = []
    for j in range(len(t)):
        if j == 0 or j==M:
            tmp.append(1/2 * np.exp(t[i] - t[j]))
        else:
            tmp.append(2 * (1/2 * np.exp(t[i] - t[j])))
    tmp = np.array(tmp) * h/2
    A.append(tmp)

A = A - np.eye(len(t))
B = -1 * np.ones(len(t))

res = np.linalg.solve(A, B)



c = 1 + ((np.exp(1) - 1)/np.exp(1)) * np.exp(t)

plt.plot(t, res)
plt.plot(t, c)
plt.show()

plt.plot(t, res - c) # разность графиков - ошибка наглядно
plt.show()