"""
/step/2
insert() вставляет заданное значение в список
index() возвращает индекс первого вхождения заданного значения
reverse() меняет порядок следования элементов на противоположный
count() возвращает количество равных заданному значению элементов
clear() удаляет все элементы из списка
find() у списков такой метод отсутствует 😂
remove() удаляет первое вхождение заданного значения

/step/3
['Violet', 'Orange', 'Purple', 'Red', 'Blue', 'Green']

/step/4
['Red', 'Blue', 'Black']

/step/5
numbers = [8, 9, 10, 11]
numbers[1] = 17
numbers.extend([4, 5, 6])
del numbers[0]
numbers *= 2
numbers.insert(3, 25)
print(numbers)

/step/6
s = input()
l1 = s.split(' ')
l = [int(i) for i in l1]
maxIdx = l.index(max(l))
max = max(l)
minIdx = l.index(min(l))
min = min(l)
l[maxIdx] = min
l[minIdx] = max
print(*l)

/step/7
s = input()
counter = 0
l = s.lower().split()
counter += l.count('a')
counter += l.count('an')
counter += l.count('the')
print('Общее количество артиклей: ' + str(counter))

/step/8
n = input()
for _ in range(int(n[1:])):
    s = input()
    if '#' in s:
        s = s[:s.find('#')]
    print(s.rstrip())
    
/step/10
[10, 8, 6, 5, 4, 4, 3, 2, 1]

/step/11
l = [int(i) for i in input().split()]
l.sort()
print(*l)
print(*l[::-1])
"""
