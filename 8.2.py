"""
/step/1
n = int(input())
s = 0
while n > 0:
    if n % 10 % 2 == 0:
        s += n % 10    
    n //= 10
print(s)

/step/2
n = 8  #
count = 0
maximum = -10 ** 6 - 1  #
for i in range(n):
    x = int(input())
    if x % 4 == 0:  #
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
    
/step/3
n = 4
count = 0
maximum = 0
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x

if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
    
/step/4
n = int(input())

for i in range(1, n+1):
    if i==1 or i==n:
        print('*'*19)
    else:
        print('*' + ' ' * 17 + '*')

/step/5
n = input()
print(n[2])

/step/6
from numpy import prod

n = input()
print(len([i for i in n if i=='3']))
lastDigit = n[-1]
print(len([i for i in n if i==lastDigit]))
print(len([i for i in n if int(i)%2==0]))
print(sum([int(i) for i in n if int(i) > 5]))
print(int(prod([int(i) for i in n if int(i) > 7])))
print(len([i for i in n if i=='0' or i=='5']))

/step/7
1 число = 1729
2 число = 4104
3 число = 13832
4 число = 20683
5 число = 32832
"""
