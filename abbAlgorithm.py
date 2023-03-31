import numpy as np
from decimal import Decimal


def combination(n, r):
    if r == 0:
        return 1
    elif n < r:
        return 0

    res = 1
    for i in range(r):
        res *= n - i
        res //= i + 1
    return res


def iota(i):
    return [1, 1, -1, -1][i % 4]


def leibniz_expansion(real, imaginary, n):
    R = np.zeros(n // 2 + 1, dtype=Decimal)
    I = np.zeros(n // 2 + 1, dtype=Decimal)
    R[0] = real
    I[0] = imaginary
    for k in range(1, n // 2 + 1):
        R[k] = R[k - 1] * real - I[k - 1] * imaginary
        I[k] = R[k - 1] * imaginary + I[k - 1] * real
    if n % 2 == 0:
        return R[-1], I[-1]
    else:
        return I[-1], R[-1]


def algorithm(real, imaginary, n, plots):
    res = np.zeros((plots, 4), dtype=Decimal)
    res[0] = [real, imaginary, n, 0]
    for i in range(1, plots):
        real, imaginary = leibniz_expansion(real, imaginary, n)
        res[i] = [real, imaginary, n, i]
    np.savetxt('datasets.csv', res, delimiter=",", fmt='%s')


algorithm(Decimal(1.0), Decimal(1.0), 2, 8)
