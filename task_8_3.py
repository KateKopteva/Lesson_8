import random
import math
def Sin1(x ,eps):
    if eps <= 0:
        print('Ошибка')
    y = x
    f = x
    i = 3
    while abs(y) > eps:
        y *= (-1) * x * x / ((i - 1) * i)
        i += 2
        f += y
    return f

eps = 0.01
for i in range(0, 6):
    x = 2
    print("eps = ", eps, "; sin(" ,x ,") = " ,Sin1(x ,eps) ,";" ,math.sin(x))
    eps /= 10


