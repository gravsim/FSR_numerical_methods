import numpy as np
from scipy.special import roots_legendre
from scipy.special import erf
import matplotlib.pyplot as plt


def S(a,b,f,M):
    h=(b-a)/M
    x=np.linspace(a,b,M+1)
    y=f(x)
    sum1=np.sum(y)
    sum2=np.sum(y[1:-1])
    sum3=2*np.sum(y[1:-1:2])
    return h/3*(sum1+sum2+sum3)

def f(x):
    return np.exp(-(x**2))/np.sqrt(np.pi)

a, b = -1, 1


for N in [2, 3, 5, 10]:
    roots, weights = roots_legendre(N)

    print(N, f"Не Симпсон{np.sum(f(roots) * weights)}")
    print(N, f"Симпсон: {S(a, b, f, N)}")

print(erf(1))
