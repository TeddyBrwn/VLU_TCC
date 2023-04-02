# th1
import math
x = 3
print(x)
x = math.sqrt(1+x) 
print (x) 
x = math.sqrt(1+x) 
print (x) 
x = math.sqrt(1+x) 
print (x) 
# th2
import math 
x = 3 
lap = 1 
while (x != math.sqrt(x+1)):
    x = math.sqrt(x+1)
    lap = lap + 1
print(x)
print(lap)
# th3
import sympy as sp 
from sympy import Symbol 
x = Symbol('x') 
print(sp.solve(x-sp.sqrt(1+x),x))
# th4
import numpy as np 
v1 = np.array([1., 2., 3.])
v2 = np.array([2., 1., 0.]) 
v3 = v1 + v2
print(v3) 
print(3*v1 + 2*v2)
print([1, 2, 3] + [2, 1, 0])
print(3*[1, 2, 3] + 2*[2, 1, 0])
v4 = np.hstack([v1, v2])
print(v4)
print(np.dot(v1, v2))
angles = np.linspace(0, np.pi/2, 5) 
print(angles)
print(np.sin(angles))
import sympy as sy 
# print(sy.sin(angles))
# th5
from sympy import sin as sysin
angles = np.linspace(0, np.pi/2, 5)
sinangle = np.zeros(5)
len(angles)
for i in range(len(angles)):
    sinangle[i] = sysin(angles[i])
print(sinangle)
import numpy as np
goc = np.pi/3
A = np.array([ [np.cos(goc), -np.sin(goc)],
 [np.sin(goc), np.cos(goc)] ])
V = np.array([1. , 0. ])
Y = np.dot(A, V)
print(Y)
# th6
from numpy import diff
dx = 0.1
y = [1, 2, 3, 4, 4, 5, 6]
dy = diff(y)/dx
print(dy)
z = np.array([1, 2, 3, 4, 4, 5, 6]) 
dz = diff(z)/dx 
print(dz)
from numpy import diff 
x = [.1, .2, .5, .6, .7, .8, .9] 
y = [1, 2, 3, 4, 4, 5, 6] 
dydx = diff(y)/diff(x) 
print (dydx)
# th7
from sympy.geometry import * 
P1 = Point(0, 0) 
P2 = Point(3, 4) 
P3 = Point(2, -1) 
P4 = Point(-1, 5) 
S1 = Segment(P1, P2) 
S2 = Segment(P3, P4) 
print(Point.is_collinear(P1, P2, P3))
print(S1.length)
print(S2.midpoint)
print(S1.slope)
print(S1.intersection(S2))
print(Segment.angle_between(S1, S2))
print(S1.contains(P3))
L1 = Line(P1, P2) 
print(L1.equation())
print(L1.is_parallel(S1)) 
print(L1.is_parallel(S2))
# th8
import sympy
from sympy import *
x = Symbol('x')
f = x * sin(1/x)
c = Symbol('c')
delta = Symbol('delta')
c = 0
delta = 1/4
sympy.plot(f,(x, c - delta, c + delta))
sympy.plot(f, abs(x), -abs(x),(x, c - delta, c + delta))
# th9
from sympy import Symbol, solve, Derivative
x = Symbol('x')
f = -x**2+4*x-3
d1=Derivative(f, x).doit()
cuctri = solve(d1)
print(cuctri)
A = cuctri[0]
d2 = Derivative(d1, x).doit() 
print(d2.subs({x:A}).evalf())
x_min=0 
x_max=4 
print(f.subs({x:A}).evalf())
print(f.subs({x:x_min}).evalf())
print(f.subs({x:x_max}).evalf())
# th10
from sympy import Symbol, solve, Derivative
x = Symbol('x')
a = float(input("nhap a: "))
A = -2*x**3+2*a*x
# y là A(x)
y = solve(Derivative(A, x).doit()) 
print(y)
# th11
from sympy import Symbol, solve, Derivative
x = Symbol('x')
P = -10*x**2+25000*x-12000000
d1 = Derivative(P, x).doit()
cuctri = solve(d1)
A = cuctri[0]
print(A)
x_min=0 
x_max=1500
print(P.subs({x:x_min}).evalf())
print(P.subs({x:A}).evalf())
print(P.subs({x:x_max}).evalf())