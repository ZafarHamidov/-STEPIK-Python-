"""
/step/2
from math import *
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
num = sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
print(num)

/step/3
R = float(input())
from math import pi
print(pi*R**2)
print(2*pi*R)

/step/4
import math
a, b  = float(input()), float(input())
sab, pab = a + b, a * b
print(sab / 2)
print(math.sqrt(pab))
print(2 * pab / sab)
print(math.sqrt((a**2 + b**2) / 2))

/step/5
from math import *
x = radians(float(input()))
print(sin(x) + cos(x) + tan(x) ** 2)

/step/6
from math import *
x = float(input())
z = ceil(x)
c = floor(x)
print(z + c)

/step/7
from math import *
a = float(input())
b = float(input())
c = float(input())
d = b**2-4*a*c
if d < 0:
    print('Нет корней')
elif d == 0:
    print(-b / (2*a))
elif d > 0:
    x1 = (-b - d ** 0.5) / (2*a)
    x2 = (-b + d ** 0.5) / (2*a)
    print(min(x1, x2))
    print(max(x1, x2))
    
/step/8
from math import *
n = int(input())
a = float(input())
print((n*a**2)/(4*(tan(pi/n))))
"""
