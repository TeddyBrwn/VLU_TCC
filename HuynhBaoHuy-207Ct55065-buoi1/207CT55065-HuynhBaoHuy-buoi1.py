# th1
blocks = 3
dayS =[1/2**n for n in range(0,blocks)]
tongS = sum(dayS)
print(tongS)

blocks = 5
dayS =[1/2**n for n in range(0,blocks)]
tongS = sum(dayS)
print(tongS)

blocks = 10000
dayS =[1/2**n for n in range(0,blocks)]
tongS = sum(dayS)
print(tongS)       
# th2
n = 1001
X = [k/(n/2) for k in range(0, n)]
S = 0
for k in range(1, n):
    S = S + X[k]**2 * (X[k] - X[k-1])
print (S) 
# th3
from sympy import *
print(Rational(1, 2) + Rational(1, 3))

print(Rational(1, 2) + 1)

print(Rational(1, 3) + 1 + 1.5)
# th4
from sympy import *
x = Symbol('x')
y = Symbol('y')
print(x+y+x-y)
print((x+y)**2)
# th5
# a
from sympy.solvers.solvers import denoms
eq = (1/x)*1/(x-3)
dd = denoms(eq)
print (dd) 
# b
eq = (1+1/x)/(x-1)
from sympy.solvers.solvers import denoms
loai_tru = set()
for d in denoms(eq):
    for s in solve(d):
        loai_tru.add(s)
print (loai_tru) 
# th6
from sympy import Symbol
x = Symbol('x',positive = True)
if (x+3) > 0:
    print('Chac chan x+3 duong!')
else:
    print ('x+3 chua chac la so duong!')
# th7
import sympy as sp
import math
theta = Symbol('theta')
math.sin(math.pi/2)
2*sp.sin(theta) == sp.sin(theta) + sp.sin(theta)
print(2*sp.sin(theta))
print((2*sp.sin(theta)*sp.cos(theta)).equals(sp.sin(2*theta)))
# th8
from sympy import sin,solve,Symbol
u = Symbol('u')
t = Symbol('t')
g = Symbol('g')         
theta = Symbol('theta')
a=solve(u*sin(theta)-g*t,t)
b=solve([u*sin(theta)/g])
print(a)
print(b)
# th9
from sympy import Limit,Symbol,S
x = Symbol('x')
Limit(1/x,x,S.Infinity)
Limit(1/x,x,oo,dir="-")
gioihan = Limit(1/x,x,S.Infinity)
print(gioihan.doit())
# th10
# a
from sympy import Limit
print(Limit(1/x, x, 0, dir='-').doit())
print(Limit(1/x, x, 0, dir='+').doit())
# b
from sympy import Symbol, sin
print(Limit(sin(x)/x, x, 0).doit())
# th11
# a
from sympy import Symbol, sin,Limit,S
x = Symbol('x',positive=int)
gioihan1 = Limit(x*sin(1/x),1,S.Infinity)
print(gioihan1.doit())
# b
from sympy import limit, sin, S
print(limit(x*sin(1/x), x, S.Infinity))
from sympy import limit, Symbol, S
n = Symbol('n')
print(limit((1+1/2)**n, n,S.Infinity ).doit())
# th12
from sympy import Symbol,Limit,S
p = Symbol('p',positive=True)
r= Symbol('r',positive=True)
t = Symbol('t',positive=True)
print(Limit(p*(1+r/n)**(n**t),n,S.Infinity).doit())
print(p*exp(r*t))
# th13
from sympy import Symbol,Limit
t= Symbol('t')
St = 5*t**2 +2*t+8
t1 = Symbol('t1')
delta_t = Symbol('delta_t')
St1 = St.subs({t:t1})
St1_delta = St1.subs({t:t1+delta_t})  
print(St)
print(delta_t)
print(St1)