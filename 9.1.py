"""
/step/2
aceg

/step/3
aaagggdddd

/step/4
051217

/step/5
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[7])

/step/6
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[39])

/step/7
n = input()
for i in range(0, len(n), 2):
    print(n[i])
    
/step/8
s = input()
for i in range(len(s)-1, -1, -1):
    print(s[i])
    
/step/9
i, f, o = input(), input(), input()
print(f[0], i[0], o[0], sep='')

/step/10
a = input()
s = 0
for i in a:
    s += int(i)
print(s)

/step/11
for i in input():
    if i in '0123456789':
        print("Цифра")
        break
else:
    print("Цифр нет")
    
/step/12
a = input()
star = 0
plus = 0
for i in a:
    if i == '*':
        star += 1
    elif i == '+':
        plus += 1
print('Символ + встречается', plus, 'раз')
print('Символ * встречается', star, 'раз')

/step/13
a = input()
count = 0
for i in range(len(a) -1):
    if a[i] == a[i + 1]:
        count += 1
print(count)

/step/14
s = input()
son, cons = 0, 0
for c in s:
    if c in ('ауоыиэяюёеАУОЫИЭЯЮЁЕ'):
        son += 1
    if c in ('бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'):
        cons += 1
print('Количество гласных букв равно', son)
print('Количество согласных букв равно', cons)

/step/15
a, b = int(input()), ""
while a > 0 :
    b = str(a % 2) + b
    a //= 2 
print(b)
"""
