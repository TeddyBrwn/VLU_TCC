def luythua(x, n):
    ketqua= 1
    for i in range(n):
        ketqua = ketqua *x
    return ketqua
print(luythua(2,0))
print(luythua(2,1))
# th2
# while 1=2:
# 10 * (1/0) 
# 3 * bien_chua_khai_bao / 4 
# ‘ba’ + 7 s
# 10 * (1/0) 
# 'ba'+(1/0) 
# 'ba'+7+(1/0) 
# th3
try:
    x = int(input('Vui long nhap so: '))
    print(x)
except:
    print('Vui long nhap so. Khong nhap chu!') 
# th3.1
while True:
    try:
        x = int(input('Vui long nhap so: ')) 
        break
    except:
        print('Vui long nhap so. Khong nhap chu')
# th4
try:
    x = int(input('Vui long nhap so: '))
except:
    print ('So vua nhap sai') 
else:
    print ('so vua nhap la: ' + str(x))
    # break
finally:
    print('Da hoan thanh chuong trinh')
# th5
def frange(batdau, ketthuc, buocnhay): 
    day_ketqua = []
    while batdau<ketthuc:
        day_ketqua.append(batdau)
        batdau =batdau+buocnhay
        return day_ketqua
# print(frange(0,10,2))
# th6
from matplotlib import pyplot as plt 
import math 
def draw_graph(x,y):
    plt.plot(x,y)
    plt.xlabel("Truc X")
    plt.ylabel("Truc Y")
    plt.title("Do thi bai toan nem qua bong")
def frange(start, final, interval):
    number = []
    while start < final:
        number.append(start)
        start = start + interval
    return number
def draw_trajectory(u, theta):
    g = 9.8
    theta = math.radians(theta)
    t_flight = 2*u*math.sin(theta)/g
    intervals = frange(0, t_flight, 0.001)
    x = []
    y = []
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)
        draw_graph(x, y)
if __name__ == '__main__':
    try:  
        u = float(input('Nhap van toc ban dau (m/s): '))
        theta = float(input('Nhap goc bay (degrees): '))
    except:
        ValueError
        print('Nhap cac gia tri sai!')
    else:
        draw_trajectory(u, theta)
        plt.show()
    finally:
        print ('Hoan thanh chuong trinh!') 
# th7
def draw_graph(x,y):
    plt.plot(x,y)
    plt.xlabel("Truc X")
    plt.ylabel("Truc Y")
    plt.title("Do thi bai toan nem qua bong")
def frange(start, final, interval):
    number = []
    while start < final:
        number.append(start)
        start = start + interval
    return number
def draw_trajectory(ds_vantoc, goc_bandau):
    g = 9.8
    goc_bandau = math.radians(goc_bandau)
    t_flight = 2*ds_vantoc*math.sin(goc_bandau)/g
    intervals = frange(0, t_flight, 0.001)
    x = []
    y = []
    for t in intervals:
        x.append(ds_vantoc*math.cos(goc_bandau)*t)
        y.append(ds_vantoc*math.sin(goc_bandau)*t - 0.5*g*t*t)
        draw_graph(x, y)
if __name__ == '__main__':
    ds_vantoc = [20, 40, 60]
    goc_bandau = 45  
    for v in ds_vantoc: 
        draw_trajectory(v, goc_bandau) 
    chudan = []
    for i in ds_vantoc: 
        chudan.append(str(i)) 
        print ("Chu dan duoc tao la: ")    
    print (chudan) 
    plt.legend(chudan) 
    plt.show() 
# th8
from sympy import Symbol, Derivative, sympify, pprint 
 
def tinh_daoham(ham_f, bien):
    bien = Symbol(bien)     
    d = Derivative(ham_f, bien).doit()     
    pprint(d)
tinh_daoham('x**3+x**2+x', 'x')
if __name__ == '__main__':
    ham = input('Nhap 1 ham so: ')
    bien = input('Nhap bien so: ')
    try:
        ham_sympy = sympify(ham)
    except sympifyError:
        print('Ham nhap bi loi!')
    else:
        tinh_daoham(ham, bien) 
# th8.1
from sympy import Symbol, sin, pi ,plot
u = Symbol('u')
u = 30.0 
g = 9.81 
theta = Symbol('theta')
R = (u**2)*sin(2.0*theta)/g
print(R)
plot(R, (theta, 0, pi/2))
# th9
import math
from sympy import Derivative, Symbol, sin
def grad_ascent(x0, f1x, x):
    epsilon = 1e-6
    step_size = 1e-4
    x_cu = x0
    x_moi = x_cu + step_size * f1x.subs({x: x_cu}).evalf()
    while abs(x_cu - x_moi) > epsilon:
        x_cu = x_moi
        x_moi = x_cu + step_size * f1x.subs({x: x_cu}).evalf()
    return x_moi
def tim_max_theta(R, theta):
    R1theta= Derivative(R, theta).doit() 
    theta_0 = 1e-3
    theta_max = grad_ascent(theta_0, R1theta, theta)
    return theta_max 
g = 9.8
u = 30
theta = Symbol('theta')
R = (u**2) * sin(2*theta) / g
theta_max = tim_max_theta(R, theta)
print ('Goc theta: {0}'.format(math.degrees(theta_max)))
print ('Khoang cach vat bay xa: {0}'.format(R.subs({theta:theta_max})))