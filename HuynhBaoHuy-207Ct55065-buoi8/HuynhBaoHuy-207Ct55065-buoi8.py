# th1a
from __future__ import division

y = (3, 5, 7) 
print(y)
print(y[1])
# print(y[1]= 4)

# th1b
import __future__
__future__.division

print(10/3)

# th1c
import sympy 
from sympy import Symbol 
x = Symbol('x') 
y = x  + 1 
print(y.subs(x, 14))
# th1d
import sympy 
from sympy import Symbol 
x = Symbol('x') 
from sympy import pi 
z = pi - 18*x 
print(z.subs(x, y))
t = Symbol('t') 
z = pi - 18*x 
print(z.subs(x, t))
# th2
from sympy import solve, sin 
x = Symbol('x') 
y = Symbol('y') 
print(solve(x-1,x))
print(solve(x**2-1,x))
print(solve(x**2+1,x))
print(solve(sin(x),x))
# th3
from sympy import solveset 
print(solveset(sin(x),x))
# th4
from sympy import solveset, S
from sympy.abc import x, y, z
print(solveset(x**2 + 1, x))
print(solveset(x**2 + 1, x, domain = S.Reals))
# th5
from sympy import solveset, S
from sympy.abc import x, y, z
from sympy import E
# print(solveset(e**x-1, x))
print(solveset(E**x-1, x))
print(solveset(E**x-1, x, domain = S.Reals))
# th6
print(solveset((sin(x)+x)*(x**2-9), x, domain = S.Reals))
# th7
from sympy import exp, S 
print(solveset(exp(x) > 1, x, domain = S.Reals))
print(solveset(E**x > 1, x, domain = S.Reals))
print(solveset(E**x > E, x, domain = S.Reals))
R = S.Reals
print(solveset(E**x > E, x, R))
# th8
from sympy import Derivative, Symbol, solve
x = Symbol('x') 
y = Symbol('y') 
z = Symbol('z')
f = 4*x*y - 8*x - 5 + z*(x+y-50)
dx = Derivative(f, x).doit() 
dy = Derivative(f, y).doit() 
dz = Derivative(f, z).doit()
nghiem = solve([dx, dy, dz], (x,y,z)) 
print (nghiem)
xx = nghiem[x] 
yy = nghiem[y] 
print(4*xx*yy-8*xx-5)
ketqua = 4*nghiem[x]* nghiem[y]-8*nghiem[x]-5
print(ketqua)