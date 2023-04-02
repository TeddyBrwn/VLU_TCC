# th1
import numpy as np
mienchia = np.linspace(0, 2, 11)
print(mienchia)
# th2
import numpy as np
import matplotlib.pyplot as plt
fs = [1, 2, 4]
all_time = np.linspace(0, 2, 200)
t = all_time[:100]
for f in fs:
    y = np.sin(2 * np.pi * f * t)
    plt.plot(t, y, label='{} Hz'.format(f))
plt.legend()
import os
os.chdir('d:\\')
plt.savefig('basics_python.pdf')
plt.show() 
# th3 //
# th4
def f (x): return x**2
print (f(8))
g = lambda x: x**2
print (g(8))
# th5
def thue(phan_tram): return lambda x: x * phan_tram
hcm = thue(0.012)
hn = thue(0.01)
print(hcm(1000000))
print(hn(1000000))
# th6
hinhthang = lambda f, a, b: (b-a)*(f(a)+f(b))/2
from math import exp
hinhthang(exp,0, 1) 
def hai_x(x):
    return 2*x
print(hinhthang(hai_x, 1, 2))
# th7

def traprule(ham, trai, phai):
    return (phai-trai)*(ham(trai) + ham(phai))/2
import math
S = "Bieu thuc can tinh tich phan la e^x:"
print(S + '[a,b]')
A = float(input('Nhap a : '))
B = float(input('Nhap b : '))
Y = traprule(math.exp, A, B)
print(S + "[%.1E,%.1E] : " % (A, B))
print('Gia tri xap xi : %.15E' % Y)
E = math.exp(B) - math.exp(A)
print(' Gia tri chinh xac : %.15E' % E)
# th8
import scipy 
from sympy import *
import sys
sys.displayhook = pprint
x = Symbol('x')
bt1 = integrate(x**2 + x + 1, x)
pprint (bt1)
bt2 = integrate(x/(x**2+2*x+1), x)
pprint (bt2)
bt3 = integrate(x**2 * exp(x) * cos(x), x)
pprint (bt3)
bt4 = integrate(exp(-x**2)*erf(x), x)
pprint (bt4) 
# th9
from sympy import Integral, Symbol
x = Symbol('x')
k = Symbol('k')
print(Integral(k*x, x))
print(Integral(k*x, x).doit())
# th10
from sympy import pprint, Integral 
F = Integral(k*x, x).doit() 
pprint(F)
print(Integral(k*x, (x, 0, 2)).doit())
# th12
from sympy import Integral, Symbol 
x = Symbol('x') 
print(Integral(x, (x, 2, 4)).doit())
# th13
from sympy import Symbol, exp, sqrt, pi, Integral 
x = Symbol('x') 
p = exp(-(x - 10)**2/2)/sqrt(2*pi) 
print(Integral(p, (x, 11, 12)).doit().evalf())
