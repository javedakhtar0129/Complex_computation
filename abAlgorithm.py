import numpy as np
import pandas as pd
from decimal import Decimal



# def exponential_fitting(result):
#     fitted_base = float(np.format_float_scientific(result.base,precision=5).split("e")[0])
#     fitted_exp = float(np.format_float_scientific(result.base,precision=5).split("e")[1])
#     result.base = fitted_base
#     result.exp = result.exp+fitted_exp
#     return result
#
#
# class Exponential:
#     def __init__(self,base,exp):
#         self.base = base
#         self.exp = exp
#
#     def __mul__(self, other):
#         multiplied =  Exponential(round(self.base * other.base,5),self.exp+other.exp)
#         return exponential_fitting(multiplied)
#
#     def __rmul__(self,other):
#         r_multiplied = Exponential(round(self.base * other,5),self.exp)
#         return exponential_fitting(r_multiplied)
#
#     def __pow__(self, power, modulo=None):
#         powered = Exponential(self.base**power,self.exp*power)
#         return exponential_fitting(powered)
#
#     def __add__(self, other):
#         new_base = 0
#         if self.exp < other.exp:
#             other.exp = other.exp + (-1)*self.exp
#             new_base = self.base + other.base*(10**other.exp)
#             new_base = np.format_float_scientific(new_base,precision=5)
#
#
#         sum = (self.base)
#         return exponential_fitting(sum)

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
    # result = Exponential(0,0)
    result = Decimal(0)
    while(k <= n):
        if k==0 and real==0:
            result += iota(n - k) * ((combination(n, k) * (1)) * (imaginary ** (n - k)))
        elif (n-k)==0 and imaginary==0:
            result += iota(n - k) * ((combination(n, k) * (real ** k)) * (1))
        else:
            result += iota(n-k)*((combination(n,k)*(real**k))*(imaginary**(n-k)))
        k+=2

    # print("result:",result)
    return result


# def algorithm_dunder_methods(real,imaginary,n,plots):
#
#     real = pd.Series([np.format_float_scientific(real,precision=5)])#,dtype=np.float64)
#     imaginary = pd.Series([np.format_float_scientific(imaginary,precision=5)])#,dtype=np.float64)
#     # print(real,imaginary)
#     R = Exponential(float(real[0].split('e')[0]),float(real[0].split('e')[1]))
#     I = Exponential(float(imaginary[0].split('e')[0]), float(imaginary[0].split('e')[1]))
#

    # for i in range(plots):
    #     df.iloc[i] = [real,imaginary,n,i]
    #     if n % 2 == 0:
    #         R = leibniz_expansion(R, I, n, 0)
    #         I = leibniz_expansion(R, I, n, 1)
    #     else:
    #         R = leibniz_expansion(R, I, n, 1)
    #         I = leibniz_expansion(R, I, n, 0)


def algorithm(real, imaginary, n, plots):

    df = pd.DataFrame(columns=['real', 'imaginary', 'power', 'iteration'])
    df.loc[len(df.index)] = ['XX','XX','XX','XX']

    for i in range(plots):
        df.loc[len(df.index)] = [real, imaginary, n, i+1]
        # print(real,imaginary,n,i)
        if n % 2 == 0:
            R = leibniz_expansion(real, imaginary, n, 0)
            I = leibniz_expansion(real, imaginary, n, 1)
        else:
            R = leibniz_expansion(real, imaginary, n, 1)
            I = leibniz_expansion(real, imaginary, n, 0)

        real = R
        imaginary = I

    df.to_csv('dataset.csv',mode='a',header=False,index=False)

    # print(df)





# leibniz_expansion(Decimal(0), Decimal(2.0),2,1)



