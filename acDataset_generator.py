from abAlgorithm_improved import algorithm
from decimal import Decimal
import numpy as np

#
# PRECISION = 0.01
# LOWER_LIMIT = -10.0
# UPPER_LIMIT = 10.0
#
# lower_real = lower_imaginary = LOWER_LIMIT
#
#
# for i in range(int((abs(LOWER_LIMIT)+abs(UPPER_LIMIT))*pow(10,int(len(str(PRECISION)[2:]))))+1):
#     for j in range(int((abs(LOWER_LIMIT)+abs(UPPER_LIMIT))*pow(10,int(len(str(PRECISION)[2:]))))+1):
#         for k in range(2,6):
#             # print(lower_real,lower_imaginary,k)
#             algorithm(Decimal(lower_real),Decimal(lower_imaginary),k,8)
#         lower_imaginary = round(lower_imaginary+PRECISION,len(str(PRECISION).split('.')[1]))
#     lower_imaginary = LOWER_LIMIT
#     lower_real = round(lower_real+PRECISION,len(str(PRECISION).split('.')[1]))



precision = 0.01
lower_limit = -10.0
upper_limit = 10.0
k_values = np.arange(2, 6)
precision_round = int(len(str(precision)[2:]))

real_values = np.around(np.arange(lower_limit, upper_limit + precision, precision), precision_round)
imaginary_values = np.around(np.arange(lower_limit, upper_limit + precision, precision), precision_round)

for i in range(real_values.shape[0]):
    for j in range(imaginary_values.shape[0]):
        for k in k_values:
            print(real_values[i], imaginary_values[j], k, 8)
            algorithm(Decimal(real_values[i]),Decimal(imaginary_values[j]),k,8)
