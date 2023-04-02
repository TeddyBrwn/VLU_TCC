# th2
from sympy import sin
dD3 = -2.515*sin(0.503*3-3.39525)
print (dD3)
dD6 = -2.515*sin(0.503*6-3.39525)
print (dD6)
dD9 = -2.515*sin(0.503*9-3.39525)
print (dD9)
dD12 = -2.515*sin(0.503*12-3.39525)
print (dD12)
# th3
from scipy.optimize import curve_fit 
import numpy as np 
x_data = np.array([3.4, 4.6, 5.2, 8.0, 10.7]) 
y_data = np.array([ 48, 52, 58, 76, 96 ]) 
import matplotlib.pyplot as plt 
plt.plot(x_data, y_data, 'b-', label='data')
def ham_bac_1(x, a, b): 
    return a*x + b 
duongcong, saiso = curve_fit(ham_bac_1, x_data, y_data) 
print(duongcong) 
gia_tri_73 = ham_bac_1(7.3, *duongcong) 
print (gia_tri_73)
plt.plot(x_data, ham_bac_1(x_data, *duongcong), 'r-', label='fit') 
plt.xlabel('Truc X') 
plt.ylabel('Truc Y') 
plt.legend() 
plt.show()
# th4
from scipy.optimize import curve_fit 
import numpy as np 
x_data = np.array([3.4, 4.6, 5.2, 8.0, 10.7]) 
y_data = np.array([ 48, 52, 58, 76, 96 ]) 
import matplotlib.pyplot as plt 
plt.plot(x_data, y_data, 'b-', label='data')
def ham_bac_2(x, a, b, c): 
    return a*x**2 + b*x + c
duongcong, saiso = curve_fit(ham_bac_2, x_data, y_data) 
print(duongcong)
gia_tri_73 = ham_bac_2(7.3, *duongcong)
print (gia_tri_73)
plt.plot(x_data, ham_bac_2(x_data, *duongcong), 'r-', label='fit') 
plt.xlabel('Truc X') 
plt.ylabel('Truc Y') 
plt.legend() 
plt.show()
# th5
from sympy import * 
x, y = symbols("x y") 
f = (3*x ** 2 - y) 
tp = integrate(f, (y, 0, 3), (x, 0, 2)) 
print(tp)
tp = integrate(f, (x, 0, 2), (y, 0, 3)) 
print(tp)
# th6
from sympy import * 
x, y = symbols("x y") 
f = x* y 
tp1 = integrate(f, (y, x, 2-x*x), (x, -2, 1)) 
print(tp1)