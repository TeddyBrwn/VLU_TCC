# th1
import math
def giaithua(n):
    if (n==0):
        return 1
    else:
        return n*giaithua(n-1)
print(giaithua(3))
print(giaithua(4))
# th2
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)
print(fibo(4))
print(fibo(5))
print(fibo(6))
# th3
def an_exp_an(n):
    if n == 1:
        return 1.0/2
    else:
        return an_exp_an(n-1)**an_exp_an(n-1)
print(an_exp_an(1))
print(an_exp_an(2))
print(an_exp_an(3))
print(an_exp_an(4))
print(an_exp_an(5))
print(an_exp_an(10))
# th4
def bai4(n):
    if n==1:
        return 4
    else:
        return 5.0/(6-bai4(n-1))
print(bai4(5))
print(bai4(6))
print(bai4(7))
print(bai4(10))
print(bai4(100))
# th5
def tisoFibo(n):
    if n==1:
        return 1
    else:
        return 1.0 + 1.0/tisoFibo(n-1)
for i in range(1, 11):
    print (i, tisoFibo(i)) 
# th5.2
from sympy import Derivative, Symbol, SympifyError, sympify
def grad_ascent(x0, ham_f1x, x):
    epsilon = 1e-6
    step_size = 1e-4
    x_old = x0
    x_new = x_old + step_size*ham_f1x.subs({x:x_old}).evalf()
    while abs(x_old - x_new) > epsilon:
        x_old = x_new
        x_new = x_old + step_size*ham_f1x.subs({x:x_old}).evalf()
    return x_new
if __name__ == '__main__':
    f = input('Nhap ham 1 bien (f): ')
    var = input('Nhap ten bien tuong ung (x): ')
    var0 = float(input('Nhap gia tri khoi dau cho bien x: '))
    try:
        f = sympify(f)
    except SympifyError:
        print('Ham nhap khong hop le!')
    else:
        var = Symbol(var)
        d = Derivative(f, var).doit()
        var_max = grad_ascent(var0, d, var)
        print('{0}: {1}'.format(var.name, var_max))
        print('Maximum value: {0}'.format(f.subs({var:var_max})))
# th5.3
from sympy import Derivative, Symbol, SympifyError, sympify
def grad_ascent(x0, ham_f1x, x):
    from sympy import solve, E
    if not solve(ham_f1x):
        print('Khong the tiep tuc, phuong trinh {0}=0 vo nghiem'.format(ham_f1x))
        return

    epsilon = 1e-6
    step_size = 1e-4
    x_old = x0
    x_new = x_old + step_size*ham_f1x.subs({x:x_old}).evalf()
    while abs(x_old - x_new) > epsilon:
        x_old = x_new
        x_new = x_old + step_size*ham_f1x.subs({x:x_old}).evalf()

    return x_new
if __name__ == '__main__':
    f = input('Nhap ham 1 bien (f): ')
    var = input('Nhap ten bien tuong ung (x): ')
    var0 = float(input('Nhap gia tri khoi dau cho bien x: '))
    try:
        f = sympify(f)
    except SympifyError:
        print('Ham nhap khong hop le!')
    else:
        var = Symbol(var)
        d = Derivative(f, var).doit()
        var_max = grad_ascent(var0, d, var)
        if var_max:
            print('{0}: {1}'.format(var.name, var_max))
            print('Maximum value: {0}'.format(f.subs({var:var_max})))