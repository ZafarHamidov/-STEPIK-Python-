"""
/step/3
  5
  3
  
/step/4
p1 = input()
p2 = input()
if p1 == p2:
    print("Пароль принят")
else:
    print("Пароль не принят")

/step/5
p = int(input())
if p % 2 == 0:
    print("Четное")
else:
    print("Нечетное")
    
/step/6
a1 = int(input())
d = a1 % 10
c = (a1 // 10) % 10
b = (a1 // 100) % 10
a = a1 // 1000
#pp = p1 + p4
#pm = p2 - p3
if (a + d) == (b - c):
    print("ДА")
else:
    print("НЕТ")
    
/step/7
age = int(input())
if age <= 17:
    print("Доступ запрещен")
else:
    print("Доступ разрешен")
    
/step/8
n1 = int(input())
n2 = int(input())
n3 = int(input())
if (n2 - n1) == (n3 - n2):
    print("YES")
else:
    print("NO")
    
/step/9
n1 = int(input())
n2 = int(input())
if n1 < n2:
    print(n1)
else:
    print(n2)
    
/step/10
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
ab = 0
cd = 0
if n1 < n2:
    ab = n1
else:
    ab = n2
if n3 < n4:
    cd = n3
else:
    cd = n4
if ab < cd:
    print(ab)
else:
    print(cd)
    
/step/11
n = int(input())
if n <= 13:
    print("детство")
elif n <= 24:
    print("молодость")
elif n <= 59:
    print("зрелость")
else:
    print("старость")
    
/step/12
a = int(input())
b = int(input())
c = int(input())
am = 0
bm = 0
cm = 0
m = 0
if a > 0:
    am = a
if b > 0:
    bm = b
if c > 0:
    cm = c
print(am + bm + cm)
"""
