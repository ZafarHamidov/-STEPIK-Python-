"""
/step/2
функция в Python может возвращать более одного значения
функции упрощают работу программистов в командах
сложные математические выражения иногда можно упрощать путем вычленения части выражения и ее помещения в функцию

/step/3
def get_middle_point(x1, y1, x2, y2):
    return (x1+x2)/2, (y1+y2)/2

# считываем данные
x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

# вызываем функцию
x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)

/step/4
from math import pi

# объявление функции
def get_circle(radius):
    return 2*pi*radius, pi * radius**2

# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)

/step/5
def solve(a, b, c):
    from math import sqrt
    D = b**2 - 4*a*c
    l = [((-b + sqrt(D)) / (2 * a)), ((-b - sqrt(D)) / (2 * a))]
    return min(l), max(l)


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)

/step/7
улучшают возможности по тестированию кода
способствуют совместной работе в команде
упрощают программный код
увеличивают скорость разработки
уменьшают дублирование кода
"""
