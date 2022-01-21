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

# def till_n(real,imaginary,n):
#     k = 1
#     result = 0
#     while(k <= n):
#         result += combination(n,k)*(real**k)*(imaginary**(n-k))*iota(n-k)
#         k+=2
#
#     return result

def even_real(real,imaginary,n):
    k = 0
    result = 0
    while(k <= n ):
        result += combination(n, k) * (real ** k) * (imaginary ** (n - k)) * iota(n - k)
        k += 2

    return result


def even_imaginary(real,imaginary,n):
    k = 1
    result = 0
    while(k <= n ):
        result += combination(n, k) * (real ** k) * (imaginary ** (n - k)) * iota(n - k)
        k += 2

    return result

def odd_real(real,imaginary,n):
    k = 1
    result = 0
    while(k <= n ):
        result += combination(n, k) * (real ** k) * (imaginary ** (n - k)) * iota(n - k)
        k += 2

    return result

def odd_imaginary(real,imaginary,n):
    k = 0
    result = 0
    while(k <= n-1 ):
        result += combination(n, k) * (real ** k) * (imaginary ** (n - k)) * iota(n - k)
        k += 2

    return result


# def till_n_minus_one(real,imaginary,n):
#     k = 0
#     result = 0
#     while(k <= n-1):
#         result += combination(n,k)*(real**k)*(imaginary**(n-k))*iota(n-k)
#         k+=2
#
#     return result



def algorithm(real,imaginary,n,plots):

    if plots == 0:
        return



    print("(", plots, ")")
    print("Real: ", real, "\nImaginary: ", imaginary)
    print()


    if n%2 == 0:
        R = even_real(real,imaginary,n)
        I = even_imaginary(real, imaginary, n)
    else:
        R = odd_real(real, imaginary, n)
        I = odd_imaginary(real,imaginary,n)

    algorithm(R,I,n,plots-1)