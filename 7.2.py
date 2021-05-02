"""
/step/2
0, 1, 2, 3, 4, 5, 6, 7

/step/3
1, 2, 3, 4, 5, 6, 7

/step/4
3, 5, 7, 9

/step/5
10, 8, 6, 4, 2

/step/6
5

/step/7
m = int(input())
n = int(input())
for i in range(m, n + 1):
    print(i)
    
/step/8
n = int(input())
m = int(input())
if n < m:
    for i in range(n, m + 1):
        print(i)
else:
    for i in range(n, m - 1, -1):
        print(i)
        
/step/9
m, n = int(input()), int(input())
for i in range(m - 1 + m % 2, n - 1, -2):
    print(i)
    
/step/10
m = int(input())
n = int(input())
for i in range(m, n + 1):
    if i % 17 == 0:
        print(i)
    elif i % 10 == 9:
        print(i)
    elif i % 3 == 0 and i % 5 == 0:
        print(i)
        
/step/11
n = int(input())
for i in range(1, 10 + 1):
    print(f'{n} x {i} = {n * i}')

"""
