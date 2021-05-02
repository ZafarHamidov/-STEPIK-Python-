"""
/step/3
a = float(input())
b = float(input())
print(1 / 2 * a * b)

/step/4
s = float(input())
v1 = float(input())
v2 = float(input())
print(s / (v1 + v2))

/step/5
number = float(input())
print(1 / number if number else "Обратного числа не существует")

/step/6
num = float(input())
c = 5 / 9 * (num - 32)
print(c)

/step/7
nn = int(input())
res = nn * 10.5 if nn <= 2 else (nn - 2) * 4 + 21
print(res)

/step/8
n = float(input())
n1 = int(n * 10)
c = n1 % 10
print(c)

/step/9
x = float(input())
print(x - int(x))

/step/11
16

/step/12
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
n = max(a, b, c, d, e)
m = min(a, b, c, d, e)
print("Наименьшее число =", m)
print("Наибольшее число =", n)

/step/13
a = int(input())
b = int(input())
c = int(input())
m = min(a, b, c)
x = max(a, b, c)
s = (a + b + c) - (m + x)
print(x)
print(s)
print(m)

/step/14
n = int(input())
n1 = n // 100
n2 = (n // 10) % 10
n3 = n % 10
m = min(n1, n2 , n3)
x = max(n1, n2 , n3)
s = (n1 + n2 + n3) - (m + x)
if x - m == s:
    print("Число интересное")
else:
    print("Число неинтересное")
    
/step/15
a1 = float(input())
a2 = float(input())
a3 = float(input())
a4 = float(input())
a5 = float(input())
a = abs(a1)
b = abs(a2)
c = abs(a3)
d = abs(a4)
e = abs(a5)
print(a + b + c + d + e)

/step/16
p1 = int(input())
p2 = int(input())
q1 = int(input())
q2 = int(input())
print(abs(p1 - q1) + abs(p2 - q2))

"""
