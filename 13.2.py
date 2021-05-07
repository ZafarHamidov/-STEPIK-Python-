"""
/step/2
аргумент

/step/3
параметр

/step/4
a 3
b 2
c 1

/step/5
4

/step/6
1 7
0 0
1 7

/step/7
PythonPythonPythonPython

/step/8
def draw_triangle(fill, base):
    l = [i for i in range(1,base//2+2,)]
    l.extend([i for i in range(base//2, 0, -1)])
    for elem in l:
        print(fill * elem)
# считываем данные
fill = input()
base = int(input())
# вызываем функцию
draw_triangle(fill, base)

/step/9
def print_fio(name, surname, patronymic):
    print(''.join([surname[0], name[0], patronymic[0]]).upper())
# считываем данные
name, surname, patronymic = input(), input(), input(),
# вызываем функцию
print_fio(name, surname, patronymic)

/step/10
def print_digit_sum(num):
    sum = 0
    while num > 0:
        sum += num%10
        num //= 10
    print(sum)
# считываем данные
n = int(input())
# вызываем функцию
print_digit_sum(n)
"""
