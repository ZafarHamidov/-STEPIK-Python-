"""
/step/3
n = int(input())
k = int(input())
if n < k:
    print("YES")
elif n == k:
    print("Don't know")
else:
    print("NO")
    
/step/4
a = int(input())
b = int(input())
c = int(input())
if (a == b and b != c) or (a == c and c != b) or (b == c and a != b):
    print("Равнобедренный")
elif a == b == c:
    print("Равносторонний")
else:
    print("Разносторонний")
    
/step/5
a = int(input())
b = int(input())
c = int(input())
 
if b < a < c or c < a < b:
    print(a)
elif a < b < c or c < b < a:
    print(b)
else:
    print(c)

/step/6
n = int(input())
if n ==0 or n > 12:
    print(0)
elif n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12:
    print(31)
elif n == 4 or n == 6 or n == 9 or n == 11:
    print(30)
elif n == 2:
    print(28)
    
/step/7
n = int(input())
if n < 60:
    print("Легкий вес")
elif n < 64:
    print("Первый полусредний вес")
elif n < 69:
    print("Полусредний вес")
    
/step/8
a, b = int(input()), int(input())
s = input()
if s == '+':
    print(a + b)
elif s == '-':
    print(a - b)
elif s == '*':
    print(a * b)
elif s == '/':
    if b == 0:
        print('На ноль делить нельзя!')
    else:
        print(a / b)
else:
    print('Неверная операция')
    
/step/9
a, b = input(), input()
if a == 'красный':
    if a == b:
        print('красный')
    elif b == 'синий':
        print('фиолетовый')
    elif b == 'желтый':
        print('оранжевый')
    else:
        print('ошибка цвета')
elif a == 'синий':
    if a == b:
        print('синий')
    elif b == 'красный':
        print('фиолетовый')
    elif b == 'желтый':
        print('зеленый')
    else:
        print('ошибка цвета')
elif a == 'желтый':
    if a == b:
        print('желтый')
    elif b == 'синий':
        print('зеленый')
    elif b == 'красный':
        print('оранжевый')
    else:
        print('ошибка цвета')
else:
    print('ошибка цвета')
    
/step/10
a = int(input())
if a == 0:
    print("зеленый")
elif a < 0 or a > 36:
    print("ошибка ввода")
elif (1 <= a <= 10 or 19 <= a <= 28) + (not a % 2) == 1:
    print("красный")
else:
    print("черный")
    
/step/11
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input()) 
if min(b1, b2) < max(a1, a2): 
    print('пустое множество')
elif min(b1, b2) == max(a1, a2):
    print(min(b1, b2))
else:
    print(max(a1, a2), min(b1, b2))
"""
