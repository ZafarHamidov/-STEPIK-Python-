"""
/step/3
count = 0
p = 1
for i in range(1, 11):
    x = int(input())
    if x >= 0:
        p = p * x
        count = count + 1
if count > 0:
    print(count)
    print(p)
else:
    print('NO')
    
/step/4
mx = -10**6 - 1
s = 0
for i in range(10):
    x = int(input())
    if x < 0:
        s += x
    if x < 0 and x > mx:
        mx = x
if s < 0:
    print(s)
    print(mx)
else:
    print('NO')
    
/step/5
s = 0
for i in range(7):
    n = int(input())
    if n % 2 == 0:
        s = s + n

print(s)

/step/6
n = int(input())
max_digit = -1
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:
            max_digit = digit
    n = n // 10
if max_digit == -1:
    print('NO')
else:
    print(max_digit)
    
/step/7
print(input()[0])

/step/8
from numpy import prod
n = input()
print(prod([int(i) for i in n]))

"""
