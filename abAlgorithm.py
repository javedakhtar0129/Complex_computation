import numpy as np
import pandas as pd

df = pd.DataFrame(columns=['real','imaginary','power','quadrant'])#,dtype=np.float64)


def exponential_fitting(result):
    fitted_base = float(np.format_float_scientific(result.base,precision=5).split("e")[0])
    fitted_exp = float(np.format_float_scientific(result.base,precision=5).split("e")[1])
    result.base = fitted_base
    result.exp = result.exp+fitted_exp
    return result


class Exponential:
    def __init__(self,base,exp):
        self.base = base
        self.exp = exp

    def __mul__(self, other):
        multiplied =  Exponential(round(self.base * other.base,5),self.exp+other.exp)
        return exponential_fitting(multiplied)

    def __rmul__(self,other):
        r_multiplied = Exponential(round(self.base * other,5),self.exp)
        return exponential_fitting(r_multiplied)

    def __pow__(self, power, modulo=None):
        powered = Exponential(self.base**power,self.exp*power)
        return exponential_fitting(powered)

    def __add__(self, other):
        sum = 0
        if self.exp != other.exp:
            if self.exp > other.exp:
                other.base = other.base * 10 ** (self.exp - other.exp)
            else:
                self.base = self.base * 10 ** (other.exp - self.exp)
            sum = Exponential(self.base + other.base, abs(self.exp - other.exp))
        else:
            sum = Exponential(self.base + other.base, self.exp)
        return exponential_fitting(sum)

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
    result = Exponential(0,0)
    while(k <= n):
        result += iota(n-k)*((combination(n,k)*(real**k))*(imaginary**(n-k)))
        k+=2

    return result


def algorithm(real,imaginary,n,plots):

    real = pd.Series([np.format_float_scientific(real,precision=5)])#,dtype=np.float64)
    imaginary = pd.Series([np.format_float_scientific(imaginary,precision=5)])#,dtype=np.float64)

    R = Exponential(float(real[0].split('e')[0]),float(real[0].split('e')[1]))
    I = Exponential(float(imaginary[0].split('e')[0]), float(imaginary[0].split('e')[1]))

    print(R.base,R.exp)
    print(I.base,I.exp)
    L = I+R
    # L = (-1)*((2*(R**3))*(I**4))
    print(L.base,L.exp)

    # for i in range(plots):
    #     df.iloc[i] = [real,imaginary,n,i]
    #     if n % 2 == 0:
    #         R = leibniz_expansion(R, I, n, 0)
    #         I = leibniz_expansion(R, I, n, 1)
    #     else:
    #         R = leibniz_expansion(R, I, n, 1)
    #         I = leibniz_expansion(R, I, n, 0)


    # for i in range(plots):
    # #     print(f"R:{real},I:{imaginary},iteration:{i}")
    #     if n%2 == 0:
    #         r_m = leibniz_expansion(real[0], imaginary[0], n, 0)
    #         i_m = leibniz_expansion(real[0], imaginary[0], n, 1)
    #     else:
    #         r_m = leibniz_expansion(real[0], imaginary[0], n, 1)
    #         i_m = leibniz_expansion(real[0], imaginary[0], n, 0)

    print(df)


# algorithm(float(0.00000134234),float(.0091231),2,5)
# algorithm(float(.0091231),float(.0091231),2,5)
algorithm(float(.00023422),float(512.1241),2,5)
