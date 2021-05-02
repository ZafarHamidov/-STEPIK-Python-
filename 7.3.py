"""
/step/2
100

/step/3
15

/step/4
1361015

/step/5
a = int(input())
b = int(input())
count = 0
for i in range(a, b + 1):
    if i % 10 == 4 or i % 10 == 9:
        count += 1
print(count)

/step/6
n = int(input())
count = 0
for i in range(n):
    a = int(input())
    count += a
print(count)

/step/7
from math import* 
counter = 0
n = int(input())
for i in range(1, n+1):
    counter = counter + 1/i
print(counter - log(n))

/step/8
print(5 * ((int(input())+5) // 10)**2)

/step/9
n = int(input())
total = 1
for i in range(1, n + 1):
    total *= i
print(total)

/step/10
p = 1
for _ in range(10):
    n = int(input())
    p *= n + (n == 0)
print(p)

/step/11
import math
n = int(input())
s = 0
r = int(math.sqrt(n))
for i in range(1, r + 1):
    if n % i == 0:
        s += i
        s += n // i
if n / r == r:
    s -= r

print(s)

/step/12
n = int(input())
if (n % 2 == 0):
    print(-n // 2)
else:
    print(n // 2 + 1)
    
/step/13
n = int(input())
max1, max2 = -1, -1
for _ in range(n):
    num = int(input())
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num
        
print(max1)
print(max2)

/step/14
flag = 'YES'
for _ in range(10):
    a = int(input())
    if a % 2 != 0:
        flag = 'NO'
print(flag)

/step/15
n = int(input())
a, b = 1, 1
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
    
"""
