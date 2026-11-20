import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp

def dy_dt(t, y):
    return y ** 2 - y ** 3

a = 0
d = 1e-5
b = 2 / d
init = np.array([d])

methods = ["RK23", "RK45", "DOP853", "BDF", "LSODA"]
t_arr = np.linspace(a, b, int(b) + 1)

for meth in methods:
    tmp = solve_ivp(dy_dt, [a, b], init, method = meth, t_eval=t_arr)
    print(tmp.nfev)
    plt.plot(t_arr, tmp.y[0], label=meth)
plt.legend()
plt.show()
