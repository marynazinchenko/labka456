# Task2

import math
import numpy as np

x = int(input("x = "))

if ((x ** 2 + np.log(x)) > 0):
    y = np.cos(x ** 2 + np.log(x))
elif (x ** 2 + np.log(x)) == 0:
    y = 1 / (x ** 2 + np.log(x))
else:
    y = np.cos(x)

print(y)