
import numpy as np
import matplotlib.pyplot as plt


def core(t_i, t_j):
    return 0.5 * np.exp(t_i - t_j)


def get_x(a, b, t, M):
    A = []
    h = (b - a) / M
    for i in range(len(t)):
        tmp = []
        for j in range(len(t)):
            if j == 0 or j == M:
                tmp.append(core(t[i], t[j]))
            else:
                tmp.append(2 * core(t[i], t[j]))
        A.append(tmp)
    A = h / 2 * np.array(A) - np.eye(len(t))
    B = -np.ones(len(t))
    return np.linalg.solve(A, B)


a = 0
b = 1
M = 10
t = np.linspace(a, b, M + 1)

answer = 1 + (np.e - 1) / np.e * np.exp(t)
result = get_x(a, b, t, M)

fig, ax = plt.subplots(1, 2)
ax[0].plot(t, result, color='red', label='result')
ax[0].plot(t, answer, color='black', linestyle='--', label='analytical')

ax[1].plot(t, result - answer, label='difference')
ax[0].legend()
ax[1].legend()
plt.show()

