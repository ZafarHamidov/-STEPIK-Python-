"""
/step/2
до

/step/3
0

/step/4
9

/step/5
бесконечно много раз

/step/6
11

/step/7
21

/step/8
a = input()
while (a!='КОНЕЦ'):
    print(a)
    a = input()
    
/step/9
a = input()
while a != 'КОНЕЦ' and a != 'конец':
    print(a)
    a = input()
    
/step/10
a, k = input(), 0
while a not in ('стоп', 'хватит', 'достаточно'):
    k += 1
    a = input()
print(k)

/step/11
n = int(input())
while not n % 7:
    print(n)
    n = int(input())
    
/step/12
a = int(input())
b = 0
while a >= 0:
    b += a
    a = int(input())
print(b)

/step/13
n, k = int(input()), 0
while 1 <= n <= 5:
    k += n == 5
    n = int(input())
print(k)

/step/14
n = int(input())
print(n // 25 + n % 25 // 10 + n % 25 % 10 // 5 + n % 5)


"""
