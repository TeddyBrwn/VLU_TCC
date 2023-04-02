# th1
from sympy import Symbol, Integral
x = Symbol('x')
f = 1.0/x
unbound1 = Integral(f, (x, 0, 2))
print(unbound1.doit())
# th2
from sympy import Symbol, Integral 
x = Symbol('x') 
f = 1.0/x**2 
unbound2 = Integral(f, (x, -1, 1)) 
print(unbound2.doit())
# th3
from sympy import Symbol, Integral, Abs
x = Symbol('x')
f = Abs(x)
discontinous1 = Integral(f, (x, -1, 2))
print(discontinous1.doit())
# th4
from sympy import Symbol, Integral
x = Symbol('x')
f = x**(0.5)
undef1 = Integral(f, (x, -1, 1))
print(undef1.doit())
# th5
from scipy import integrate
import numpy as np
y = np.array([0.0, 4.1, 8.9, 8.5, 6.7, 4.3, 2.5, 1.2,0.2])
x = np.arange(0,9)
print(integrate.simps(y, x))
S = 2*integrate.simps(y, x)
print(S)
A = 5.5
F = A/S * 60
print(F)
# th6
from sympy import Symbol, Derivative, Integral
x = Symbol('x')
f = x**3/2
fx=Derivative(f, x).doit()
print(fx)
fx1=Integral(fx,(x,0,2))
print(fx1.doit())
# th7
# th8
from sympy import difference_delta as dd
from sympy.abc import n
print(dd(n*(n+1), n))
print(dd(n*(n+1), n, 2))
from sympy.abc import n, k
from sympy import limit_seq, Sum
print(limit_seq((3*n**3+5*n**2+4)/(5*n**3+200*n**2+400), n))
print(limit_seq((3*n**3+5*n**2+4)/(5*n**3+200*n**2+400), n))
from sympy.abc import n, k, m
print(limit_seq(Sum(k**2 * Sum(2**m/m,(m,1,k)),(k,1,n))/(2**n*n), n))
# th8.1
from sympy import series 
from sympy import Sum 
from sympy.series.limitseq import dominant
from sympy.abc import n,k 
dominant(n**3+100*n**2+200*n+1, n)
# n**3
print(dominant(2**n + Sum(k, (k,0,n)), n))
print(dominant(n**2 + Sum(k, (k,0,n)), n))
print(dominant(2*n**2 + Sum(k, (k,0,n)), n))
print(dominant(n**3 + Sum(k, (k,0,n)), n))
print(dominant(n*3 + Sum(k, (k,0,n)), n))
print(dominant(2*n*3 + Sum(k, (k,0,n)), n))
print(dominant(2*n**3 + Sum(k, (k,0,n)), n))
# th9
from sympy import Sum 
from sympy.abc import n, k 
S = Sum(k, (k, 0, n))
print(S)
from sympy import limit_seq 
print(limit_seq(S, n))
from sympy.abc import n 
e = (1+1/n)**n 
print(round(e.subs(n, 100).evalf(),10)) 
