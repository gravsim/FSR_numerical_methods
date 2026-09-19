
import numpy as np


def integral(n):
    answer = 1
    for k in range(n):
        answer = 1 - n * answer
    return answer


def back_integral(n):
    answer = 1
    for k in range(n):
        answer = (1 - answer) / n
    return answer

value = integral(50)
print(f'integral value: {value}')
value = back_integral(50)
print(f'back_integral value: {value}')
