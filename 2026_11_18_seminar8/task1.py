import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp

def dy_dt(t, y):
    return -y - 5 * np.exp(-t) * np.sin(5 * t)

a = 0
b = 4
t0 = 0
y0 = 1
N = 1000
methods = ["RK23", "RK45", "DOP853", "BDF", "LSODA"]
t = np.linspace(a, b, N)
for meth in methods:
    tmp = solve_ivp(dy_dt, [a, b], [t0, y0], meth, t_eval=t)
    print(tmp.nfev)
    plt.plot(t, tmp.y[1], label=meth)

plt.show()
