from sympy.abc import n, k, m
from sympy import limit_seq 
import matplotlib.pyplot as plt
from sympy import Sum, factorial, oo, IndexedBase, Function
import numpy as np
# n = float(input("nhap n: "))
x_1 = np.linspace(start=4, stop=24, num=100)

def f(x):
    return Sum(k**2 * Sum(2**m/m,(m,1,k)),(k,1,n))/(2**n*n),n
y_1 = f(x_1)
plt.plot(x_1, y_1)
plt.show()