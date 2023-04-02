# th1
chuoitinhtoan = "a*b+c" 
a = 2 
b = 5 
c = 8 
print(eval(chuoitinhtoan)) 
# th1.2
from sympy import Symbol
x = Symbol('x') 
y = Symbol('y') 
bieuthuc = x+y 
thaytheso = bieuthuc.subs({x:10, y:5}) 
print(thaytheso)
#subs
u = Symbol('u') 
v = Symbol('v') 
bieuthuc_theo_uv = bieuthuc.subs({x:u, y:v}) 
print(bieuthuc_theo_uv) 
# sub1
thaythe_tinhtoan = bieuthuc.subs({x:2*u*v, y:u**2+v**2}) 
thaythe_tinhtoan = u**2 + 2*u*v + v**2 
print(thaythe_tinhtoan.factor()) 
# sub1.2
from sympy import Symbol
x = Symbol('x') 
y = Symbol('y') 
bieuthuc = x + y
bieuthuc2 = x**2 + y**2 
u = Symbol('u') 
v = Symbol('v') 
a = Symbol('a') 
from sympy import sin, cos 
bieuthuc_theo_uv = bieuthuc2.subs({x : a*sin(u), y : a*cos(u)}) 
print(bieuthuc_theo_uv)
print(bieuthuc_theo_uv.simplify())
# th3
danhsach_so = [10, 15, 20] 
danhsach_so[0] 
10 
danhsach_so[1] 
15 
danhsach_so[2] 
20
# th4
ds = [1, 2, 3]
for so in ds:
    print(so)
# th4.1
ds = [10, 11, 12] 
for chiso, giatri in enumerate(ds): 
    print(chiso, giatri)
# th5
x_numbers = [1, 6, 8] 
y_numbers = [2, 5, 9] 
from pylab import plot, show
plot(x_numbers, y_numbers)
show()
# th6
plot(x_numbers, y_numbers, marker = 'o')
show()
plot(x_numbers, y_numbers, 'x') 
show() 
# th7
hcm_rain = [13.8, 4.1, 10.5, 50.4, 218.4, 311.7, 293.7, 269.8, 327.1, 266.7, 116.5, 48.3] 
months = range(1, 13) 
plot(months, hcm_rain, marker = 'o') 
show()
# th8
from sympy import Symbol, Derivative 
t = Symbol('t') 
st = 5*t**2 + 2*t + 8 
print(Derivative(st, t)) 
d = Derivative(st, t)
print(d.doit())
print(d.doit().subs({t:1}))
t1 = Symbol('t1') 
print(d.doit().subs({t:t1}))
t2=10
print(d.doit().subs({t:t2}))
# th9
from sympy import Derivative, Symbol 
x = Symbol('x') 
f = (x**3+x**2+x)*(x**2+x) 
Derivative(f, x).doit() 
print((2*x + 1)*(x**3 + x**2 + x) + (x**2 + x)*(3*x**2 + 2*x + 1))
# th10
import sympy
f = sympy.sin(2*x) 
print(Derivative(f, x).doit())
f = sympy.sin(x)*sympy.cos(x) 
print(Derivative(f, x).doit())
# th11
from sympy import Symbol, solve, Derivative 
x = Symbol('x') 
f = x**5-30*x**3+50*x 
d1 = Derivative(f, x).doit()
cuctri = solve(d1) 
print(cuctri)
A = cuctri[0] 
A = cuctri[2] 
B = cuctri[0] 
C = cuctri[1] 
D = cuctri[3] 
d2 = Derivative(d1, x, 2).doit() 
print(d2.subs({x:B}).evalf())
print(d2.subs({x:C}).evalf())
print(d2.subs({x:A}).evalf())
print(d2.subs({x:D}).evalf())
x_min = -5 
x_max = 5 
print(f.subs({x:B}).evalf())
print(f.subs({x:D}).evalf())
print(f.subs({x:x_min}).evalf()) 
print(f.subs({x:x_max}).evalf()) 









