"""
/step/1
n = int(input())
if n % 100 == 0:
    print("YES")
else:
    print("NO")
    
/step/2
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a + b + c + d) % 2 == 0:
    print("YES")
else:
    print("NO")
    
/step/3
a = int(input())
b = input()
if (10 <= a <= 15) and b == "f":
    print("YES")
else:
    print("NO")
    
step/4
a = int(input())
if a == 1:
    print('I')
elif a == 2:
    print('II')
elif a == 3:
    print('III')
elif a == 4:
    print('IV')
elif a == 5:
    print('V')
elif a == 6: 
    print('VI')
elif a == 7:
    print('VII')
elif a == 8:
    print('VIII')
elif a == 9:
    print('IX')
elif a == 10:
    print('X')
else:
    print('ошибка')
    
/step/5
a = int(input())
if a % 2 != 0:
    print("YES")
elif (a % 2 == 0) and (a >= 2 and a <= 5):
    print("NO")
elif (a % 2 == 0) and (a >= 6 and a <= 20):
    print("YES")
elif (a % 2 == 0) and (a > 20):
    print("NO")
    
/step/6
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a - b == c - d) or (a + b == c + d):
    print("YES")
else:
    print("NO")
    
/step/7
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('YES')
else:
    print('NO')
    
/step/8
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')

"""
