
import numpy as np

n = 2000
x = 50



def factorial(n):
    answer = 1
    i = 1
    while i < n:
        i += 1
        answer *= i

    return answer

def exp(x):
    result = 0
    for i in range(1, n):
        result += x ** i / factorial(i)
    return result

print(np.exp(x), exp(x), np.exp(x) - exp(x))