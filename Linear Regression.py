import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Reading Data
C = [40, 60, 100, 15, 30]
F = [104,140, 212, 59, 86]

mean_C = np.mean(C)
mean_F = np.mean(F)

#total number of values
n = len(C)
#using the formula to calculate b1 and b0

numer = 0
denom = 0

for i in range(n):
    numer += (C[i] - mean_C) * (F[i] - mean_F)
    denom += (C[i] - mean_C) ** 2
b1 = numer/denom
b0 = mean_F - (b1*mean_C)

#print Coefficients
print ("The intercept is " , b0 ," and the slope is " ,  b1)

# 50 Celsius is 122 Faranheit

Celsius = 50
res = Celsius * b1 + b0
print (res)
