"""
/step/2
120

/step/3
5

/step/4
n = int(input())
while n:
    print(n % 10)
    n = n // 10
    
/step/5
n = int(input())
while n:
    print(n % 10, end="")
    n = n // 10
    
/step/6
n = int(input())
n1 = str(n)
print("Максимальная цифра равна",max(n1))
print("Минимальная цифра равна",min(n1))

/step/7
n = int(input())
b = n
sum_n = 0
count = 0
mult = 1
while n != 0:
    sum_n += n % 10
    count += 1
    mult *= n % 10
    n = n // 10
print(sum_n)
print(count)
print(mult)
print(sum_n / count)
print(b // (10 ** (count - 1)))
print((b // (10 ** (count - 1)))+(b%10))

/step/8
n = int(input())
while n > 99:
    n //= 10
print(n % 10)

/step/9
n = int(input())
n1 = str(n)
z = max(n1)
x = min(n1)
if z == x:
    print("YES")
else:
    print("NO")
    
/step/10
n,b = int(input()),'YES'
while n // 10 != 0 :
    a = n % 10  
    n = n // 10
    if a > n % 10:
        b = 'NO'
print(b)
"""
