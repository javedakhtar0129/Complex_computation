import numpy as np
import pandas as pd
# using recursion for combination

def combination(n,r):
    if r==0:
        return 1
    elif n<r:
        return 0
    else:
        return combination(n-1,r-1) + combination(n-1,r)

# gives sign of the iota, lambda expression
def iota(i):
    return [1, 1, -1, -1][i % 4]


def leibniz_expansion(real, imaginary, n, k):
    result = 0
    while(k <= n):
        result += combination(n,k)*(real**k)*(imaginary**(n-k))*iota(n-k)
        k+=2

    return result

def algorithm(real,imaginary,n,plots,XX,YY):

    # XX.append(str(real))
    # YY.append(str(imaginary))

    if plots == 0:
    #     print("REAL\n",XX)
    #     print("IMAGINARY\n",YY)
    #
        return

    print("(", plots, ")")
    print("Real: ", real, "\nImaginary: ", imaginary)
    print()

    if n%2 == 0:
        R = leibniz_expansion(real, imaginary, n, 0)
        I = leibniz_expansion(real, imaginary, n, 1)
    else:
        R = leibniz_expansion(real, imaginary, n, 1)
        I = leibniz_expansion(real, imaginary, n, 0)

    algorithm(R,I,n,plots-1,XX,YY)